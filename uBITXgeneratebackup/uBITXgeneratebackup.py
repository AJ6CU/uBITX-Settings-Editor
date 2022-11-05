#from typing import Any
import tkinter.messagebox


import serial
#import functools
from time import sleep
import time

import platform
from os.path import exists


from globalvars import *
from backup_userconfig import *
from readEEPROMData import readEEPROMData
from helpsubsystem import *
from fonts import *

from tkinter import *
from tkinter import ttk                     # has to be in this order so that ttk comes after general import of tkinter
                                            # this ensures that the style/themed (ttk) widgets are used
import serial.tools.list_ports              # Used to get a list of com ports
from tkinter import filedialog as fd


# Set any platform specific variables
if(platform.system()=='Windows'):
    appTheme = 'vista'
    startDir = "~\Documents"
elif (platform.system() == 'Darwin'):
    appTheme = 'aqua'
    startDir = "~"
else:
    appTheme = 'default'
    startDir = "~"



#   Callbacks ("command") function defintions

def backupFileSelect():
    global BACKUPFILE, fileName, startDir
    filetypes = (
        ('uBITX Backup File', '*.btx'),
        ('All files', '*.*')
    )
    tmpFName = fd.asksaveasfilename(
        title='Backup file',
        initialdir=startDir,
        defaultextension='.btx',
        filetypes=filetypes,
        confirmoverwrite=False)
    if tmpFName != "":
        BACKUPFILE = tmpFName
        fileName.delete(0,END)
        fileName.insert(0,BACKUPFILE)


def comPortSelected(value):
    global COM_PORT
    COM_PORT = value

def updateComPorts(comPortOptions, comPort):
    global COM_PORT
    ports = serial.tools.list_ports.comports()      #Gets list of ports
    comPortList =[("Select Serial Port")]           #Seeds option list with Selection instructions

    for p in ports:                                 #this used to strip down to just the com port# or path
        comPortList.append(p.device)

    comPortOptions.set_menu("Select Serial Port", *comPortList)     #updates the list
    COM_PORT = "COM PORT"     #reset COM_PORT to an illegal value



def printlnToLog(lineToLog):
    printToLog(lineToLog + '\n')

def printToLog(textToLog):
    global logBox
    logBox.insert(END, textToLog)

def get_time_stamp():
    return time.strftime('%D %T')

def copyLogToClipboard():
    global logBox
    logBox.clipboard_clear()
    logBox.clipboard_append(logBox.get("1.0",END))
    #logBox.update()


def backup():                   # This actually performs the backup
    # First doublecheck that we are not overwriting a file, and if so, confirm it is ok
    if (exists(BACKUPFILE)):
        response = tkinter.messagebox.askquestion(title="Warning", message=BACKUPFILE + " already exists.\nDo you want to replace it?", icon='warning')
        if response == 'no' :
            backupFileSelect()
        else:
#           All set, perform backup

            printlnToLog(get_time_stamp() + ": ***Starting backup of device on " + COM_PORT + "***")
            try:
                RS232 = serial.Serial(COM_PORT, BAUD, timeout=0, stopbits=1, parity=serial.PARITY_NONE, xonxoff=0, rtscts=0)
            except:
                printlnToLog(get_time_stamp() + ": " + COM_PORT + " not selected or no device attached")
                printlnToLog(get_time_stamp() + ": ***Backup Aborted***")
                printlnToLog(" ")                     #print blank line in case backup run again
                printlnToLog(" ")                     #print blank line in case backup run again
                tkinter.messagebox.showerror("Error", message="COM Port not selected or no device attached")
            else:
                sleep(3)  #this is required to allow Nano to reset after open

                printlnToLog(get_time_stamp() + ": Reading EEPROM into buffer")
                EEPROMBuffer=readEEPROMData(RS232, 0, EEPROMSIZE)       #Read the EEPROM into memory
                printlnToLog(get_time_stamp() + ": EEPROM read into buffer")

                printlnToLog(get_time_stamp() + ": Writing EEPROM to: " + BACKUPFILE)
                backup = open(BACKUPFILE, "wb")
                backup.write(bytearray(EEPROMBuffer))

                printlnToLog(get_time_stamp() + ": Making file compatible with uBITX Memory Manager V1")
                backup.write(b"\0"* (BACKUPFILESIZE-EEPROMSIZE))

                backup.close()
                RS232.close()
                printlnToLog(get_time_stamp() + ": ***Backup Successfully Completed***")
                printlnToLog(" ")                     #print blank line in case backup run again
                printlnToLog(" ")                     #print blank line in case backup run again

#
#   Setup starts here
#
#   defines the root window
root = Tk()
root.title("uBITX Backup")

#   Style definition
appStyle = ttk.Style()
appStyle.theme_use(appTheme)

#   fontList from fonts.py
appStyle.configure('Heading1.TLabel',font=fontList['Heading1'])
appStyle.configure('Heading3.TLabel',font=fontList['Heading3'])
appStyle.configure('Button1.TButton',font=fontList['Emphasis'])
appStyle.configure('Symbol.TLabel',font=fontList['Symbol'])

#   widget definitions and layouts

#   define and layout the 4 frames
titleFrame=ttk.Frame(root, width=100, height=100)
configFrame=ttk.Frame(root, width=100, height=50)
logFrame=ttk.Frame(root, width=100, height=50)
commandFrame=ttk.Frame(root, width=100, height=50)

titleFrame.grid(row=0,column=0, pady=20)
configFrame.grid(row=1, column=0, pady=10)
logFrame.grid(row=2, column=0)
commandFrame.grid(row=3, column=0, sticky='ew')


# Define and layout the contents of titleFrame
titleBar = ttk.Label(titleFrame, text="uBITX EEPROM BACKUP", style='Heading1.TLabel')
separator_bar = ttk.Separator(titleFrame,orient='horizontal')

titleBar.grid(row=0, sticky='ew')
separator_bar.grid(row=1,  sticky='ew')

#   Define and layout the contents of the configuration frame
#   On click of refresh button, the list of com ports is probed and they are updated in updateComPorts
#

#   These are informational labels that go to the left of the configuration settings to make clear
#   which is the source and which is the target
#
sourceLabel=ttk.Label(configFrame,text="SOURCE:", style='Heading3.TLabel')
targetLabel=ttk.Label(configFrame,text="TARGET:", style='Heading3.TLabel')
downArrowLabel=ttk.Label(configFrame,text='\xAF', style='Symbol.TLabel')

#   First Row is the "source" that will be backed up. It is a Com Port that the uBITX is attached
#
#   The refresh button allows the software to detect a new device that is plugged in after the program is started
#
refreshComPortsButton = ttk.Button(configFrame, text="Refresh Port List", command=lambda: updateComPorts(comPortOptions, comPort))
#
#   This code builds the option menu that allows the com port to be selected. Note that initially the menu is empty '[]'
#
comPort = StringVar(root)
comPortOptions = ttk.OptionMenu(configFrame, comPort, [], command=comPortSelected)
comPortOptions.config(width=15)
#   This function will actually sense the Com Ports in use and fill in the Com Port option menu
updateComPorts(comPortOptions, comPort)

#   Layout the first line for the source of the backup
sourceLabel.grid(row=0, column=0, sticky=E)
refreshComPortsButton.grid(row=0, column=1, sticky=E)
comPortOptions.grid(row=0,column=2, sticky=W)

#   This just puts an arrow to clarify the source to target relationship
downArrowLabel.grid(row=1,column=0)

#   Now create the target line
fileName = ttk.Entry(configFrame, width=50)
fileName.insert(0, BACKUPFILE)
backupFileButton = ttk.Button(configFrame, text="Save Backup To:", command=backupFileSelect)

#   Put the Target line in the second row (actually # 3)
targetLabel.grid(row=2,column=0)
backupFileButton.grid(row=2,column=1, sticky=E)
fileName.grid(row=2, column=2, padx=5)

#   Finally we need to add the Run button to start the backup
runButton = ttk.Button(configFrame, text="Run Backup", command=backup, style='Button1.TButton')
runButton.grid(row=3, column=0, columnspan=3, pady=15)



# Add log file and buttons to third frame
logLabel = ttk.Label(logFrame, text="Backup Log", style='Heading3.TLabel')
helpButton = ttk.Button(logFrame, text="Help", command=lambda: helpDialog("Help","help.xml"))

logBox = Text(logFrame, width=100)
logBoxScrollBar = ttk.Scrollbar(logFrame, command=logBox.yview)     #   these two lines attach a scroll bar on right
logBox['yscrollcommand'] = logBoxScrollBar.set                      #   side of the text box

copyToClipboardButton = ttk.Button(commandFrame, text="Copy Log To Clipboard", command=copyLogToClipboard)
quitButton = ttk.Button(commandFrame, text="Quit", command=root.destroy)
aboutButton = ttk.Button(commandFrame, text="About", command=lambda: helpDialog("About","about.xml"))


logBox.bind("<Key>", lambda e: "break")         # this disables all typing into the logbox by mapping all keys to break

logLabel.grid(row=0, column=0, sticky='sw')
helpButton.grid(row=0,column=0, pady=5, padx=10, sticky='se')
logBox.grid(row=1,column=0, sticky="nsew", padx=2)
logBoxScrollBar.grid(row=1, column=1, sticky='nsew')

#   Adjust the weight of how free space is allocated to roughly layout the 3 buttons evenly
commandFrame.grid_columnconfigure(0, weight=2)
commandFrame.grid_columnconfigure(1, weight=1)
commandFrame.grid_columnconfigure(2, weight=2)

copyToClipboardButton.grid(row=0, column=0, padx=20, pady=10, sticky='w')
quitButton.grid(row=0, column=1, padx=15, pady=10, sticky='ew' )
aboutButton.grid(row=0, column=2, padx=20, pady=10,  sticky='e')


root.mainloop()