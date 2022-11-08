from time import sleep
from time import *
import sys
from restore_userconfig import *

from globalvars import *
from printtolog import *


def writeEEPROMData(portdesc: object, memlocation: int, numBytesToWrite: int, memBuffer: bytes, protectFactory: int):
    global PROTECTFACTORYRESTORE

    # send command buffer to radio
    # byte1 = LSB of the start location in EEPROM
    # byte2 = MSB of the start location in EEPROM
    # byte3 = byte actually being written
    # byte4 - checkByte
    # byte5 - Command telling the radio what to do

    i: int=0
    retryCnt: int=0
    while (i<numBytesToWrite):
        if (protectFactory==1)&((memlocation+i) >= STARTFACTOREYRESTORE)&((memlocation+i) <= ENDFACTORYRESTORE):
            if(i == STARTFACTOREYRESTORE):
                printlnToLog(get_time_stamp() + ": EEPROM bytes written: 0-"+ str(STARTFACTOREYRESTORE-1))
                printlnToLog(get_time_stamp() + ": Skipping Factory Recovery Data in EEPROM bytes=64-100")
            i+=1
            retryCnt=0
        else:

            LSB = (memlocation+i) & 0xff
            MSB = ((memlocation+i) >> 8) & 0xff
            checkByte: int = ((LSB + MSB + memBuffer[i]) % 256) & 0xff
            bytesToWrite = bytes([LSB, MSB, memBuffer[i], checkByte, WRITECOMMAND])
            portdesc.write(bytesToWrite)

            #   Radio returns two bytes. 1st is a an ACK (Ox00) and second is a 0x00
            #   Retry if you dont get the correct response

            while portdesc.in_waiting == 0:
                sleep(0.005)
            resultCode = int.from_bytes(portdesc.read(1), "little", signed=False)

            while portdesc.in_waiting == 0:
                sleep(0.005)
            trailingByte = int.from_bytes(portdesc.read(1), "little", signed=False)

            if (resultCode != OK) | (trailingByte != ACK):
                printlnToLog(get_time_stamp() + ": retrying byte =" + str(i))
                printlnToLog(get_time_stamp() + ": resultcode=" + str(resultCode))
                printlnToLog(get_time_stamp() + ": trailingByte=" +str(trailingByte))
                retryCnt +=1
            if retryCnt > RETRIES:
                sys.exit("EEPROM Write Failed, try again")
            else:
                if (i % 100 == 0) & (i!=0):
                    printlnToLog(get_time_stamp() + ": EEPROM bytes written: " + str(i-99)+ "-" +str(i))
                elif(i==(numBytesToWrite-1)):
                    printlnToLog(get_time_stamp() + ": EEPROM bytes written: " + str((divmod(i,100)[0]*100)+1)+ "-" +str(i))
                i+=1
                retryCnt=0
