from lxml import etree as ET

#   General System Imports

import platform
from os.path import exists

#   Tkinter imports
from tkinter import *
from tkinter import ttk

import tkinter.messagebox
from tkinter import filedialog as fd


from globalvars import *
from printtolog import *

from helpsubsystem import *
from fileSelect import fileFD
from SettingsNotebook import SettingsNotebook


import pygubu.widgets.simpletooltip as tooltip


#####################################
#   Callbacks ("command") function definitions
#####################################


def readModFile(fd, entryFieldObj, logMe):
    global userModtree

   # First doublecheck that the modfile exists
    if (exists(fd.get_filename())==False):
        response = tkinter.messagebox.askquestion(title="Warning", message=USERMODFILE +  " does not exist. Please select an existing backup file", icon='warning')
        fd.select(readFileName)
    else:
#       try to open and parse usermodfile
        logMe.println("timestamp", "Opening User Modification File")
        try:
            userModtree = ET.parse(fd.get_filename())
        except:
            logMe.println("timestamp", fd.get_filename() + "is corrupted")
            tkinter.messagebox.showerror(title="FATAL ERROR", message=USERMODFILE + "is corrupted. Please correct or recreate. \nEXITING")
            sys.exit(-1)

        UserModroot = userModtree.getroot()
        logMe.println("timestamp", "Completed preprocessing of User Modification File")


        logMe.println("timestamp", "Loading Contents User Modification File")


        for userSetting in UserModroot.findall('.//SETTING'):
            userModFileValues[userSetting.get("NAME")] = userSetting.find("value").text
            userModFileDirty[userSetting.get("NAME")] = 0
            userModFileToolTips[userSetting.get("NAME")] = userSetting.find("tooltip").text

        print (userModFileValues)
        print (userModFileDirty)
        print (userModFileToolTips)
        prepareNotebook(userModFileValues)
        saveButton.configure(state='enabled')



def saveModFile(outputModfile, logMe):
    global userModtree

    UserModroot = userModtree.getroot()                     # get ptr to the root of the XML file
    logMe.println("timestamp", "Updating User Modification File")

    for userSetting in UserModroot.findall('.//SETTING'):   # for every SETTING Element we see in the tree do
            tagName = userSetting.get("NAME")               # get the NAME of the element
            if (tagName in readyToGo):                      # for the value element associated with NAME, update its
                                                            # value with the value entered in the screen
                                                            # getattr is a tricky function that for an object, gets
                                                            # the address of it, and then we can just use get/set for
                                                            # the stingvar associated with it
                userSetting.find("value").text = getattr(settingsNotebook, tagName).get()


    logMe.println("timestamp", "Finished Updating User Modification File")
    logMe.println("timestamp", "Writing User Modification to File")
    userModtree.write(outputModfile,method="html", pretty_print=True)
    logMe.println("timestamp", "***Successful Completion***")

def prepareNotebook(valueDictionary):
    global settingsNotebook

    for name in valueDictionary:
        if name in readyToGo:
            print("name=", name)
            getattr(settingsNotebook, name).set(valueDictionary[name])
            if userModFileToolTips[name] != None:
                tooltip.create(getattr(settingsNotebook, name + "_WIDGET"), userModFileToolTips[name])
    enableNotebook()

def clearValidationMessages():
    for widget in clearErrorMessages:
        getattr(settingsNotebook, widget).forget()

def enableNotebook():
    valueFrame.grid(row=2, column=0, padx=15, sticky='ewns')

def disableNotebook():
    valueFrame.forget()


#####################################
#   Start of main program
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
root.title("uBITX Setting Customization")
root.geometry('850x900')            # width x height
root.minsize(650,650)

ttk.Style().theme_use('vista')


#   define and layout the 5 frames

titleFrame=ttk.Frame(root, height=50, style='Title.TFrame')
configFrame=ttk.Frame(root)


valueFrame = ttk.Frame(root)

logFrame=ttk.Frame(root)
commandFrame=ttk.Frame(root)

#   Assign extra/less space to column 0 which contains the text widget
root.grid_columnconfigure(0, weight=1)

root.grid_rowconfigure(0,weight=0)
titleFrame.grid(row=0,column=0, sticky='ewns')

root.grid_rowconfigure(1,weight=0)
configFrame.grid(row=1, column=0, pady=(10,0))

root.grid_rowconfigure(2,weight=1)
#valueFrame.grid(row=2, column=0, padx=15, sticky='ewns')   #   this is its location, but dont want it enabled
                                                            #   until there is data in the notebook. use enableNotebook()
                                                            #   and disableNotebook() to show/hide it

root.grid_rowconfigure(3,weight=0)
logFrame.grid(row=3, column=0, sticky='ns')

root.grid_rowconfigure(4,weight=0)
commandFrame.grid(row=4, column=0, sticky='ew')



# Define and layout the contents of titleFrame
titleBar = ttk.Label(titleFrame, text="uBITX Setting Customization Editor", style='Heading1.TLabel')
titleBar.pack(anchor='center')

#   create a new file description object
readFile = fileFD("READ", "Read usermodfile...", USERMODFILE, startDir, "Mod File", "*.xml" )

#   Now create the source line
readFileLabel=ttk.Label(configFrame, text="SOURCE:", style='Heading3.TLabel')
readFileButton = ttk.Button(configFrame, text="Select User Modification File:", command=lambda: readFile.select(readFileName))
readFileName = ttk.Entry(configFrame, width=50)
readFileName.delete(0,END)
readFileName.insert(0, readFile.get_filename())                 # update name from fileFD object


readButton = ttk.Button(configFrame, text="READ", command=lambda: readModFile(readFile, readFileName, status))

#   Layout the first line for the source file
readFileLabel.grid(row=0, column=0, sticky='e')
readFileButton.grid(row=0, column=1, padx=(3, 0), sticky='e')
readFileName.grid(row=0, column=2, padx=5, sticky='e')
readButton.grid(row=0, column=3, sticky='e')

#   Add down arrow to make clear where file being saved to
downArrowLabel=ttk.Label(configFrame)
downArrowLabelImage = PhotoImage(file="./images/red-arrow-pointing-down59x36.png")
downArrowLabel.configure(image=downArrowLabelImage)
downArrowLabel.grid(row=1,column=0)

#   Layout the line for where we will save the result

#   create a new file description object for the save file
saveFile = fileFD("SAVE", "Save usermodfile to...", USERMODFILE, startDir, "Mod File", "*.xml" )

saveFileLabel=ttk.Label(configFrame,text="SAVE TO:", style='Heading3.TLabel')
saveFileButton = ttk.Button(configFrame, text="Select User Modification File:", command=lambda: saveFile.select(saveFileName))
saveFileName = ttk.Entry(configFrame, width=50)
saveFileName.delete(0,END)
saveFileName.insert(0, readFile.get_filename())                 # update name from fileFD object
saveButton = ttk.Button(configFrame, text="SAVE", command=lambda: saveModFile(saveFileName.get(), status), state='disabled' )


#   Layout the first line for the source file
saveFileLabel.grid(row=2, column=0, sticky='e')
saveFileButton.grid(row=2, column=1, padx=(3, 0), sticky='e')
saveFileName.grid(row=2, column=2, padx=5, sticky='e')
saveButton.grid(row=2, column=3, sticky='e')

settingsNotebook = SettingsNotebook(valueFrame)


# Add status and buttons to fourth frame
logLabel = ttk.Label(logFrame, text="Log", style='Heading3.TLabel')
helpButton = ttk.Button(logFrame, text="Help", command=lambda: helpDialog("Help", "help.xml", status))

logBox = Text(logFrame)
logBox.configure(height=5)
logBoxScrollBar = ttk.Scrollbar(logFrame, command=logBox.yview)     #   these two lines attach a scroll bar on right
logBox['yscrollcommand'] = logBoxScrollBar.set                      #   side of the text box

logBox.bind("<Key>", lambda e: "break")         # this disables all typing into the logbox by mapping all keys to break

status = log(logBox)

#   Allocate any change in vertical space to row 1 which contains the text widget
logFrame.grid_rowconfigure(1, weight=1)

#   Allocate any change in height to column 1 that contains the text widget
logFrame.grid_columnconfigure(0, weight=1)

logLabel.grid(row=0, column=0, padx=10, sticky='sw')
helpButton.grid(row=0,column=0, pady=5, sticky='se')
logBox.grid(row=1, column=0, padx=(10, 0), sticky="nsew")
logBoxScrollBar.grid(row=1, column=1, sticky='nsew')




#   Now create and layout the final frame with the commands
copyToClipboardButton = ttk.Button(commandFrame, text="Copy Log To Clipboard", command=status.copyLogToClipboard)
quitButton = ttk.Button(commandFrame, text="Quit", command=root.destroy)
aboutButton = ttk.Button(commandFrame, text="About", command=lambda: helpDialog("About","about.xml", status))
tooltip.create(aboutButton,"A very long tool tip. \nhow does it work? \nhow does it work?")

#   Adjust the weight of how free space is allocated to the only column in the frame
commandFrame.grid_columnconfigure(0, weight=1)

#   Now layout the buttons
copyToClipboardButton.grid(row=0, column=0, padx=(10,0), pady=5, sticky='w')
quitButton.grid(row=0, column=0, padx=15, pady=5)
aboutButton.grid(row=0, column=0, padx=(0,15), pady=5, sticky='e')

clearValidationMessages()

root.mainloop()
