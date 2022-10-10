from typing import Any
import serial
import functools
from time import sleep
import sys
from globalvars import *
from backup_userconfig import *
from readEEPROMData import readEEPROMData


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