from lxml import etree as ET
from bitarray import bitarray
from time import sleep
import tkinter as tk
from tkinter import messagebox

from globalvars import *
from printtolog import *


class eepromObj:
#
#   Class variables
#
#   we only need to parse EEPROM memory maping and usermodtemplate file once. Following variables will
#   hold the pointer to root of the XML trees
#
    EEPROMroot = None           # This template maps memory locations to contents
    UserModroot  = None         # This template is used to create an internal XML tree that is easier to work with

    xmlTemplatesProcessed = False       # only need to parse the templates once...



    #******************************************************************************************
    #   getter interclass
    #   Takes an in-memory copy of the EEPROM or Binary File copy of the EEPROM. a memory location and a XML tree element
    #   and fills in the value for that element in the xlml tree. It is the opposite of the "setters" which updates the binary
    #   copy of the file using the value from each element.
    #
    #   The technique is a little too tricky where the Setting name is used to drive the calling of each member function
    #   with the same name. For example. the setting element "MASTER_CAL" is used to call the member function "MASTER_CAL" below
    #   The key is the "get" function
    #           def get(self, cmd, *args):
    #                 return getattr(self, cmd, self.defaultFunc)(*args)
    #   and the invoking action is
    #           EEPROM_Memory.get(userSettingName, userSettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)
    #   So the first "userSettingName" is the cmd (i.e. MASTER_CAL), and the rest are the args to the member function MASTER_CAL
    #******************************************************************************************

    class getters(object):
        def __init__(self, log, **kw):
            super().__init__ (**kw)
            self.log = log
        # utility functions
        def get_uint8_FromEEPROM(self, memBuffer: bytearray, memlocation: int) -> int:
            return (memBuffer[memlocation])

        def get_uint16_FromEEPROM(self, memBuffer: bytearray, memlocation: int) -> int:
            return memBuffer[memlocation] + (memBuffer[memlocation + 1] << 8)

        def get_uint32_FromEEPROM(self, memBuffer: bytearray, memlocation: int) -> int:
            return memBuffer[memlocation] + (memBuffer[memlocation + 1] << 8) + (memBuffer[memlocation + 2] << 16) + (
                        memBuffer[memlocation + 3] << 24)

        def XML_Get_uint8_FromEEPROM  (self, xmlSubTree, settingName, buffer) -> int:
            settingTag =  xmlSubTree.find(('.//SETTING[@NAME="{}"]'.format(settingName)))
            location = int(settingTag.find("EEPROMStart").text)
            return(self.get_uint8_FromEEPROM(buffer, location))

        def XML_MemLocation_FromEEPROM(self, xmlSubTree, settingName) -> int:
            settingTag = xmlSubTree.find(('.//SETTING[@NAME="{}"]'.format(settingName)))
            memAddress = int(settingTag.find("EEPROMStart").text)
            return memAddress


    #         #***********************************
    #         #   Firmware validation and factory defaults
    #         #***********************************
        def FIRMWARE_ID_ADDR1(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = hex(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))

        def FIRMWARE_ID_ADDR2(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = hex(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))

        def FIRMWARE_ID_ADDR3(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = hex(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))

        def VERSION_ADDRESS(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = INTERNAL_FIRMWARE_VERSION[int(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))]

        def FACTORY_VALUES_MASTER_CAL(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            tmpInt = self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation)
            if tmpInt & 0x80000000:                                         #We have a negative number
                value.text = "-" + str((~tmpInt+1)& 0xffffffff)             #convert from 2's complement
            else:
                value.text = str(tmpInt)
        def FACTORY_VALUES_USB_CAL(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str(self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation))

        def FACTORY_VALUES_VFO_A (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str(self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation))

        def FACTORY_VALUES_VFO_B(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str(self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation))

        def FACTORY_VALUES_CW_SIDETONE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str(self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation))

        def FACTORY_VALUES_CW_SPEED (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            if self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation) != 0:
                value.text = str(round(1200/self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)))
            else:
                value.text = DEFAULTCWSPEED

    #         #***********************************
    #         #   RADIO CALIBRATION SETTINGS
    #         #***********************************

        def MASTER_CAL(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            tmpInt = self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation)
            if tmpInt & 0x80000000:                                         #We have a negative number
                value.text = "-" + str((~tmpInt+1)& 0xffffffff)             #convert from 2's complement
            else:
                value.text = str(tmpInt)

        def USB_CAL(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str(self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation))

        def CW_CAL(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str(self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation))

        def IF1_CAL_ON_OFF_SWITCH(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = BOOL_SELECT[(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation) & 0x01)]

        def IF1_CAL(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))

        def IF1_CAL_ADD_SUB(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = BOOL_SELECT[((self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)>>7) & 0x01)]


    #
    #         #***********************************
    #         #   VFO SETTING FOR ON BOOT
    #         #***********************************
    #

        def VFO_A (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = '{:,}'.format(self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation)).replace(',','.')

        def VFO_B(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = '{:,}'.format(self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation)).replace(',','.')

        def VFO_A_MODE (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = MODE_SELECT[self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)]

        def VFO_B_MODE (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = MODE_SELECT[self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)]

        def TUNING_STEP_INDEX (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))

        def TUNING_STEP (self, SettingName, EEPROMBuffer, memLocation, value):
            tmpInt: int = self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)
            value.text = str((10**(tmpInt>>6)) * (tmpInt&0x3f))

        def TUNING_STEP1 (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.TUNING_STEP(SettingName, EEPROMBuffer, memLocation, value)

        def TUNING_STEP2 (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.TUNING_STEP(SettingName, EEPROMBuffer, memLocation, value)

        def TUNING_STEP3 (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.TUNING_STEP(SettingName, EEPROMBuffer, memLocation, value)

        def TUNING_STEP4 (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.TUNING_STEP(SettingName, EEPROMBuffer, memLocation, value)

        def TUNING_STEP5 (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.TUNING_STEP(SettingName, EEPROMBuffer, memLocation, value)

    #
    #         #***********************************
    #         #   COMMON CW SETTINGS
    #         #***********************************
    #

        def CW_KEY_TYPE (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str(CW_KEY_SELECT[self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)])

        def CW_SIDETONE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str(self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation))

        def CW_SPEED_WPM (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            if self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation) != 0:
                value.text = str(round(1200/self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)))
            else:
                value.text = DEFAULTCWSPEED

        def CW_DELAY_MS(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str(10 * self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))

        def CW_START_MS(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str(2 * self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))

    #         #***********************************
    #         #   COMMON MEMORY KEYER
    #         #***********************************
    #

        def USER_CALLSIGN_KEY (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str(MAGIC_USER_CALLSIGN_KEY)                       # Set for output, validation done later
                                                                            # goes back to the original memory contents


        def USER_CALLSIGN(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, _unused1):
    #       First need to confirm that a valid call sign has been entered by looking for 0x59 in
    #       "USER_CALLSIGN_KEY"

            if ((self.XML_Get_uint8_FromEEPROM(EEPROMroot, "USER_CALLSIGN_KEY", EEPROMBuffer) & 0xff) == MAGIC_USER_CALLSIGN_KEY):     # good a good one, can continue
                callSignLength = self.XML_Get_uint8_FromEEPROM (EEPROMroot, "USER_CALLSIGN_LEN", EEPROMBuffer) & 0x7f   #Important to mask it here as

                j: int = 0                                                                                        #Upper bit used to for LCD display callsign on startup
                callSignStr: str = ''
                while j < callSignLength:
                    callSignStr += str(chr(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation + j)))
                    j += 1
                value.text = str(callSignStr)
            else:           # bad magic number, set value to null ('')
                value.text = ''
                self.log.printerror("timestamp",  "WARNING!: Bad Magic# for User Callsign, Callsign data ignored")

        def CW_AUTO_MAGIC_KEY (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str(MAGIC_CW_AUTO_MAGIC_KEY)

        def QSO_CALLSIGN(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, _unused1):

    #       To get the alternative callsign for CW keyer, need to first get its length
            QSOCallSignLenLocation = self.XML_MemLocation_FromEEPROM(EEPROMroot, "QSO_CALLSIGN")

    #       Contents of the QSOCallSignLenLocation is the length of the call sign
            altCallSignLen = self.get_uint8_FromEEPROM(EEPROMBuffer, QSOCallSignLenLocation)

            if (altCallSignLen >0) & (altCallSignLen <= MAXCALLSIGNLEN):                    #validate call sign before processing

                callSignStr: str = ''
                #       The trick here is that the callsign actually aways ends at the location *just before* its length
                #   So need to create the offset from which the call sign actually starts and then iterate forward
                #
                callSignOffset = QSOCallSignLenLocation - altCallSignLen
                j: int = 0
                while j < altCallSignLen:
                    callSignStr += str(chr(self.get_uint8_FromEEPROM(EEPROMBuffer, callSignOffset + j)))
                    j += 1
                value.text = str(callSignStr)

        def CW_AUTO_COUNT(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, _unused1 ):
            if ((self.XML_Get_uint8_FromEEPROM(EEPROMroot, "CW_AUTO_MAGIC_KEY", EEPROMBuffer) & 0xff) == MAGIC_CW_AUTO_MAGIC_KEY):     # good a good one, can continue
                self.CW_Number_of_Msgs = self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)
                value.text = str(self.CW_Number_of_Msgs)
            else:           # bad magic number, set value to 0
                self.CW_Number_of_Msgs = 0
                value.text = '0'
                self.log.printerror("timestamp",  "WARNING!: Bad Magic# for CW Autokeyer Message storage, message data ignored")


        def CW_AUTO_DATA(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1 ):
            self.cwAutoDataPtr = memLocation
            value.text = str(self.cwAutoDataPtr)

        def CW_MEMORY_KEYER_MSGS(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, valueElement):

            # #
            # # We are now going to set the offset in the heap for each message that exists
            # # msg1 will get slot 803/804 for stat end, msg2 will get slot 805/806, etc.
            # # each message will start at self.totalMsgChar and end at self.totalMsgChar + lenght(msg)-1
            # # and then self.totalmsgChar will be incremented by length(msg)
            # # Note:self.totalChar starts at 20 to allow for the pairs of index used for offsets
            # #
            #
            # # find index in offset table
            #
            if SettingName[19] in CW_MSG_LABEL:

                i = CW_MSG_LABEL.index(SettingName[19])

                #   Only fetch the number of known messages
                if i < self.CW_Number_of_Msgs:

                    #
                    # #
                    # # cwAutoDataPtr points to first location in the heap
                    # # Starting there, each two bytes is start/end pairs. So if there are 3 messages
                    # # cwAutoDataPtr = location containing the start byte of 1st message, +1 the byte containing the end location
                    # # +2 is start of second message, +3 end of second message, etc. Note these are locations, you got to
                    # # get the data in these locations to actually get the offset for each message.
                    # #
                    #
                    msgStartInHeapLocation = self.cwAutoDataPtr +(i*2)       #The start ends are are beginning of heap. 1st msg has start at
                    msgStartInHeap = self.cwAutoDataPtr + self.get_uint8_FromEEPROM(EEPROMBuffer, msgStartInHeapLocation)
                    #
                    msgEndInHeapLocation = self.cwAutoDataPtr + (i*2)+1      #cwAutoDataptr , end at cwAutoDataPtr+1, 2nd cwAutoDataPtr+2, cwAutoDataPtr+3), etc.
                    msgEndInHeap = self.cwAutoDataPtr + self.get_uint8_FromEEPROM(EEPROMBuffer, msgEndInHeapLocation)
                    # #
                    # #so at this point we have the locations of start/end of each message. Now go collect the actual characters
                    # #
                    #
                    j = 0
                    msgStr: str = ''
                    numBytes = (msgEndInHeap+1) - msgStartInHeap
                    while j< int(numBytes):
                        msgStr += str(chr(self.get_uint8_FromEEPROM(EEPROMBuffer, msgStartInHeap + j)))
                        j+=1

                    if len(msgStr) > 0:
                        value.text = msgStr
                        return
            value.text = ''




        def CW_MEMORY_KEYER_MSG0(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)
                
        def CW_MEMORY_KEYER_MSG1(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSG2(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSG3(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSG4(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSG5(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSG6(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSG7(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSG8(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSG9(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer,  memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGA(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGB(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGC(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGD(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGE(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGF(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGG(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGH(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGI(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGJ(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGK(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGL(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGM(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGN(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGO(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, userSetting)



    #
    #         #***********************************
    #         #   CW ADC SETTINGS
    #         #***********************************

    #   This section is made more complex as the KD8CEC code stores the upper two bytes of the ADC values in one byte
    #   Either CW_ADC_MOST_BIT1 for Straight keys and DOTS or CQ_ADC_MOST_BIT2 for DASH and BOTH.
    #   So getting value out of EEPROM requires that we first figure out the location of the upper bits and
    #   then move them into position and add them to the lower 8 bits to get a 10 bit resolution for the ADC.

        def CW_ADC_ST_FROM(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, _unused1):
            upperBitsByte = self.XML_Get_uint8_FromEEPROM (EEPROMroot, "CW_ADC_MOST_BIT1", EEPROMBuffer)      #get byte with upper two bits
            memContents: int = self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)                               #now get the lower 8 bits
            value.text = str(memContents | ((upperBitsByte &0x03)  << 8))           #4 sets of 2 bits, find them, put them to the left and add


        def CW_ADC_ST_TO(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, _unused1):
            upperBitsByte = self.XML_Get_uint8_FromEEPROM (EEPROMroot, "CW_ADC_MOST_BIT1", EEPROMBuffer)      #get byte with upper two bits
            memContents: int = self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)                               #now get the lower 8 bits
            value.text = str(memContents | ((upperBitsByte &0x0C)  << 6))           #4 sets of 2 bits, find them, put them to the left and add

        def CW_ADC_DOT_FROM(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, _unused1):
            upperBitsByte = self.XML_Get_uint8_FromEEPROM (EEPROMroot, "CW_ADC_MOST_BIT1", EEPROMBuffer)      #get byte with upper two bits
            memContents: int = self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)                               #now get the lower 8 bits
            value.text = str(memContents | ((upperBitsByte & 0x30) << 4))

        def CW_ADC_DOT_TO(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, _unused1):
            upperBitsByte = self.XML_Get_uint8_FromEEPROM (EEPROMroot, "CW_ADC_MOST_BIT1", EEPROMBuffer)      #get byte with upper two bits
            memContents: int = self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)                               #now get the lower 8 bits
            value.text = str(memContents | ((upperBitsByte & 0xC0) << 2))



        def CW_ADC_DASH_FROM(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, _unused1):
            upperBitsByte = self.XML_Get_uint8_FromEEPROM (EEPROMroot, "CW_ADC_MOST_BIT2", EEPROMBuffer)      #get byte with upper 2 bits
            memContents: int = self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)                               # now get the lower 8 bits
            value.text = str(memContents | ((upperBitsByte & 0x03) << 8))           # 4 sets of 2 bits, find them, put them to the left

        def CW_ADC_DASH_TO(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, _unused1):
            upperBitsByte = self.XML_Get_uint8_FromEEPROM (EEPROMroot, "CW_ADC_MOST_BIT2", EEPROMBuffer)      #get byte with upper 2 bits
            memContents: int = self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)                               # now get the lower 8 bits
            value.text = str(memContents | ((upperBitsByte & 0x0C) << 6))

        def CW_ADC_BOTH_FROM(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, _unused1):
            upperBitsByte = self.XML_Get_uint8_FromEEPROM (EEPROMroot, "CW_ADC_MOST_BIT2", EEPROMBuffer)      #get byte with upper 2 bits
            memContents: int = self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)                               # now get the lower 8 bits
            value.text = str(memContents | ((upperBitsByte & 0x30) << 4))

        def CW_ADC_BOTH_TO(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, _unused1):
            upperBitsByte = self.XML_Get_uint8_FromEEPROM (EEPROMroot, "CW_ADC_MOST_BIT2", EEPROMBuffer)      #get byte with upper 2 bits
            memContents: int = self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)                               # now get the lower 8 bits
            value.text = str(memContents | ((upperBitsByte & 0xC0) << 2))



    #         #***********************************
    #         #   USER CHANNELS
    #         #***********************************
    #
        def CHANNEL_FREQ(self, SettingName, EEPROMBuffer, memLocation, value):
            value.text = '{:,}'.format((self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation)&0x1FFFFFFF)).replace(',','.')     #upper 3 bits are the mode must mask off

        def CHANNEL_FREQ1(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ2(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ3(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ4(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ5(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ6(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ7(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ8(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ9(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ10(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ11(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ12(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ13(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ14(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ15(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ16(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ17(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ18(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ19(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ20(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName,EEPROMBuffer, memLocation, value)



        def CHANNEL_FREQ_MODE(self, SettingName, EEPROMBuffer, memLocation, value):
            value.text = str(MODE_SELECT[((self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)) >>5)])

        def CHANNEL_FREQ1_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ2_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ3_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ4_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ5_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ6_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ7_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ8_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ9_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ10_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ11_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ12_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ13_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ14_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ15_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ16_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ17_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ18_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ19_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ20_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, memLocation, value)


        def CHANNEL_FREQ_SHOW_NAME(self, SettingName, EEPROMBuffer, memLocation, value):
            if((self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))== 0x03):        #0x03 is a flag for "yes"
                value.text = BOOL_SELECT[1]
            else:
                value.text = BOOL_SELECT[0]

        def CHANNEL_FREQ1_SHOW_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ2_SHOW_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ3_SHOW_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ4_SHOW_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ5_SHOW_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ6_SHOW_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ7_SHOW_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ8_SHOW_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ9_SHOW_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ10_SHOW_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, memLocation, value)


        def CHANNEL_FREQ_NAME(self, SettingName, EEPROMBuffer, memLocation, value):
            i: int =0
            tmpStr: str = ''
            while i<CHANNELNAMELENGTH:
                tmp = str(chr((self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+i))))
                if (tmp.isprintable()):
                    tmpStr += tmp
                else:
                    tmpStr += ' '
                i += 1
            value.text = tmpStr


        def CHANNEL_FREQ1_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ2_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ3_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ4_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ5_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ6_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ7_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ8_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ9_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def CHANNEL_FREQ10_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, memLocation, value)



    #         #***********************************
    #         #   HAM BANDS
    #         #***********************************
    #
        def TUNING_RESTICTIONS(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = TUNE_RESTRICT_SELECT[self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)>>1 & 0x01]

        def TX_RESTRICTIONS(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            if (self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation) >= TX_RESTRICT_MINIMUM):
                value.text = TX_RESTRICT_SELECT[1]              #Restriction of TX to only HAM bands
            else:
                value.text = TX_RESTRICT_SELECT[0]              #Restrictions on TX


        def HAM_BAND_COUNT(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))


        def HAM_BAND_RANGE_START(self, SettingName, EEPROMBuffer, memLocation, value):
            value.text = '{:,}'.format(self.get_uint16_FromEEPROM(EEPROMBuffer, memLocation)).replace(',','.')

        def HAM_BAND_RANGE1_START(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_RANGE2_START(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_RANGE3_START(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_RANGE4_START(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_RANGE5_START(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_RANGE6_START(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_RANGE7_START(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_RANGE8_START(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_RANGE9_START(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_RANGE10_START(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, memLocation, value)


        def HAM_BAND_RANGE_END(self, SettingName, EEPROMBuffer, memLocation, value):
            value.text = '{:,}'.format(self.get_uint16_FromEEPROM(EEPROMBuffer, memLocation)).replace(',','.')

        def HAM_BAND_RANGE1_END(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_RANGE2_END(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_RANGE3_END(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_RANGE4_END(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_RANGE5_END(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_RANGE6_END(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_RANGE7_END(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_RANGE8_END(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_RANGE9_END(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_RANGE10_END(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, memLocation, value)

    #         #***********************************
    #         #   Last Frequency and Mode Used per Band
    #         #***********************************
    #
        def HAM_BAND_FREQS(self, SettingName, EEPROMBuffer, memLocation, value):
     #       value.text = str((self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation)&0x1FFFFFFF))     #upper 3 bits are the mode must mask off
            value.text = '{:,}'.format(self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation)&0x1FFFFFFF).replace(',','.')

        def HAM_BAND_FREQS1(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS(SettingName,EEPROMBuffer, memLocation, value)

        def HAM_BAND_FREQS2(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS(SettingName,EEPROMBuffer, memLocation, value)

        def HAM_BAND_FREQS3(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS(SettingName,EEPROMBuffer, memLocation, value)

        def HAM_BAND_FREQS4(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS(SettingName,EEPROMBuffer, memLocation, value)

        def HAM_BAND_FREQS5(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS(SettingName,EEPROMBuffer, memLocation, value)

        def HAM_BAND_FREQS6(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS(SettingName,EEPROMBuffer, memLocation, value)

        def HAM_BAND_FREQS7(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS(SettingName,EEPROMBuffer, memLocation, value)

        def HAM_BAND_FREQS8(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS(SettingName,EEPROMBuffer, memLocation, value)

        def HAM_BAND_FREQS9(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS(SettingName,EEPROMBuffer, memLocation, value)

        def HAM_BAND_FREQS10(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS(SettingName,EEPROMBuffer, memLocation, value)

        def HAM_BAND_FREQS_MODE(self, SettingName, EEPROMBuffer, memLocation, value):
            value.text = str(MODE_SELECT[((self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)) >>5)])

        def HAM_BAND_FREQS1_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_FREQS2_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_FREQS3_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_FREQS4_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_FREQS5_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_FREQS6_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_FREQS7_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_FREQS8_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_FREQS9_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, memLocation, value)

        def HAM_BAND_FREQS10_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, memLocation, value)


    #         # ***********************************
    #         #   SDR SETTINGS
    #         # ***********************************
    #
        def BOOT_INTO_SDR_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = BOOT_MODE[(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation) >> 1) & 0x01]

        def SDR_OFFSET_MODE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = SDR_OFFSET_MODE[((self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation) & 0xFF) >> 2) & 0x03]

        def SDR_FREQUENCY(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = '{:,}'.format(self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation)).replace(',','.')



    #         # ***********************************
    #         #   WSPR SETTINGS
    #         # ***********************************
    #
        def WSPR_BAND1_TXFREQ(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = '{:,}'.format(self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation)).replace(',','.')

        def WSPR_BAND2_TXFREQ(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = '{:,}'.format(self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation)).replace(',','.')

        def WSPR_BAND3_TXFREQ(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = '{:,}'.format(self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation)).replace(',','.')

        def WSPR_BAND1_MULTICHAN(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str(self.get_uint16_FromEEPROM(EEPROMBuffer, memLocation))

        def WSPR_BAND2_MULTICHAN(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str(self.get_uint16_FromEEPROM(EEPROMBuffer, memLocation))

        def WSPR_BAND3_MULTICHAN(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str(self.get_uint16_FromEEPROM(EEPROMBuffer, memLocation))


        def WSPR_BAND_REG1(self, SettingName, EEPROMBuffer, memLocation, value ):
            j: int = 0
            msgStr: str = ''

            while j < WSPRREG1LENGTH:
                msgStr+='{:02X}'.format(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation + j))+','
                j += 1
            value.text = msgStr.rstrip(',')                 #strip off extra , on right

        def WSPR_BAND1_REG1(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.WSPR_BAND_REG1(SettingName, EEPROMBuffer, memLocation, value)

        def WSPR_BAND2_REG1(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.WSPR_BAND_REG1(SettingName, EEPROMBuffer, memLocation, value)

        def WSPR_BAND3_REG1(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.WSPR_BAND_REG1(SettingName, EEPROMBuffer, memLocation, value)


        def WSPR_BAND_REG2(self, SettingName, EEPROMBuffer, memLocation, value ):
            j: int = 0
            msgStr: str = ''

            while j < WSPRREG2LENGTH:
                msgStr+='{:02X}'.format(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation + j))+','
                j += 1
            value.text = msgStr.rstrip(',')                 #strip off extra , on right

        def WSPR_BAND1_REG2(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.WSPR_BAND_REG2(SettingName, EEPROMBuffer, memLocation, value)

        def WSPR_BAND2_REG2(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.WSPR_BAND_REG2(SettingName, EEPROMBuffer, memLocation, value)

        def WSPR_BAND3_REG2(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.WSPR_BAND_REG2(SettingName, EEPROMBuffer, memLocation, value)


        def WSPR_COUNT(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))

        def WSPR_MESSAGE_NAME(self, SettingName, EEPROMBuffer, memLocation, value):
            i: int =0
            tmpStr: str = ''
            while i<WSPRNAMELENGTH:
                tmp = str(chr((self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+i))))
                if (tmp.isprintable()):
                    tmpStr += tmp
                else:
                    tmpStr += ' '
                i += 1
            value.text = tmpStr



        def WSPR_MESSAGE1_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.WSPR_MESSAGE_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def WSPR_MESSAGE2_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.WSPR_MESSAGE_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def WSPR_MESSAGE3_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.WSPR_MESSAGE_NAME(SettingName, EEPROMBuffer, memLocation, value)

        def WSPR_MESSAGE4_NAME(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.WSPR_MESSAGE_NAME(SettingName, EEPROMBuffer, memLocation, value)


        def WSPR_MESSAGE(self, SettingName, EEPROMBuffer, memLocation, value):
            j: int = 0
            msgStr: str = ''

            while j < SIZEOFWSPRMESSAGES:
                msgStr+='{:02X}'.format(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation + j))+','
                j += 1
            value.text = msgStr.rstrip(',')                 #strip off extra , on right

        def WSPR_MESSAGE1(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.WSPR_MESSAGE(SettingName, EEPROMBuffer, memLocation, value)

        def WSPR_MESSAGE2(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.WSPR_MESSAGE(SettingName, EEPROMBuffer, memLocation, value)

        def WSPR_MESSAGE3(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.WSPR_MESSAGE(SettingName, EEPROMBuffer, memLocation, value)

        def WSPR_MESSAGE4(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.WSPR_MESSAGE(SettingName, EEPROMBuffer, memLocation, value)

    #
    #         # ***********************************
    #         #   HARDWARE SETTINGS
    #         # ***********************************
    #

        def S_METER_LEVELS(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            if ((self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)) & 0x08):  # a 0x08 bit pattern indicates s-meter on
                value.text = BOOL_SELECT[1]
            else:
                value.text = BOOL_SELECT[0]

        def S_METER_LEVEL(self, SettingName, EEPROMBuffer, memLocation, value):
            value.text = str(4 * self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))


        def S_METER_LEVEL1(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.S_METER_LEVEL(SettingName, EEPROMBuffer, memLocation, value)

        def S_METER_LEVEL2(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.S_METER_LEVEL(SettingName, EEPROMBuffer, memLocation, value)

        def S_METER_LEVEL3(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.S_METER_LEVEL(SettingName, EEPROMBuffer, memLocation, value)

        def S_METER_LEVEL4(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.S_METER_LEVEL(SettingName, EEPROMBuffer, memLocation, value)

        def S_METER_LEVEL5(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.S_METER_LEVEL(SettingName, EEPROMBuffer, memLocation, value)

        def S_METER_LEVEL6(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.S_METER_LEVEL(SettingName, EEPROMBuffer, memLocation, value)

        def S_METER_LEVEL7(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.S_METER_LEVEL(SettingName, EEPROMBuffer, memLocation, value)

        def S_METER_LEVEL8(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.S_METER_LEVEL(SettingName, EEPROMBuffer, memLocation, value)


        def I2C_LCD_MASTER(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = hex(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))

        def I2C_LCD_SECOND(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = hex(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))

        def I2C_ADDR_SI5351(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = hex(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))



    #
    #         # ***********************************
    #         #   ADVANCED UX SETTINGS
    #         # ***********************************
    #

        def MESSAGE_LINE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = BOOL_SELECT[(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation) >>4)&0x01]

        def SCROLLING_DISPLAY(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = BOOL_SELECT[(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation) >> 2) & 0x01]

        def ONE_TWO_LINE_TOGGLE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = BOOL_SELECT[self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)  & 0x01]

        def NEXTION_DISPLAY_CALL_SIGN(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = BOOL_SELECT[(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation) >> 1) & 0x01]

        def MAIN_SCREEN_FORMAT(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = MAIN_MENU_SELECT[(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))]

        def CW_DISPLAY_FREQ(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):

            shiftDisplay = (self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation) >>7) & 0x01
            enableAdjustCWFreq = (self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+1) >>7) & 0x01

            if shiftDisplay & ~enableAdjustCWFreq:      #By definition means display shows RX freq
                value.text = "RX"
            else:
                value.text = "TX"                       #Shows TX Freq seems to be the preferred option


        def STORED_IF_SHIFT(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = BOOL_SELECT[(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation) >> 6) & 0x01]

        def IF_SHIFTVALUE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            tmpInt = self.get_uint16_FromEEPROM(EEPROMBuffer, memLocation)
            if tmpInt & 0x8000:                                         #We have a negative number
                value.text = "-" + str((~tmpInt+1)& 0xffff)             #convert from 2's complement
            else:
                value.text = str(tmpInt)

        def CW_FREQUENCY_ADJUSTMENT(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = str((self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation) &  0x3f)*10)



    #
    #         # ***********************************
    #         #   EXTENDED KEYS
    #         # ***********************************
    #

        def EXTENDED_KEY_START(self, SettingName, EEPROMBuffer, memLocation, value):
            value.text = str(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)*4)

        def EXTENDED_KEY1_START(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.EXTENDED_KEY_START(SettingName, EEPROMBuffer, memLocation,value)

        def EXTENDED_KEY2_START(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.EXTENDED_KEY_START(SettingName, EEPROMBuffer, memLocation,value)

        def EXTENDED_KEY3_START(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.EXTENDED_KEY_START(SettingName, EEPROMBuffer, memLocation,value)

        def EXTENDED_KEY4_START(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.EXTENDED_KEY_START(SettingName, EEPROMBuffer, memLocation,value)

        def EXTENDED_KEY5_START(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.EXTENDED_KEY_START(SettingName, EEPROMBuffer, memLocation,value)

        def EXTENDED_KEY6_START(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.EXTENDED_KEY_START(SettingName, EEPROMBuffer, memLocation,value)


        def EXTENDED_KEY_END(self, SettingName, EEPROMBuffer, memLocation, value):
            value.text = str(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)*4)

        def EXTENDED_KEY1_END(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.EXTENDED_KEY_END(SettingName, EEPROMBuffer, memLocation,value)

        def EXTENDED_KEY2_END(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.EXTENDED_KEY_END(SettingName, EEPROMBuffer, memLocation,value)

        def EXTENDED_KEY3_END(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.EXTENDED_KEY_END(SettingName, EEPROMBuffer, memLocation,value)

        def EXTENDED_KEY4_END(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.EXTENDED_KEY_END(SettingName, EEPROMBuffer, memLocation,value)

        def EXTENDED_KEY5_END(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.EXTENDED_KEY_END(SettingName, EEPROMBuffer, memLocation,value)

        def EXTENDED_KEY6_END(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.EXTENDED_KEY_END(SettingName, EEPROMBuffer, memLocation,value)


        def EXTENDED_KEY_FUNC(self, SettingName, EEPROMBuffer, memLocation, value):
            value.text = FTN_KEY_SELECT[self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)]

        def EXTENDED_KEY1_FUNC(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.EXTENDED_KEY_FUNC(SettingName, EEPROMBuffer, memLocation, value)

        def EXTENDED_KEY2_FUNC(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.EXTENDED_KEY_FUNC(SettingName, EEPROMBuffer, memLocation, value)

        def EXTENDED_KEY3_FUNC(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.EXTENDED_KEY_FUNC(SettingName, EEPROMBuffer, memLocation, value)

        def EXTENDED_KEY4_FUNC(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.EXTENDED_KEY_FUNC(SettingName, EEPROMBuffer, memLocation, value)

        def EXTENDED_KEY5_FUNC(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.EXTENDED_KEY_FUNC(SettingName, EEPROMBuffer, memLocation, value)

        def EXTENDED_KEY6_FUNC(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.EXTENDED_KEY_FUNC(SettingName, EEPROMBuffer, memLocation, value)


    #
    #         # ***********************************
    #         #   CUSTOM LPF FILTERS
    #         # ***********************************
    #
    #

        def CUST_LPF_ENABLED(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            try:
                indexPos = LPF_MODE_SETTING.index((self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)))
            except:
                value.text = LPF_MODE_SELECT[0]
            else:
                value.text = LPF_MODE_SELECT[LPF_MODE_SETTING.index((self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)))]

        def CUST_LPF_FILTER_ENDFREQ(self, SettingName, EEPROMBuffer, memLocation, value):
            value.text = str(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))
            if value.text == '0' :
                value.text = ''

        def CUST_LPF_FILTER1_ENDFREQ(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, memLocation, value)

        def CUST_LPF_FILTER2_ENDFREQ(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, memLocation, value)

        def CUST_LPF_FILTER3_ENDFREQ(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, memLocation, value)

        def CUST_LPF_FILTER4_ENDFREQ(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, memLocation, value)

        def CUST_LPF_FILTER5_ENDFREQ(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, memLocation, value)

        def CUST_LPF_FILTER6_ENDFREQ(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, memLocation, value)

        def CUST_LPF_FILTER7_ENDFREQ(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, memLocation, value)


        def CUST_LPF_FILTER_CONTROL(self, SettingName, EEPROMBuffer, memLocation, value):

            j = 0
            tmpStr = ""
            LPFControlByte = self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)
            if LPFControlByte == 0x00:
                value.text="NONE"
            else:
                while j < 7:
                    if ((LPFControlByte>>j)&0x01):

                        tmpStr += (LPF_CTRL_SELECT[j] + ",")
                    j += 1
                value.text = tmpStr.rstrip(',')

        def CUST_LPF_FILTER1_CONTROL(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, memLocation, value)

        def CUST_LPF_FILTER2_CONTROL(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, memLocation, value)

        def CUST_LPF_FILTER3_CONTROL(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, memLocation, value)

        def CUST_LPF_FILTER4_CONTROL(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, memLocation, value)

        def CUST_LPF_FILTER5_CONTROL(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, memLocation, value)

        def CUST_LPF_FILTER6_CONTROL(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, memLocation, value)

        def CUST_LPF_FILTER7_CONTROL(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, memLocation, value)

    #
    #         # ***********************************
    #         #   Extended EEPROM Settings (>= 1204)
    #         # ***********************************
    #
    #

        def EXT_FIRMWARE_ID_ADDR1(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = hex(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))

        def EXT_FIRMWARE_ID_ADDR2(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = hex(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))

        def EXT_FIRMWARE_ID_ADDR3(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = hex(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))

        def EXT_UBITX_BOARD_VERSION(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = EXT_UBITX_BOARD_VERSION_SELECT[self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)]

        def EXT_DATE_TIME_STAMP(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):

            timeStamp :str = ''

            # Get month# and translate to month text

            timeStamp += MONTH3CHARS[int(chr(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))
                                        + chr(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+1)))] + ' '

            # get day
            timeStamp += chr(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+2)) \
                            + chr(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+3)) \
                            + ', '

            # Get year
            timeStamp += chr(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+4)) \
                            + chr(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+5)) \
                            + chr(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+6)) \
                            + chr(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+7)) \
                            + " "

            # Add the hour
            timeStamp += chr(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+8)) \
                            + chr(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+9)) \
                            + ':'

            # Add the min
            timeStamp += chr(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+10)) \
                            + chr(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+11))

            value.text = timeStamp


        def EXT_PROCESSOR_TYPE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = EXT_PROCESSOR_TYPE_SELECT[self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)]

        def EXT_DISPLAY_TYPE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = EXT_DISPLAY_TYPE_SELECT[self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)]

        def EXT_FUNCTIONALITY_SET(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = EXT_FUNCTIONALITY_SET_SELECT[self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)]

        def EXT_SMETER_SELECTION(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            value.text = EXT_SMETER_SELECTION_SELECT[self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)]

        def defaultFunc(self, *args):
                print ("Command not recognised:", args[0])

        def get(self, cmd, *args):
                return getattr(self, cmd, self.defaultFunc)(*args)


    #******************************************************************************************
    #   setter interclass
    #   Takes an Setting Element from and XML Tree, determines its value and then writes to an i
    #   in-memory copy of the EEPROM or Binary File copy of the EEPROM. This is the opposite class
    #   as "getters"
    #
    #   The technique is a little too tricky where the Setting name is used to drive the calling of each member function
    #   with the same name. For example. the setting element "MASTER_CAL" is used to call the member function "MASTER_CAL" below
    #   The key is the "set" function
    #           def set(self, cmd, *args):
    #                 return getattr(self, cmd, self.defaultFunc)(*args)
    #   and the invoking action is
    #           EEPROM_Memory.set(userSettingName, userSettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)
    #   So the first "userSettingName" is the cmd (i.e. MASTER_CAL), and the rest are the args to the member function MASTER_CAL
    #******************************************************************************************

    class setters(object):
        def __init__(self, **kw):
            super().__init__ (**kw)
            self.CW_Messages_Buffer = {}

    #         #***********************************
    #         #   SHARED UTILITY ROUTINES
    #         #***********************************
        def assembleTuneStepByte(self, number) -> bytes:            #creates byte for tuning steps. 01234567 -01 exp, rest mantissa
            localNum = int(number)
            if localNum >= 100000:
                exp = 4
            elif localNum >= 10000:
                exp = 3
            elif localNum >= 1000:
                exp = 2
            elif localNum >= 100:
                exp = 1
            else:
                exp = 0
            divisor = 10 ** exp
            mantissa = round(localNum / divisor) & 0x3f
            exp = (exp << 6) & 0xc0

            return(exp + mantissa)


        def XML_Get_unit8_FromEEPROM(self, xmlSubTree, settingName, memBuffer) -> int:
            settingTag = xmlSubTree.find(('.//SETTING[@NAME="{}"]'.format(settingName)))
            memAddress = int(settingTag.find("EEPROMStart").text)
            return memBuffer[memAddress]

        def XML_MemLocation_FromEEPROM(self, xmlSubTree, settingName) -> int:
            settingTag = xmlSubTree.find(('.//SETTING[@NAME="{}"]'.format(settingName)))
            memAddress = int(settingTag.find("EEPROMStart").text)
            return memAddress

        def set_unit8_InEEPROMBuffer(self, memBuffer: bytearray, dirty: bitarray, memAddress: int, outData: bytes):
            if memBuffer[memAddress] != outData:  # we have new data here; update and mark dirty
                memBuffer[memAddress] = outData
                dirty[memAddress] = 1

        def set_unit16_InEEPROMBuffer(self, memBuffer: bytearray, dirty: bitarray, memAddress: int, outData: int):
            LSB: bytes = int(outData) & 0xFF
            MSB: bytes = (int(outData) >> 8) & 0xFF
            self.set_unit8_InEEPROMBuffer(memBuffer, dirty, memAddress, LSB)
            self.set_unit8_InEEPROMBuffer(memBuffer, dirty, memAddress + 1, MSB)

        def set_unit32_InEEPROMBuffer(self, memBuffer: bytearray, dirty: bitarray, memAddress: int, outData: int):
            LSB: bytes = int(outData) & 0xFF
            LSB1: bytes = (int(outData) >> 8) & 0xFF
            LSB2: bytes = (int(outData) >> 16) & 0xFF
            MSB: bytes = (int(outData) >> 24) & 0xFF

            self.set_unit8_InEEPROMBuffer(memBuffer, dirty, memAddress, LSB)
            self.set_unit8_InEEPROMBuffer(memBuffer, dirty, memAddress + 1, LSB1)
            self.set_unit8_InEEPROMBuffer(memBuffer, dirty, memAddress + 2, LSB2)
            self.set_unit8_InEEPROMBuffer(memBuffer, dirty, memAddress + 3, MSB)

    #         #***********************************
    #         #   Firmware validation and factory defaults
    #         #***********************************

        def FIRMWARE_ID_ADDR1(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue,16))

        def FIRMWARE_ID_ADDR2(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue,16))

        def FIRMWARE_ID_ADDR3(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue,16))

        def VERSION_ADDRESS(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, INTERNAL_FIRMWARE_VERSION.index(userSettingValue))

        def FACTORY_VALUES_MASTER_CAL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            if( userSettingValue[0] == '-'):              #we have a negative number and have to put it into 2's complement
                tmpStr: str = userSettingValue[1:len(userSettingValue)]         #strip off the leading "-"
                tmpInt: int = int(tmpStr)
                tmpInt = (~tmpInt+1)& 0xffffffff                                    #Put it in 2's complement
                self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpInt)
            else:
                self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue) & 0xffffffff)

        def FACTORY_VALUES_USB_CAL(self,  SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def FACTORY_VALUES_VFO_A(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

        def FACTORY_VALUES_VFO_B(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

        def FACTORY_VALUES_CW_SIDETONE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

        def FACTORY_VALUES_CW_SPEED(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit16_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, round(1200/int(userSettingValue)))

    #         #***********************************
    #         #   RADIO CALIBRATION SETTINGS
    #         #***********************************
        def MASTER_CAL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            if( userSettingValue[0] == '-'):              #we have a negative number and have to put it into 2's complement
                tmpStr: str = userSettingValue[1:len(userSettingValue)]         #strip off the leading "-"
                tmpInt: int = int(tmpStr)
                tmpInt = (~tmpInt+1)& 0xffffffff                                    #Put it in 2's complement
                self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpInt)
            else:
                self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue) & 0xffffffff)

        def USB_CAL(self,  SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CW_CAL(self,  SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def IF1_CAL_ON_OFF_SWITCH(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            if BOOL_SELECT.index(userSettingValue):
                tmpByte: bytes = EEPROMBuffer[memLocation] | 0x01
            else:
                tmpByte: bytes = EEPROMBuffer[memLocation] & (~0x01)
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)


        def IF1_CAL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            if userSettingValue == '':
                userSettingValue = 0            # protect against an empty field
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))


        def IF1_CAL_ADD_SUB(self,  SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            if BOOL_SELECT.index(userSettingValue):                   #1 = Yes, so subtract if cal
                tmpByte = EEPROMBuffer[memLocation] | 0x80
            else:
                tmpByte = EEPROMBuffer[memLocation] & (~0x80)
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

    #
    #         #***********************************
    #         #   VFO SETTING FOR ON BOOT
    #         #***********************************
    #
        def VFO_A(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            cleanValue = int(userSettingValue.translate({ord(c): None for c in"-.,+"}))
            self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, cleanValue)

        def VFO_B(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            cleanValue = int(userSettingValue.translate({ord(c): None for c in"-.,+"}))
            self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, cleanValue)

        def VFO_A_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, MODE_SELECT.index(userSettingValue))

        def VFO_B_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, MODE_SELECT.index(userSettingValue))

        def TUNING_STEP_INDEX(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

        def TUNING_STEP1(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, self.assembleTuneStepByte(userSettingValue))

        def TUNING_STEP2(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, self.assembleTuneStepByte(userSettingValue))

        def TUNING_STEP3(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, self.assembleTuneStepByte(userSettingValue))

        def TUNING_STEP4(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, self.assembleTuneStepByte(userSettingValue))


        def TUNING_STEP5(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, self.assembleTuneStepByte(userSettingValue))

    #
    #         #***********************************
    #         #   COMMON CW SETTINGS
    #         #***********************************
    #
        def CW_KEY_TYPE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, CW_KEY_SELECT.index(userSettingValue))

        def CW_SIDETONE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

        def CW_SPEED_WPM(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit16_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, round(1200/int(userSettingValue)))

        def CW_DELAY_MS(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, round(int(userSettingValue)/10))

        def CW_START_MS(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, round(int(userSettingValue)>>1))

    #         #***********************************
    #         #   COMMON MEMORY KEYER
    #         #***********************************
    #
        def USER_CALLSIGN_KEY (self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, value, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, MAGIC_USER_CALLSIGN_KEY )


        def USER_CALLSIGN(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1):
            # Get memory location assigned to Call Sign Key and CW Key Lenght
            callSignKeyLocation: int = self.XML_MemLocation_FromEEPROM(EEPROMroot, "USER_CALLSIGN_KEY")
            callSignLenLocation: int = self.XML_MemLocation_FromEEPROM(EEPROMroot, "USER_CALLSIGN_LEN")

            if(userSettingValue != None):
                #First set key value in EEPROM to signif
                self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, callSignKeyLocation, 0x59)

                # Store lenght of call sign
                self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, callSignLenLocation, len(userSettingValue))

                #store call sign
                i: int = 0
                while (i< len(userSettingValue)):
                    self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation+i, ord(userSettingValue[i]))
                    i += 1
            else:
                # Turn off key indicating no call sign
                self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, callSignKeyLocation, 0x00)

        def QSO_CALLSIGN(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            altCallSignLen: int = len(userSettingValue)

            # Validate we have a valid QSO Call sign. If not, ignore the entry
            if (altCallSignLen > 0) & (altCallSignLen <= MAXCALLSIGNLEN):
                # store the length in the QSO_CALLSIGN EEPROM slot
                self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, altCallSignLen)

                # now the tricky piece. The Alternative call sign is stored starting in memLocation - altCallSignLen and
                # ends just before the length value

                startingLoc: int = memLocation - altCallSignLen
                i: int = 0
                while (i < altCallSignLen):
                    self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, startingLoc+i, ord(userSettingValue[i]))
                    i += 1

        def CW_AUTO_MAGIC_KEY (self, SettingName, EEPROMBuffer, EEPROMBufferDirty,  memLocation, value, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, MAGIC_CW_AUTO_MAGIC_KEY )

        def CW_AUTO_COUNT(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))
            self.CW_Number_of_Msgs = int(userSettingValue)

        def CW_AUTO_DATA(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            pass

        def CW_MEMORY_KEYER_MSGS(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            # Welcome to one of the more complex storage data structure: CW Keyer Messages...
            #
            # CW_AUTO_DATA: It is important to understand the use and purpose of value. This is a location
            # in EEPROM where the heap starts. (Currently, and probably forever location 803 (decimal) in EEPROM)
            #
            # The start/end offsets for *every* cw message are in each of the next two bytes. For example, if there
            # were 3 messages, of 10, 15, 20 characters each:
            #   Location    Contents        Comment
            #   803          6              Offset for start of first message
            #   804          15             Offset for end of first message
            #   805          16             Offset for start of second message
            #   806          30             Offset for end of second message
            #   807          31             Offset for start of third message
            #   808          50             Offset for end of end message
            #   809                         Actual start of first message
            #   818                         Actual end of first message
            #   819                         Actual start of second message
            #   833                         Actual end of second message
            #   834                         Actual start of third message
            #   853                         Actual end of third message
            #
            #  note that all offsets are from location 803 or CW_AUTO_DATA. e.g. message 1 starts at 803 + 6
            #  This particular data structure is easy to invalidate lots of bytes of EEPROM. For exmaple, just changing
            #  the length of message one could make all subsequent bytes dirty.
            #
            #  The number of messages actually stored is stored in the location "CW_AUTO_COUNT".  That will tell you how
            #  many of start/end offsets you have at starting at location 803...
            #
            #  To add to your oonfusion, this function serves as an aggregator of the Cw messages. It is called once for every
            #   CW message, collects the message, *and* with the call to the *last message, actually starts processing
            #   and storing the messages in the EEPROM.
            #
            msgLabel = SettingName[19]

            #   collect the message
            self.CW_Messages_Buffer[msgLabel] = userSettingValue
            if len(self.CW_Messages_Buffer) == CW_MSG_TOTAL:        # collected all the message buffers
                # Starting location is the *address* of "CW_AUTO_DATA" get that first
                cwAutoDataMemLocation = self.XML_MemLocation_FromEEPROM(EEPROMroot, "CW_AUTO_DATA")

                messageHeap: str = ''
                messageStart: int = []
                messageEnd: int =[]
                messageLoc = 0
                messageOffset = 0

                for msgkey in CW_MSG_LABEL:
                    if len(self.CW_Messages_Buffer[msgkey]) != 0:           # ignore empty messages
                        messageStart.append(messageLoc)
                        messageEnd.append (messageLoc + len(self.CW_Messages_Buffer[msgkey]) -1)
                        messageLoc += len(self.CW_Messages_Buffer[msgkey])                     # this updates pointer for next place a message can go
                        messageOffset += 2                                                     # track the extra offsets because of leading start, ends
                        messageHeap += self.CW_Messages_Buffer[msgkey]

                # At this point we have the raw start end of each message, just need to offset them by the bytes
                # Occupied by the start,end pairs. And then we can write the start end to EEPROM
                #

                numMessage = len (messageStart)

                i=0
                while (i < numMessage):
                    messageStart[i] += messageOffset                    #offset the start,end pairs by the size of the start,end list
                    messageEnd[i] += messageOffset
                    self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, cwAutoDataMemLocation + (2*i), messageStart[i])
                    self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, cwAutoDataMemLocation + (2 * i) +1, messageEnd[i])
                    i += 1

                # Write the message heap to EEPROM
                i: int = 0
                offset: int = cwAutoDataMemLocation + messageOffset
                while (i < messageLoc):
                    self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, i+offset, ord(messageHeap[i]))
                    i += 1

                # Finally need to update the total CW message  count in EEPROM. First gets its location, and then update
                cwAutoCountMemLocation = self.XML_MemLocation_FromEEPROM(EEPROMroot, "CW_AUTO_COUNT")
                self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, cwAutoCountMemLocation, numMessage)

        def CW_MEMORY_KEYER_MSG0(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSG1(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)
        def CW_MEMORY_KEYER_MSG2(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSG3(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSG4(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSG5(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSG6(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSG7(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSG8(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSG9(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGA(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGB(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGC(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGD(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGF(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGG(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGH(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGI(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGJ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGK(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGM(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGN(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)

        def CW_MEMORY_KEYER_MSGO(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting):
            self.CW_MEMORY_KEYER_MSGS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, userSetting)
    #
    #         #***********************************
    #         #   CW ADC SETTINGS
    #         #***********************************

        def CW_ADC_ST_DOT(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1):

            # first get the byte that holds all the upper bits for Straight keys and "DOTs"
            upperBitsByte = self.XML_Get_unit8_FromEEPROM(EEPROMroot, "CW_ADC_MOST_BIT1", EEPROMBuffer)  # get byte with upper two bits
            MSB_Bits = (int(userSettingValue) >> 8) & 0x03              #masking off the upper two and lower two bits
            LSB_Bits = int(userSettingValue) & 0xff

            if SettingName == "CW_ADC_ST_FROM":
                tmpByte: bytes = upperBitsByte & (~0x03) | MSB_Bits         # MSB are in postions 67
            elif SettingName ==  "CW_ADC_ST_TO":
                tmpByte: bytes = upperBitsByte & (~0x0C) | (MSB_Bits << 2)  # MSB are in postions 56
            elif SettingName == "CW_ADC_DOT_FROM":
                tmpByte: bytes = upperBitsByte & (~0x30) | (MSB_Bits << 4)  # MSB are in postions 34
            elif SettingName ==  "CW_ADC_DOT_TO":
                tmpByte: bytes = upperBitsByte & (~0xC0) | (MSB_Bits << 6)  # MSB are in postions 12

            upperBitsMemLocation = self.XML_MemLocation_FromEEPROM(EEPROMroot, "CW_ADC_MOST_BIT1")
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, upperBitsMemLocation, tmpByte)
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, LSB_Bits)


        def CW_ADC_ST_FROM(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1):
            self.CW_ADC_ST_DOT(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1)

        def CW_ADC_ST_TO(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1):
            self.CW_ADC_ST_DOT(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1)

        def CW_ADC_DOT_FROM(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1):
            self.CW_ADC_ST_DOT(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1)

        def CW_ADC_DOT_TO(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1):
            self.CW_ADC_ST_DOT(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1)


        def CW_ADC_DASH_BOTH(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1):

            # first get the byte that holds all the upper bits for Straight keys and "DOTs"
            upperBitsByte = self.XML_Get_unit8_FromEEPROM(EEPROMroot, "CW_ADC_MOST_BIT2", EEPROMBuffer)  # get byte with upper two bits
            MSB_Bits = (int(userSettingValue) >> 8) & 0x03              #masking off the upper two and lower two bits
            LSB_Bits = int(userSettingValue) & 0xff

            if SettingName == "CW_ADC_DASH_FROM":
                tmpByte: bytes = upperBitsByte & (~0x03) | MSB_Bits         # MSB are in postions 67
            elif SettingName ==  "CW_ADC_DASH_TO":
                tmpByte: bytes = upperBitsByte & (~0x0C) | (MSB_Bits << 2)  # MSB are in postions 56
            elif SettingName ==  "CW_ADC_BOTH_FROM":
                tmpByte: bytes = upperBitsByte & (~0x30) | (MSB_Bits << 4)  # MSB are in postions 34
            elif SettingName ==  "CW_ADC_BOTH_TO":
                tmpByte: bytes = upperBitsByte & (~0xC0) | (MSB_Bits << 6)  # MSB are in postions 12

            upperBitsMemLocation = self.XML_MemLocation_FromEEPROM(EEPROMroot, "CW_ADC_MOST_BIT2")
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, upperBitsMemLocation, tmpByte)
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, LSB_Bits)


        def CW_ADC_DASH_FROM(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1):
            self.CW_ADC_DASH_BOTH(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1)

        def CW_ADC_DASH_TO(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1):
            self.CW_ADC_DASH_BOTH(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1)

        def CW_ADC_BOTH_FROM(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1):
            self.CW_ADC_DASH_BOTH(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1)

        def CW_ADC_BOTH_TO(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1):
            self.CW_ADC_DASH_BOTH(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1)


    #         #***********************************
    #         #   USER CHANNELS
    #         #***********************************
    #
        def CHANNEL_FREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
           cleanValue = int(userSettingValue.translate({ord(c): None for c in"-.,+"}))
           LSB: bytes = cleanValue & 0xFF
           LSB1: bytes = (cleanValue >> 8) & 0xFF
           LSB2: bytes = (cleanValue >> 16) & 0xFF
           MSB: bytes = (cleanValue >> 24) & 0xFF

           MSB = (MSB & 0x1f) + (EEPROMBuffer[memLocation+3] & 0xe0)            # must preserve upper 3 bits which is mode

           self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, LSB)
           self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation + 1, LSB1)
           self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation + 2, LSB2)
           self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation + 3, MSB)


        def CHANNEL_FREQ1(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ2(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ3(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ4(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ5(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ6(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ7(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ8(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ9(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ10(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ11(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ12(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ13(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ14(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ15(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ16(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ17(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ18(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ19(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ20(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)


        def CHANNEL_FREQ_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
            updatedByte = (EEPROMBuffer[memLocation] & 0x1f) + (MODE_SELECT.index(userSettingValue)<<5)
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, updatedByte)

        def CHANNEL_FREQ1_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ2_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ3_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ4_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ5_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ6_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ7_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ8_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ9_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ10_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ11_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ12_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ13_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ14_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ15_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ16_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ17_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ18_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ19_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ20_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)



        def CHANNEL_FREQ_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
            if userSettingValue == "YES":
                self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, SHOW_CHANNEL_NAME)
            else:
                self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, HIDE_CHANNEL_NAME)

        def CHANNEL_FREQ1_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ2_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ3_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ4_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ5_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ6_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ7_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ8_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ9_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ10_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue: str):
            i: int = 0
            while i < CHANNELNAMELENGTH:
                if i < len(str(userSettingValue)):
                    self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation + i, ord(userSettingValue[i]))
                else:
                    self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation + i, ord(' '))           # blank fill
                i += 1

        def CHANNEL_FREQ1_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ2_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ3_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ4_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ5_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ6_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ7_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ8_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ9_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CHANNEL_FREQ10_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)


    #         #***********************************
    #         #   HAM BANDS
    #         #***********************************
    #
        def TUNING_RESTICTIONS(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            tmpByte: bytes = (EEPROMBuffer[memLocation] & (~0x02)) | ((TUNE_RESTRICT_SELECT.index(str(userSettingValue)))<<1)
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

        def TX_RESTRICTIONS(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            if TX_RESTRICT_SELECT.index(str(userSettingValue)):
                tmpByte: bytes = (EEPROMBuffer[memLocation] & 0x02) + TX_RESTRICT_MINIMUM  #TX Restrictions are >= 100
            else:
                tmpByte: bytes = (EEPROMBuffer[memLocation] & 0x02)                        #This clears restriction if still there
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

        def HAM_BAND_COUNT(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))


        def HAM_BAND_RANGE_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
            cleanValue = int(userSettingValue.translate({ord(c): None for c in"-.,+"}))
            self.set_unit16_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, cleanValue)

        def HAM_BAND_RANGE1_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

        def HAM_BAND_RANGE1_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

        def HAM_BAND_RANGE2_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

        def HAM_BAND_RANGE3_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

        def HAM_BAND_RANGE4_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

        def HAM_BAND_RANGE5_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

        def HAM_BAND_RANGE6_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

        def HAM_BAND_RANGE7_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

        def HAM_BAND_RANGE8_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

        def HAM_BAND_RANGE9_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

        def HAM_BAND_RANGE10_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)


        def HAM_BAND_RANGE_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
            cleanValue = int(userSettingValue.translate({ord(c): None for c in"-.,+"}))
            self.set_unit16_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, cleanValue)

        def HAM_BAND_RANGE1_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

        def HAM_BAND_RANGE1_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

        def HAM_BAND_RANGE2_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

        def HAM_BAND_RANGE3_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

        def HAM_BAND_RANGE4_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

        def HAM_BAND_RANGE5_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

        def HAM_BAND_RANGE6_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

        def HAM_BAND_RANGE7_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

        def HAM_BAND_RANGE8_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

        def HAM_BAND_RANGE9_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

        def HAM_BAND_RANGE10_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )


    #         #***********************************
    #         #   Last Frequency and Mode Used per Band
    #         #***********************************
    #
        def HAM_BAND_FREQS(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
           cleanValue = int(userSettingValue.translate({ord(c): None for c in"-.,+"}))
           LSB: bytes = cleanValue & 0xFF
           LSB1: bytes = (cleanValue >> 8) & 0xFF
           LSB2: bytes = (cleanValue >> 16) & 0xFF
           MSB: bytes = (cleanValue >> 24) & 0xFF

           MSB = (MSB & 0x1f) + (EEPROMBuffer[memLocation+3] & 0xe0)            # must preserve upper 3 bits which is mode

           self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, LSB)
           self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation + 1, LSB1)
           self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation + 2, LSB2)
           self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation + 3, MSB)


        def HAM_BAND_FREQS1(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.HAM_BAND_FREQS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def HAM_BAND_FREQS2(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.HAM_BAND_FREQS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def HAM_BAND_FREQS3(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.HAM_BAND_FREQS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def HAM_BAND_FREQS4(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.HAM_BAND_FREQS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def HAM_BAND_FREQS5(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.HAM_BAND_FREQS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def HAM_BAND_FREQS6(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_FREQS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def HAM_BAND_FREQS7(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.HAM_BAND_FREQS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def HAM_BAND_FREQS8(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.HAM_BAND_FREQS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def HAM_BAND_FREQS9(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.HAM_BAND_FREQS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def HAM_BAND_FREQS10(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
           self.HAM_BAND_FREQS(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)


        def HAM_BAND_FREQS_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
            updatedByte = (EEPROMBuffer[memLocation] & 0x1f) + (MODE_SELECT.index(userSettingValue)<<5)
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, updatedByte)

        def HAM_BAND_FREQS1_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def HAM_BAND_FREQS2_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def HAM_BAND_FREQS3_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def HAM_BAND_FREQS4_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def HAM_BAND_FREQS5_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def HAM_BAND_FREQS6_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def HAM_BAND_FREQS7_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def HAM_BAND_FREQS8_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def HAM_BAND_FREQS9_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def HAM_BAND_FREQS10_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.HAM_BAND_FREQS_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)


    #         # ***********************************
    #         #   SDR SETTINGS
    #         # ***********************************
    #
        def BOOT_INTO_SDR_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            if BOOT_MODE.index(userSettingValue):
                tmpByte: bytes = EEPROMBuffer[memLocation] | 0x02
            else:
                tmpByte: bytes = EEPROMBuffer[memLocation] & (~0x02)
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

        def SDR_OFFSET_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            tmpByte: bytes = (SDR_OFFSET_MODE.index(userSettingValue)<<2) | EEPROMBuffer[memLocation] & (~0xC)
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

        def SDR_FREQUENCY(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            cleanValue = int(userSettingValue.translate({ord(c): None for c in"-.,+"}))
            self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, cleanValue)


    #         # ***********************************
    #         #   WSPR SETTINGS
    #         # ***********************************
    #
        def WSPR_BAND1_TXFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            cleanValue = int(userSettingValue.translate({ord(c): None for c in"-.,+"}))
            self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, cleanValue)

        def WSPR_BAND2_TXFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            cleanValue = int(userSettingValue.translate({ord(c): None for c in"-.,+"}))
            self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, cleanValue)

        def WSPR_BAND3_TXFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            cleanValue = int(userSettingValue.translate({ord(c): None for c in"-.,+"}))
            self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, cleanValue)

        def WSPR_BAND1_MULTICHAN(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit16_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

        def WSPR_BAND2_MULTICHAN(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit16_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

        def WSPR_BAND3_MULTICHAN(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit16_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

        def WSPR_BAND_REG1(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
            i: int =0
            regContents = userSettingValue.split(',')
            while i < WSPRREG1LENGTH:
                self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation+i, int(regContents[i],16))
                i += 1

        def WSPR_BAND1_REG1(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
                self.WSPR_BAND_REG1(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def WSPR_BAND2_REG1(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
                self.WSPR_BAND_REG1(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def WSPR_BAND3_REG1(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
                self.WSPR_BAND_REG1(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)


        def WSPR_BAND_REG2(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
            i: int =0
            regContents = userSettingValue.split(',')
            while i < WSPRREG2LENGTH:
                self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation+i, int(regContents[i],16))
                i += 1

        def WSPR_BAND1_REG2(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
                self.WSPR_BAND_REG2(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def WSPR_BAND2_REG2(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
                self.WSPR_BAND_REG2(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def WSPR_BAND3_REG2(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
                self.WSPR_BAND_REG2(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def WSPR_COUNT(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

        def WSPR_MESSAGE_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
            i: int =0
            nameLength = len(userSettingValue)
            while i < WSPRNAMELENGTH:
                if i < nameLength:
                    self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation+i, ord(userSettingValue[i]))
                else:
                    self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation + i, ord(" ") )  #blank pads
                i += 1


        def WSPR_MESSAGE1_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.WSPR_MESSAGE_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def WSPR_MESSAGE2_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.WSPR_MESSAGE_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def WSPR_MESSAGE3_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.WSPR_MESSAGE_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def WSPR_MESSAGE4_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.WSPR_MESSAGE_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def WSPR_MESSAGE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
            i: int =0
            message = userSettingValue.split(',')
            while i < SIZEOFWSPRMESSAGES:
                self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation+i, int(message[i],16))
                i += 1

        def WSPR_MESSAGE1(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.WSPR_MESSAGE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def WSPR_MESSAGE2(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.WSPR_MESSAGE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def WSPR_MESSAGE3(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.WSPR_MESSAGE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def WSPR_MESSAGE4(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.WSPR_MESSAGE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    #
    #         # ***********************************
    #         #   HARDWARE SETTINGS
    #         # ***********************************
    #
        def S_METER_LEVELS(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            if(BOOL_SELECT.index(userSettingValue)):
                tmpByte: bytes = EEPROMBuffer[memLocation] | 0x08
            else:
                tmpByte: bytes = EEPROMBuffer[memLocation] & (~0x08)
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

        def S_METER_LEVEL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, round(int(userSettingValue)>>2))

        def S_METER_LEVEL1(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.S_METER_LEVEL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def S_METER_LEVEL2(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.S_METER_LEVEL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def S_METER_LEVEL3(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.S_METER_LEVEL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def S_METER_LEVEL4(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.S_METER_LEVEL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def S_METER_LEVEL5(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.S_METER_LEVEL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def S_METER_LEVEL6(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.S_METER_LEVEL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def S_METER_LEVEL7(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.S_METER_LEVEL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def S_METER_LEVEL8(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.S_METER_LEVEL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)


        def I2C_LCD_MASTER(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue,16))

        def I2C_LCD_SECOND(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue, 16))

        def I2C_ADDR_SI5351(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue,16))


    #
    #         # ***********************************
    #         #   ADVANCED UX SETTINGS
    #         # ***********************************
    #

        def MESSAGE_LINE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            tmpByte: bytes = (EEPROMBuffer[memLocation] & (~0x10)) | (BOOL_SELECT.index(userSettingValue)<<4)
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

        def SCROLLING_DISPLAY(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            tmpByte: bytes = (EEPROMBuffer[memLocation] & (~0x04)) | (BOOL_SELECT.index(userSettingValue)<<2)
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

        def ONE_TWO_LINE_TOGGLE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            tmpByte: bytes = (EEPROMBuffer[memLocation] & (~0x01)) | BOOL_SELECT.index(userSettingValue)
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

        def NEXTION_DISPLAY_CALL_SIGN(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            tmpByte: bytes = (EEPROMBuffer[memLocation] & (~0x02)) | (BOOL_SELECT.index(userSettingValue) << 1)
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

        def MAIN_SCREEN_FORMAT(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, MAIN_MENU_SELECT.index(userSettingValue) )

        def STORED_IF_SHIFT(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            tmpByte: bytes = (EEPROMBuffer[memLocation] & (~0x40)) | (BOOL_SELECT.index(userSettingValue) << 6)
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

        def IF_SHIFTVALUE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):

            if( userSettingValue[0] == '-'):              #we have a negative number and have to put it into 2's complement
                tmpStr: str = userSettingValue[1:len(userSettingValue)]         #strip off the leading "-"
                tmpInt: int = int(tmpStr)
                tmpInt = (~tmpInt+1)& 0xffff                                    #Put it in 2's complement
                self.set_unit16_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpInt)
            else:
                self.set_unit16_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue) & 0xffff)

        def CW_DISPLAY_FREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            if (userSettingValue == "RX"):                                      #If RX Display shows RX frequency
                tmpByte: bytes = EEPROMBuffer[memLocation]  | 0x80              #set shiftDisplay on
                self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

                tmpByte: bytes = EEPROMBuffer[memLocation+1]  & (~0x80)           #set enable Adjust CW Frequency off
                self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation+1, tmpByte)

            else:                                                               #Assume its the display shows TX frequency (preferred)
                tmpByte: bytes = EEPROMBuffer[memLocation]  & (~0x80)             #set shiftDisplay off
                self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

                tmpByte: bytes = EEPROMBuffer[memLocation+1]  |  0x80            #set disable Adjust CW Frequency off
                self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation + 1, tmpByte)

        def CW_FREQUENCY_ADJUSTMENT(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            tmpByte: bytes = (EEPROMBuffer[memLocation] & (~0x3f)) + (round(int(userSettingValue)/10))
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

    #
    #         # ***********************************
    #         #   EXTENDED KEYS
    #         # ***********************************
    #
        def EXTENDED_KEY_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, round(int(userSettingValue)>>2))

        def EXTENDED_KEY1_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.EXTENDED_KEY_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def EXTENDED_KEY2_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.EXTENDED_KEY_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def EXTENDED_KEY3_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.EXTENDED_KEY_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def EXTENDED_KEY4_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.EXTENDED_KEY_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def EXTENDED_KEY5_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.EXTENDED_KEY_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def EXTENDED_KEY6_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.EXTENDED_KEY_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)


        def EXTENDED_KEY_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, round(int(userSettingValue)>>2))

        def EXTENDED_KEY1_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.EXTENDED_KEY_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def EXTENDED_KEY2_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.EXTENDED_KEY_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def EXTENDED_KEY3_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.EXTENDED_KEY_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def EXTENDED_KEY4_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.EXTENDED_KEY_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def EXTENDED_KEY5_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.EXTENDED_KEY_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def EXTENDED_KEY6_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.EXTENDED_KEY_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)


        def EXTENDED_KEY_FUNC(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, FTN_KEY_SELECT.index(userSettingValue))

        def EXTENDED_KEY1_FUNC(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.EXTENDED_KEY_FUNC(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def EXTENDED_KEY2_FUNC(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.EXTENDED_KEY_FUNC(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def EXTENDED_KEY3_FUNC(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.EXTENDED_KEY_FUNC(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def EXTENDED_KEY4_FUNC(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.EXTENDED_KEY_FUNC(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def EXTENDED_KEY5_FUNC(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.EXTENDED_KEY_FUNC(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def EXTENDED_KEY6_FUNC(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.EXTENDED_KEY_FUNC(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)


    #
    #         # ***********************************
    #         #   CUSTOM LPF FILTERS
    #         # ***********************************
    #
    #
        def CUST_LPF_ENABLED(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, LPF_MODE_SETTING[LPF_MODE_SELECT.index(userSettingValue)])


        def CUST_LPF_FILTER_ENDFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
            if userSettingValue != '':
                self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))
            else:
                self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, 0)
        def CUST_LPF_FILTER1_ENDFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CUST_LPF_FILTER2_ENDFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CUST_LPF_FILTER3_ENDFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CUST_LPF_FILTER4_ENDFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CUST_LPF_FILTER5_ENDFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CUST_LPF_FILTER6_ENDFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CUST_LPF_FILTER7_ENDFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)


        def CUST_LPF_FILTER_CONTROL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):

            tmpByte: bytes = 0x00
            if str(userSettingValue) != "NONE":
                for i in LPF_CTRL_SELECT:
                    if str(i) in str(userSettingValue):
                        tmpByte = tmpByte | (1<<LPF_CTRL_SELECT.index(i))

            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)


        def CUST_LPF_FILTER1_CONTROL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CUST_LPF_FILTER2_CONTROL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CUST_LPF_FILTER3_CONTROL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CUST_LPF_FILTER4_CONTROL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CUST_LPF_FILTER5_CONTROL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CUST_LPF_FILTER6_CONTROL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

        def CUST_LPF_FILTER7_CONTROL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
            self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)


    #
    #         # ***********************************
    #         #   Extended EEPROM Settings (>= 1204)
    #         # ***********************************
    #
    #

        def EXT_FIRMWARE_ID_ADDR1(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            # value.text = hex(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))
            pass

        def EXT_FIRMWARE_ID_ADDR2(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            # value.text = hex(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))
            pass

        def EXT_FIRMWARE_ID_ADDR3(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            # value.text = hex(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))
            pass

        def EXT_UBITX_BOARD_VERSION(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            # value.text = EXT_UBITX_BOARD_VERSION_SELECT[self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)]
            pass

        def EXT_DATE_TIME_STAMP(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):

            # timeStamp :str = ''
            #
            # # Get month# and translate to month text
            #
            # timeStamp += = MONTH3CHARS[int((self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)
            #                             + self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+1)))] + ' '
            #
            # # get day
            # timeStamp += = str(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+2))
            #                 + str(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+3)) \
            #                 + ', '
            #
            # # Get year
            # timeStamp += = str((self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+4))
            #                 + str(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+5))
            #                 + str(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+6))
            #                 + str(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation+7))
            #
            # # Add the hour
            # timeStamp += str(get_uint8_FromEEPROM(EEPROMBuffer, memLocation+8))
            #                 + str(get_uint8_FromEEPROM(EEPROMBuffer, memLocation+9))
            #                 + ':'
            # # Add the min
            # timeStamp += str(get_uint8_FromEEPROM(EEPROMBuffer, memLocation+10))
            #                 + str(get_uint8_FromEEPROM(EEPROMBuffer, memLocation+11))
            #
            # value.text = timeStamp
            pass


        def EXT_PROCESSOR_TYPE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            # value.text = EXT_PROCESSOR_TYPE_SELECT[self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)]
            pass

        def EXT_DISPLAY_TYPE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            # value.text = EXT_DISPLAY_TYPE_SELECT[self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)]
            pass

        def EXT_FUNCTIONALITY_SET(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            # value.text = EXT_FUNCTIONALITY_SET_SELECT[self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)]
            pass

        def EXT_SMETER_SELECTION(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
            # value.text = EXT_SMETER_SELECTION_SELECT[self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)]
            pass


        def defaultFunc(self, *args):
                print ("Command not recognised:", args[0])

        def get(self, cmd, *args):
                return getattr(self, cmd, self.defaultFunc)(*args)




        def defaultFunc(self, *args):
            print ("Command not recognised:", args[0])

        def set(self, cmd, *args):
            return getattr(self, cmd, self.defaultFunc)(*args)


#   ******************************************************************************************************
#   member functions of the eepromObj Class
#   ******************************************************************************************************

    def __init__(self, log, **kw):
        self.log = log
        self.EEPROMBuffer = bytearray(MAXEEPROMSIZE)     # Used to save the in memory copy

        self.EEPROMBufferDirty=bitarray(MAXEEPROMSIZE)         # create a bit array of the same size that we can use to track dirty "bytes"
        self.EEPROMBufferDirty.setall(0)                    # clear all bits. When we write a byte into the EEPROMBuffer, we will set
                                                            # corresponding dirty bit to 1

        if eepromObj.xmlTemplatesProcessed == False:        # first time here, so go ahead and parse the two template files
            eepromObj.xmlTemplatesProcessed = True          # Only one try per customer

            self.log.println("timestamp",  "Opening EEPROM Memory Mapping file")

            # Try reading and parsing the XML files that maps the EEPROM memory locations

            try:
                eepromObj.EEPROMroot = ET.parse(EEPROMMEMORYMAP)
            except:
                self.log.println("timestamp",  EEPROMMEMORYMAP + " is missing or corrupted")
                tk.messagebox.showerror(title="FATAL ERROR", message=EEPROMMEMORYMAP + " is missing or corrupted. Please re-install application. \nEXITING")
                sys.exit(-1)

            self.log.println("timestamp",  "Completed preprocessing of EEPROM Memory Mapping")

            # No we need to process the binary data into an XML tree
            self.log.println("timestamp",  "Opening User Modification File template")

            try:
                eepromObj.UserModroot = ET.parse(USERMODFILETEMPLACE)
            except:
                self.log.printerror("timestamp",  USERMODFILETEMPLACE + " is missing or corrupted")
                tk.messagebox.showerror(title="FATAL ERROR", message=USERMODFILETEMPLACE + " is missing or corrupted. Please re-install application. \nEXITING")
                sys.exit(-1)

            self.log.println("timestamp",  "Completed preprocessing of User Modification Template")

    def read(self):
        pass

    def write(self):
        pass

    def decode(self)->object:
        #
        #   This routine uses the EEPROM map to drive decoding of the contents in the EEPROMBuffer
        #   and merge it into the userModroot template.
        #   returns a pointer to the root of this created tree
        #
        #
        #   We have opened the template file, now merge the contents into the tree
        UserMods = self.getters(self.log)

        self.log.println("timestamp", "Interpreting BINARY data")
        #
        # For each setting in the EEPROM Map, there is a "getter" that will process it and write it to the user
        # mod file
        #
        for userSetting in eepromObj.EEPROMroot.findall('.//SETTING'):


            #get name, location in eeprom buffer, number of bytes, and type of data
            userSettingName = userSetting.get("NAME")
            memLocation = int(userSetting.find("EEPROMStart").text)

            #now look in eeprom map for buffer memory location, size (in bytes) and data type

            eepromSetting = eepromObj.EEPROMroot.find('.//SETTING[@NAME="{}"]'.format(userSettingName))

            memLocation = int(eepromSetting.find("EEPROMStart").text)


            #get tag for where data will be stored withing UserModroot

            userSettingTag = eepromObj.UserModroot.find('.//SETTING[@NAME="{}"]'.format(userSettingName))

            if (userSettingTag != None):
                valueTag=userSettingTag.find('.//value')
                UserMods.get(userSettingName, userSettingName, self.EEPROMBuffer, memLocation, valueTag, eepromObj.EEPROMroot, userSettingTag)

        return eepromObj.UserModroot


        self.log.println("timestamp", "Completed Processing of Binary Data")



    def encode(self, updatedUserModroot):

        EEPROM_Memory = self.setters()

        #
        # using the modified user settings (updatedUserModroot) call the "setter" functions for each xml element
        # to update the value in the instances EEPROMBuffer
        #
        for userSetting in updatedUserModroot.findall('.//SETTING'):


            #get setting name and value
            userSettingName = userSetting.get("NAME")
            userSettingValue = userSetting.find("value").text
            if DEBUGAPP:
                print(userSettingName)

            #now look in eeprom map for buffer memory location, size (in bytes) and data type

            eepromSetting = eepromObj.EEPROMroot.find('.//SETTING[@NAME="{}"]'.format(userSettingName))

            memLocation = int(eepromSetting.find("EEPROMStart").text)

            if (userSettingValue != None):
                EEPROM_Memory.set(userSettingName, userSettingName, self.EEPROMBuffer, self.EEPROMBufferDirty, memLocation, userSettingValue, eepromObj.EEPROMroot, userSetting)
            else:
                self.log.printerror("timestamp","Warning: skipping because value = NONE, Setting Name" + userSettingName)

#   ******************************************************************************************************
#   Two subclasses of eepromObj that are refined for Com and File writing
#   ******************************************************************************************************

class eepromUBITX (eepromObj):          # subclass

    def __init__(self, comPort, log, **kw):
        super().__init__ (log, **kw)
        self.comPort = comPort

    def getEEPROMSize(self):                # Read from Com Port

        self.comPort.write(bytes([0, 0, 0, 0, GETSIZECOMMAND]))

        # create buffer to save bytes being returned
        # byte1 = 0x2 - always
        # 4 bytes LSB first
        # byte3 = checksum of bytes above
        # byte4 = 0x0 (ACK)


        checkSum: int = 0x02
        theEEPROMsize: int =0

        i = -1
        while i < 4:
             if self.comPort.in_waiting != 0:
                if i< 0:
                    throwaway = self.comPort.read(1)
                else:
                    readByte = int.from_bytes(self.comPort.read(),"little",signed=False)
                    theEEPROMsize += readByte << (i*8)
                    checkSum = (checkSum + readByte ) & 0xFF
                i += 1

    #   get checksum sent by radio CAT control
        while self.comPort.in_waiting == 0:
            sleep(0.01)
        sentCheckSum = int.from_bytes(self.comPort.read(1),"little",signed=False)

    #   get trailing byte. Must be an ACK (0x00)
        while self.comPort.in_waiting == 0:
            sleep(0.01)
        trailingByte = int.from_bytes(self.comPort.read(1),"little",signed=False)

        if(sentCheckSum!=checkSum)|(trailingByte!=0):
            self.log.printerror("timestamp","Bad Checksum on EEPROM Read")
            tkinter.messagebox.showerror(title="ERROR", message="Bad Checksum reading size of EEPROM from Radio.\nTry restarting radio, ensuring the USB cable plugged in securely, and then restart application. \nEXITING")
            sys.exit(-1)
        return theEEPROMsize


    def read(self):                # Read from Com Port

        EEPROMSIZE = self.getEEPROMSize()
        if EEPROMSIZE > MAXEEPROMSIZE:
            EEPROMSIZE = MAXEEPROMSIZE
        print("eepromsize = ", EEPROMSIZE)

        # LSB = memlocation & 0xff
        # MSB = (memlocation >> 8) & 0xff

        NumLSB = EEPROMSIZE & 0xff
        NumMSB = (EEPROMSIZE >> 8) & 0xff

        # send command buffer to radio
        # byte1 = LSB of the start location in EEPROM
        # byte2 = MSB of the start location in EEPROM
        # byte3 = LSB of the total bytes to read from EEPROM
        # byte4 - MSB of the total bytes to read from EEPROM
        # byte5 - Command telling the radio what to do

        self.comPort.write(bytes([0, 0, NumLSB, NumMSB, READCOMMAND]))

        # create buffer to save bytes being returned
        # byte1 = 0x2 - always
        # lots of bytes = number of bytes requested
        # byte3 = checksum of bytes above
        # byte4 = 0x0 (ACK)


        checkSum: int = 0x02

        i = -1
        while i < EEPROMSIZE:
            if self.comPort.in_waiting != 0:
                if i< 0:
                    throwaway = self.comPort.read(1)
                else:
                    self.EEPROMBuffer[i] = int.from_bytes(self.comPort.read(1),"little")
                    checkSum = (checkSum+self.EEPROMBuffer[i] ) & 0xFF
                i += 1

    #   get checksum sent by radio CAT control
        while self.comPort.in_waiting == 0:
            sleep(0.01)
        sentCheckSum = int.from_bytes(self.comPort.read(1),"little",signed=False)

    #   get trailing byte. Must be an ACK (0x00)
        while self.comPort.in_waiting == 0:
            sleep(0.01)
        trailingByte = int.from_bytes(self.comPort.read(1),"little",signed=False)

        if(sentCheckSum!=checkSum)|(trailingByte!=0):
            self.log.printerror("timestamp","Bad Checksum on EEPROM Read")
            tkinter.messagebox.showerror(title="ERROR", message="Bad Checksum reading from Radio.\nTry restarting radio, ensuring the USB cable plugged in securely, and then restart application. \nEXITING")
            sys.exit(-1)



    def writeByteToEEPROM(self, memAddress: int, outbyte: int):
        self.log.println("timestamp","EEPROM Memory Address = " + str(memAddress))
        LSB: bytes = memAddress & 0xff
        MSB: bytes = (memAddress >> 8) & 0xff
    #    print(type(LSB),"\t", type(MSB),"\t", type(outbyte))
    #    print(memAddress)
        checkByte: int = ((LSB + MSB + outbyte) % 256) & 0xff
        bytesToWrite = bytes([LSB, MSB, outbyte, checkByte, WRITECOMMAND])
        self.comPort.write(bytesToWrite)


    def write(self):                # Write to Com Port

        self.log.println("timestamp","The Following EEPROM Locations Were Updated")
        i: int = 0
        while i < EEPROMSIZE:
            if self.EEPROMBufferDirty[i]:  # Got a dirty byte
    #            print(f"{i:04}", "\t", inMemBuffer[i],"\t",type(inMemBuffer[i]))
                self.writeByteToEEPROM(i, self.EEPROMBuffer[i])

                doneWithByte: bool = False
                retryCnt: int = 0
                while True:  # keep tring to write until successful or exceed # retries

                    while self.comPort.in_waiting == 0:
                        sleep(0.005)
                    resultCode = int.from_bytes(self.comPort.read(1), "little", signed=False)
                    while self.comPort.in_waiting == 0:
                        sleep(0.005)
                    trailingByte = int.from_bytes(self.comPort.read(1), "little", signed=False)
                    if (resultCode == OK) & (trailingByte == ACK):
                        break
                    else:
                        self.log.printerror("timestamp","retrying byte =" + str(i))
                        self.log.printerror("timestamp","resultcode=" + str(resultCode))
                        self.log.printerror("timestamp","trailingByte=" + str(trailingByte))
                        retryCnt += 1
                        if retryCnt > RETRIES:
                            self.log.printerror("timestamp","number of retries exceeded on memory location: " + str(i))
                            return (1)  # Failure
            i += 1
        return (0)                      # Success

class eepromFILE (eepromObj):
    def __init__(self, fname, log, **kw):
        super().__init__ (log, **kw)
        self.fname = fname

    def read(self):                 # Read from binary file
        fd = open(self.fname, "rb")
        self.EEPROMBuffer=bytearray(fd.read(BACKUPFILESIZE))
        fd.close()

    def write(self):                # Write to binary file
        fd = open(self.fname, "wb")
        fd.write(self.EEPROMBuffer)
        fd.close()