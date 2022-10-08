from lxml import etree as ET

from typing import Any
import serial
import functools
from time import sleep
import sys

from globalvars import *
from userconfig import *

from getters import getters

#definitions################################################


EEPROMMEMORYMAP="eeprommemorymap.xml"               #Maps EEPROM locations to settings
USERMODFILETEMPLACE="usermodfiletemplate.xml"       #Template file used to fill in with data from EEPROM


#end definitions############################################



def readEEPROMData(portdesc: object, memlocation: int, numBytesToRead: int) -> bytearray:

    LSB = memlocation & 0xff
    MSB = (memlocation >> 8) & 0xff

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

# def get_Byte_FromEEPROM(memBuffer:bytearray, memlocation: int) -> int:
#     #return int.from_bytes(memBuffer[memlocation],"little",signed=False)
#     return(memBuffer[memlocation])
#
# def get_uint16_FromEEPROM(memBuffer:bytearray, memlocation: int) -> int:
#     return memBuffer[memlocation] + (memBuffer[memlocation+1]<<8)
#
# def get_uint32_FromEEPROM(memBuffer:bytearray, memlocation: int) -> int:
#     return memBuffer[memlocation] + (memBuffer[memlocation+1]<<8) +(memBuffer[memlocation+2]<<16) +(memBuffer[memlocation+3]<<24)
#
# def XML_Get_Byte_FromEEPROM (xmlSubTree, settingName, buffer) -> int:
#     settingTag =  xmlSubTree.find(('.//SETTING[@NAME="{}"]'.format(settingName)))
#     location = int(settingTag.find("EEPROMStart").text)
#     return(get_Byte_FromEEPROM(buffer, location))


#####################################
#Start Main Progrm
#####################################
print("Opening connection to radio")
RS232 = serial.Serial(COM_PORT, BAUD, timeout=0, stopbits=1, parity=serial.PARITY_NONE, xonxoff=0, rtscts=0)
sleep(3)  #this is required to allow Nano to reset after open

print("Reading EEPROM")
EEPROMBuffer=readEEPROMData(RS232, 0, EEPROMSIZE)       #Read the EEPROM into memory

print("Opening template files")
EEPROMtree = ET.parse(EEPROMMEMORYMAP)
EEPROMroot = EEPROMtree.getroot()


UserModtree = ET.parse(USERMODFILETEMPLACE)
UserModroot = UserModtree.getroot()

UserMods = getters()

print("Creating User Mod File from EEPROM data...")

# first step is to take the "easy" ones from the EEPROM buffer and write to the corresponding <value></value>
# in the usermod template file
#
for userSetting in EEPROMroot.findall('.//SETTING'):


    #get name, location in eeprom buffer, number of bytes, and type of data
    userSettingName = userSetting.get("NAME")
    memLocation = int(userSetting.find("EEPROMStart").text)

    #now look in eeprom map for buffer memory location, size (in bytes) and data type

    eepromSetting = EEPROMroot.find('.//SETTING[@NAME="{}"]'.format(userSettingName))

    memLocation = int(eepromSetting.find("EEPROMStart").text)
    numBytes = eepromSetting.find("sizeInBytes").text
    dataType = eepromSetting.find("displayFormat").text

    #get tag for where data will be stored withing UserModroot

    userSettingTag = UserModroot.find('.//SETTING[@NAME="{}"]'.format(userSettingName))
    if (userSettingTag != None):
        valueTag=userSettingTag.find('.//value')
        UserMods.get(userSettingName, userSettingName, EEPROMBuffer, memLocation, valueTag, EEPROMroot, userSettingTag)

ET.indent(UserModtree,'    ')
UserModtree.write(USERMODFILE,method="html", pretty_print=True)
print("All done!")

