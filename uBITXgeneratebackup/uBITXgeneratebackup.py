from typing import Any
import serial
import functools
from time import sleep
import sys

#definitions################################################
COM_PORT = "COM14"
BAUD = 38400

READCOMMAND=0xDB

EEPROMSIZE=1024
BACKUPFILESIZE=2048


BACKUPFILE="binarybackupdump.btx"
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


#####################################
#Start Main Progrm
#####################################
print("starting backup...")
RS232 = serial.Serial(COM_PORT, BAUD, timeout=0, stopbits=1, parity=serial.PARITY_NONE, xonxoff=0, rtscts=0)
sleep(3)  #this is required to allow Nano to reset after open

print("reading EEPROM into buffer")
EEPROMBuffer=readEEPROMData(RS232, 0, EEPROMSIZE)       #Read the EEPROM into memory
print("EEPROM read into buffer")

print("writing EEPROM to backup file")
backup = open(BACKUPFILE, "wb")
backup.write(bytearray(EEPROMBuffer))

print("Making file compatible with uBITX Memory Manager")
backup.write(b"\0"* (BACKUPFILESIZE-EEPROMSIZE))

backup.close()
print("All done!")