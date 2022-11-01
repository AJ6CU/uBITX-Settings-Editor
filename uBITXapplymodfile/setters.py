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


    def XML_Get_unit8_FromEEPROM(self, xmlSubTree, settingName, memBuffer) -> int:
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
        self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

    def VFO_B(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
        self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

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
        # Starting location is the *address* of "CW_AUTO_DATA" get that first
        cwAutoDataMemLocation = self.XML_MemLocation_FromEEPROM(EEPROMroot, "CW_AUTO_DATA")

        messageHeap: str = ''
        messageStart: int = []
        messageEnd: int =[]
        messageLoc = 0
        messageOffset = 0

        messageTag = userSetting.findall('message')             # get the tags to all the message elements
        for tag in messageTag:
            if(tag.text != None):                               # don't process empty message tags
                messageStart.append(messageLoc)
                messageEnd.append (messageLoc + len(tag.text) -1)
                messageLoc += len(tag.text)                     # this updates pointer for next place a message can go
                messageOffset += 2                              # track the extra offsets because of leading start, ends
                messageHeap += tag.text

        # At this point we have the raw start end of each message, just need to offset them by the bytes
        # Occupied by the start,end pairs. And then we can write the start end to EEPROM
        #
        i: int = 0
        numMessage = len (messageStart)

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


#
#         #***********************************
#         #   CW ADC SETTINGS
#         #***********************************

    def CW_ADC_ST_DOT(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot, _unused1):

        # first get the byte that holds all the upper bits for Straight keys and "DOTs"
        upperBitsByte = self.XML_Get_unit8_FromEEPROM(EEPROMroot, "CW_ADC_MOST_BIT1", EEPROMBuffer)  # get byte with upper two bits
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
       LSB: bytes = int(userSettingValue) & 0xFF
       LSB1: bytes = (int(userSettingValue) >> 8) & 0xFF
       LSB2: bytes = (int(userSettingValue) >> 16) & 0xFF
       MSB: bytes = (int(userSettingValue) >> 24) & 0xFF

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
        self.set_unit16_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

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
        self.set_unit16_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

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
        tmpByte: Bytes = (SDR_OFFSET_MODE.index(userSettingValue)<<2) | EEPROMBuffer[memLocation] & (~0xC)
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, tmpByte)

    def SDR_FREQUENCY(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
        self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))


#         # ***********************************
#         #   WSPR SETTINGS
#         # ***********************************
#
    def WSPR_BAND1_TXFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
        self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

    def WSPR_BAND2_TXFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
        self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

    def WSPR_BAND3_TXFREQ(self, SettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, _unused, _unused1):
        self.set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

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
 #       print("*****")
 #       print("ext key master called, userSettingValue =", userSettingValue, "memory addres =", memLocation)
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
        self.set_unit8_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))

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




    def defaultFunc(self, *args):
        print ("Command not recognised:", args[0])

    def set(self, cmd, *args):
        return getattr(self, cmd, self.defaultFunc)(*args)

