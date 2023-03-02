from time import sleep
import tkinter as tk

from wsprmsggenwidget import WsprmsggenWidget
from com_portManager import com_portManager
from globalvars import *
from wsprEncoder import wsprEncoder

class WSPRmsggen(WsprmsggenWidget):


    def __init__(self, num, msg):
        super().__init__()
        self.counter = num
        self.mymessage =msg

    def WSPR_Msg_Gen_Button(self):
        # Clicking the Apply button means we need to update the original ADC values
        self.mymessage.set(wsprEncoder(self.callsign.get(), self.gridSq.get(), int(self.dbm.get())))

        # close the window
        self.destroy()


    def WSPR_Msg_Gen_Cancel_Button(self):
        self.destroy()

