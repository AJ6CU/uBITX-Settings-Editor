from time import sleep
import tkinter as tk
import pygubu.widgets.simpletooltip as tooltip
import re

from printtolog import *
from wsprmsggenwidget import WsprmsggenWidget
from com_portManager import com_portManager
from globalvars import *
from wsprEncoder import wsprEncoder

class WSPRmsggen(WsprmsggenWidget):

    priorValues={}

    def __init__(self, num, msg, log):
        super().__init__()
        self.grab_set()         # Make the window model to prevent multiple clicks

        self.counter = num
        self.mymessage =msg

        self.log = log

        tooltip.create(self.callsign_WIDGET,"Enter your callsign for WSPR. Maximum of 6 characters. 1st character number, letter, blank, 2nd: letter or number "+
                       "3rd: Must be a number, 4-6 can be a letter or blank")
        tooltip.create(self.gridSq_WIDGET,"Enter 4 charcter grid square locator (e.g.CM87)")
        tooltip.create(self.dbm_WIDGET,"Enter power level in dbm 0 -60)")
        tooltip.create(self.WSPR_Msg_Gen_Button_WIDGET,"Click to generate a WSPR message")
        tooltip.create(self.WSPR_Msg_Gen_Cancel_Button_WIDGET,"Click to cancel the operation and return to prior screen.")


    def validate_WSPR_callsign(self, p_entry_value, v_condition):
        if  (re.match("^[0-9a-zA-Z]{,1}[a-zA-Z0-9][0-9][a-zA-Z]{,3}$",p_entry_value.strip())):
            self.callsign.set(p_entry_value.strip())
            return True

        # if we reach this point, there is an error...
        self.log.printerror("timestamp", "WSPR Callsign must be <6 characters, first letter or number or left blank " +
                            " character letter or number, third must be a number, and last 3 characters letters or blanks.\n")
        self.callsign.set("")
        return False

    def validate_WSPR_gridSq(self, p_entry_value, v_condition):
        if  (re.match("^[a-zA-Z]{2}[0-9]{2}$",p_entry_value.strip())):
            self.gridSq.set(p_entry_value.strip())
            return True

        # if we reach this point, there is an error...
        self.log.printerror("timestamp", "Invalid Maidenhead Grid Square entered. Valid GRID squares are two letters followed by two numbers.\n")
        self.gridSq.set("")
        return False

    def validate_WSPR_dbm(self, p_entry_value, v_condition):
        if  (re.match("^[0-9]{1,2}$",p_entry_value.strip())):
            if ((int(p_entry_value.strip()) > -1)) & (int(p_entry_value.strip()) < 61):
                self.dbm.set(p_entry_value.strip())
                return True

        # if we reach this point, there is an error...
        self.log.printerror("timestamp", "Invalid dbm value entered. Valid values are 0-60.\n")
        self.dbm.set("10")
        return False

    def WSPR_Msg_Gen_Button(self):
        # Clicking the Apply button means we need to update the original ADC values
        self.mymessage.set(wsprEncoder(self.callsign.get(), self.gridSq.get(), int(self.dbm.get())))

        # close the window
        self.destroy()


    def WSPR_Msg_Gen_Cancel_Button(self):
        self.destroy()

