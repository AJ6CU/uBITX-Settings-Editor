import tkinter
import time

whereToLog: object

def startLog(textObj: object):
    global whereToLog
    whereToLog = textObj


def printlnToLog(lineToLog):
    printToLog(lineToLog + '\n')

def printToLog(textToLog):
    global whereToLog
    whereToLog.insert(tkinter.END, textToLog)
    whereToLog.see(tkinter.END)
    whereToLog.update()

def get_time_stamp():
    return time.strftime('%D %T')

def copyLogToClipboard():
    global whereToLog
    whereToLog.clipboard_clear()
    whereToLog.clipboard_append(whereToLog.get("1.0",tkinter.END))
    whereToLog.update()
    time.sleep(0.2)
    whereToLog.update()

