
#   General System Imports

import platform
import tkinter.messagebox

from helpsubsystem import *
from SettingsNotebook import SettingsNotebook
from inputProcessor import InputProcessor
from outputProcessor import  OutputProcessor

from globalvars import *


import pygubu.widgets.simpletooltip as tooltip

def tryToQuit(root, inputProcessorPtr):

    if inputProcessorPtr.getIOstate() == 'READ':
        answer = tkinter.messagebox.askyesno(title='Confirm Quit',
                message='Settings have NOT been saved, are you sure you want to QUIT?', default="no", icon="warning")
        if answer == False:
            return
    root.destroy()

def center_window(theRoot, width, height):
    # get screen width and height
    screen_width = theRoot.winfo_screenwidth()
    # screen_height = theRoot.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    # y = (screen_height/2) - (height/2)
    theRoot.geometry('%dx%d+%d+%d' % (width, height, x, 0))


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
    appTheme = 'alt'                # used by Linux
    startDir = "~"

IOstate = 'NONE'                        #used to track whether we have written the settings or not prior to quiting

#   defines the root window
root = Tk()
root.title("uBITX Setting Customization")



center_window(root,DEFAULT_ROOT_WINDOW_WIDTH,DEFAULT_ROOT_WINDOW_HEIGHT)
#root.geometry('1280x900+0+0')            # width x height
root.minsize(1024,650)

ttk.Style().theme_use(appTheme)


#   define and layout the 5 frames

titleFrame=ttk.Frame(root, height=50, style='Title.TFrame')

inputProcessorFrame=InputProcessor(root)
outputProcessorFrame=OutputProcessor(root, inputProcessorFrame)


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

root.grid_rowconfigure(3,weight=0)
logFrame.grid(row=2, column=1, sticky='ns')

root.grid_rowconfigure(4,weight=0)
commandFrame.grid(row=6, column=0, columnspan=2, sticky='ew',pady=10)

outputProcessorFrame.grid(row=5, column=0, columnspan=2, pady=(10, 0))

# Define and layout the contents of titleFrame
titleBar = ttk.Label(titleFrame, text="uBITX Settings Editor - "+ VERSION, style='Heading1.TLabel')
titleBar.config(anchor=CENTER)
titleBar.pack()



settingsNotebook = SettingsNotebook(valueFrame)
inputProcessorFrame.setNotebook(settingsNotebook)
outputProcessorFrame.setNotebook(settingsNotebook)


# Add status and buttons to fourth frame
logLabel = ttk.Label(logFrame, text="Log", style='Heading3.TLabel')



logBox = Text(logFrame, font=('Arial',8))
logBox.configure(width=70)
logBoxScrollBar = ttk.Scrollbar(logFrame, command=logBox.yview)     #   these two lines attach a scroll bar on right
logBox['yscrollcommand'] = logBoxScrollBar.set                      #   side of the text box

logBox.bind("<Key>", lambda e: "break")         # this disables all typing into the logbox by mapping all keys to break

status = log(logBox)
inputProcessorFrame.setLog(status)              #tell input processor where the log is
outputProcessorFrame.setLog(status)              #tell input processor where the log is
settingsNotebook.setLog(status)
copyToClipboardButton = ttk.Button(logFrame, text="Copy Log To Clipboard", width=25, command=status.copyLogToClipboard, style='Button4.TButton')
tooltip.create(copyToClipboardButton,"Copies the log output to the clipboard.\nYou can then paste it into a document for future reference.")

#   Allocate any change in vertical space to row 1 which contains the text widget
logFrame.grid_rowconfigure(1, weight=1)

#   Allocate any change in height to column 1 that contains the text widget
#logFrame.grid_columnconfigure(0, weight=1)

logLabel.grid(row=0, column=0, padx=10, sticky='sw')
#helpButton.grid(row=0,column=0, pady=5, sticky='se')
logBox.grid(row=1, column=0, padx=(10, 0), sticky="nsew")
logBoxScrollBar.grid(row=1, column=1, sticky='nsew')


copyToClipboardButton.grid(row=0, column=0, pady=5, sticky='se')





#   Now create and layout the final frame with the commands

quitButton = ttk.Button(commandFrame, text="Quit", command=lambda: tryToQuit(root, inputProcessorFrame), style='Button4.TButton')
tooltip.create(quitButton,"Exit application. Are you sure you saved your changes?")
helpButton = ttk.Button(commandFrame, text="Help", command=lambda: helpDialog("Help", HELPFILE, status))
tooltip.create(helpButton,"Provides access to online help")
aboutButton = ttk.Button(commandFrame, text="About", command=lambda: helpDialog("About", ABOUTFILE, status))
tooltip.create(aboutButton,"Access version info, author and software license")

#   Adjust the weight of how free space is allocated to the only column in the frame
commandFrame.grid_columnconfigure(0, weight=1)

#   Now layout the buttons

quitButton.grid(row=0, column=0, padx=(100,15), pady=5, columnspan=2 )
helpButton.grid(row=0, column=2, padx=15, pady=5)
aboutButton.grid(row=0, column=3, padx=15, pady=5)


#clearValidationMessages()


root.mainloop()
