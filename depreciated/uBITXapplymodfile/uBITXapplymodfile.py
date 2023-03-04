#   General System Imports

from lxml import etree as ET
import serial
from bitarray import bitarray
from time import sleep
import sys
import platform
from os.path import exists

#   Tkinter imports
import tkinter

import tkinter.messagebox
import serial.tools.list_ports              # Used to get a list of com ports
from tkinter import filedialog as fd

#   Application includes
from globalvars import *
from readEEPROMData import readEEPROMData
from writeEEPROM import *
from printtolog import *
from helpsubsystem import *
from fonts import *

from setters import setters

#####################################
#   Callbacks ("command") function definitions
#####################################
def modFileSelect():
    global USERMODFILE, fileName, startDir
    filetypes = (
        ('uBITX Mod File', '*.xml'),
        ('All files', '*.*')
    )
    tmpFName = fd.asksaveasfilename(
        title='Modification File',
        initialdir=startDir,
        defaultextension='.btx',
        filetypes=filetypes,
        confirmoverwrite=False)
    if tmpFName != "":
        USERMODFILE = tmpFName
        fileName.delete(0,END)
        fileName.insert(0,USERMODFILE)

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

def applyModFile():
 # First doublecheck that the modfile exists
    if (exists(USERMODFILE)==False):
        response = tkinter.messagebox.askquestion(title="Warning", message=USERMODFILE +  " does not exist. Please select an existing backup file", icon='warning')
        modFileSelect()
    else:

#       Backup file exists, now validate COM Port

        printlnToLog(get_time_stamp() + ": ***Starting Applying User Modification File to device on " + COM_PORT +"***")
        printlnToLog(get_time_stamp() + ": Will read User Modification File From : " + USERMODFILE)

        printlnToLog(get_time_stamp() + ": Opening connection to radio")

        try:
            RS232 = serial.Serial(COM_PORT, BAUD, timeout=0, stopbits=1, parity=serial.PARITY_NONE, xonxoff=0, rtscts=0)
        except:
            printlnToLog(get_time_stamp() + ": " + COM_PORT + " not selected or no uBITX attached")
            printlnToLog(get_time_stamp() + ": ***Applying Modifications to uBITX Aborted***")
            printlnToLog(" ")                     #print blank line in case backup run again
            printlnToLog(" ")                     #print blank line in case backup run again
            tkinter.messagebox.showerror("Error", message="COM Port not selected or no uBITX attached")
        else:       # We now have a usermodfile and a valid com port. Let's go!
            printlnToLog(get_time_stamp() + ": Establishing Connection to uBITX on " + COM_PORT)
            printlnToLog(get_time_stamp() + ": Awaiting uBITX Processor Ready this will take 3-5 seconds")

            sleep(3)  #this is required to allow Arduino processors to reset after open

            printlnToLog(get_time_stamp() + ": Reading EEPROM into buffer")
            EEPROMBuffer=readEEPROMData(RS232, 0, EEPROMSIZE)       #Read the EEPROM into memory


            EEPROMBufferDirty=bitarray(EEPROMSIZE)          # create a bit array of the same size that we can use to track dirty "bytes"
            EEPROMBufferDirty.setall(0)                     # clear all bits. When we write a byte into the EEPROMBuffer, we will set
                                                            # corresponding dirty bit to 1


            printlnToLog(get_time_stamp() + ": Opening EEPROM Memory Map of parameter locations")
            # Try reading the two XML files and flag any erors
            try:
                EEPROMtree = ET.parse(EEPROMMEMORYMAP)
            except:
                printlnToLog(get_time_stamp() + ": eeprommemorymap.xml is missing or corrupted")
                tkinter.messagebox.showerror(title="FATAL ERROR", message="'eeprommemorymap.xml' is missing or corrupted. Please re-install application. \nEXITING")
                sys.exit(-1)

            EEPROMroot = EEPROMtree.getroot()
            printlnToLog(get_time_stamp() + ": Completed preprocessing of EEPROM Memory Mapping")

            printlnToLog(get_time_stamp() + ": Opening User Modification File")

            try:
                UserModtree = ET.parse(USERMODFILE)
            except:
                printlnToLog(get_time_stamp() + ": " + USERMODFILE + "is corrupted")
                tkinter.messagebox.showerror(title="FATAL ERROR", message=USERMODFILE + "is corrupted. Please correct or recreate. \nEXITING")
                sys.exit(-1)

            UserModroot = UserModtree.getroot()

            printlnToLog(get_time_stamp() + ": Processing usermodfile and updating in memory copy of EEPROM.")


            EEPROM_Memory = setters()

            # For each setting in the EEPROM Map, there is a "getter" that will process it and write it to the user
            # mod file
            #
            for userSetting in UserModroot.findall('.//SETTING'):


                #get setting name and value
                userSettingName = userSetting.get("NAME")
                userSettingValue = userSetting.find("value").text

                #now look in eeprom map for buffer memory location, size (in bytes) and data type

                eepromSetting = EEPROMroot.find('.//SETTING[@NAME="{}"]'.format(userSettingName))

                memLocation = int(eepromSetting.find("EEPROMStart").text)
                numBytes = eepromSetting.find("sizeInBytes").text
                dataType = eepromSetting.find("displayFormat").text
                if (userSettingValue != None):
                    EEPROM_Memory.set(userSettingName, userSettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)
                else:
                    printlnToLog(get_time_stamp() + ": Warning: skipping " + userSettingName +"because value = NONE")

            printlnToLog(get_time_stamp() + ": In memory EEPROM copy updated. Now updating actual EEPROM")

            # write out eeprom and specific locations updated based on dirty bits


            if(updateEEPROM( RS232, EEPROMBuffer, EEPROMBufferDirty  )==0):
                printlnToLog(get_time_stamp() + ": ***User Modification File Successfully Applied***")
                printlnToLog(" ")                     #print blank line in case backup run again
                printlnToLog(" ")                     #print blank line in case backup run again
            else:
                printlnToLog(get_time_stamp() + ": Error, see message above")
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
titleBar = ttk.Label(titleFrame, text="uBITX Apply User Modifications File", style='Heading1.TLabel')
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
fileName.insert(0, USERMODFILE)
backupFileButton = ttk.Button(configFrame, text="Select User Modification File:", command=modFileSelect)

#   Layout the first line for the source of the backup
sourceLabel.grid(row=0, column=0, sticky=E)
backupFileButton.grid(row=0,column=1, padx=(3,0), sticky=E)
fileName.grid(row=0, column=2, padx=5)

#   This just puts an arrow to clarify the source to target relationship
downArrowLabel.grid(row=1,column=0)

#
#   The target of the application will be a UBITX that is attached to a COM Port. The potential COM Port candidates
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




#   Finally we need to add the RESTORE button to start the restoration
runButton = ttk.Button(configFrame, text="RUN", command=applyModFile, style='Button1.TButton')
runButton.grid(row=3, column=0, columnspan=3, pady=(20,0))



# Add log file and buttons to third frame
logLabel = ttk.Label(logFrame, text="Log", style='Heading3.TLabel')
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


