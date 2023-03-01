import pygubu.widgets.simpletooltip as tooltip
import tkinter as tk

from wsprfreqselectwidget import WsprfreqselectWidget
from globalvars import *

class WSPRFreqSelect(WsprfreqselectWidget):
    def __init__(self, num, currentValue):

        super().__init__()
        if currentValue != '':
            self.WSPR_BAND_SELECTION.set('40m')
        else:
            self.WSPR_BAND_SELECTION.set('20m')
        print("in init for band switch", num)


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