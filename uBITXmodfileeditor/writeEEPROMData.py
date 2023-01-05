#   General System Imports

from lxml import etree as ET
import serial
from bitarray import bitarray
from time import sleep
import sys
import platform
from os.path import exists
import os

#   Tkinter imports
import tkinter

import tkinter.messagebox
import serial.tools.list_ports              # Used to get a list of com ports
from tkinter import filedialog as fd

#   local function imports

from globalvars import *

from printtolog import *
from helpsubsystem import *
#from fonts import *
from setters import setters

EEPROMMEMORYMAP="eeprommemorymap.xml"               #Maps EEPROM locations to settings


def readEEPROMData(portdesc: object, memAddress: int, numBytesToRead: int) -> bytearray:

    LSB = memAddress & 0xff
    MSB = (memAddress >> 8) & 0xff

    NumLSB = numBytesToRead & 0xff
    NumMSB = (numBytesToRead >> 8) & 0xff

    # send command buffer to radio
    # byte1 = LSB of the start location in EEPROM
    # byte2 = MSB of the start location in EEPROM
    # byte3 = LSB of the total bytes to read from EEPROM
    # byte4 - MSB of the total bytes to read from EEPROM
    # byte5 - Command telling the radio what to do

    portdesc.write(bytes([LSB, MSB, NumLSB, NumMSB, READCOMMAND]))

    # create buffer to save bytes being returned
    # byte1 = 0x2 - always
    # lots of bytes = number of bytes requested
    # byte3 = checksum of bytes above
    #byte4 = 0x0 (ACK)

    returnBuffer: bytesarray = []
    checkSum: int = 0x02

    i = -1
    while i < numBytesToRead:
         if portdesc.in_waiting != 0:
            if i< 0:
                throwawy = portdesc.read(1)
            else:
                returnBuffer.extend(portdesc.read(1))
                checkSum = (checkSum+returnBuffer[i] ) & 0xFF
            i += 1

#   get checksum sent by radio CAT control
    while portdesc.in_waiting == 0:
        sleep(0.01)
    sentCheckSum = int.from_bytes(portdesc.read(1),"little",signed=False)

#   get trailing byte. Must be an ACK (0x00)
    while portdesc.in_waiting == 0:
        sleep(0.01)
    trailingByte = int.from_bytes(portdesc.read(1),"little",signed=False)

    if(sentCheckSum!=checkSum)|(trailingByte!=0):
        sys.exit("Bad Checksum on EEPROM Read")

    return returnBuffer

def writeByteToEEPROM(portdesc: object, memAddress: int, outbyte: int, log):
    log.println("timestamp","eeprom mem address =" + str(memAddress))
    LSB: bytes = memAddress & 0xff
    MSB: bytes = (memAddress >> 8) & 0xff
#    print(type(LSB),"\t", type(MSB),"\t", type(outbyte))
#    print(memAddress)
    checkByte: int = ((LSB + MSB + outbyte) % 256) & 0xff
    bytesToWrite = bytes([LSB, MSB, outbyte, checkByte, WRITECOMMAND])
    portdesc.write(bytesToWrite)


def updateEEPROM(portdesc: object, inMemBuffer: bytearray, itsDirty: bitarray, log) -> int:
    log.println("timestamp","following EEPROM locations were updated")
    i: int = 0
    while i < EEPROMSIZE:
        if itsDirty[i]:  # Got a dirty byte
#            print(f"{i:04}", "\t", inMemBuffer[i],"\t",type(inMemBuffer[i]))
            writeByteToEEPROM(portdesc, i, inMemBuffer[i], log)

            doneWithByte: bool = False
            retryCnt: int = 0
            while True:  # keep tring to write until successful or exceed # retries

                while portdesc.in_waiting == 0:
                    sleep(0.005)
                resultCode = int.from_bytes(portdesc.read(1), "little", signed=False)
                while portdesc.in_waiting == 0:
                    sleep(0.005)
                trailingByte = int.from_bytes(portdesc.read(1), "little", signed=False)
                if (resultCode == OK) & (trailingByte == ACK):
                    break
                else:
                    log.println("timestamp","retrying byte =" + str(i))
                    log.println("timestamp","resultcode=" + str(resultCode))
                    log.println("timestamp","trailingByte=" + str(trailingByte))
                    retryCnt += 1
                    if retryCnt > RETRIES:
                        log.println("timestamp","number of retries exceeded on memory location: " + str(i))
                        return (1)  # Failure
        i += 1
    return (0)                      # Success

def writeEEPROMData (RS232, userModroot, log):

    # log.println("timestamp","Opening connection to radio")
    # RS232 = serial.Serial(COM_PORT, BAUD, timeout=0, stopbits=1, parity=serial.PARITY_NONE, xonxoff=0, rtscts=0)
    # sleep(3)  #this is required to allow Nano to reset after open

    log.println("timestamp","Reading EEPROM into memory")
    EEPROMBuffer=readEEPROMData(RS232, 0, EEPROMSIZE)       #Read the EEPROM into memory


    EEPROMBufferDirty=bitarray(EEPROMSIZE)          # create a bit array of the same size that we can use to track dirty "bytes"
    EEPROMBufferDirty.setall(0)                     # clear all bits. When we write a byte into the EEPROMBuffer, we will set
                                                    # corresponding dirty bit to 1


    log.println("timestamp","Opening EEPROM Memory Map of parameter locations")
    EEPROMtree = ET.parse(EEPROMMEMORYMAP)
    EEPROMroot = EEPROMtree.getroot()

    log.println("timestamp","Opening Usermod file")
    # UserModtree = ET.parse(USERMODFILE)
    # UserModroot = UserModtree.getroot()

    log.println("timestamp","Processing Usermod file and updating in memory copy of EEPROM...")



    EEPROM_Memory = setters()

    # first step is to take the "easy" ones from the EEPROM buffer and write to the corresponding <value></value>
    # in the usermod template file
    #
    for userSetting in userModroot.findall('.//SETTING'):


        #get setting name and value
        userSettingName = userSetting.get("NAME")
        userSettingValue = userSetting.find("value").text

        #now look in eeprom map for buffer memory location, size (in bytes) and data type

        eepromSetting = EEPROMroot.find('.//SETTING[@NAME="{}"]'.format(userSettingName))

        memLocation = int(eepromSetting.find("EEPROMStart").text)
        numBytes = eepromSetting.find("sizeInBytes").text
        dataType = eepromSetting.find("displayFormat").text
        if (userSettingValue != None):
            EEPROM_Memory.set(userSettingName, userSettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)
        else:
            log.println("timestamp","Warning: skipping because value = NONE, Setting Name" + userSettingName)

    log.println("timestamp","In memory EEPROM copy updated. Now updating actual EEPROM")

    # write out eeprom and specific locations updated based on dirty bits


    if(updateEEPROM( RS232, EEPROMBuffer, EEPROMBufferDirty, log  )==0):
        log.println("timestamp", "All done!")
    else:
        log.println("timestamp","Error, see message above")





