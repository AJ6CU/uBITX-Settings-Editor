from bitarray import bitarray
from time import sleep
from printtolog import *
from globalvars import *


def writeByteToEEPROM(portdesc: object, memAddress: int, outbyte: int):
    printlnToLog(get_time_stamp() + ": eeprom mem address =" + str(memAddress))
    LSB: bytes = memAddress & 0xff
    MSB: bytes = (memAddress >> 8) & 0xff
#    print(type(LSB),"\t", type(MSB),"\t", type(outbyte))
#    print(memAddress)
    checkByte: int = ((LSB + MSB + outbyte) % 256) & 0xff
    bytesToWrite = bytes([LSB, MSB, outbyte, checkByte, WRITECOMMAND])
    portdesc.write(bytesToWrite)


def updateEEPROM(portdesc: object, inMemBuffer: bytearray, itsDirty: bitarray) -> int:
    printlnToLog(get_time_stamp() + ": following EEPROM locations (if any) were updated")
    i: int = 0
    while i < EEPROMSIZE:
        if itsDirty[i]:  # Got a dirty byte
 #           print(f"{i:04}", "\t", inMemBuffer[i],"\t",type(inMemBuffer[i]))
            writeByteToEEPROM(portdesc, i, inMemBuffer[i])

 #           doneWithByte: bool = False
            retryCnt: int = 0
            while True:  # keep tring to write until successful or exceed # retries

                while portdesc.in_waiting == 0:
                    sleep(0.005)
                resultCode = int.from_bytes(portdesc.read(1), "little", signed=False)
                while portdesc.in_waiting == 0:
                    sleep(0.005)
                trailingByte = int.from_bytes(portdesc.read(1), "little", signed=False)
                if (resultCode == OK) & (trailingByte == ACK):
#                    print("got an ack")
                    break
                else:
                    printlnToLog(get_time_stamp() + ": retrying byte =", i)
                    printlnToLog(get_time_stamp() + ": resultcode=", resultCode)
                    printlnToLog(get_time_stamp() + ": trailingByte=", trailingByte)
                    retryCnt += 1
                    if retryCnt > RETRIES:
                        printToLog("Failed writing to EEPROM -- number of Retries exceeded")
                        tkinter.messagebox.showerror(title="ERROR", message="Failed writing to EEPROM -- number of Retries exceeded\nTry restarting uBITX, ensuring the USB cable plugged in securely, and then restart application. \nEXITING")
                        sys.exit(-1)
        i += 1
    return (0)                      # Success