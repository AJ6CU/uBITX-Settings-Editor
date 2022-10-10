from lxml import etree as ET

from typing import Any
import serial
import functools
from time import sleep
import sys

from globalvars import *
from genmodfile_userconfig import *
from readEEPROMData import readEEPROMData

from getters import getters

#definitions################################################


EEPROMMEMORYMAP="eeprommemorymap.xml"               #Maps EEPROM locations to settings
USERMODFILETEMPLACE="usermodfiletemplate.xml"       #Template file used to fill in with data from EEPROM


#end definitions############################################



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

