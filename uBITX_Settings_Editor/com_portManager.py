import serial.tools.list_ports              # Used to get a list of com ports

import tkinter.messagebox
from PIL import Image
from PIL import ImageTk

from comportmanagerwidget import ComPortmanagerWidget
from time import sleep
from globalvars import *

def _is_usb_port(device):
    """A USB serial adapter's name on Linux and macOS (Windows' COM names
    say nothing, so they sort by name)."""
    name = device.rsplit("/", 1)[-1]
    return name.startswith(("ttyUSB", "ttyACM", "cu.usb", "cu.wchusb", "cu.SLAB", "tty.usb"))


def _is_real_port(port):
    """False for a serial slot the kernel reserves but nothing drives, which
    pyserial reports with "n/a" for both its description and its hardware
    id (the unused /dev/ttyS* on Linux)."""
    return not (getattr(port, "description", "") == "n/a" and getattr(port, "hwid", "") == "n/a")


def _looks_like_port(text):
    """Something a user could mean as a port: a device path or a COM name,
    not the prompt or nothing."""
    text = (text or "").strip()
    return text.startswith("/dev/") or (text.upper().startswith("COM") and text[3:].isdigit())


class com_portManager(ComPortmanagerWidget):


    open_com_ports ={}
    waitTime = 5
    last_com_port_selected = "INVALID"


    def __init__(self, parentContainer, actionButtonStateChange):
        super().__init__(parentContainer)

        self.img_img_Reload24x24 = ImageTk.PhotoImage(Image.open(RELOADICON))
        self.comPortListRefresh.configure(image=self.img_img_Reload24x24)

        self.actionButton_CB = actionButtonStateChange         # Callback function invoked when state change

        self.updateComPorts()               #preload the available com ports
        # FIX (2026-11-19): a list you can also TYPE into. A port the system
        # has but pyserial does not list (seen on Ubuntu 26.04: /dev/ttyUSB0
        # there and openable, yet missing from the list) can be typed in --
        # /dev/ttyUSB0, COM7, /dev/cu.usbserial-1410 -- so a missing entry
        # never blocks a read.
        self.comPortsOptionMenu.configure(width=20)
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
        # FIX (2026-11-19): USB adapters first -- the radio is one; the PC's
        # own serial ports (ttyS*, COM1) after them.
        # FIX (2026-11-19): AND ONLY PORTS THAT ARE THERE. Ubuntu 26.04
        # reports all 32 of the kernel's ttyS slots, most with no hardware
        # behind them ("n/a"); with ttyUSB0 listed after them, it fell off
        # the bottom of the screen (PA1CJT: "33 ports found"). A slot with
        # nothing behind it is left out; a port typed in is still used.
        found = sorted((p.device for p in ports if _is_real_port(p)),
                       key=lambda d: (not _is_usb_port(d), d))
        self.comPortList = list(found)
        self.comPortsOptionMenu.configure(values=self.comPortList)

        last = com_portManager.last_com_port_selected
        if last in self.comPortList or _looks_like_port(last):
            # The last port chosen -- listed, or typed in by hand (FIX: kept
            # even when the list does not show it, see above).
            self.availableComPorts.set(last)
            self.actionButton_CB('normal')                                  #signal to parent that we have a valid selection
        else:                       # no last valid port, to force selection
            self.availableComPorts.set("Select Serial Port")
            self.actionButton_CB('disabled')                                  #signal to parent that we have a invalid selection
        return


    def comPortSelected(self, *args):
        com_portManager.last_com_port_selected = self.availableComPorts.get()
        self.actionButton_CB('normal')                                  #signal to parent that we have a valid selection

    def comPortTyped(self, *args):
        # FIX (2026-11-19): a port typed in counts as chosen once it looks
        # like one; anything else (empty, the prompt) leaves the action
        # buttons off.
        typed = self.availableComPorts.get().strip()
        if _looks_like_port(typed):
            com_portManager.last_com_port_selected = typed
            self.actionButton_CB('normal')
        else:
            self.actionButton_CB('disabled')


    def getSelectedComPort(self):
        return self.availableComPorts.get().strip()


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

