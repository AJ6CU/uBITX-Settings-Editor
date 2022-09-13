from typing import Any
import serial
import functools
from time import sleep
import sys

#definitions################################################
COM_PORT = "COM14"
BAUD = 38400

WRITECOMMAND=0xDC
OK=0x77
ACK = 0x00
RETRIES=3

EEPROMSIZE=1024

PROTECTFACTORYRESTORE=1
STARTFACTOREYRESTORE=64
ENDFACTORYRESTORE=100

BACKUPFILE="binarybackupdump.btx"
#end definitions############################################


def writeEEPROMData(portdesc: object, memlocation: int, numBytesToWrite: int, memBuffer: bytes):


    # send command buffer to radio
    # byte1 = LSB of the start location in EEPROM
    # byte2 = MSB of the start location in EEPROM
    # byte3 = byte actually being written
    # byte4 - checkByte
    # byte5 - Command telling the radio what to do

    i: int=0
    retryCnt: int=0
    while (i<numBytesToWrite):
        if (PROTECTFACTORYRESTORE==1)&((memlocation+i) >= STARTFACTOREYRESTORE)&((memlocation+i) <= ENDFACTORYRESTORE):
            print("skipping factory byte=",i)
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
                print("retrying byte =", i)
                print("resultcode=",resultCode)
                print("trailingByte=", trailingByte)
                retryCnt +=1
            if retryCnt > RETRIES:
                sys.exit("EEPROM Write Failed, try again")
            else:
                if (i % 100 == 0) & (i!=0):
                    print("bytes written",i)
                i+=1
                retryCnt=0



#####################################
#Start Main Progrm
#####################################
print("Establishing Connection to Radio:")
RS232 = serial.Serial(COM_PORT, BAUD, timeout=0, stopbits=1, parity=serial.PARITY_NONE, xonxoff=0, rtscts=0)

print("reading backup file into buffer")
backup = open(BACKUPFILE, "rb")
inMemoryFile=bytearray(backup.read(EEPROMSIZE))
backup.close()

print("Writing to EEPROM")
writeEEPROMData(RS232, 0, EEPROMSIZE, inMemoryFile)

print("All Done!")
