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
from SettingsNotebook import SettingsNotebook
from inputProcessor import InputProcessor
from outputProcessor import  OutputProcessor


import pygubu.widgets.simpletooltip as tooltip


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
root.geometry('1024x800')            # width x height
root.minsize(650,650)

ttk.Style().theme_use('vista')


#   define and layout the 5 frames

titleFrame=ttk.Frame(root, height=50, style='Title.TFrame')

inputProcessorFrame=InputProcessor(root)
outputProcessorFrame=OutputProcessor(root)


valueFrame = ttk.Frame(root)

logFrame=ttk.Frame(root)
commandFrame=ttk.Frame(root)

#   Assign extra/less space to column 0 which contains the text widget
root.grid_columnconfigure(0, weight=1)

root.grid_rowconfigure(0,weight=0)
titleFrame.grid(row=0,column=0,columnspan=2, sticky='ewns')

root.grid_rowconfigure(1,weight=0)
inputProcessorFrame.grid(row=1, column=0, columnspan=2, pady=(10, 0))

root.grid_rowconfigure(2,weight=1)
#valueFrame.grid(row=2, column=0, padx=15, sticky='ewns')   #   this is its location, but dont want it enabled
                                                            #   until there is data in the notebook. use enableNotebook()
                                                            #   and disableNotebook() to show/hide it

root.grid_rowconfigure(3,weight=0)
logFrame.grid(row=2, column=1, sticky='ns')

root.grid_rowconfigure(4,weight=0)
commandFrame.grid(row=6, column=0, columnspan=2, sticky='ew')

outputProcessorFrame.grid(row=5, column=0, columnspan=2, pady=(10, 0))

# Define and layout the contents of titleFrame
titleBar = ttk.Label(titleFrame, text="uBITX Setting Customization Editor", style='Heading1.TLabel')
titleBar.config(anchor=CENTER)
titleBar.pack()



settingsNotebook = SettingsNotebook(valueFrame)
inputProcessorFrame.setNotebook(settingsNotebook)
outputProcessorFrame.setNotebook(settingsNotebook)


# Add status and buttons to fourth frame
logLabel = ttk.Label(logFrame, text="Log", style='Heading3.TLabel')
helpButton = ttk.Button(logFrame, text="Help", command=lambda: helpDialog("Help", "help.xml", status))


logBox = Text(logFrame, font=('Arial',8))
logBox.configure(width=60)
logBoxScrollBar = ttk.Scrollbar(logFrame, command=logBox.yview)     #   these two lines attach a scroll bar on right
logBox['yscrollcommand'] = logBoxScrollBar.set                      #   side of the text box

logBox.bind("<Key>", lambda e: "break")         # this disables all typing into the logbox by mapping all keys to break

status = log(logBox)
inputProcessorFrame.setLog(status)              #tell input processor where the log is
outputProcessorFrame.setLog(status)              #tell input processor where the log is
settingsNotebook.setLog(status)
copyToClipboardButton = ttk.Button(logFrame, text="Copy Log To Clipboard", width=25, command=status.copyLogToClipboard)

#   Allocate any change in vertical space to row 1 which contains the text widget
logFrame.grid_rowconfigure(1, weight=1)

#   Allocate any change in height to column 1 that contains the text widget
#logFrame.grid_columnconfigure(0, weight=1)

logLabel.grid(row=0, column=0, padx=10, sticky='sw')
helpButton.grid(row=0,column=0, pady=5, sticky='se')
logBox.grid(row=1, column=0, padx=(10, 0), sticky="nsew")
logBoxScrollBar.grid(row=1, column=1, sticky='nsew')


copyToClipboardButton.grid(row=2, column=0)





#   Now create and layout the final frame with the commands

quitButton = ttk.Button(commandFrame, text="Quit", command=root.destroy)
aboutButton = ttk.Button(commandFrame, text="About", command=lambda: helpDialog("About","about.xml", status))
tooltip.create(aboutButton,"A very long tool tip. \nhow does it work? \nhow does it work?")

#   Adjust the weight of how free space is allocated to the only column in the frame
commandFrame.grid_columnconfigure(0, weight=1)

#   Now layout the buttons

quitButton.grid(row=0, column=0, padx=(0,15), pady=5, sticky='w')
aboutButton.grid(row=0, column=0, padx=15, pady=5)


#clearValidationMessages()

root.mainloop()
