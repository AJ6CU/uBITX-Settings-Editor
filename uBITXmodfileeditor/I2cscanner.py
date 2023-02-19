from Scanner import Scanner
from com_portManager import com_portManager
from time import sleep
from globalvars import *

class I2Cscanner (Scanner):
    # Known I2C devices
    knownI2C={'0x50':'EEPROM', '0x60':'Si5351', '0x27': 'LCD'}

    def __init__(self, parent):
        super().__init__(parent)

        # create com port
        self.comPortObj = com_portManager(self.com_portManager_frame, self)

        # pre-load com ports
        self.comPortObj.updateComPorts()                           # Fill in available Com Ports

        self.comPortObj.pack()                          # make com it visible


    def scannerDone(self):
        self.destroy()

    def scannerStart(self):
        if(self.comPortObj.openComPort(self.comPortObj.getSelectedComPort())):        # was able to open com port
            self.RS232 = self.comPortObj.getComPortPTR(self.comPortObj.getSelectedComPort())

            magic1 = 0x16
            magic2 = 0xe8

            self.RS232.write(bytes([magic1, magic2, 0, 0, READCOMMAND]))
            self.RS232.flush()

            i = 0

            self.log_msg(self.scannerLog_Text, "\n***Starting Scan of I2C for Devices***")
            while i < 127:
                if self.RS232.in_waiting != 0:
                    if i== 0:
                        throwaway = self.RS232.read(1)
                    else:
                        response = bytes(self.RS232.read(1))
                        if response != b'\x00':
                            strResponse = str(hex(ord(response)))
                            if (strResponse in I2Cscanner.knownI2C.keys()):
                                self.log_msg(self.scannerLog_Text, "0x"f'{i:01X}'":  "+I2Cscanner.knownI2C[strResponse])
                            else:
                                self.log_msg(self.scannerLog_Text, "0x"f'{i:01X}'": (found)")
                    i += 1

        #   get checksum sent by radio CAT control
            while self.RS232.in_waiting == 0:
                sleep(0.01)
            sentCheckSum = int.from_bytes(self.RS232.read(1),"little",signed=False)

        #   get trailing byte. Must be an ACK (0x00)
            while self.RS232.in_waiting == 0:
                sleep(0.01)
            trailingByte = int.from_bytes(self.RS232.read(1),"little",signed=False)

            return
    def enableGoButtonComPort(self):
        self.scanner_Go_Button_Widget.configure(state='normal')

    def disableGoButtonComPort(self):
        self.scanner_Go_Button_Widget.configure(state='disabled')
