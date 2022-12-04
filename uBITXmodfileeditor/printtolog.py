#   Tkinter imports

from tkinter import *
from tkinter import ttk

import time

whereToLog: object
class log:
    def __init__(self, whereToLog):
        self.whereToLog = whereToLog

    def println(self, timestamp, lineToLog):
        if(timestamp == "timestamp"):
            self.whereToLog.insert(END, self.__get_time_stamp() + ": " + lineToLog + '\n')
        else:
            self.whereToLog.insert(END, lineToLog + '\n')
        self.whereToLog.see(END)
        self.whereToLog.update()



    def print(self, timestamp, textToLog):
        if(timestamp == "timestamp"):
            self.whereToLog.insert(END, self.__get_time_stamp() + ": " + textToLog)
        else:
            self.whereToLog.insert(END, textToLog)
        self.whereToLog.see(tkinter.END)
        self.whereToLog.update()


    def __get_time_stamp(self):
        return time.strftime('%D %T')


    def copyLogToClipboard(self):
        self.clipboard_clear()
        self.clipboard_append(self.get(0,END))
        self.whereToLog.update()


