from os import path

from eepromObj import *
from processor import Processor

class OutputProcessor(Processor):
    def __init__(self, parent, readerObj):

        super().__init__(parent)

        self.configure(
        height=300,
        style="Heading2.TLabelframe",
        text='Select Target',
        width=200)
        self.savedFilePathChooserWidget.config(
            mustexist=False,
            title="Save Settings to:")
        self.goButton.set("WRITE")
        self.readerObj = readerObj              # save ptr to the reader object that holds the state of whether data
                                                # has been written or not

    def reset_ubitx(self):
        print("reset ubitx called")

        if(self.comPortObj.openComPort(self.comPortObj.getSelectedComPort())):        # was able to open com port
            self.RS232 = self.comPortObj.getComPortPTR(self.comPortObj.getSelectedComPort())

            magic1 = 0x4B   # 75 decimal
            magic2 = 0x33   # 51 decimal
            magic3 = 0x51   # 81 decimal
            magic4 = (magic1 + magic2 + magic3) % 256       #checksum calculation

            self.RS232.write(bytes([magic1, magic2, magic3, magic4, WRITECOMMAND]))
            self.RS232.flush()


    def processFile(self, *args):

        self.log.println("timestamp", "\n***Saving Settings to File***")
        self.log.println("timestamp", "Updating Internal Settings Data Structure")
        userModroot = self.settingsNotebook.getNotebook()
        self.log.println("timestamp", "Finished Internal Settings Data Structure")

        # Process based on file extension. ".btx" = binary file ".xml" = ascii xml file

        fileParts = path.splitext(self.savedFilePathChooser.get())

        if(fileParts[1] == ''):
            self.log.printerror("timestamp", "No file extension provided, defaulting to '.btx'")
            self.savedFilePathChooser.set(self.savedFilePathChooser.get()+".btx")
            fileParts[1] == ".btx"

        if (fileParts[1] == ".xml"):

            ET.indent(userModroot,'    ')
            self.log.println("timestamp", "Writing settings to file")
            userModroot.write(self.savedFilePathChooser.get(),method="html", pretty_print=True)

            self.log.println("timestamp", "***Settings Saved to: " + self.savedFilePathChooser.get() + "***\n")
        else:
            self.log.println("timestamp", "Writing settings to file")
            self.eepromFile= eepromFILE(self.savedFilePathChooser.get(), self.log)
            self.eepromFile.encode(userModroot)
            self.eepromFile.write()
            self.log.println("timestamp", "***Settings Saved to: " + self.savedFilePathChooser.get() + "***\n")

        #   Saved Info, set state
            self.readerObj.setIOstate('WRITE')                # We did save the data. set state


    def processComPort(self, *args):

        self.log.println("timestamp", "***Saving Settings to uBITX***")
        self.log.println("timestamp","On Com Port: " + self.comPortObj.getSelectedComPort())

        self.log.println("timestamp", "Updating Internal Settings Data Structure")

        userModroot = self.settingsNotebook.getNotebook()

        self.log.println("timestamp", "Finished Internal Settings Data Structure")

        if(self.comPortObj.openComPort(self.comPortObj.getSelectedComPort())):        # was able to open com port
            self.RS232 = self.comPortObj.getComPortPTR(self.comPortObj.getSelectedComPort())

        self.log.println("timestamp",  "Refreshing In-memory Copy of EEPROM")

        self.eepromCom = eepromUBITX(self.RS232, self.log)

        self.eepromCom.read()
        self.eepromCom.encode(userModroot)

        self.eepromCom.write()

        self.log.println("timestamp", "***Settings Successfully Written to uBITX***\n")
        #   Saved Info, set state
        self.readerObj.setIOstate('WRITE')                # We did save the data. set state

        self.resetButton_WIDGET.configure(state="normal")
        self.resetButton_WIDGET.pack()
