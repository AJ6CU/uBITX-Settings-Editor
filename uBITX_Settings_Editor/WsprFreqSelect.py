import pygubu.widgets.simpletooltip as tooltip
import tkinter as tk

from wsprfreqselectwidget import WsprfreqselectWidget
from calcRegisters import buildWSPRRegs
from globalvars import *

class WSPRFreqSelect(WsprfreqselectWidget):
    def getBandFromFreq(self, freq):
        for bands in WSPRBANDS:         #[1] = begin freq of band; [3] = end freq, [2]= central freq
            if (WSPRBANDS[bands][1] <= int(freq)) and (int(freq) <= WSPRBANDS[bands][3]):
                return bands

    def __init__(self, cal, freq,  reg1, reg2, reg3):

        super().__init__()

        self.grab_set()                 # Make the window modal to prevent multiple clicks
        self.cal = cal
        self.freq_ptr = freq
        self.reg1_ptr = reg1            # controller for frequency
        self.reg2_ptr = reg2            # for final divider for s5351
        self.reg3_ptr = reg3            # Multichan/wsprsidetone
        #
        #   Set the tooltips for this window
        #
        tooltip.create(self.WSPR_BAND_SELECTION_WIDGET,"First select the desired band to use for WSPR")
        tooltip.create(self.WSPR_SLIDER_MOVED_WIDGET,"Slider moves TX off center (default) frequency")
        tooltip.create(self.WSPR_BAND_OK_Button_WIDGET,"Click to use this date and return to prior screen.")
        tooltip.create(self.WSPR_BAND_CANCEL_Button_WIDGET,"Click to cancel the operation and return to prior screen.")

        currentFreq = self.freq_ptr.get().replace(".","")

        if currentFreq == '':                   #   Empty value, so go for the default band and center frequency
            theBand = DEFAULTWSPRBAND
            self.WSPR_BAND_SELECTION.set(theBand)
            self.WSPR_SLIDER.set(str(DEFAULTWSPRTONE))
            theFreq = WSPRBANDS[theBand][1] +  int(self.WSPR_SLIDER.get())

        else:                                   #   Existing value, set from input
            theBand = self.getBandFromFreq(int(currentFreq))
            self.WSPR_BAND_SELECTION.set(theBand)
            self.WSPR_SLIDER.set(str(float(int(currentFreq) - WSPRBANDS[theBand][1])))
            theFreq = currentFreq

        self.WSPR_CURRENT_FREQUENCY.set('{:,}'.format(int(float(theFreq))).replace(",","."))
        self.WSPR_CURRENT_BANDWIDTH.set('{:,}'.format(1400 + int(float(self.WSPR_SLIDER.get()))).replace(",","."))

        self.WSPR_BAND_DESCRIPTION.set(("DIAL: " + '{:,}'.format(WSPRBANDS[theBand][0]) + " Hz - TX: " +
                                       '{:,}'.format(WSPRBANDS[theBand][1]) + " Hz thru "  +
                                        '{:,}'.format(WSPRBANDS[theBand][3])+ " Hz").replace(",","."))

    def WSPR_BAND_SELECTED_CB(self, event=None):
        theBand = self.WSPR_BAND_SELECTION.get()
        self.WSPR_BAND_DESCRIPTION.set(("DIAL: " + '{:,}'.format(WSPRBANDS[theBand][0]) + " Hz - TX: " +
                                       '{:,}'.format(WSPRBANDS[theBand][1]) + " Hz thru "  +
                                        '{:,}'.format(WSPRBANDS[theBand][3])+ " Hz").replace(",","."))
        theFreq = WSPRBANDS[theBand][1] + int(float(self.WSPR_SLIDER.get()))
        self.WSPR_CURRENT_FREQUENCY.set('{:,}'.format(theFreq).replace(",","."))
        self.WSPR_CURRENT_BANDWIDTH.set('{:,}'.format(1400 + int(float(self.WSPR_SLIDER.get()))).replace(",","."))


    def WSPR_SLIDER_MOVED_CB(self, scale_value):
        self.scale_value = int(float(scale_value))
        theFreq = WSPRBANDS[self.WSPR_BAND_SELECTION.get()][1] + self.scale_value
        self.WSPR_CURRENT_FREQUENCY.set('{:,}'.format(theFreq).replace(",","."))
        self.WSPR_CURRENT_BANDWIDTH.set('{:,}'.format(1400 + int(float(scale_value))).replace(",","."))

    def WSPR_BAND_OK_Button_CB(self):
        # print("wspr OK button clicked")
        self.freq_ptr.set(self.WSPR_CURRENT_FREQUENCY.get())
        newregs = buildWSPRRegs ( int(self.WSPR_CURRENT_FREQUENCY.get().replace(".","")), self.WSPR_BAND_SELECTION.get(), int(self.cal))
        self.reg1_ptr.set(newregs[0])
        # print ('newregs=', newregs[0], self.reg1_ptr.get())
        self.reg2_ptr.set(newregs[1])
        self.reg3_ptr.set(newregs[2])
        self.destroy()

    def WSPR_BAND_CANCEL_Button_CB(self):
        self.destroy()
