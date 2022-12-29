
import serial
from time import sleep
import platform
from os.path import exists


#   Tkinter imports
import tkinter

import tkinter.messagebox

from tkinter import filedialog as fd

#   Application includes
from globalvars import *
from readEEPROMData import readEEPROMData
from printtolog import *
from helpsubsystem import *
from fonts import *

#####################################
#   Callbacks ("command") function definitions
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


def backup():                   # This actually performs the backup
    # First doublecheck that we are not overwriting a file, and if so, confirm it is ok
    if (exists(BACKUPFILE)):
        response = tkinter.messagebox.askquestion(title="Warning", message=BACKUPFILE + " already exists.\nDo you want to replace it?", icon='warning')
        if response == 'no' :
            backupFileSelect()
            return

#       All set, perform backup

    printlnToLog(get_time_stamp() + ": ***Starting backup of uBITX on " + COM_PORT + "***")
    printlnToLog(get_time_stamp() + ": Writing backup tp file: " + BACKUPFILE)
    try:
        RS232 = serial.Serial(COM_PORT, BAUD, timeout=0, stopbits=1, parity=serial.PARITY_NONE, xonxoff=0, rtscts=0)
    except:
        printlnToLog(get_time_stamp() + ": " + COM_PORT + " not selected or no uBITX attached")
        printlnToLog(get_time_stamp() + ": ***Backup Aborted***")
        printlnToLog(" ")                     #print blank line in case backup run again
        printlnToLog(" ")                     #print blank line in case backup run again
        tkinter.messagebox.showerror("Error", message="COM Port not selected or no uBITX attached")
    else:
        printlnToLog(get_time_stamp() + ": Establishing Connection to uBITX on " + COM_PORT)
        printlnToLog(get_time_stamp() + ": Awaiting Radio Processor Ready this will take 3-5 seconds")
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
root.geometry('700x650')
root.minsize(700,400)

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
configFrame.grid(row=1, column=0, pady=10)
root.grid_rowconfigure(2,weight=1)
logFrame.grid(row=2, column=0, sticky='ns')
root.grid_rowconfigure(3,weight=0)
commandFrame.grid(row=3, column=0, sticky='ew')


# Define and layout the contents of titleFrame
titleBar = ttk.Label(titleFrame, text="uBITX EEPROM BACKUP", style='Heading1.TLabel')
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
runButton = ttk.Button(configFrame, text="BACKUP", command=backup, style='Button1.TButton')
runButton.grid(row=3, column=0, columnspan=3, pady=15)



# Add log file and buttons to third frame
logLabel = ttk.Label(logFrame, text="Backup Log", style='Heading3.TLabel')
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