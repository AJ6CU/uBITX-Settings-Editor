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
        if int(master.VERSION_ADDRESS.get()[1]) < 2:                    # 5 is the start of the 2.0 series
            tkinter.messagebox.showerror("Error", "Calibration Wizard only works with KD8CEC Version 2.0 or later")
            return                  # don't even create the object, just go home

        self.myparent = master
        self.log = log
        super().__init__()

        self.grab_set()                 # grab all events to ensure they come here

        self.BFORate = 5                          # base rate for changing BFO 1 notch left or right. Same as encoder in firmware
        self.CalibrationRate = 8750                 # base rate for changing Calibration 1 notch left or right. Same as encoder in firmware
        self.current_step = -1           # init to first step
        self.currentMASTER_CAL.set("")
        self.currentUSB_CAL.set("")
        self.currentCW_CAL.set("")

        self.steps = [self.calibrationWizardStep0_Frame , self.calibrationWizardStep1_Frame , self.calibrationWizardStep2_Frame,
                      self.calibrationWizardStep3_Frame , self.calibrationWizardStep4_Frame , self.calibrationWizardStep5_Frame,
                      self.calibrationWizardStep6_Frame , self.calibrationWizardStep7_Frame ]
        for s in self.steps:            # hide all the wizard steps initially
            s.grid_forget()
        self.setTooltips()              # Add tooltips
        self.show_step(0)               # this one will show the first (0) step
        self.run_step(0)

        #  create com port. This uses the last com port that was opened (cached)
        self.comPortObj = com_portManager(self.com_portManager_Enclosing_frame, self.on_ComPort_state_change )

        self.comPortObj.pack_forget()                         # make com it visible

    def setTooltips(self):              #collects all the tooltips for the wizard in one place by step
#
        #   Common to all steps
        tooltip.create(self.backButton,"Go back to prior step in the Calibration Wizard")
        tooltip.create(self.nextButton,"Go on to the next step in the Calibration Wizard")
        tooltip.create(self.saveButton,"Saves your changes to EEPROM and reboots your uBITX")
        tooltip.create(self.cancelButton,"Discards all changes, resets EEPROM and radio to original values")

        # Step 1 - Documents existing calibration
        tooltip.create(self.copyExistingCalibrationToClipboard_Button, "Click to copy your existing calibration to the " \
                       + "clipboard where you should then paste it in a document and save it")
        # Step 2 - Provides links to HF Signals Video and Calibration Aid
        tooltip.create(self.CalVideoCopy_Button, "Click to copy the URL for the HF Signals Calibration Video to your clipboard" )
        tooltip.create(self.hfsiganlsBFOTuningAidCopy_Button, "Click to copy the URL for the HF Signals BFO Tuning Aid to your clipboard" )

        # Step 3 - First effort of tuning BFO
        tooltip.create(self.moveFreqLower_Button, "Click to move the audio spectrum to the LEFT" )
        tooltip.create(self.bfo_speed_multiplier_OptionMenu, "Allows you to set the speed of movement of the audio spectrum" )
        tooltip.create(self.moveFreqHigher_Button, "Click to move the audio spectrum to the RIGHT" )
        tooltip.create(self.currentBFOSetting_Entry, "Current BFO Setting (read only)" )

        #step 4 - Calibrating Frequency
        tooltip.create(self.calibrationFreqWWV5MHz_RadioButton, "Click to use the 5MHz WWV signal as a source" )
        tooltip.create(self.calibrationFreqWWV10MHz_RadioButton, "Click to use the 10MHz WWV signal as a source" )
        tooltip.create(self.calibrationFreqWWV15MHz_RadioButton, "Click to use the 15MHz WWV signal as a source" )
        tooltip.create(self.calibrationFreqWWV20MHz_RadioButton, "Click to use the 20MHz WWV signal as a source" )
        tooltip.create(self.calibrationFreqCustom_RadioButton, "Click to specify your own frequency for calibration" )
        tooltip.create(self.calibrationFreqCustomSource_Entry, "Enter your calibration frequency in Hz" )
        tooltip.create(self.calculateMASTER_CAL_Button, "Click to calculate your new Master Calibration value based on "+\
                       "your calibration frequency, VFO and current Master Calibration value")
        tooltip.create(self.currentRadioVFO_Label, "The VFO frequency that the read from your radio after doing the Calculation. " +\
                       "You should doublecheck that it matches what you see on your radio.")
        tooltip.create(self.currentMASTER_CAL_Label, "This is the value of the original MASTER_CAL. (read only)" )
        tooltip.create(self.newMASTER_CAL_Label, "This is the new calculated value for the MASTER_CAL. (read only)" )

        #step 5 - Fine tuning BFO
        tooltip.create(self.fineTunehfsiganlsBFOTuningAidCopy_Button, "Click to copy the URL for the HF Signals BFO Tuning Aid to your clipboard" )
        tooltip.create(self.fineTuneMoveFreqLower_Button, "Click to move the audio spectrum to the LEFT" )
        tooltip.create(self.fineTuneBFOMultiplier_OptionMenu, "Allows you to set the speed of movement of the audio spectrum" )
        tooltip.create(self.fineTuneMoveFreqHigher_Button, "Click to move the audio spectrum to the RIGHT" )
        tooltip.create(self.newBFOSetting_Entry, "New BFO Setting (read only)" )

        #step 6 - Setting the CW BFO
        tooltip.create(self.CWTunehfsiganlsBFOTuningAidCopy_Button, "Click to copy the URL for the HF Signals BFO Tuning Aid to your clipboard" )
        tooltip.create(self.moveCWBFOFreqLower_Button, "Click to move the audio spectrum to the LEFT" )
        tooltip.create(self.CWspeedMultiplier_OptionMenu, "Allows you to set the speed of movement of the audio spectrum" )
        tooltip.create(self.moveCWBFOFreqHigher_Button, "Click to move the audio spectrum to the RIGHT" )
        tooltip.create(self.newCWBFOSetting_Entry, "New CW BFO Setting (read only)" )

        #step 7 - Last check

        tooltip.create(self.finalReviewMasterCalInitial_Label, "Original MASTER_CAL Setting (read only)" )
        tooltip.create(self.finalReviewMasterCalNew_Label, "The New MASTER_CAL Setting (read only)" )

        tooltip.create(self.finalReviewBFOCalInitial_Label, "Original SSB BFO Setting (read only)" )
        tooltip.create(self.finalReviewBFOCalNew_Label, "The New SSB BFO Setting (read only)" )

        tooltip.create(self.finalReviewCWCalInitial_Label, "Original CW BFO Setting (read only)" )
        tooltip.create(self.finalReviewCWCalNew_Label, "The New CW BFO Setting (read only)" )


    def setSaveButtonState(self, newstate):
        self.saveButton.configure(state=newstate)

    def show_step(self, step):                          # Display the screen for the current "step"

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
        elif step == 4:
            self.badFreqEnteredError_Message.pack_forget()

        elif step == 7:
            # last step
            self.backButton.configure(state='normal')
            self.nextButton.configure(state='disabled')

        else:
            # all other steps
            self.backButton.configure(state='normal')
            self.nextButton.configure(state='normal')



    def run_step(self, step):                                       #allows automatic actions to occur on entry to step
        if step == 1:
            self.getInMemoryCalibration()

        elif step == 7:                 # this is the final review step. Highlight any changes
            # configure Save to EEPROM button to allow Save and Exit

            self.setSaveButtonState('normal')

            #   Check each calibration value and highlight any differences from original values
            if self.currentMASTER_CAL.get() != self.newMASTER_CAL.get():
                self.finalReviewMasterCalInitial_Label.configure(style="Heading4.TLabel")
            else:
                self.finalReviewMasterCalInitial_Label.configure(style="Normal.TLabel")     #else necessary because could backup and restore old value
                                                                                            # and then come back to here. Only wanted bolded if value different

            if self.currentUSB_CAL.get() != self.newUSB_CAL.get():
                self.finalReviewBFOCalNew_Label.configure(style="Heading4.TLabel")
            else:
                self.finalReviewBFOCalNew_Label.configure(style="Normal.TLabel")

            if self.currentCW_CAL.get() != self.newCW_CAL.get():
                self.finalReviewCWCalNew_Label.configure(style="Heading4.TLabel")
            else:
                self.finalReviewCWCalNew_Label.configure(style="Normal.TLabel")

    def on_ComPort_state_change (self, newState):           # just a dummy since we are re-using existing com port that was cached
        pass

    def wizardBack(self):                       # Back button
        self.run_step(self.current_step-1)
        self.show_step(self.current_step-1)

    def wizardNext(self):                       # Next button
        self.run_step(self.current_step+1)
        self.show_step(self.current_step+1)


    def wizardSave(self):                       # Save and Exit button
        self.specialgetInMemoryCalibration()
        self.log.println("timestamp", "Saving new values to EEPROM")
        RS232=self.comPortObj.sendCommand(bytes([0, 0, 0, 0, WRITECALVALUESTOEEPROM]))
        self.specialgetInMemoryCalibration()
        print("updating1 USBcal=", self.myparent.USB_CAL.get())
        self.myparent.MASTER_CAL.set(self.newMASTER_CAL.get())                  #update the Setting Editors internal variable
        self.myparent.USB_CAL.set(self.newUSB_CAL.get())                        #update the Setting Editors internal variable
        print("updating2 USBcal=", self.myparent.USB_CAL.get())
        self.myparent.CW_CAL.set(self.newCW_CAL.get())                          #update the Setting Editors internal variable

        self.log.printerror("timestamp", "Rebooting uBITX")
        self.reset_ubitx()
        self.destroy()

    def reset_ubitx(self):                  # Need to reset uBITX to get it to read new values from EEPROm and load in memory copies
        magic1 = 0x4B   # 75 decimal
        magic2 = 0x33   # 51 decimal
        magic3 = 0x51   # 81 decimal
        magic4 = (magic1 + magic2 + magic3) % 256       #checksum calculation

        RS232=self.comPortObj.sendCommand(bytes([magic1, magic2, magic3, magic4, WRITECOMMAND]))
        RS232.flush()


    def wizardCancel(self):                       # Cancel button. Need to undo any changes
        # If any of these cal values are still the empty string, we are still at step 0. Just exit right away.
        if (self.currentMASTER_CAL.get()=="") or (self.currentUSB_CAL.get()=="")  or (self.currentCW_CAL.get()==""):
            self.destroy()
        else:

            answer = tkinter.messagebox.askokcancel(title='Confirm Cancel',
                    message='EEPROM in Memory calibration settings will be reset to original values.',default="cancel", icon="warning")

            if answer :
                self.myparent.MASTER_CAL.set(self.currentMASTER_CAL.get())                    #update the Setting Editors internal variable
                self.myparent.USB_CAL.set(self.currentUSB_CAL.get())                         #update the Setting Editors internal variable
                self.myparent.CW_CAL.set(self.currentCW_CAL.get())

                print("updating USBcal=", self.myparent.USB_CAL.get())

                self.updateCalSetting(self.currentMASTER_CAL, 0, WRITEMASTERCALINMEMORY)      #restore in memory Master_CAL
                self.updateCalSetting(self.currentUSB_CAL, 0, WRITEUSBCALINMEMORY)            #restore in memory USB_CAL
                self.updateCalSetting(self.currentCW_CAL, 0, WRITECWCALINMEMORY)              #restore in memory CW_CAL

                RS232=self.comPortObj.sendCommand(bytes([0, 0, 0, 0, WRITECALVALUESTOEEPROM]))      #write in memory cal to EEPROM

                self.destroy()


    def getVFOinfo(self):
        #
        #   Gets the current setting for the VFO. This is used in calculating the MASTER_CAL (frequency calibration)
        #

        returnVal= {"freq":1, "mode":1}           #returning a dictionary with frequency and mode used

        i = 0
        totalBytes = 4         # 5 total bytes, 4 for freq, 1 for mode
        tempBytes = [0,0,0,0]   #temp storage for the 32 bits values we read in.

        RS232=self.comPortObj.sendCommand(bytes([0, 0, 0, 0, READVFO]))
        while i < totalBytes:
            lastReadTime = millis()

            if RS232.in_waiting != 0:          # have a byte to read
                lastReadTime = millis()                 #reset time out clock

                tempBytes[i] = RS232.read(1)
                i += 1
            else:
                if (millis() - lastReadTime > SERIALTIMEOUT):
                    self.log.printerror("timestamp",  "**ERROR**: Timeout communicating with uBTIX.")
                    self.log.printerror("timestamp",  "Check your port selection and try again.")
                    return 0

        return (ord(tempBytes[0])+ (ord(tempBytes[1])<<8)  + (ord(tempBytes[2])<<16) + (ord(tempBytes[3])<<24))



    def getInMemoryCalibration(self):
        #
        #   After the EEPROM values are read in, the software makes local copies to use. These values can be different
        #   than the EEPROM values if the EEPROM values are not valid for the particular uBITX board
        #   or some tuning of the values have been done. e.g. This is what this wizard does until you Save them or Cancel
        #

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

                    bcount += 1
                    i += 1
                else:
                    if (millis() - lastReadTime > SERIALTIMEOUT):
                        self.log.printerror("timestamp",  "**ERROR**: Timeout communicating with uBTIX.")
                        self.log.printerror("timestamp",  "Check your port selection and try again.")

                        return
            bcount = 0

            newValue = ord(tempBytes[0])+ (ord(tempBytes[1])<<8)  + (ord(tempBytes[2])<<16) + (ord(tempBytes[3])<<24)

            #newValue = str(int.from_bytes(bytes(tempBytes), "little", signed=False))
            if i < 5:
                if newValue & 0x80000000:   #   Master Cal can be negative,so decode it from 2's complement
                    newValue = -((~newValue+1)& 0xffffffff)

                self.currentMASTER_CAL.set(str(newValue))
                self.newMASTER_CAL.set(str(newValue))
            elif i< 9:
                self.currentUSB_CAL.set(str(newValue))
                self.newUSB_CAL.set(str(newValue))
            else:
                self.currentCW_CAL.set(str(newValue))
                self.newCW_CAL.set(str(newValue))

            if i == totalBytes:
                throwaway = RS232.read(1)   # last byte is zero

        return
    def specialgetInMemoryCalibration(self):
        #
        #   After the EEPROM values are read in, the software makes local copies to use. These values can be different
        #   than the EEPROM values if the EEPROM values are not valid for the particular uBITX board
        #   or some tuning of the values have been done. e.g. This is what this wizard does until you Save them or Cancel
        #

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

                    bcount += 1
                    i += 1
                else:
                    if (millis() - lastReadTime > SERIALTIMEOUT):
                        self.log.printerror("timestamp",  "**ERROR**: Timeout communicating with uBTIX.")
                        self.log.printerror("timestamp",  "Check your port selection and try again.")

                        return
            bcount = 0

            newValue = ord(tempBytes[0])+ (ord(tempBytes[1])<<8)  + (ord(tempBytes[2])<<16) + (ord(tempBytes[3])<<24)

            #newValue = str(int.from_bytes(bytes(tempBytes), "little", signed=False))
            if i < 5:
                if newValue & 0x80000000:   #   Master Cal can be negative,so decode it from 2's complement
                    newValue = -((~newValue+1)& 0xffffffff)
                print("master cal in memory =", newValue)
                # self.currentMASTER_CAL.set(str(newValue))
                # self.newMASTER_CAL.set(str(newValue))
            elif i< 9:
                print("new usb cal in memory =", newValue)
                # self.currentUSB_CAL.set(str(newValue))
                # self.newUSB_CAL.set(str(newValue))
            else:
                print("new cwcal in memory =", newValue)
                # self.currentCW_CAL.set(str(newValue))
                # self.newCW_CAL.set(str(newValue))

            if i == totalBytes:
                throwaway = RS232.read(1)   # last byte is zero

        return

    def copyExistingCalibrationToClipboard(self):       # callback for the copy to clipboard of existing values
        calValues = "Master Calibration: " + self.currentMASTER_CAL.get() +"\n"\
                    "SSB BFO: "+ self.currentUSB_CAL.get() + "\n" +\
                    "CW BFO: "+ self.currentCW_CAL.get() + "\n"

        copyLogToClipboard(calValues)


    def copyCalVideoToClipboard(self):                  # this copies to clipboard callback for the HF video link
        copyLogToClipboard(self.hfsignalsCalVideoLink.get())

    def copyTuningAidLinkToClipboard(self):             # this copies to clipboard the link for the HF Signals BFO Tuning Aid
        copyLogToClipboard(self.hfsignalsBFOTuningAid.get())


    # Step 2 Call backs

    def updateCalSetting(self, calValue, offset, catCommand):   # General tool o update in memory Calibration values
        newValue = int(calValue.get()) + offset
        calValue.set(str(newValue))
        self.setSaveButtonState('normal')                      # info is dirty because a change was made, enable save


        byte1 = newValue & 0xff
        byte2 = (newValue >> 8)  & 0xff
        byte3 = (newValue >> 16)  & 0xff
        byte4 = (newValue >> 24)  & 0xff
        RS232=self.comPortObj.sendCommand(bytes([byte1, byte2, byte3, byte4, catCommand]))

    def moveFreqLower_CB(self):         # Callback for left arrow in the SSB BFO tuning screen
        self.updateCalSetting(self.newUSB_CAL, +self.BFORate * int(self.bfo_speed_multiplier.get().lstrip("X")), WRITEUSBCALINMEMORY)

    def moveFreqLHigher_CB(self):       # Callback for right arrow in the SSB BFO tuning screen
        self.updateCalSetting(self.newUSB_CAL, -self.BFORate * int(self.bfo_speed_multiplier.get().lstrip("X")), WRITEUSBCALINMEMORY)

    def moveCWBFOFreqLower_CB(self):    # Callback for left arrow in the CW BFO tuning screen
        self.updateCalSetting(self.newCW_CAL, +self.BFORate * int(self.CWbfo_speed_mulitpier.get().lstrip("X")), WRITECWCALINMEMORY)

    def moveCWBFOFreqLHigher_CB(self):  # Callback for right arrow in the CW BFO tuning screen
        self.updateCalSetting(self.newCW_CAL, -self.BFORate * int(self.CWbfo_speed_mulitpier.get().lstrip("X")), WRITECWCALINMEMORY)

    def calculateMASTER_CAL(self):      # Does the work of calculating new Master_Cal value

        self.badFreqEnteredError_Message.pack_forget()      # hide the error message for a bad custom freq entry

        # Determine target frequency

        sourceFreq = 0                      #initialize to nothing

        if self.freqSelectButton.get() == "WWV5":
            sourceFreq = 5000000
        elif self.freqSelectButton.get() == "WWV10":
            sourceFreq = 10000000
        elif self.freqSelectButton.get() == "WWV15":
            sourceFreq = 15000000
        elif self.freqSelectButton.get() == "WWV20":
            sourceFreq = 20000000
        elif self.freqSelectButton.get() == "CUSTOM":  ## work on validateion...
            testValue = self.customSourceFreq.get().translate({ord(c): None for c in" .,"})
            if testValue.isdigit() and testValue != '0':
                sourceFreq = int(testValue)
                if sourceFreq > 60000000:
                    self.badFreqEnteredError_Message.pack()
                    self.customSourceFreq.set("0")
            else:
                self.badFreqEnteredError_Message.pack()
                self.customSourceFreq.set("0")

        #   if the source frequency is "0", we have a custom freq with bad data. so do nothing.

        if sourceFreq != 0:
            #   Get the value of the current VFO

            self.currentVFOFreq.set(self.getVFOinfo())
            val = (round(875000000/int(self.currentVFOFreq.get())) * (sourceFreq - int(self.currentVFOFreq.get())))+int(self.currentMASTER_CAL.get())
            val = ((round(875000000/sourceFreq)) * (sourceFreq - int(self.currentVFOFreq.get())))+int(self.currentMASTER_CAL.get())
            self.newMASTER_CAL.set(str(val))

            self.updateCalSetting(self.newMASTER_CAL, 0, WRITEMASTERCALINMEMORY)            #change the master cal in memory


