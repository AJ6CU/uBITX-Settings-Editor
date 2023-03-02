#   Tkinter imports

from tkinter import *
from tkinter import ttk

import tkinter.messagebox

import sys

from lxml import etree as ET
from printtolog import *



def helpPrintln(outputBox, itsStyle, content):
    fontList = {'Heading1': ('Times New Roman', 24, 'bold', 'italic'),
                    'Heading2': ('Arial', 18, 'bold'),
                    'Heading3': ('Arial', 12, 'bold'),
                    'Heading4': ('Arial', 10, 'bold'),
                    'Normal': ('Default', 10),
                    'Emphasis': ('Default', 12, 'bold'),
                    'Symbol1': ('Symbol', 18, 'bold'),
                    'Symbol3': ('Symbol', 12, 'bold')}
    outputBox.tag_configure(itsStyle, font=fontList[itsStyle],wrap=WORD)
    outputBox.insert(END, f'{content}\n', itsStyle)

def helpDialog(winTitle, helpFile, logMe):
    try:
        helpRoot = ET.parse(helpFile)
    except:
        logMe.println("timestamp"," Missing file: " + helpFile)
        tkinter.messagebox.showerror(title="FATAL ERROR", message=helpFile+" is missing or corrupted. Please re-install application. \nEXITING")
        sys.exit(-1)
#   create new top level window for the help

    helpWindow = Toplevel()
    helpWindow.title(winTitle)

    #   create a Text box, scrollbar, and an OK button to close
    helpTextBox = Text(helpWindow, width=100)

    #   not sure why, but this attaches a scrollbar to the text box
    helpBoxScrollBar = ttk.Scrollbar(helpWindow, command=helpTextBox.yview)
    helpTextBox['yscrollcommand'] = helpBoxScrollBar.set

    #   turn off typing into the text box by mapping any keystroke to the break key
    helpTextBox.bind("<Key>", lambda e: "break")

    #   Create the OK button
    okButton = ttk.Button(helpWindow,text='OK', command=helpWindow.destroy)

    #   Place the objects on the screen
    helpTextBox.grid(row=0, sticky=N)
    okButton.grid(row=1, columnspan=2)
    helpBoxScrollBar.grid(row=0, column=1, sticky='nsew')


    for textTag in helpRoot.findall('.//FORMAT'):
        formatting = textTag.get("NAME")
        textToDisplay = textTag.find("TEXT").text

        helpPrintln(helpTextBox, formatting, textToDisplay.strip().replace("\n"," ").replace("\t",""))
        helpPrintln(helpTextBox, formatting,'')             #   this creates line spacing after each element is printed






