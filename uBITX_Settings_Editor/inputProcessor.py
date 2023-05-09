
import tkinter as tk
from tkinter import messagebox
from os import path
import pygubu.widgets.simpletooltip as tooltip


from processor import Processor
from eepromObj import *

class InputProcessor(Processor):
    def __init__(self,  parent):
        super().__init__("Read", parent)

        #self.goButton.set("READ")
        self.optionalInfo_Frame.forget()                # not needing the optional frame while reading

        self.savedFilePathChooserWidget.config(
            mustexist=True,
            title="Select Previously Saved Settings File")

        self.optionalInfo_Frame.grid_forget()                # don't need any optional info (reset ubitx and protect factory) on input

       #   add tooltips
        tooltip.create(self.uBITX_sourceSelector_WIDGET,"Click to read the settings from an attached uBITX")
        tooltip.create(self.File_sourceSelector_WIDGET,"Click to read the settings from a previously saved backup file")



        #   Dictionary to hold current values of usermodfile and whether dirty or not
        self.userModFileValues = {}
        self.userModFileDirty = {}
        self.userModFileToolTips = {}

        self.IOState = "NONE"

    def setIOstate(self, state):
        self.IOstate = state

    def getIOstate(self):
        return (self.IOstate)

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
                self.log.printerror("timestamp", self.savedFilePathChooser.get() + "is corrupted")
                tkinter.messagebox.showerror(title="FATAL ERROR", message=self.savedFilePathChooser.get() + " is corrupted. Please correct or recreate. \nEXITING")
                sys.exit(-1)

            self.log.println("timestamp", "Completed preprocessing of settings file")



        elif fileParts[1] == ".btx":               # have a binary file here to load
            # confirm file exists
            if path.exists(self.savedFilePathChooser.get()) == False:
                self.log.printerror("timestamp", self.savedFilePathChooser.get() + " does not exist. Please select an existing file.")
                return
            else:
                self.log.println("timestamp", "Loading Backup File")

                self.eepromFile = eepromFILE(self.savedFilePathChooser.get(), self.log)
                self.eepromFile.read()
                self.UserModroot = self.eepromFile.decode()


        else:
                self.log.printerror("timestamp", self.savedFilePathChooser.get() + " is not a '.xml' or '.btx' file")
                tkinter.messagebox.showerror(title="FATAL ERROR", message=self.savedFilePathChooser.get() + " is not a '.xml' or '.btx' file \nEXITING")
                sys.exit(-1)


        self.log.println("timestamp", "Loading Settings into uBITX Settings Editor")

        #   Having built the tree, we can load it into the Notebook widget
        self.settingsNotebook.setNotebook(self.UserModroot)         #update notebook widget with settings
        self.log.println("timestamp", "***Settings Successfully loaded***\n")
        self.setIOstate('READ')                # we have live data here that might need to be written
        return


    def readFromComPort(self):              # reads from Com POrt using readEEPROMData
        self.log.println("","")
        self.log.println("timestamp",  "***Reading EEPROM from uBITX***")
        self.log.println("timestamp", "From Com Port: " + self.comPortObj.getSelectedComPort())
        self.log.println("timestamp",  "Awaiting Radio Processor Ready this will take 3-5 seconds")

        self.eepromCom = eepromUBITX(self.comPortObj, self.log)
        if (self.eepromCom.readFromCom() == True):         #returns True if read successful
            self.log.println("timestamp",  "Finished reading EEPROM into memory")
            return True
        else:
            self.log.printerror("timestamp",  "Failed reading uBITX on selected Serial Port.")
            self.log.printerror("timestamp",  "Please check your Serial Port selection and try again")
            return False


    def processComPort(self, *args):
        if(self.readFromComPort()):          # read the contents of the EEPROM
            self.UserModroot = self.eepromCom.decode()


            self.log.println("timestamp", "Loading Settings into uBITX Settings Editor")

            #   Having built the tree, we can load it into the Notebook widget
            self.settingsNotebook.setNotebook(self.UserModroot)         #update notebook widget with settings
            self.log.println("timestamp", "***Settings Successfully loaded***\n")
            self.setIOstate('READ')                # we have live data here that might need to be written




