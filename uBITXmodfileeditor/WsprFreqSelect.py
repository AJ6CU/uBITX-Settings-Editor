import pygubu.widgets.simpletooltip as tooltip
import tkinter as tk

from wsprfreqselectwidget import WsprfreqselectWidget
from globalvars import *

class WSPRFreqSelect(WsprfreqselectWidget):
    def getBandFromFreq(self, freq):
        for bands in WSPRBANDS:         #[1] = begin freq of band; [3] = end freq, [2]= central freq
            if (WSPRBANDS[bands][1] <= int(freq)) and (int(freq) <= WSPRBANDS[bands][3]):
                return bands

    def __init__(self, num, freq):

        super().__init__()
        self.freq_ptr = freq

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
        print("wspr OK button clicked")
        self.freq_ptr.set(self.WSPR_CURRENT_FREQUENCY.get())
        self.destroy()

    def WSPR_BAND_CANCEL_Button_CB(self):
        print("wspr Cancel button clicked")
        self.destroy()

    def WSPR_BAND_SELECTION_DEFAULT_CB(self):
        pass