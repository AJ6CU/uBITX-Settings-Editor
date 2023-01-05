from tkinter import *
import tkinter as tk
#import os, sys
#import time
from printtolog import *
from lxml import etree as ET
import serial.tools.list_ports              # Used to get a list of com ports
from globalvars import *
from readEEPROMData import readEEPROMData
from getters import getters
from time import sleep
#import pathlib

from processor import Processor

class InputProcessor(Processor):
    def __init__(self, parent):
        super().__init__(parent)
        self.goButton.set("READ")
        #   Dictionary to hold current values of usermodfile and whether dirty or not
        self.userModFileValues = {}
        self.userModFileDirty = {}
        self.userModFileToolTips = {}


    def processFile(self, *args):

        self.log.println("timestamp", "Opening User Modification File")

    #   try to open and parse usermodfile
        try:
            self.userModroot = ET.parse(self.savedFilePathChooser.get())
        except:
            self.log.println("timestamp", self.savedFilePathChooser.get() + "is corrupted")
            tk.messagebox.showerror(title="FATAL ERROR", message=USERMODFILE + " is corrupted. Please correct or recreate. \nEXITING")
            sys.exit(-1)

        self.log.println("timestamp", "Completed preprocessing of settings file")

        self.log.println("timestamp", "Loading settings from file")

        self.settingsNotebook.setNotebook(self.userModroot)         #update notebook widget with settings
        self.log.println("timestamp", "Settings loaded")


    def processComPort(self, *args):

        #self.log.println("timestamp", "***Starting to read EEPROM of uBITX on " + self.COM_PORT + "***")

        # try:
        #     RS232 = serial.Serial(self.COM_PORT, BAUD, timeout=0, stopbits=1, parity=serial.PARITY_NONE, xonxoff=0, rtscts=0)
        # except:
        #     self.log.println("timestamp",  self.COM_PORT + " not selected or no uBITX attached")
        #     self.log.println("timestamp",  "***Reading EEPROM Aborted***")
        #     self.log.println(" ", " ")                                  #print blank line in case backup run again
        #     self.log.println(" ", " ")                                  #print blank line in case backup run again
        #     tk.messagebox.showerror("Error", message="COM Port not selected or no uBITX attached")
        #     self.availableComPorts.set(self.comPortList[0])
        # else:
#        self.log.println("timestamp",  "Establishing Connection to uBITX on " + self.COM_PORT)
        self.log.println("timestamp",  "Awaiting Radio Processor Ready this will take 3-5 seconds")
        #sleep(3)  #this is required to allow Nano to reset after open
        print("in process comp port")
        if(self.comPortObj.openComPort(self.comPortObj.getSelectedComPort())):        # was able to open com port
            self.RS232 = self.comPortObj.getComPortPTR(self.comPortObj.getSelectedComPort())

        self.log.println("timestamp",  "Reading EEPROM into memory")
        self.EEPROMBuffer=readEEPROMData(self.RS232, 0, EEPROMSIZE)      #Read the EEPROM into memory
        self.log.println("timestamp",  "Finished reading EEPROM into memory")

        #RS232.close()                                               #done with uBITX connection so close the serial port

        self.log.println("timestamp",  "Opening EEPROM Memory Mapping file")

        # Try reading the two XML files and flag any erors
        try:
            EEPROMroot = ET.parse(EEPROMMEMORYMAP)
        except:
            self.log.println("timestamp",  "eeprommemorymap.xml is missing or corrupted")
            tk.messagebox.showerror(title="FATAL ERROR", message="'eeprommemorymap.xml' is missing or corrupted. Please re-install application. \nEXITING")
            sys.exit(-1)

        self.log.println("timestamp",  "Completed preprocessing of EEPROM Memory Mapping")

        # No we need to process the binary data into an XML tree
        self.log.println("timestamp",  "Opening User Modification File template")

        try:
            self.UserModroot = ET.parse(USERMODFILETEMPLACE)
        except:
            self.log.println("timestamp",  "usermodfiletemplate.xml is missing or corrupted")
            tk.messagebox.showerror(title="FATAL ERROR", message="'usermodfiletemplate.xml' is missing or corrupted. Please re-install application. \nEXITING")
            sys.exit(-1)

        self.log.println("timestamp",  "Completed preprocessing of User Modification Template")

        #   We have openned the template file, now merge the contents into the tree
        UserMods = getters()

        self.log.println("timestamp", "Interpreting EEPROM contents")
        #
        # For each setting in the EEPROM Map, there is a "getter" that will process it and write it to the user
        # mod file
        #
        for userSetting in EEPROMroot.findall('.//SETTING'):


            #get name, location in eeprom buffer, number of bytes, and type of data
            userSettingName = userSetting.get("NAME")
            memLocation = int(userSetting.find("EEPROMStart").text)

            #now look in eeprom map for buffer memory location, size (in bytes) and data type

            eepromSetting = EEPROMroot.find('.//SETTING[@NAME="{}"]'.format(userSettingName))

            memLocation = int(eepromSetting.find("EEPROMStart").text)
            #numBytes = eepromSetting.find("sizeInBytes").text
            #dataType = eepromSetting.find("displayFormat").text

            #get tag for where data will be stored withing UserModroot

            userSettingTag = self.UserModroot.find('.//SETTING[@NAME="{}"]'.format(userSettingName))
            if (userSettingTag != None):
                valueTag=userSettingTag.find('.//value')
                UserMods.get(userSettingName, userSettingName, self.EEPROMBuffer, memLocation, valueTag, EEPROMroot, userSettingTag)


        self.log.println("timestamp", "Completed preprocessing of EEPROM contents")

        self.log.println("timestamp", "Loading Contents User Modification File")


        #   Having built the tree, we can load it into the Notebook widget
        self.settingsNotebook.setNotebook(self.UserModroot)         #update notebook widget with settings
        self.log.println("timestamp", "Settings loaded")




