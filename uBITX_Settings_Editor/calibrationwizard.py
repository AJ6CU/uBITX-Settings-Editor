#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from com_portManager import com_portManager
import pygubu.widgets.simpletooltip as tooltip
from calibrationwizardwidget import CalibrationWizardWidget
from printtolog import *
from globalvars import *


class calibrationWizard(CalibrationWizardWidget):

    def __init__(self, log, master=None, **kw):
        print("calibration wizard subclass called")

        self.myparent = master
        self.log = log
        super().__init__()
        self.current_step = -1           # init to first step
        self.steps = [self.calibrationWizardStep0_Frame , self.calibrationWizardStep1_Frame , self.calibrationWizardStep2_Frame ]
        for s in self.steps:            # hide all the wizard steps initially
            s.grid_forget()
        self.show_step(0)               # this one will show the first (0) step
        self.run_step(0)

        #  create com port
        print(" creating com port")
        self.comPortObj = com_portManager(self.com_portManager_Enclosing_frame, self.on_ComPort_state_change )
        print("com port loaded, updating list")

        # pre-load com ports
        self.comPortObj.updateComPorts()                           # Fill in available Com Ports
        print("lsit updated")

        self.comPortObj.pack()                         # make com it visible
        print("exiting init")


    def show_step(self, step):

        if self.current_step != -1:
            # remove current step
            current_step = self.steps[self.current_step]
            current_step.grid_forget()

        self.current_step = step

        new_step = self.steps[self.current_step]
        new_step.grid(row=0, column=0)

        if step == 0:
            # first step
            self.backButton.configure(state='disabled')
            self.saveButton.configure(state='disabled')

        elif step == len(self.steps)-1:
            # last step
            self.backButton.configure(state='normal')
            self.nextButton.configure(state='disabled')

        else:
            # all other steps
            self.backButton.configure(state='normal')
            self.nextButton.configure(state='normal')
            self.saveButton.configure(state='normal')

    def run_step(self, step):
        if step == 0:
            print("doing step# ", step)
        elif step == 1:
            print("doing step# ", step)
            self.getInMemoryCalibration()

        elif step == 2:
            print("doing step# ", step)

    def on_ComPort_state_change (self, newState):
        pass


    def wizardBack(self):
        self.run_step(self.current_step-1)
        self.show_step(self.current_step-1)


    def wizardNext(self):
        self.run_step(self.current_step+1)
        self.show_step(self.current_step+1)


    def wizardSave(self):
        print("wizard save called")

    def wizardCancel(self):
        print("wizard cancel called")
        self.destroy()


    def getInMemoryCalibration(self):
        #
        #   Some definitions might be helpful here...
        #
        #   self.comPortObj  is a handle to the comport that was openned when the eeprom was first read in
        #                    in most cases, this should be still openned and can be directly read.
        #   self.comPortObj.getSelectedComPort()  returns the name of the com port. e.g. COM8
        #
        #   so self.comPOrtObj.openSelectedComPort(self.comPortObj.getSelected()) is equivalent to asking whether COM8
        #                   (or whatever) was opened previously, and if not open it.

        i = 0
        totalBytes = 12         # long: master cal, usbbfo, and cwbfo + one ack byte
        tempBytes = [0,0,0,0]   #temp storage for the 32 bits values we read in.

        RS232=self.comPortObj.sendCommand(bytes([0, 0, 0, 0, READCALINMEMORY]))
        while i < totalBytes:


            bcount = 0
            lastReadTime = millis()

            while bcount < 4:
                if RS232.in_waiting != 0:          # have a byte to read
                    lastReadTime = millis()                 #reset time out clock

                    tempBytes[bcount] = RS232.read(1)
                    print("bcount=", bcount, "readvalue=", tempBytes[bcount])

                    bcount += 1
                    i += 1
                else:
                    if (millis() - lastReadTime > SERIALTIMEOUT):
                        self.log.printerror("timestamp",  "**ERROR**: Timeout communicating with uBTIX.")
                        self.log.printerror("timestamp",  "Check your port selection and try again.")

                        return
            bcount = 0

            print("tempbytes=",tempBytes)
            #newValue = int(ord(tempBytes[0])+ ord(tempBytes[1])*256  + ord(tempBytes[2])*65536 + ord(tempBytes[3])*16777216)
            newValue = ord(tempBytes[0])+ (ord(tempBytes[1])<<8)  + (ord(tempBytes[2])<<16) + (ord(tempBytes[3])<<24)
            print("newval=", newValue)

            #newValue = str(int.from_bytes(bytes(tempBytes), "little", signed=False))
            if i < 5:
                self.currentMasterCal.set(str(newValue))
            elif i< 9:
                self.currentSSBBFO.set(str(newValue))
            else:
                self.currentCWBFO.set(str(newValue))

            if i == totalBytes:
                throwaway = RS232.read(1)   # last byte is zero
                print("throway =", throwaway)

        return


