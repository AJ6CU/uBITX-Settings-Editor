import serial.tools.list_ports              # Used to get a list of com ports
from comportmanagerwidget import ComPortmanagerWidget
from time import sleep
from globalvars import *

class com_portManager(ComPortmanagerWidget):


    open_com_ports ={}
    waitTime = 5
    last_com_port_selected = "INVALID"


    def __init__(self, parentContainer, parentHook):
        super().__init__(parentContainer)

        self.parentPtr = parentHook         # need pointer to parent to invoke callback to enable/disable buttons
        self.updateComPorts()               #preload the available com ports


    def openComPort (self, comPort):
        if comPort in com_portManager.open_com_ports.keys():
            return True
        else:
            try:
                RS232 = serial.Serial(comPort, BAUD, timeout=0, stopbits=1, parity=serial.PARITY_NONE, xonxoff=0, rtscts=0)
            except:
                print("failed to open port", RS232)
                return False
            else:
                com_portManager.open_com_ports[comPort] = RS232
                sleep (com_portManager.waitTime)                # if the com port has not been previously opened, must wait for
                                                                # processor to reset.
                return True

    def getComPortPTR (self, comPort):
        return com_portManager.open_com_ports[comPort]


    def updateComPorts(self, *args):
        ports = serial.tools.list_ports.comports()      #Gets list of ports
        self.comPortList =[("Select Serial Port")]           #Seeds option list with Selection instructions

        for p in ports:                                 #this used to strip down to just the com port# or path
            self.comPortList.append(p.device)

        if com_portManager.last_com_port_selected in self.comPortList:      #check whether the last port selected is in list
            self.comPortsOptionMenu.set_menu(*self.comPortList)             #put found ports into the option menu
            self.availableComPorts.set(com_portManager.last_com_port_selected)          #default to last port
            self.parentPtr.enableGoButtonComPort()                          # tell parent to enable the go button
        else:                       # no last valid port, to force selection
            self.comPortsOptionMenu.set_menu("Select Serial Port", *self.comPortList)
            self.parentPtr.disableGoButtonComPort()            # tell parent to disable the go button until valid selection
        return


    def comPortSelected(self, *args):
        com_portManager.last_com_port_selected = self.availableComPorts.get()
        self.parentPtr.enableGoButtonComPort()              # tell parent that it can enable the go button for the process


    def getSelectedComPort(self):
        return self.availableComPorts.get()

