#   Tkinter imports


import tkinter

import time

whereToLog: object
class log:
    def __init__(self, whereToLog):
        self.whereToLog = whereToLog
        self.whereToLog.tag_configure("error", foreground="red", font=('Arial',8, 'bold' ))

    def println(self, timestamp, lineToLog):
        if(timestamp == "timestamp"):
            self.whereToLog.insert(tkinter.END, self.__get_time_stamp() + ": " + lineToLog + '\n')
        else:
            self.whereToLog.insert(tkinter.END, lineToLog + '\n')
        self.whereToLog.see(tkinter.END)
        self.whereToLog.update()

    def printerror(self, timestamp, lineToLog):
        if(timestamp == "timestamp"):
            self.whereToLog.insert(tkinter.END, self.__get_time_stamp() + ": " + lineToLog + '\n', "error")
        else:
            self.whereToLog.insert(tkinter.END, lineToLog + '\n', "error")
        self.whereToLog.see(tkinter.END)
        self.whereToLog.update()



    def print(self, timestamp, textToLog):
        if(timestamp == "timestamp"):
            self.whereToLog.insert(tkinter.END, self.__get_time_stamp() + ": " + textToLog)
        else:
            self.whereToLog.insert(tkinter.END, textToLog)
        self.whereToLog.see(tkinter.END)
        self.whereToLog.update()


    def __get_time_stamp(self):
        return time.strftime('%D %T')


    def copyLogToClipboard(self):
        self.whereToLog.clipboard_clear()
        self.whereToLog.clipboard_append(self.whereToLog.get("1.0",tkinter.END))
        self.whereToLog.update()


