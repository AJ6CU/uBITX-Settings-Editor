
#   Tkinter imports
from tkinter import *
from tkinter import ttk

from tkinter import filedialog as fd

class fileFD:
    def __init__(self, opType, title, defaultFileName, startDir, fileExtensionDesc, fileExtension):
        self.opType= opType
        self.title = title
        self.fileName = defaultFileName
        self.startDir = startDir
        self.filetypes= (
            (fileExtensionDesc, fileExtension),
            ('All files', '*.*')
        )


    def select (self, entryFieldObj):

        if(self.opType == "SAVE"):
            self.fileName = fd.asksaveasfilename(
                title=self.title,
                initialdir=self.startDir,
                defaultextension=self.filetypes[1],
                filetypes=self.filetypes,
                confirmoverwrite=True)
        else:
                self.fileName = fd.askopenfilename(
                title=self.title,
                initialdir=self.startDir,
                defaultextension=self.filetypes[1],
                filetypes=self.filetypes)
        entryFieldObj.delete(0,END)
        entryFieldObj.insert(0, self.fileName)


    def get_filename(self):
        return self.fileName
