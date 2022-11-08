#   General System Imports
import serial
from time import sleep
import time
import platform
from os.path import exists
import os

#   Tkinter imports
import tkinter

import tkinter.messagebox
import serial.tools.list_ports              # Used to get a list of com ports
from tkinter import filedialog as fd

#   local function imports
from globalvars import *
from restore_userconfig import *
from writeEEPROMData import writeEEPROMData
from printtolog import *
from helpsubsystem import *
from fonts import *

#####################################
#   Callbacks ("command") function defintions
#####################################

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


def restore():              # this actually does the restore
    #   First confirm that the backup file exists
    if (exists(BACKUPFILE)==False):           # The backup file does not exist, so go to ask user to select another one
        tkinter.messagebox.showerror(title='ERROR', message = BACKUPFILE + " does not exist. Please select an existing backup file")
        backupFileSelect()
    elif (os.path.getsize(BACKUPFILE) != BACKUPFILESIZE):
        tkinter.messagebox.showerror(title='ERROR', message = BACKUPFILE + " is not the right size. Please chose valid backup file")
        backupFileSelect()
    else:       # Have what looks like a valid backupfile, now check the com port
        printlnToLog(get_time_stamp() + ": ***Starting restore of uBITX on " + COM_PORT + "***")
        printlnToLog(get_time_stamp() + ": Restoring from file: " + BACKUPFILE)
        try:
            RS232 = serial.Serial(COM_PORT, BAUD, timeout=0, stopbits=1, parity=serial.PARITY_NONE, xonxoff=0, rtscts=0)
        except:
            printlnToLog(get_time_stamp() + ": " + COM_PORT + " not selected or no device attached")
            printlnToLog(get_time_stamp() + ": ***Backup Aborted***")
            printlnToLog(" ")                     #print blank line in case backup run again
            printlnToLog(" ")                     #print blank line in case backup run again
            tkinter.messagebox.showerror("Error", message="COM Port not selected or no device attached")
        else:       # We now have a valid backup file and a valid com port. Let's go!
            printlnToLog(get_time_stamp() + ": Establishing Connection to Radio on " + COM_PORT)
            printlnToLog(get_time_stamp() + ": Awaiting Radio Processor Ready this will take 3-5 seconds")

            sleep(3)  #this is required to allow Nano to reset after open
            printlnToLog(get_time_stamp() + ": Reading backup file into memory")

            backup = open(BACKUPFILE, "rb")
            inMemoryFile=bytearray(backup.read(EEPROMSIZE))
            backup.close()

            printlnToLog(get_time_stamp() + ": Writing to EEPROM")
            writeEEPROMData(RS232, 0, EEPROMSIZE, inMemoryFile, overWriteFactoryCBState.get())

            RS232.close()
            printlnToLog(get_time_stamp() + ": ***Restore Successfully Completed***")
            printlnToLog(" ")                     #print blank line in case backup run again
            printlnToLog(" ")                     #print blank line in case backup run again

            #   Uncheck overwrite factory settings
            overWriteFactoryCBState.set(1)


#####################################
#Start Main Progrm
#####################################
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

#   defines the root window
root = Tk()
root.title("uBITX Backup")
root.geometry('650x650')
root.minsize(650,400)

#   Style definition
appStyle = ttk.Style()
appStyle.theme_use(appTheme)

#   fontList from fonts.py
appStyle.configure('Heading1.TLabel',font=fontList['Heading1'], background='blue', foreground='white')
appStyle.configure('Heading3.TLabel',font=fontList['Heading3'])
appStyle.configure('Button1.TButton',font=fontList['Emphasis'])
appStyle.configure('Symbol.TLabel',font=fontList['Symbol'])
appStyle.configure('Title.TFrame', background='blue', foreground='white')
#
#   Widget definitions and layouts
#

#   define and layout the 4 frames

titleFrame=ttk.Frame(root, width=50, height=50, style='Title.TFrame')
configFrame=ttk.Frame(root, width=50, height=50)
logFrame=ttk.Frame(root, width=50, height=50)
commandFrame=ttk.Frame(root, width=50, height=25)

#   Assign extra/less space to column 0 which contains the text widget
root.grid_columnconfigure(0, weight=1)

titleFrame.grid(row=0,column=0, sticky='ewns')
configFrame.grid(row=1, column=0, pady=(10,0))
root.grid_rowconfigure(2,weight=1)
logFrame.grid(row=2, column=0, sticky='ns')
root.grid_rowconfigure(3,weight=0)
commandFrame.grid(row=3, column=0, sticky='ew')


# Define and layout the contents of titleFrame
titleBar = ttk.Label(titleFrame, text="uBITX EEPROM RESTORE", style='Heading1.TLabel')
titleBar.pack(anchor='center')

#   Define and layout the contents of the configuration frame
#   On click of refresh button, the list of com ports is probed and they are updated in updateComPorts
#

#   These are informational labels that go to the left of the configuration settings to make clear
#   which is the source and which is the target
#
sourceLabel=ttk.Label(configFrame,text="SOURCE:", style='Heading3.TLabel')
targetLabel=ttk.Label(configFrame,text="TARGET:", style='Heading3.TLabel')
downArrowLabel=ttk.Label(configFrame,text='\xAF', style='Symbol.TLabel')

#   First Row is the "source" of the backup information. It will be an existing ".btx" file

#   Now create the source line
fileName = ttk.Entry(configFrame, width=50)
fileName.insert(0, BACKUPFILE)
backupFileButton = ttk.Button(configFrame, text="Select Backup File:", command=backupFileSelect)

#   Layout the first line for the source of the backup
sourceLabel.grid(row=0, column=0, sticky=E)
backupFileButton.grid(row=0,column=1, padx=(3,0), sticky=E)
fileName.grid(row=0, column=2, padx=5)

#   This just puts an arrow to clarify the source to target relationship
downArrowLabel.grid(row=1,column=0)

#
#   The target of the restoratiion will be a UBITX that is attached to a COM Port. The potential COM Port candidates
#   are detected at runtime. The refresh button allows the software to detect a new device that is plugged in after
#   the program is started
#
#
#   This code builds the option menu that allows the com port to be selected. Note that initially the menu is empty '[]'
#
comPort = StringVar(root)
comPortOptions = ttk.OptionMenu(configFrame, comPort, [], command=comPortSelected)
comPortOptions.config(width=15)

#   This function will actually sense the Com Ports in use and fill in the Com Port option menu
updateComPorts(comPortOptions, comPort)
refreshComPortsButton = ttk.Button(configFrame, text="Refresh Port List", command=lambda: updateComPorts(comPortOptions, comPort))

#   Put the Target line in the second row (actually # 3)
targetLabel.grid(row=2,column=0)
refreshComPortsButton.grid(row=2, column=1, sticky=E)
comPortOptions.grid(row=2,column=2, sticky=W)


overWriteFactoryCBState = tkinter.IntVar()

overWriteFactoryCB = ttk.Checkbutton(configFrame, onvalue=0, offvalue=1, variable=overWriteFactoryCBState,
                                     text='Overwrite Factory Recovery Data\n(not recommended)')
#                                     command=overWriteFactoryRecovery)
overWriteFactoryCBState.set(1)
overWriteFactoryCB.grid(row=3, column=1, columnspan=2, pady=(20,0), padx=10, sticky='ew')

#   Finally we need to add the RESTORE button to start the restoration
runButton = ttk.Button(configFrame, text="RESTORE", command=restore, style='Button1.TButton')
runButton.grid(row=4, column=0, columnspan=3, pady=(20,0))



# Add log file and buttons to third frame
logLabel = ttk.Label(logFrame, text="Restore Log", style='Heading3.TLabel')
helpButton = ttk.Button(logFrame, text="Help", command=lambda: helpDialog("Help","help.xml"))

logBox = Text(logFrame, width=300)
logBoxScrollBar = ttk.Scrollbar(logFrame, command=logBox.yview)     #   these two lines attach a scroll bar on right
logBox['yscrollcommand'] = logBoxScrollBar.set                      #   side of the text box

logBox.bind("<Key>", lambda e: "break")         # this disables all typing into the logbox by mapping all keys to break

#   Allocate any change in vertical space to row 1 which contains the text widget
logFrame.grid_rowconfigure(1,weight=1)

#   Allocate any change in height to column 1 that contains the text widget
logFrame.grid_columnconfigure(0,weight=1)

logLabel.grid(row=0, column=0, padx=10, sticky='sw')
helpButton.grid(row=0,column=0, pady=5, sticky='se')
logBox.grid(row=1,column=0, padx=(10,0), sticky="nsew")
logBoxScrollBar.grid(row=1, column=1, sticky='nsew')

#   Now create and layout the final frame with the commands
copyToClipboardButton = ttk.Button(commandFrame, text="Copy Log To Clipboard", command=copyLogToClipboard)
quitButton = ttk.Button(commandFrame, text="Quit", command=root.destroy)
aboutButton = ttk.Button(commandFrame, text="About", command=lambda: helpDialog("About","about.xml"))

#   Adjust the weight of how free space is allocated to the only column in the frame
commandFrame.grid_columnconfigure(0, weight=1)

#   Now layout the buttons
copyToClipboardButton.grid(row=0, column=0, padx=(10,0), pady=5, sticky='w')
quitButton.grid(row=0, column=0, padx=15, pady=5)
aboutButton.grid(row=0, column=0, padx=(0,15), pady=5, sticky='e')

startLog(logBox)

root.mainloop()


