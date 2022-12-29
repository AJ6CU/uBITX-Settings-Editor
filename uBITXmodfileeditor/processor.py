from tkinter import *
import tkinter as tk
#import os, sys
#import time
from printtolog import *
#from lxml import etree as ET
import serial.tools.list_ports              # Used to get a list of com ports
from globalvars import *
#from readEEPROMData import readEEPROMData
#from getters import getters
#from time import sleep
import pathlib

from sourceselectorwidget import SourceselectorWidget

class Processor(SourceselectorWidget):
    def __init__(self, parent):
        super().__init__(parent)


        self.goButtonWidget.configure(state=DISABLED)         # Disable "go" button

        # put file selector in default state
        self.selectSaveFileFrame.forget()               #  Want to show the com port option  as default, hide safed file option
        self.savedFilePathChooserWidget.config(filetypes=[('uBITX Saved Files','.xml')])         # Manually add restriction to only XML files
        self.savedFilePathChooserWidget.config(initialdir=HOMEDIRECTORY)         # Manually add restriction to only XML files
        self.savedFilePathChooser.set(USERMODFILE)
        self.lastDir = HOMEDIRECTORY

        # pre-load com ports
        self.updateComPorts()                                       # Fill in available Com Ports


    def setLog(self, log ):                     # this method is called to tell object where to write the log
        self.log = log

    def setNotebook(self, settingsNotebook):
        self.settingsNotebook = settingsNotebook


    def sourceSelected(self):                   # this method allows user to select comport vs file and loads the right UX to select
                                                # the desired object
                                                # also disables the goButtonWidget and allows downstream selection to re-enable once
                                                # a valid com port or file is selected.

        if self.sourceSelectorRadioButton.get() == "uBITX":
            self.goButtonWidget.unbind("<Button-1>")            # Must explictly unbind button to prevent disabled button from being clickable
            self.goButtonWidget.configure(state=DISABLED)       # Now fade it out

            # since a user can switch  back and forth, or have to correct errors. update initial directories to make their life easier
            # also reset default file name to a message to select one
            # USERMODFILE always has the text "Please Select File"
            #
            if (self.lastDir != HOMEDIRECTORY):
                self.lastDir = pathlib.Path(self.savedFilePathChooser.get()).parent
            self.savedFilePathChooserWidget.config(path=USERMODFILE, initialdir=self.lastDir)

            self.selectSaveFileFrame.forget()
            self.updateComPorts()                                       # Fill in available Com Ports
            self.selectComPortFrame.pack()

        else:
            self.goButtonWidget.unbind("<Button-1>")            # In this case we have switched into file selection mode. Unbind and disable read button
            self.goButtonWidget.configure(state=DISABLED)       # If user selects a valid file, the button is re-enabled and callback connected
            self.selectComPortFrame.forget()                # In the on_path_changed event
            self.selectSaveFileFrame.pack()

    def on_path_changed(self, event=None):
        self.path=self.savedFilePathChooser.get()
        if (pathlib.Path(self.path).exists()):
            self.goButtonWidget.bind("<Button-1>", self.processFile)
            self.goButtonWidget.configure(state=NORMAL)
            self.lastDir = pathlib.Path(self.savedFilePathChooser.get()).parent


    def processFile(self, *args):
        pass


    def comPortSelected (self, *args):
        self.goButtonWidget.bind("<Button-1>", self.processComPort)
        self.goButtonWidget.configure(state=NORMAL)

        self.COM_PORT = self.availableComPorts.get()

    def updateComPorts(self):
        ports = serial.tools.list_ports.comports()      #Gets list of ports
        self.comPortList =[("Select Serial Port")]           #Seeds option list with Selection instructions

        for p in ports:                                 #this used to strip down to just the com port# or path
            self.comPortList.append(p.device)

        self.comPortsOptionMenu.set_menu("Select Serial Port", *self.comPortList)
        self.COM_PORT = "COM PORT"     #reset COM_PORT to an illegal value

    def processComPort(self, *args):
        pass




