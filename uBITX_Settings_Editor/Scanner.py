
from scannerwidget import ScannerWidget
from com_portManager import com_portManager
import pygubu.widgets.simpletooltip as tooltip

class Scanner (ScannerWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.scrollbar1.config(command=self.scannerLog_Text.yview)
        self.scannerLog_Text['yscrollcommand'] = self.scrollbar1.set
        self.protocol("WM_DELETE_WINDOW", self.scannerQuit)             # This is used to catch a window closed event

        # create com port
        self.comPortObj = com_portManager(self.com_portManager_frame, self.on_ComPort_state_change )

        # pre-load com ports
        self.comPortObj.updateComPorts()                           # Fill in available Com Ports

        self.comPortObj.pack()                          # make com it visible
                #   add tooltips
        tooltip.create(self.scanner_Start_Button_Widget,"Click to run continuous scan.")
        tooltip.create(self.scanner_Stop_Button_Widget,"Click to stop scanning")
        tooltip.create(self.scanner_Quit_Button_Widget,"Click to close te scanner window and return to main window")
        tooltip.create(self.comPortObj.comPortsOptionMenu,"Select the com port used by your uBITX")
        tooltip.create(self.comPortObj.comPortListRefresh,"Refresh list of available com ports. "+\
                        "You can also plug in your uBITX and then refresh list")

        self.grab_set()             # make the window model so all keystrokes go there.


    def log_msg(self, txBox, msg:str):
        txBox.config(state="normal")
        txBox.insert("end", msg + "\n")
        txBox.config(state="disabled")
        txBox.see("end")

    def scannerQuit(self):
        self.stop = True
        self.destroy()

    def scannerStop(self):
        self.stop = True
        self.scanner_Stop_Button_Widget.configure(state='disabled')

    def on_ComPort_state_change (self, newState):
        self.scanner_Start_Button_Widget.configure (state=newState)