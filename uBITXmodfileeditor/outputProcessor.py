from tkinter import *
import tkinter as tk
import time
from printtolog import *
from lxml import etree as ET
import serial.tools.list_ports              # Used to get a list of com ports
from globalvars import *
from readEEPROMData import readEEPROMData
from getters import getters
from time import sleep
import pathlib

from writeEEPROMData import *
from processor import Processor

class OutputProcessor(Processor):
    def __init__(self, parent):

        super().__init__(parent)

        self.configure(
        height=300,
        style="Heading2.TLabelframe",
        text='Select Target',
        width=200)
        self.savedFilePathChooserWidget.config(
            initialdir="~",
            mustexist=False,
            textvariable=self.savedFilePathChooser,
            title="Select Previously Saved Settings File",
            type="file")
        self.goButton.set("WRITE")

    def processFile(self, *args):
        print("process output file called")

        self.log.println("timestamp", "Updating User Modification File")
        userModroot = self.settingsNotebook.getNotebook()
        self.log.println("timestamp", "Finished Updating User Modification File")

        ET.indent(userModroot,'    ')
        self.log.println("timestamp", "Writing settings to file")
        userModroot.write(self.savedFilePathChooser.get(),method="html", pretty_print=True)

        self.log.println("timestamp", "***Settings Saved to: " + self.savedFilePathChooser.get() + "***")

    def processComPort(self, *args):
        print("process output com port called called")

        self.log.println("timestamp", "Updating User Modification File")
        userModroot = self.settingsNotebook.getNotebook()
        self.log.println("timestamp", "Finished Updating User Modification File")

        writeEEPROMData (self.COM_PORT, userModroot, self.log)
