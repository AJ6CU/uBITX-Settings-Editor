from Scanner import Scanner
#from com_portManager import com_portManager
import pygubu.widgets.simpletooltip as tooltip
from time import sleep
from globalvars import *


class I2Cscanner (Scanner):
    # Known I2C devices
    knownI2C={'0x50':'EEPROM', '0x60':'Si5351', '0x27': 'LCD'}

    def __init__(self, parent):
        super().__init__(parent)
        self.title("I2C Bus Scanner")


    def scannerStart(self):
        #
        #   Some definitions might be helpful here...
        #
        #   self.comPortObj  is a handle to the comport that was openned when the eeprom was first read in
        #                    in most cases, this should be still openned and can be directly read.
        #   self.comPortObj.getSelectedComPort()  returns the name of the com port. e.g. COM8
        #
        #   so self.comPOrtObj.openSelectedComPort(self.comPortObj.getSelected()) is equivalent to asking whether COM8
        #                   (or whatever) was opened previously, and if not open it.

        #print("comport real name =", self.comPortObj.getSelectedComPort())

        #if(self.comPortObj.openSelectedComPort()):        # was able to open com port

        self.log_msg(self.scannerLog_Text, "\n***Starting Scan of I2C for Devices***")
        self.update()                                   #allows the updating of the text window

        #self.RS232 = self.comPortObj.getComPortDesc()

        # Enable Stop Button
        self.scanner_Stop_Button_Widget.configure(state='normal')

        magic1 = 0x16
        magic2 = 0xe8
        self.stop = False

        while self.stop == False:
                                #
            #   This sends the command to the serial port. Notice that it is possible that the port
            #   had been previously opened, was unplugged, and then re-plugged in.
            #   In this case, the prior handle would be invalid. The only way to tell is to try
            #   to write to it and see if it fails. This happens within sendCommand, and if the
            #   write fails, it closes the old port, opens it up again to get a valid handle
            #   and then sends the command.
            #   So it has to update the original port handle by returning it. That is what is happening
            #   below.

            RS232=self.comPortObj.sendCommand(bytes([magic1, magic2, 0, 0, READCOMMAND]))

            i = 0


            while i < 127:
                if RS232.in_waiting != 0:
                    if i== 0:
                        throwaway = RS232.read(1)
                    else:
                        response = bytes(RS232.read(1))
                        if response != b'\x00':
                            strResponse = str(hex(ord(response)))
                            if (strResponse in I2Cscanner.knownI2C.keys()):
                                self.log_msg(self.scannerLog_Text, "0x"f'{i:01X}'":  "+I2Cscanner.knownI2C[strResponse])
                            else:
                                self.log_msg(self.scannerLog_Text, "0x"f'{i:01X}'": (found)")
                    i += 1

        #   get checksum sent by radio CAT control
            while RS232.in_waiting == 0:
                sleep(0.01)
            sentCheckSum = int.from_bytes(RS232.read(1),"little",signed=False)

        #   get trailing byte. Must be an ACK (0x00)
            while RS232.in_waiting == 0:
                sleep(0.01)
            trailingByte = int.from_bytes(RS232.read(1),"little",signed=False)

            self.log_msg(self.scannerLog_Text,' ')          #forces a newline between scans
            self.update()                                   #allows the updating of the text window

            sleep(1)

        return

    def enableGoButtonComPort(self):
        self.scanner_Start_Button_Widget.configure(state='normal')

    def disableGoButtonComPort(self):
        self.scanner_Start_Button_Widget.configure(state='disabled')
