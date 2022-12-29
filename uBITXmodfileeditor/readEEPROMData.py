from time import sleep
import sys

from globalvars import *
from printtolog import *

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
        printToLog("Bad Checksum on EEPROM Read")
        tkinter.messagebox.showerror(title="ERROR", message="Bad Checksum reading from Radio.\nTry restarting radio, ensuring the USB cable plugged in securely, and then restart application. \nEXITING")
        sys.exit(-1)

    return returnBuffer
