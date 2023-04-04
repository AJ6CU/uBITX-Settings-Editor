from os import path
import pygubu.widgets.simpletooltip as tooltip

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
        #   add tooltips
        tooltip.create(self.uBITX_sourceSelector_WIDGET,"Click to write the settings to an attached uBITX")
        tooltip.create(self.File_sourceSelector_WIDGET,"Click to write the settings to a file")
        tooltip.create(self.goButtonWidget,"Click after selecting the destination for the settings")
        tooltip.create(self.comPortObj.comPortsOptionMenu,"Select the com port used by your uBITX")
        tooltip.create(self.comPortObj.comPortListRefresh,"Refresh list of available com ports. "+
                                                        "(You can also plug in your uBITX and then refresh list")
        tooltip.create(self.reset_uBITX_Button_WIDGET, "Click to reboot your uBITX with the new settings")

    def reset_ubitx(self):

        magic1 = 0x4B   # 75 decimal
        magic2 = 0x33   # 51 decimal
        magic3 = 0x51   # 81 decimal
        magic4 = (magic1 + magic2 + magic3) % 256       #checksum calculation

        RS232=self.comPortObj.sendCommand(bytes([magic1, magic2, 0, 0, READCOMMAND]))
        RS232.flush()


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
            # for settings in userModroot.findall('SETTING'):  # unused as we always write whole tree. Makes multiple
            #     if settings.get("NAME")[:4] == "EXT_":       # reads easier as data is overwritten
            #         settings.getparent().remove(settings)

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

        self.log.println("timestamp",  "Refreshing In-memory Copy of EEPROM")

        self.eepromCom = eepromUBITX(self.comPortObj, self.log)

        if (self.eepromCom.readFromCom() == False):             # Error reading from EEPROM. Abort write
            self.log.printerror("timestamp",  "Error communicating with EEPROM. Please check your Serial Port selection and try reading again")
            return

        self.eepromCom.encode(userModroot)                      # Talking to EEPROM, now can proceed to updating it

        cntWritten = self.eepromCom.write()

        if (cntWritten > 0):
            self.log.println("timestamp", "***Settings Successfully Written to uBITX***\n")
        else:
            self.log.println("timestamp", "***No Changes to Settings. Nothing written to uBTIX***\n")


        #   Saved Info, set state
        self.readerObj.setIOstate('WRITE')                # We did save the data. set state

        self.reset_uBITX_Button_WIDGET.configure(state="normal")
        self.reset_uBITX_Button_WIDGET.pack()
