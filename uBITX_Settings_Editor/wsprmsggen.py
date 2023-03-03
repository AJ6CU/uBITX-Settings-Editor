from time import sleep
import tkinter as tk
import pygubu.widgets.simpletooltip as tooltip

from wsprmsggenwidget import WsprmsggenWidget
from com_portManager import com_portManager
from globalvars import *
from wsprEncoder import wsprEncoder

class WSPRmsggen(WsprmsggenWidget):


    def __init__(self, num, msg):
        super().__init__()
        self.grab_set()         # Make the window model to prevent multiple clicks

        self.counter = num
        self.mymessage =msg

        tooltip.create(self.callsign_WIDGET,"Enter your callsign for WSPR. Maximum of 6 characters. 1st character number, letter, blank, 2nd: letter or number "+
                       "3rd: Must be a number, 4-6 can be a letter or blank")
        tooltip.create(self.gridSq_WIDGET,"Enter 4 charcter grid square locator (e.g.CM87)")
        tooltip.create(self.dbm_WIDGET,"Enter power level in dbm 0 -60)")
        tooltip.create(self.WSPR_Msg_Gen_Button_WIDGET,"Click to generate a WSPR message")
        tooltip.create(self.WSPR_Msg_Gen_Cancel_Button_WIDGET,"Click to cancel the operation and return to prior screen.")

    def WSPR_Msg_Gen_Button(self):
        # Clicking the Apply button means we need to update the original ADC values
        self.mymessage.set(wsprEncoder(self.callsign.get(), self.gridSq.get(), int(self.dbm.get())))

        # close the window
        self.destroy()


    def WSPR_Msg_Gen_Cancel_Button(self):
        self.destroy()

