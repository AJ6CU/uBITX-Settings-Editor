# from tkinter import *
import tkinter as tk
#import os, sys
#import time
from os import path
# from printtolog import *
# from lxml import etree as ET
# import serial.tools.list_ports              # Used to get a list of com ports
# from globalvars import *
# from time import sleep
#import pathlib

from processor import Processor
from eepromObj import *

class InputProcessor(Processor):
    def __init__(self, parent):
        super().__init__(parent)
        self.goButton.set("READ")
        self.savedFilePathChooserWidget.config(
            mustexist=True,
            title="Select Previously Saved Settings File")

        #   Dictionary to hold current values of usermodfile and whether dirty or not
        self.userModFileValues = {}
        self.userModFileDirty = {}
        self.userModFileToolTips = {}


    def processFile(self, *args):

        self.log.println("timestamp", "***Opening Save/Backup File***")
        self.log.println("timestamp", "Selected file: " + self.savedFilePathChooser.get())

        # Process based on file extension. ".btx" = binary file ".xml" = ascii xml file

        fileParts = path.splitext(self.savedFilePathChooser.get())

        if fileParts[1] == ".xml":

            #   try to open and parse save file
            try:
                self.UserModroot = ET.parse(self.savedFilePathChooser.get())
            except:
                self.log.println("timestamp", self.savedFilePathChooser.get() + "is corrupted")
                tk.messagebox.showerror(title="FATAL ERROR", message=self.savedFilePathChooser.get() + " is corrupted. Please correct or recreate. \nEXITING")
                sys.exit(-1)

            self.log.println("timestamp", "Completed preprocessing of settings file")


        elif fileParts[1] == ".btx":               # have a binary file here to load
            # confirm file exists
            if path.exists(self.savedFilePathChooser.get()) == False:
                self.log.println("timestamp", self.savedFilePathChooser.get() + " does not exist. Please select an existing file.")
                return
            else:
                self.log.println("timestamp", "Loading Backup File")

                self.eepromFile = eepromFILE(self.savedFilePathChooser.get(), self.log)
                self.eepromFile.read()
                self.UserModroot = self.eepromFile.decode()


        else:
                self.log.println("timestamp", self.savedFilePathChooser.get() + " is not a '.xml' or '.btx' file")
                tk.messagebox.showerror(title="FATAL ERROR", message=self.savedFilePathChooser.get() + " is not a '.xml' or '.btx' file \nEXITING")
                sys.exit(-1)


        self.log.println("timestamp", "Loading Settings into uBITX Memory Manager")
        #   Having built the tree, we can load it into the Notebook widget
        self.settingsNotebook.setNotebook(self.UserModroot)         #update notebook widget with settings
        self.log.println("timestamp", "***Settings Successfully loaded***\n")
        return


    def readFromComPort(self):              # reads from Com POrt using readEEPROMData
        self.log.println("timestamp",  "\n***Reading EEPROM from uBITX***")
        self.log.println("timestamp", "From Com Port: " + self.comPortObj.getSelectedComPort())
        self.log.println("timestamp",  "Awaiting Radio Processor Ready this will take 3-5 seconds")

        if(self.comPortObj.openComPort(self.comPortObj.getSelectedComPort())):        # was able to open com port
            self.RS232 = self.comPortObj.getComPortPTR(self.comPortObj.getSelectedComPort())

        self.log.println("timestamp",  "Refreshing In-memory Copy of EEPROM")
        self.eepromCom = eepromUBITX(self.RS232, self.log)
        self.eepromCom.read()


        #self.EEPROMBuffer=readEEPROMData(self.RS232, 0, EEPROMSIZE)      #Read the EEPROM into memory using CAT commands
        self.log.println("timestamp",  "Finished reading EEPROM into memory")

    # def mergeEEPROMData(self):                  # reads from Com POrt using readEEPROMData
    #     self.log.println("timestamp",  "Opening EEPROM Memory Mapping file")
    #
    #     # Try reading the two XML files and flag any errors
    #     try:
    #         EEPROMroot = ET.parse(EEPROMMEMORYMAP)
    #     except:
    #         self.log.println("timestamp",  "eeprommemorymap.xml is missing or corrupted")
    #         tk.messagebox.showerror(title="FATAL ERROR", message="'eeprommemorymap.xml' is missing or corrupted. Please re-install application. \nEXITING")
    #         sys.exit(-1)
    #
    #     self.log.println("timestamp",  "Completed preprocessing of EEPROM Memory Mapping")
    #
    #     # No we need to process the binary data into an XML tree
    #     self.log.println("timestamp",  "Opening User Modification File template")
    #
    #     try:
    #         self.UserModroot = ET.parse(USERMODFILETEMPLACE)
    #     except:
    #         self.log.println("timestamp",  "usermodfiletemplate.xml is missing or corrupted")
    #         tk.messagebox.showerror(title="FATAL ERROR", message="'usermodfiletemplate.xml' is missing or corrupted. Please re-install application. \nEXITING")
    #         sys.exit(-1)
    #
    #     self.log.println("timestamp",  "Completed preprocessing of User Modification Template")
    #
    #     #   We have opened the template file, now merge the contents into the tree
    #     UserMods = getters()
    #
    #     self.log.println("timestamp", "Interpreting BINARY data")
    #     #
    #     # For each setting in the EEPROM Map, there is a "getter" that will process it and write it to the user
    #     # mod file
    #     #
    #     for userSetting in EEPROMroot.findall('.//SETTING'):
    #
    #
    #         #get name, location in eeprom buffer, number of bytes, and type of data
    #         userSettingName = userSetting.get("NAME")
    #         memLocation = int(userSetting.find("EEPROMStart").text)
    #
    #         #now look in eeprom map for buffer memory location, size (in bytes) and data type
    #
    #         eepromSetting = EEPROMroot.find('.//SETTING[@NAME="{}"]'.format(userSettingName))
    #
    #         memLocation = int(eepromSetting.find("EEPROMStart").text)
    #         #numBytes = eepromSetting.find("sizeInBytes").text
    #         #dataType = eepromSetting.find("displayFormat").text
    #
    #         #get tag for where data will be stored withing UserModroot
    #
    #         userSettingTag = self.UserModroot.find('.//SETTING[@NAME="{}"]'.format(userSettingName))
    #         if (userSettingTag != None):
    #             valueTag=userSettingTag.find('.//value')
    #             UserMods.get(userSettingName, userSettingName, self.EEPROMBuffer, memLocation, valueTag, EEPROMroot, userSettingTag)
    #
    #
    #     self.log.println("timestamp", "Completed Processing of Binary Data")
    #


    def processComPort(self, *args):
        self.readFromComPort()          # read the contents of the EEPROM
        self.UserModroot = self.eepromCom.decode()


        self.log.println("timestamp", "Loading Settings into uBITX Memory Manager")

        #   Having built the tree, we can load it into the Notebook widget
        self.settingsNotebook.setNotebook(self.UserModroot)         #update notebook widget with settings
        self.log.println("timestamp", "***Settings Successfully loaded***\n")




