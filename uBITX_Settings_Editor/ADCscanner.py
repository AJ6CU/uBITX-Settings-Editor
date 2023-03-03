#import serial.tools.list_ports              # Used to get a list of com ports
# import tkinter
import pygubu.widgets.simpletooltip as tooltip
from Scanner import Scanner
from com_portManager import com_portManager
# from time import sleep
from globalvars import *

class ADCscanner (Scanner):

    def __init__(self, parent):
        super().__init__(parent)
        self.grab_set()

        self.title("Analog Pin (ADC) Scanner")

        # create com port
        self.comPortObj = com_portManager(self.com_portManager_frame, self)

        # pre-load com ports
        self.comPortObj.updateComPorts()                           # Fill in available Com Ports

        self.comPortObj.pack()                          # make com it visible
                #   add tooltips
        tooltip.create(self.scanner_Go_Button_Widget,"Click to run one scan of the Analog pins.")
        tooltip.create(self.scanner_Done_Button_Widget,"Click when done scanning")
        tooltip.create(self.comPortObj.comPortsOptionMenu,"Select the com port used by your uBITX")
        tooltip.create(self.comPortObj.comPortListRefresh,"Refresh list of available com ports. "+
                                                        "(You can also plug in your uBITX and then refresh list")

    def scannerDone(self):
        self.destroy()

    def scannerStart(self):

        if(self.comPortObj.openComPort(self.comPortObj.getSelectedComPort())):        # was able to open com port
            self.RS232 = self.comPortObj.getComPortPTR(self.comPortObj.getSelectedComPort())
            self.log_msg(self.scannerLog_Text, "\n***Starting ADC Scan***")

            for x in range(8):
                #xB = int_to_bytes(x)
                self.RS232.write(bytes([x, 0, 0, 0, READADC]))
                self.RS232.flush()

                i = 0

                while i < 3:
                    if self.RS232.in_waiting != 0:          # have a byte to read
                        if i == 0:          #got first byte
                            byte1 = self.RS232.read(1)
                        elif i == 1:        #got second byte
                            byte2 = self.RS232.read(1)
                        else:
                            throwaway = self.RS232.read(1)   # last byte is zero
                        i += 1

                adcValue = (ord(byte1)<<8) + ord(byte2)


                # Output value to log
                self.log_msg(self.scannerLog_Text, "A"+str(x)+" = "+str(adcValue))
            return

    def enableGoButtonComPort(self):
        self.scanner_Go_Button_Widget.configure(state='normal')

    def disableGoButtonComPort(self):
        self.scanner_Go_Button_Widget.configure(state='disabled')
