
import tkinter as tk
from tkinter import messagebox
from os import path


from processor import Processor
from eepromObj import *

class InputProcessor(Processor):
    def __init__(self, parent):
        super().__init__(parent)
        self.goButton.set("READ")
        self.resetButton_WIDGET.forget()
        self.savedFilePathChooserWidget.config(
            mustexist=True,
            title="Select Previously Saved Settings File")

        #   Dictionary to hold current values of usermodfile and whether dirty or not
        self.userModFileValues = {}
        self.userModFileDirty = {}
        self.userModFileToolTips = {}

        self. IOState = "NONE"

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

        if(self.comPortObj.openComPort(self.comPortObj.getSelectedComPort())):        # was able to open com port
            self.RS232 = self.comPortObj.getComPortPTR(self.comPortObj.getSelectedComPort())

            self.log.println("timestamp",  "Refreshing In-memory Copy of EEPROM")
            self.eepromCom = eepromUBITX(self.RS232, self.log)
            self.eepromCom.read()

            self.log.println("timestamp",  "Finished reading EEPROM into memory")

            return True
        else:
            return False


    def processComPort(self, *args):
        if(self.readFromComPort()):          # read the contents of the EEPROM
            self.UserModroot = self.eepromCom.decode()


            self.log.println("timestamp", "Loading Settings into uBITX Settings Editor")

            #   Having built the tree, we can load it into the Notebook widget
            self.settingsNotebook.setNotebook(self.UserModroot)         #update notebook widget with settings
            self.log.println("timestamp", "***Settings Successfully loaded***\n")
            self.setIOstate('READ')                # we have live data here that might need to be written



