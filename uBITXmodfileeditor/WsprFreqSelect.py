import pygubu.widgets.simpletooltip as tooltip
import tkinter as tk

from wsprfreqselectwidget import WsprfreqselectWidget
from globalvars import *

class WSPRFreqSelect(WsprfreqselectWidget):
    def __init__(self, num, currentValue):

        super().__init__()
        band='30m'
        if currentValue != '':
            self.WSPR_BAND_SELECTION.set(band)
        else:
            band='20m'
            self.WSPR_BAND_SELECTION.set(band)

        self.WSPR_BAND_DESCRIPTION.set(("DIAL: " + '{:,}'.format(WSPRBANDS[band][0]) + " Hz - TX: " +
                                       '{:,}'.format(WSPRBANDS[band][1]) + " Hz thru "  +
                                        '{:,}'.format(WSPRBANDS[band][3])+ " Hz").replace(",","."))
    def WSPR_BAND_SELECTED_CB(self, event=None):
        band = self.WSPR_BAND_SELECTION.get()
        self.WSPR_BAND_DESCRIPTION.set(("DIAL: " + '{:,}'.format(WSPRBANDS[band][0]) + " Hz - TX: " +
                                       '{:,}'.format(WSPRBANDS[band][1]) + " Hz thru "  +
                                        '{:,}'.format(WSPRBANDS[band][3])+ " Hz").replace(",","."))



    def wsprBandSelected(self, option):
        print("wspr band selected")

    def WSPR_SLIDER_MOVED_CB(self, scale_value):
        print("wspr slider moved")

    def WSPR_BAND_OK_Button_CB(self):
        print("wspr OK button clicked")
        self.destroy()

    def WSPR_BAND_CANCEL_Button_CB(self):
        print("wspr Cancel button clicked")
        self.destroy()

    def WSPR_BAND_SELECTION_DEFAULT_CB(self):
        pass