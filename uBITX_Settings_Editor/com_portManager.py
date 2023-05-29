import serial.tools.list_ports              # Used to get a list of com ports

import tkinter.messagebox

from comportmanagerwidget import ComPortmanagerWidget
from time import sleep
from globalvars import *

class com_portManager(ComPortmanagerWidget):


    open_com_ports ={}
    waitTime = 5
    last_com_port_selected = "INVALID"


    def __init__(self, parentContainer, actionButtonStateChange):
        super().__init__(parentContainer)

        self.img_img_Reload24x24 = tk.PhotoImage(file=RELOADICON)
        self.comPortListRefresh.configure(image=self.img_img_Reload24x24)

        self.actionButton_CB = actionButtonStateChange         # Callback function invoked when state change

        self.updateComPorts()               #preload the available com ports
        self.comPortsOptionMenu.configure(width=15)
        #self.comPortsOptionMenu.grid_configure(sticky='e')




    def openSelectedComPort (self):
        comPort = self.getSelectedComPort()                    # get the selected com port
        if comPort in com_portManager.open_com_ports.keys():  #so we have seen this port before.
            return True

        # if we made it to this point, port is either new, or was interrupted and we closed it.

        try:
            RS232 = serial.Serial(comPort, BAUD, timeout=5, stopbits=1, parity=serial.PARITY_NONE, xonxoff=0, rtscts=0)
        except:
            return False
        else:
            com_portManager.open_com_ports[comPort] = RS232
            sleep (com_portManager.waitTime)                # if the com port has not been previously opened, must wait for
                                                            # processor to reset.
            return True

    def resetComPort (self):
        comPort = self.getSelectedComPort()
        try:
            com_portManager.open_com_ports[comPort].close()
        except:
            pass
        del com_portManager.open_com_ports[comPort]
        return self.openSelectedComPort ()

    def getComPortDesc (self):
        return com_portManager.open_com_ports[self.getSelectedComPort()]


    def updateComPorts(self, *args):

        ports = serial.tools.list_ports.comports()          #Gets list of ports
        self.comPortList =[("Select Serial Port")]          #Seeds option list with Selection instructions

        for p in ports:                                 #this used to strip down to just the com port# or path
            self.comPortList.append(p.device)

        if com_portManager.last_com_port_selected in self.comPortList:      #check whether the last port selected is in list
            self.comPortsOptionMenu.set_menu(*self.comPortList)             #put found ports into the option menu
            self.availableComPorts.set(com_portManager.last_com_port_selected)          #default to last port
            self.actionButton_CB('normal')                                  #signal to parent that we have a valid selection
        else:                       # no last valid port, to force selection
            self.comPortsOptionMenu.set_menu("Select Serial Port", *self.comPortList)
            self.actionButton_CB('disabled')                                  #signal to parent that we have a invalid selection
        return


    def comPortSelected(self, *args):
        com_portManager.last_com_port_selected = self.availableComPorts.get()
        self.actionButton_CB('normal')                                  #signal to parent that we have a valid selection


    def getSelectedComPort(self):
        return self.availableComPorts.get()


    def sendCommand (self, theCommand): # DO WE NEED THE PORT AS AN INPUT?ISn't it always the selected port???'
                                          # DEPENDING ON WRITE OR READ ARE DIFFERENT OBJECTS. SO SELECTED PORT SHOULD BE THE PORT FOR
                                           # INPUT OR OUR OUTPUT OR SCANNER
        if(self.openSelectedComPort()):       # Was able to open the com port or it was already openned
            port = self.getComPortDesc()
            try:
                port.write(theCommand)
            except:
                if(self.resetComPort()):     # Successful was able to reset serial port, try again
                    port = self.getComPortDesc()

                    try:                    # Try one more time...
                        port.write(theCommand)
                    except:
                        tkinter.messagebox.showerror(title="ERROR", message="Communication failed to uBITX. Unplug the USB cable, power cycle your radio, reconnect and try again. \nEXITING")
                        sys.exit(-1)
                else:
                        tkinter.messagebox.showerror(title="ERROR", message="Communication failed to uBITX. Unplug the USB cable, power cycle your radio, reconnect and try again. \nEXITING")
                        sys.exit(-1)
            #port.flush()
            return port
        else:
            tkinter.messagebox.showerror(title="ERROR", message="Unexpected error trying to open serial communications to uBITX. Unplug the USB cable, power cycle your radio, reconnect and try again. \nEXITING")
            sys.exit(-1)

