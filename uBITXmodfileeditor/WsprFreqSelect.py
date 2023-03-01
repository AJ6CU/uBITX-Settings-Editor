import pygubu.widgets.simpletooltip as tooltip
import tkinter as tk

from wsprfreqselectwidget import WsprfreqselectWidget
from globalvars import *

class WSPRFreqSelect(WsprfreqselectWidget):
    def __init__(self, num, currentValue):

        super().__init__()

        self.band='20m'
        self.scale_value = 100
        if currentValue != '':
            self.WSPR_BAND_SELECTION.set(self.band)
        else:
            self.band='20m'
            self.WSPR_BAND_SELECTION.set(self.band)
        self.freq = WSPRBANDS[self.band][1] +  self.scale_value
        self.WSPR_CURRENT_FREQUENCY.set(str(self.freq))
        self.WSPR_CURRENT_BANDWIDTH.set(str(1400 + self.scale_value))

        self.WSPR_BAND_DESCRIPTION.set(("DIAL: " + '{:,}'.format(WSPRBANDS[self.band][0]) + " Hz - TX: " +
                                       '{:,}'.format(WSPRBANDS[self.band][1]) + " Hz thru "  +
                                        '{:,}'.format(WSPRBANDS[self.band][3])+ " Hz").replace(",","."))
    def WSPR_BAND_SELECTED_CB(self, event=None):
        self.band = self.WSPR_BAND_SELECTION.get()
        self.WSPR_BAND_DESCRIPTION.set(("DIAL: " + '{:,}'.format(WSPRBANDS[self.band][0]) + " Hz - TX: " +
                                       '{:,}'.format(WSPRBANDS[self.band][1]) + " Hz thru "  +
                                        '{:,}'.format(WSPRBANDS[self.band][3])+ " Hz").replace(",","."))
        self.freq = WSPRBANDS[self.band][1] + self.scale_value
        self.WSPR_CURRENT_FREQUENCY.set(str(self.freq))
        self.WSPR_CURRENT_BANDWIDTH.set(str(1400 + self.scale_value))


    def wsprBandSelected(self, option):
        print("wspr band selected")

    def WSPR_SLIDER_MOVED_CB(self, scale_value):
        self.scale_value = int(float(scale_value))
        self.freq = WSPRBANDS[self.band][1] + self.scale_value
        self.WSPR_CURRENT_FREQUENCY.set(str(self.freq))
        self.WSPR_CURRENT_BANDWIDTH.set(str(1400 + self.scale_value))

    def WSPR_BAND_OK_Button_CB(self):
        print("wspr OK button clicked")
        self.destroy()

    def WSPR_BAND_CANCEL_Button_CB(self):
        print("wspr Cancel button clicked")
        self.destroy()

    def WSPR_BAND_SELECTION_DEFAULT_CB(self):
        pass