#import serial.tools.list_ports              # Used to get a list of com ports
import tkinter as tk
import pygubu.widgets.simpletooltip as tooltip
from Scanner import Scanner
# from com_portManager import com_portManager
from time import sleep
from globalvars import *

class ADCscanner (Scanner):

    def __init__(self, listOfPins, parent):
        super().__init__(parent)
        self.listOfPins = listOfPins    #the class handles a list of pins (i.e., ["CW KEYer", "ENC SW"], etc.)

        self.title("Scan Analog Pin(s)")
        #self.iconbitmap(WINDOWMANAGERICON)


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
        self.log_msg(self.scannerLog_Text, "\n***Starting ADC Scan***")
        self.update()                                   #allows the updating of the text window

        # self.RS232 = self.comPortObj.getComPortDesc()


        # Enable Stop Button
        self.scanner_Stop_Button_Widget.configure(state='normal')

        self.stop = False
        while self.stop == False:
            for aPin in self.listOfPins:
                #
                #   This sends the command to the serial port. Notice that it is possible that the port
                #   had been previously opened, was unplugged, and then re-plugged in.
                #   In this case, the prior handle would be invalid. The only way to tell is to try
                #   to write to it and see if it fails. This happens within sendCommand, and if the
                #   write fails, it closes the old port, opens it up again to get a valid handle
                #   and then sends the command.
                #   So it has to update the original port handle by returning it. That is what is happening
                #   below.
                RS232=self.comPortObj.sendCommand(bytes([ANALOGPINS[aPin], 0, 0, 0, READADCDATA]))

                i = 0
                lastReadTime = millis()

                while i < 3:
                    if RS232.in_waiting != 0:          # have a byte to read
                        lastReadTime = millis()                 #reset time out clock
                        if i == 0:          #got first byte
                            byte1 = RS232.read(1)
                        elif i == 1:        #got second byte
                            byte2 = RS232.read(1)
                        else:
                            throwaway = RS232.read(1)   # last byte is zero
                        i += 1
                    else:
                        if (millis() -lastReadTime > SERIALTIMEOUT):
                            self.log_msg(self.scannerLog_Text, "**ERROR**: Timeout communicating with uBTIX.")
                            self.log_msg(self.scannerLog_Text, "Check your port selection and try again.")
                            return

                adcValue = (ord(byte1)<<8) + ord(byte2)


                # Output value to log
                self.log_msg(self.scannerLog_Text, aPin.ljust(10) +str(adcValue).rjust(4))

            self.log_msg(self.scannerLog_Text,' ')          #forces a newline between scans
            self.update()                                   #allows the updating of the log window
            sleep(1)      # one second interval between reports.
        return

    def enableGoButtonComPort(self):
        self.scanner_Start_Button_Widget.configure(state='normal')


    def disableGoButtonComPort(self):
        self.scanner_Start_Button_Widget.configure(state='disabled')

