import bitarray
from lxml import etree as ET
from globalvars import *

class setters(object):

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


    def XML_Get_Byte_FromEEPROM(self, xmlSubTree, settingName, memBuffer) -> int:
        settingTag = xmlSubTree.find(('.//SETTING[@NAME="{}"]'.format(settingName)))
        memAddress = int(settingTag.find("EEPROMStart").text)
        return memBuffer[memAddress]

    def XML_MemLocation_FromEEPROM(self, xmlSubTree, settingName) -> int:
        settingTag = xmlSubTree.find(('.//SETTING[@NAME="{}"]'.format(settingName)))
        memAddress = int(settingTag.find("EEPROMStart").text)
        return memAddress

    def set_unit8_InEEPROMBuffer(self, memBuffer: bytearray, dirty: bitarray.bitarray, memAddress: int, outData: bytes):
        if memBuffer[memAddress] != outData:  # we have new data here; update and mark dirty
            memBuffer[memAddress] = outData
            dirty[memAddress] = 1

    def set_unit16_InEEPROMBuffer(self, memBuffer: bytearray, dirty: bitarray.bitarray, memAddress: int, outData: int):
        LSB: bytes = int(outData) & 0xFF
        MSB: bytes = (int(outData) >> 8) & 0xFF
        self.set_unit8_InEEPROMBuffer(memBuffer, dirty, memAddress, LSB)
        self.set_unit8_InEEPROMBuffer(memBuffer, dirty, memAddress + 1, MSB)

    def set_unit32_InEEPROMBuffer(self, memBuffer: bytearray, dirty: bitarray.bitarray, memAddress: int, outData: int):
        LSB: bytes = int(outData) & 0xFF
        LSB1: bytes = (int(outData) >> 8) & 0xFF
        LSB2: bytes = (int(outData) >> 16) & 0xFF
        MSB: bytes = (int(outData) >> 24) & 0xFF

        self.set_unit8_InEEPROMBuffer(memBuffer, dirty, memAddress, LSB)
        self.set_unit8_InEEPROMBuffer(memBuffer, dirty, memAddress + 1, LSB1)
        self.set_unit8_InEEPROMBuffer(memBuffer, dirty, memAddress + 2, LSB2)
        self.set_unit8_InEEPROMBuffer(memBuffer, dirty, memAddress + 3, MSB)

#         #***********************************
#         #   RADIO CALIBRATION SETTINGS
#         #***********************************
    def MASTER_CAL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def USB_CAL(self,  SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CW_CAL(self,  SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def IF1_CAL_ON_OFF_SWITCH(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        if BOOL_SELECT.index(userSettingValue):
            tmpByte: bytes = EEPROMBuffer[memLocation] | 0x01
        else:
            tmpByte: bytes = EEPROMBuffer[memLocation] & (~0x01)
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)


    def IF1_CAL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))


    def IF1_CAL_ADD_SUB(self,  SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
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
    def VFO_A(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

    def VFO_B(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

    def VFO_A_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, MODE_SELECT.index(userSettingValue))

    def VFO_B_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, MODE_SELECT.index(userSettingValue))

    def TUNING_STEP_INDEX(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

    def TUNING_STEP1(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, self.assembleTuneStepByte(userSettingValue))

    def TUNING_STEP2(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, self.assembleTuneStepByte(userSettingValue))

    def TUNING_STEP3(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, self.assembleTuneStepByte(userSettingValue))

    def TUNING_STEP4(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, self.assembleTuneStepByte(userSettingValue))


    def TUNING_STEP5(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, self.assembleTuneStepByte(userSettingValue))

#
#         #***********************************
#         #   COMMON CW SETTINGS
#         #***********************************
#
    def CW_KEY_TYPE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, CW_KEY_SELECT.index(userSettingValue))

    def CW_SIDETONE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

    def CW_SPEED_WPM(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit16_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, round(1200/int(userSettingValue)))

    def CW_DELAY_MS(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, round(int(userSettingValue)/10))

    def CW_START_MS(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, round(int(userSettingValue)>>1))

#         #***********************************
#         #   COMMON MEMORY KEYER
#         #***********************************
#


#
#         case "USER_CALLSIGN":
#             print("need work:", userSettingName)
# #     # First need to confirm that a valid call sign has been entered by looking for 0x59 in
# #     # "USER_CALLSIGN_KEY"
# #
# #     if ((XML_Get_Byte_FromEEPROM (EEPROMroot, "USER_CALLSIGN_KEY", EEPROMBuffer) & 0xff) == 0x59):  # good a good one, can continue
# #         callSignLength = XML_Get_Byte_FromEEPROM(EEPROMroot, "USER_CALLSIGN_LEN", EEPROMBuffer) & 0x7f   #Important to mask it here as
# #
# #         j: int = 0                                                                                        #Upper bit used to for LCD display callsign on startup
# #         callSignStr: str = ''
# #         while j < callSignLength:
# #             callSignStr += str(chr(get_Byte_FromEEPROM(EEPROMBuffer, memLocation + j)))
# #             j += 1
# #         value.text = str(callSignStr)
#         case "QSO_CALLSIGN":
#             print("need work:", userSettingName)
# #     # To get the alternative callsign for CW keyer, need to first get its length
# #     settingTag = EEPROMroot.find('.//SETTING[@NAME="QSO_CALLSIGN"]')
# #     lastPosCallSign = int(settingTag.find("EEPROMStart").text)
# #     altCallSignLen = get_Byte_FromEEPROM(EEPROMBuffer, lastPosCallSign)
# #
# #     if (altCallSignLen >0) & (altCallSignLen <= MAXCALLSIGNLEN):                    #validate call sign before processing
# #
# #         callSignStr: str = ''
# #         callSignOffset = lastPosCallSign - altCallSignLen
# #         j: int = 0
# #         while j < altCallSignLen:
# #             callSignStr += str(chr(get_Byte_FromEEPROM(EEPROMBuffer, callSignOffset + j)))
# #             j += 1
# #         value.text = str(callSignStr)
#         case "CW_MEMORY_KEYER_MSGS":
#             print("need work:", userSettingName)
# #     cwAutoData = EEPROMroot.find('.//SETTING[@NAME="CW_AUTO_DATA"]')                 #Get ptr to start of data heap
# #     cwAutoDataPtr = int(cwAutoData.find('EEPROMStart').text)
# #
# #     msgCount=XML_Get_Byte_FromEEPROM(EEPROMroot, "CW_AUTO_COUNT", EEPROMBuffer)     #Get total existing msgs
# #
# #     value.text = str(msgCount)                                                      #Store message count in Element
# #     #
# #     # We are now going to create one <message>cq cq de ...</message> for each existing message in eprom
# #     #
# #     i = 0
# #     while i < msgCount:
# #         #
# #         # cwAutoDataPtr points to first location in the heap
# #         # Starting there, each two bytes is start/end pairs. So if there are 3 messages
# #         # cwAutoDataPtr = location containing the start byte of 1st message, +1 the byte containing the end location
# #         # +2 is start of second message, +3 end of second message, etc. Note these are locations, you got to
# #         # get the data in these locations to actually get the offset for each message.
# #         #
# #         msgStartInHeapLocation = cwAutoDataPtr +(i*2)       #The start ends are are beginning of heap. 1st msg has start at
# #         msgStartInHeap = cwAutoDataPtr + get_Byte_FromEEPROM(EEPROMBuffer, msgStartInHeapLocation)
# #
# #         msgEndInHeapLocation = cwAutoDataPtr + (i*2)+1      #cwAutoDataptr , end at cwAutoDataPtr+1, 2nd cwAutoDataPtr+2, cwAutoDataPtr+3), etc.
# #         msgEndInHeap = cwAutoDataPtr + get_Byte_FromEEPROM(EEPROMBuffer, msgEndInHeapLocation)
# #         #
# #         #so at this point we have the locations of start/end of each message. Now go collect the actual characters
# #         #
# #
# #         j: int = 0
# #         msgStr: str = ''
# #         numBytes = (msgEndInHeap+1) - msgStartInHeap
# #         while j< int(numBytes):
# #             msgStr += str(chr(get_Byte_FromEEPROM(EEPROMBuffer, msgStartInHeap + j)))
# #             j+=1
# #         ET.SubElement(valueElement,'message').text = msgStr
# #         i+=1
# #     # add blank message elements for user to fill in so a total of 10 are displayed
# #     while i < TOTALCWMESSAGES:
# #         ET.SubElement(valueElement, 'message')
# #         i+=1
#


#
#         #***********************************
#         #   CW ADC SETTINGS
#         #***********************************

    def CW_ADC_ST_DOT(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot):

        # first get the byte that holds all the upper bits for Straight keys and "DOTs"
        upperBitsByte = self.XML_Get_Byte_FromEEPROM(EEPROMroot, "CW_ADC_MOST_BIT1", EEPROMBuffer)  # get byte with upper two bits
        MSB_Bits = (int(userSettingValue) >> 8) & 0x03              #masking off the upper two and lower two bits
        LSB_Bits = int(userSettingValue) & 0xff

        match SettingName:                                          # bit number 01234567
            case "CW_ADC_ST_FROM":
                tmpByte: bytes = upperBitsByte & (~0x03) | MSB_Bits         # MSB are in postions 67
            case "CW_ADC_ST_TO":
                tmpByte: bytes = upperBitsByte & (~0x0C) | (MSB_Bits << 2)  # MSB are in postions 56
            case "CW_ADC_DOT_FROM":
                tmpByte: bytes = upperBitsByte & (~0x30) | (MSB_Bits << 4)  # MSB are in postions 34
            case "CW_ADC_DOT_TO":
                tmpByte: bytes = upperBitsByte & (~0xC0) | (MSB_Bits << 6)  # MSB are in postions 12

        upperBitsMemLocation = self.XML_MemLocation_FromEEPROM(EEPROMroot, "CW_ADC_MOST_BIT1")
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, upperBitsMemLocation, tmpByte)
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, LSB_Bits)


    def CW_ADC_ST_FROM(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot):
        self.CW_ADC_ST_DOT(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot)

    def CW_ADC_ST_TO(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot):
        self.CW_ADC_ST_DOT(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot)

    def CW_ADC_DOT_FROM(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot):
        self.CW_ADC_ST_DOT(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot)

    def CW_ADC_DOT_TO(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot):
        self.CW_ADC_ST_DOT(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot)


    def CW_ADC_DASH_BOTH(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot):

        # first get the byte that holds all the upper bits for Straight keys and "DOTs"
        upperBitsByte = self.XML_Get_Byte_FromEEPROM(EEPROMroot, "CW_ADC_MOST_BIT2", EEPROMBuffer)  # get byte with upper two bits
        MSB_Bits = (int(userSettingValue) >> 8) & 0x03              #masking off the upper two and lower two bits
        LSB_Bits = int(userSettingValue) & 0xff

        match SettingName:                                          # bit number 01234567
            case "CW_ADC_DASH_FROM":
                tmpByte: bytes = upperBitsByte & (~0x03) | MSB_Bits         # MSB are in postions 67
            case "CW_ADC_DASH_TO":
                tmpByte: bytes = upperBitsByte & (~0x0C) | (MSB_Bits << 2)  # MSB are in postions 56
            case "CW_ADC_BOTH_FROM":
                tmpByte: bytes = upperBitsByte & (~0x30) | (MSB_Bits << 4)  # MSB are in postions 34
            case "CW_ADC_BOTH_TO":
                tmpByte: bytes = upperBitsByte & (~0xC0) | (MSB_Bits << 6)  # MSB are in postions 12

        upperBitsMemLocation = self.XML_MemLocation_FromEEPROM(EEPROMroot, "CW_ADC_MOST_BIT2")
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, upperBitsMemLocation, tmpByte)
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, LSB_Bits)


    def CW_ADC_DASH_FROM(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot):
        self.CW_ADC_DASH_BOTH(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot)

    def CW_ADC_DASH_TO(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot):
        self.CW_ADC_DASH_BOTH(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot)

    def CW_ADC_BOTH_FROM(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot):
        self.CW_ADC_DASH_BOTH(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot)

    def CW_ADC_BOTH_TO(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot):
        self.CW_ADC_DASH_BOTH(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot)


#         #***********************************
#         #   USER CHANNELS
#         #***********************************
#
    def CHANNEL_FREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
       LSB: bytes = int(userSettingValue) & 0xFF
       LSB1: bytes = (int(userSettingValue) >> 8) & 0xFF
       LSB2: bytes = (int(userSettingValue) >> 16) & 0xFF
       MSB: bytes = (int(userSettingValue) >> 24) & 0xFF

       MSB = (MSB & 0x1f) + (EEPROMBuffer[memLocation+3] & 0xe0)            # must preserve upper 3 bits which is mode

       self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, LSB)
       self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation + 1, LSB1)
       self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation + 2, LSB2)
       self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation + 3, MSB)


    def CHANNEL_FREQ1(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
       self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ2(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
       self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ3(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
       self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ4(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
       self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ5(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
       self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ6(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ7(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
       self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ8(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
       self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ9(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
       self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ10(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
       self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ11(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
       self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ12(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
       self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ13(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
       self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ14(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
       self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ15(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
       self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ16(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
       self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ17(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
       self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ18(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
       self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ19(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
       self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ20(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
       self.CHANNEL_FREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)


    def CHANNEL_FREQ_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
        updatedByte = (EEPROMBuffer[memLocation] & 0x1f) + (MODE_SELECT.index(userSettingValue)<<5)
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, updatedByte)

    def CHANNEL_FREQ1_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ2_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ3_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ4_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ5_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ6_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ7_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ8_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ9_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ10_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ11_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ12_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ13_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ14_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ15_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ16_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ17_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ18_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ19_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ20_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_MODE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)



    def CHANNEL_FREQ_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
        if userSettingValue == "YES":
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, SHOW_CHANNEL_NAME)
        else:
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, HIDE_CHANNEL_NAME)

    def CHANNEL_FREQ1_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ2_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ3_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ4_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ5_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ6_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ7_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ8_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ9_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ10_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ11_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ12_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ13_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ14_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ15_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ16_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ17_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ18_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ19_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ20_SHOW_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.CHANNEL_FREQ_SHOW_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)



    def CHANNEL_FREQ_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue: str):
        i: int = 0
        while i < len(str(userSettingValue)):
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation + i, ord(userSettingValue[i]))
            i += 1

    def CHANNEL_FREQ1_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ2_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ3_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ4_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ5_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ6_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ7_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ8_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ9_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ10_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ11_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ12_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ13_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ14_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ15_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ16_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ17_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ18_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ19_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CHANNEL_FREQ20_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CHANNEL_FREQ_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)



#         #***********************************
#         #   HAM BANDS
#         #***********************************
#
    def TUNING_RESTICTIONS(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        tmpByte: bytes = (EEPROMBuffer[memLocation] & (~0x02)) | ((TUNE_RESTRICT_SELECT.index(str(userSettingValue)))<<1)
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

    def TX_RESTRICTIONS(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        if TX_RESTRICT_SELECT.index(str(userSettingValue)):
            tmpByte: bytes = (EEPROMBuffer[memLocation] & 0x02) + TX_RESTRICT_MINIMUM  #TX Restrictions are >= 100
        else:
            tmpByte: bytes = (EEPROMBuffer[memLocation] & 0x02)                        #This clears restriction if still there
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

    def HAM_BAND_COUNT(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))


    def HAM_BAND_RANGE_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
        self.set_unit16_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

    def HAM_BAND_RANGE1_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

    def HAM_BAND_RANGE1_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

    def HAM_BAND_RANGE2_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

    def HAM_BAND_RANGE3_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

    def HAM_BAND_RANGE4_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

    def HAM_BAND_RANGE5_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

    def HAM_BAND_RANGE6_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

    def HAM_BAND_RANGE7_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

    def HAM_BAND_RANGE8_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

    def HAM_BAND_RANGE9_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)

    def HAM_BAND_RANGE10_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,)


    def HAM_BAND_RANGE_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
        self.set_unit16_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

    def HAM_BAND_RANGE1_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

    def HAM_BAND_RANGE1_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

    def HAM_BAND_RANGE2_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

    def HAM_BAND_RANGE3_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

    def HAM_BAND_RANGE4_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

    def HAM_BAND_RANGE5_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

    def HAM_BAND_RANGE6_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

    def HAM_BAND_RANGE7_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

    def HAM_BAND_RANGE8_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

    def HAM_BAND_RANGE9_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

    def HAM_BAND_RANGE10_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.HAM_BAND_RANGE_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, )

#         # ***********************************
#         #   SDR SETTINGS
#         # ***********************************
#
    def BOOT_INTO_SDR_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        if BOOT_MODE.index(userSettingValue):
            tmpByte: bytes = EEPROMBuffer[memLocation] | 0x02
        else:
            tmpByte: bytes = EEPROMBuffer[memLocation] & (~0x02)
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

    def SDR_OFFSET_MODE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        tmpByte: Bytes = (SDR_OFFSET_MODE.index(userSettingValue)<<2) | EEPROMBuffer[memLocation] & (~0xC)
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

    def SDR_FREQUENCY(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))


#         # ***********************************
#         #   WSPR SETTINGS
#         # ***********************************
#

    def WSPR_COUNT(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

    def WSPR_MESSAGE_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
        i: int =0
        nameLength = len(userSettingValue)
        while i < 5:
            if i < nameLength:
                self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation+i, ord(userSettingValue[i]))
            else:
                self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation + i, ord(" ") )  #blank pads
            i += 1


    def WSPR_MESSAGE1_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.WSPR_MESSAGE_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def WSPR_MESSAGE2_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.WSPR_MESSAGE_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def WSPR_MESSAGE3_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.WSPR_MESSAGE_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def WSPR_MESSAGE4_NAME(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.WSPR_MESSAGE_NAME(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def WSPR_MESSAGE(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
        i: int =0
        message = userSettingValue.split(':')
        while i < SIZEOFWSPRMESSAGES:
            self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation+i, int(message[i],16))
            i += 1

    def WSPR_MESSAGE1(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.WSPR_MESSAGE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def WSPR_MESSAGE2(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.WSPR_MESSAGE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def WSPR_MESSAGE3(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.WSPR_MESSAGE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def WSPR_MESSAGE4(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue,_unused):
        self.WSPR_MESSAGE(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

#
#         # ***********************************
#         #   HARDWARE SETTINGS
#         # ***********************************
#
    def S_METER_LEVELS(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        if(BOOL_SELECT.index(userSettingValue)):
            tmpByte: bytes = EEPROMBuffer[memLocation] | 0x08
        else:
            tmpByte: bytes = EEPROMBuffer[memLocation] & (~0x08)
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

    def S_METER_LEVEL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, round(int(userSettingValue)>>2))

    def S_METER_LEVEL1(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.S_METER_LEVEL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def S_METER_LEVEL2(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.S_METER_LEVEL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def S_METER_LEVEL3(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.S_METER_LEVEL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def S_METER_LEVEL4(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.S_METER_LEVEL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def S_METER_LEVEL5(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.S_METER_LEVEL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def S_METER_LEVEL6(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.S_METER_LEVEL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def S_METER_LEVEL7(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.S_METER_LEVEL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def S_METER_LEVEL8(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.S_METER_LEVEL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)


    def I2C_LCD_MASTER(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue,16))

    def I2C_LCD_SECOND(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue, 16))

    def I2C_ADDR_SI5351(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue,16))


#
#         # ***********************************
#         #   ADVANCED UX SETTINGS
#         # ***********************************
#

#
#         # ***********************************
#         #   EXTENDED KEYS
#         # ***********************************
#
    def EXTENDED_KEY_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, round(int(userSettingValue)>>2))

    def EXTENDED_KEY1_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.EXTENDED_KEY_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def EXTENDED_KEY2_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.EXTENDED_KEY_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def EXTENDED_KEY3_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.EXTENDED_KEY_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def EXTENDED_KEY4_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.EXTENDED_KEY_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def EXTENDED_KEY5_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.EXTENDED_KEY_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def EXTENDED_KEY6_START(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.EXTENDED_KEY_START(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)


    def EXTENDED_KEY_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
 #       print("*****")
 #       print("ext key master called, userSettingValue =", userSettingValue, "memory addres =", memLocation)
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, round(int(userSettingValue)>>2))

    def EXTENDED_KEY1_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.EXTENDED_KEY_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def EXTENDED_KEY2_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.EXTENDED_KEY_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def EXTENDED_KEY3_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.EXTENDED_KEY_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def EXTENDED_KEY4_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.EXTENDED_KEY_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def EXTENDED_KEY5_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.EXTENDED_KEY_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def EXTENDED_KEY6_END(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.EXTENDED_KEY_END(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)


    def EXTENDED_KEY_FUNC(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, FTN_KEY_SELECT.index(userSettingValue))

    def EXTENDED_KEY1_FUNC(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.EXTENDED_KEY_FUNC(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def EXTENDED_KEY2_FUNC(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.EXTENDED_KEY_FUNC(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def EXTENDED_KEY3_FUNC(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.EXTENDED_KEY_FUNC(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def EXTENDED_KEY4_FUNC(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.EXTENDED_KEY_FUNC(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def EXTENDED_KEY5_FUNC(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.EXTENDED_KEY_FUNC(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def EXTENDED_KEY6_FUNC(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.EXTENDED_KEY_FUNC(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)


#
#         # ***********************************
#         #   CUSTOM LPF FILTERS
#         # ***********************************
#
#
    def CUST_LPF_ENABLED(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, LPF_MODE_SETTING[LPF_MODE_SELECT.index(userSettingValue)])

    def CUST_LPF_FILTER_ENDFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

    def CUST_LPF_FILTER1_ENDFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CUST_LPF_FILTER2_ENDFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CUST_LPF_FILTER3_ENDFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CUST_LPF_FILTER4_ENDFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CUST_LPF_FILTER5_ENDFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CUST_LPF_FILTER6_ENDFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CUST_LPF_FILTER7_ENDFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CUST_LPF_FILTER_ENDFREQ(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)


    def CUST_LPF_FILTER_CONTROL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue):

        tmpByte: bytes = 0x00
        if str(userSettingValue) != "NONE":
            for i in LPF_CTRL_SELECT:
                if str(i) in str(userSettingValue):
                    tmpByte = tmpByte | (1<<LPF_CTRL_SELECT.index(i))

        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)


    def CUST_LPF_FILTER1_CONTROL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CUST_LPF_FILTER2_CONTROL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CUST_LPF_FILTER3_CONTROL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CUST_LPF_FILTER4_CONTROL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CUST_LPF_FILTER5_CONTROL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CUST_LPF_FILTER6_CONTROL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)

    def CUST_LPF_FILTER7_CONTROL(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused):
        self.CUST_LPF_FILTER_CONTROL(SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)




    def defaultFunc(self, *args):
        print ("Command not recognised:", args[0])

    def set(self, cmd, *args):
        return getattr(self, cmd, self.defaultFunc)(*args)

