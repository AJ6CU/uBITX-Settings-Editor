from lxml import etree as ET
from globalvars import *



class getters(object):
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
    def FIRMWAR_ID_ADDR1(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        value.text = hex(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))

    def FIRMWAR_ID_ADDR2(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        value.text = hex(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))

    def FIRMWAR_ID_ADDR3(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
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
        value.text = str(round(1200/self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)))

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
        value.text = str(round(1200/self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)))

    def CW_DELAY_MS(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        value.text = str(10 * self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))

    def CW_START_MS(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        value.text = str(2 * self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))

#         #***********************************
#         #   COMMON MEMORY KEYER
#         #***********************************
#

    def USER_CALLSIGN(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, _unused1):
#       First need to confirm that a valid call sign has been entered by looking for 0x59 in
#       "USER_CALLSIGN_KEY"

        if ((self.XML_Get_uint8_FromEEPROM  (EEPROMroot, "USER_CALLSIGN_KEY", EEPROMBuffer) & 0xff) == 0x59):     # good a good one, can continue
            callSignLength = self.XML_Get_uint8_FromEEPROM (EEPROMroot, "USER_CALLSIGN_LEN", EEPROMBuffer) & 0x7f   #Important to mask it here as

            j: int = 0                                                                                        #Upper bit used to for LCD display callsign on startup
            callSignStr: str = ''
            while j < callSignLength:
                callSignStr += str(chr(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation + j)))
                j += 1
            value.text = str(callSignStr)


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

    def CW_MEMORY_KEYER_MSGS(self, SettingName, EEPROMBuffer, memLocation, value, EEPROMroot, valueElement):

        cwAutoDataPtr = self.XML_MemLocation_FromEEPROM(EEPROMroot, "CW_AUTO_DATA")
        msgCount=self.XML_Get_uint8_FromEEPROM (EEPROMroot, "CW_AUTO_COUNT", EEPROMBuffer)                #Get total existing msgs

        value.text = str(msgCount)                                                      #Store message count in Element
        #
        # We are now going to create one <message>cq cq de ...</message> for each existing message in eprom
        #
        i = 0
        while i < msgCount:
            #
            # cwAutoDataPtr points to first location in the heap
            # Starting there, each two bytes is start/end pairs. So if there are 3 messages
            # cwAutoDataPtr = location containing the start byte of 1st message, +1 the byte containing the end location
            # +2 is start of second message, +3 end of second message, etc. Note these are locations, you got to
            # get the data in these locations to actually get the offset for each message.
            #
            msgStartInHeapLocation = cwAutoDataPtr +(i*2)       #The start ends are are beginning of heap. 1st msg has start at
            msgStartInHeap = cwAutoDataPtr + self.get_uint8_FromEEPROM(EEPROMBuffer, msgStartInHeapLocation)

            msgEndInHeapLocation = cwAutoDataPtr + (i*2)+1      #cwAutoDataptr , end at cwAutoDataPtr+1, 2nd cwAutoDataPtr+2, cwAutoDataPtr+3), etc.
            msgEndInHeap = cwAutoDataPtr + self.get_uint8_FromEEPROM(EEPROMBuffer, msgEndInHeapLocation)
            #
            #so at this point we have the locations of start/end of each message. Now go collect the actual characters
            #

            j: int = 0
            msgStr: str = ''
            numBytes = (msgEndInHeap+1) - msgStartInHeap
            while j< int(numBytes):
                msgStr += str(chr(self.get_uint8_FromEEPROM(EEPROMBuffer, msgStartInHeap + j)))
                j+=1

            ET.SubElement(valueElement,'message').text = msgStr         # Have the message, add a message tag to XML file
            i+=1
        # add blank message elements for user to fill in so a total of 10 are displayed
        while i < TOTALCWMESSAGES:
            ET.SubElement(valueElement, 'message')
            i+=1

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
        value.text = LPF_MODE_SELECT[LPF_MODE_SETTING.index((self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation)))]

    def CUST_LPF_FILTER_ENDFREQ(self, SettingName, EEPROMBuffer, memLocation, value):
        value.text = str(self.get_uint8_FromEEPROM(EEPROMBuffer, memLocation))

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



    def defaultFunc(self, *args):
            print ("Command not recognised:", args[0])

    def get(self, cmd, *args):
            return getattr(self, cmd, self.defaultFunc)(*args)