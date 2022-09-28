from lxml import etree as ET

from typing import Any
import serial
import functools
from bitarray import bitarray
from time import sleep
import sys
from globalvars import *

from setters import setters

#definitions################################################
COM_PORT = "COM24"
#COM_PORT = "COM14"
BAUD = 38400



EEPROMMEMORYMAP="eeprommemorymap.xml"               #Maps EEPROM locations to settings

USERMODFILE="usermodfile.xml"                       #Output of process - file that User can customize



#end definitions############################################




def readEEPROMData(portdesc: object, memAddress: int, numBytesToRead: int) -> bytearray:

    LSB = memAddress & 0xff
    MSB = (memAddress >> 8) & 0xff

    NumLSB = numBytesToRead & 0xff
    NumMSB = (numBytesToRead >> 8) & 0xff

    # send command buffer to radio
    # byte1 = LSB of the start location in EEPROM
    # byte2 = MSB of the start location in EEPROM
    # byte3 = LSB of the total bytes to read from EEPROM
    # byte4 - MSB of the total bytes to read from EEPROM
    # byte5 - Command telling the radio what to do

    portdesc.write(bytes([LSB, MSB, NumLSB, NumMSB, READCOMMAND]))

    # create buffer to save bytes being returned
    # byte1 = 0x2 - always
    # lots of bytes = number of bytes requested
    # byte3 = checksum of bytes above
    #byte4 = 0x0 (ACK)

    returnBuffer: bytesarray = []
    checkSum: int = 0x02

    i = -1
    while i < numBytesToRead:
         if portdesc.in_waiting != 0:
            if i< 0:
                throwawy = portdesc.read(1)
            else:
                returnBuffer.extend(portdesc.read(1))
                checkSum = (checkSum+returnBuffer[i] ) & 0xFF
            i += 1

#   get checksum sent by radio CAT control
    while portdesc.in_waiting == 0:
        sleep(0.01)
    sentCheckSum = int.from_bytes(portdesc.read(1),"little",signed=False)

#   get trailing byte. Must be an ACK (0x00)
    while portdesc.in_waiting == 0:
        sleep(0.01)
    trailingByte = int.from_bytes(portdesc.read(1),"little",signed=False)

    if(sentCheckSum!=checkSum)|(trailingByte!=0):
        sys.exit("Bad Checksum on EEPROM Read")

    return returnBuffer

def writeByteToEEPROM(portdesc: object, memAddress: int, outbyte: int):
    print("eeprom mem address =", memAddress)
    LSB: bytes = memAddress & 0xff
    MSB: bytes = (memAddress >> 8) & 0xff
#    print(type(LSB),"\t", type(MSB),"\t", type(outbyte))
#    print(memAddress)
    checkByte: int = ((LSB + MSB + outbyte) % 256) & 0xff
    bytesToWrite = bytes([LSB, MSB, outbyte, checkByte, WRITECOMMAND])
    portdesc.write(bytesToWrite)

def get_Byte_FromEEPROM(memBuffer:bytearray, memAddress: int) -> int:
    return(memBuffer[memAddress])



def get_uint16_FromEEPROM(memBuffer:bytearray, memAddress: int) -> int:
    return memBuffer[memAddress] + (memBuffer[memAddress+1]<<8)

def get_uint32_FromEEPROM(memBuffer:bytearray, memAddress: int) -> int:
    return memBuffer[memAddress] + (memBuffer[memAddress+1]<<8) +(memBuffer[memAddress+2]<<16) +(memBuffer[memAddress+3]<<24)



def updateEEPROM(portdesc: object, inMemBuffer: bytearray, itsDirty: bitarray) -> int:
    print("following EEPROM locations were updated")
    i: int = 0
    while i < EEPROMSIZE:
        if itsDirty[i]:  # Got a dirty byte
#            print(f"{i:04}", "\t", inMemBuffer[i],"\t",type(inMemBuffer[i]))
            writeByteToEEPROM(portdesc, i, inMemBuffer[i])

            doneWithByte: bool = False
            retryCnt: int = 0
            while True:  # keep tring to write until successful or exceed # retries

                while portdesc.in_waiting == 0:
                    sleep(0.005)
                resultCode = int.from_bytes(portdesc.read(1), "little", signed=False)
                while portdesc.in_waiting == 0:
                    sleep(0.005)
                trailingByte = int.from_bytes(RS232.read(1), "little", signed=False)
                if (resultCode == OK) & (trailingByte == ACK):
                    break
                else:
                    print("retrying byte =", i)
                    print("resultcode=", resultCode)
                    print("trailingByte=", trailingByte)
                    retryCnt += 1
                    if retryCnt > RETRIES:
                        print("number of retries exceeded on memory location: ", i)
                        return (1)  # Failure
        i += 1
    return (0)                      # Success

#####################################
#Start Main Progrm
#####################################
print("Opening connection to radio")
RS232 = serial.Serial(COM_PORT, BAUD, timeout=0, stopbits=1, parity=serial.PARITY_NONE, xonxoff=0, rtscts=0)
sleep(3)  #this is required to allow Nano to reset after open

print("Reading EEPROM into memory")
EEPROMBuffer=readEEPROMData(RS232, 0, EEPROMSIZE)       #Read the EEPROM into memory


EEPROMBufferDirty=bitarray(EEPROMSIZE)          # create a bit array of the same size that we can use to track dirty "bytes"
EEPROMBufferDirty.setall(0)                     # clear all bits. When we write a byte into the EEPROMBuffer, we will set
                                                # corresponding dirty bit to 1


print("Opening EEPROM Memory Map of parameter locations")
EEPROMtree = ET.parse(EEPROMMEMORYMAP)
EEPROMroot = EEPROMtree.getroot()

print("Opening Usermod file")
UserModtree = ET.parse(USERMODFILE)
UserModroot = UserModtree.getroot()

print("Processing Usermod file and updating in memory copy of EEPROM...")



EEPROM_Memory = setters()

# first step is to take the "easy" ones from the EEPROM buffer and write to the corresponding <value></value>
# in the usermod template file
#
for userSetting in UserModroot.findall('.//SETTING'):


    #get setting name and value
    userSettingName = userSetting.get("NAME")
    userSettingValue = userSetting.find("value").text

    #now look in eeprom map for buffer memory location, size (in bytes) and data type

    eepromSetting = EEPROMroot.find('.//SETTING[@NAME="{}"]'.format(userSettingName))

    memLocation = int(eepromSetting.find("EEPROMStart").text)
    numBytes = eepromSetting.find("sizeInBytes").text
    dataType = eepromSetting.find("displayFormat").text
    if (userSettingValue != None):
        EEPROM_Memory.set(userSettingName, userSettingName, EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue, EEPROMroot)
    else:
        print("skipping because value = NONE, Setting Name", userSettingName)

#    print("processing=",settingName, "\tmemLocation=", memLocation, "\tMemcontents=", str(EEPROMBuffer[memLocation]), "\tnumber of bytes=", numBytes,"\tdatatype=",dataType)


#     #    if (setting.find("SPECIAL_PROCESSING").text=="no"):
#     if (eepromSetting.find("SPECIAL_PROCESSING").text=="no"):
#         print("simple is:", userSettingName)
#         match numBytes:
#             case '1':
#                 match dataType:
#                     case "selection_mode":
# #                        print("MODE SELECT: User Setting Name: ", userSettingName, " location= ", memLocation, "\tvalue =", userSettingValue)
#                         set_Byte_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, MODE_SELECT.index(userSettingValue) )
#                     case "selection_cw_key":
# #                        print("CW KEY SElECT: User Setting Name: ", userSettingName," location= ", memLocation, "\tvalue =", userSettingValue)
#                         set_Byte_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, CW_KEY_SELECT.index(userSettingValue) )
#                     case "selection_main_format":
# #                        print("MAIN MENU SELECT:  User Setting Name: ", userSettingName, " location= ", memLocation, "\tvalue =", userSettingValue)
#                         set_Byte_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, MAIN_MENU_SELECT.index(userSettingValue))
#
#                     case "selection_ftn_key":
# #                        print("FTN_KEY_SELECT:  User Setting Name: ", userSettingName, " location= ", memLocation, "\tvalue =", userSettingValue)
#                         set_Byte_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, FTN_KEY_SELECT.index(userSettingValue))
#
#                     case "bool":
# #                        print("BOOL_SELECT:  User Setting Name: ", userSettingName, " location= ", memLocation, "\tvalue =", userSettingValue)
#                         set_Byte_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, BOOL_SELECT.index(userSettingValue))
#
#                     case "hex":
# #                        print("hex called:  User Setting Name: ", userSettingName," location= ", memLocation, "\tvalue =", userSettingValue)
#                         set_Byte_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue,base=16))
#                     case _:
# #                        print("default called:  User Setting Name: ", userSettingName," location= ", memLocation, "\tvalue =", userSettingValue)
#                         set_Byte_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))
#
#             case '2':
#                 print("2 Byte Storage: User Setting Name: ", userSettingName, " location= ", memLocation, "\tvalue =",
#                       userSettingValue)
#
#                 set_unit16_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)
#             case '4':
#                 print("4 Byte Storage: User Setting Name: ", userSettingName, " location= ", memLocation, "\tvalue =",
#                       userSettingValue)
#                 set_unit32_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, userSettingValue)
#             case _:
#                 i: int =0
#                 print("default case: -", userSettingName)
#                 # tmpStr: str = ''
#                 # while i<int(numBytes):
#                 #     match dataType:
#                 #         case "int":
#                 #             tmpStr += str(get_Byte_FromEEPROM(EEPROMBuffer, memLocation+i))
#                 #         case "str":
#                 #             tmpStr += str(chr((get_Byte_FromEEPROM(EEPROMBuffer, memLocation+i))))
#                 #         case "hex":
#                 #             tmpStr += str(hex(get_Byte_FromEEPROM(EEPROMBuffer, memLocation+i)))
#                 #         case _:
#                 #             tmpStr += str(get_Byte_FromEEPROM(EEPROMBuffer, memLocation+i))
#                 #     i += 1
#                 # if tmpStr.isprintable():
#                 #     value.text = tmpStr
#     else:                   # the many special cases that require individual specialized processing are handled below


#         #***********************************
#         #   COMMON MEMORY KEYER
#         #***********************************
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
#         #***********************************
#         #   CW ADC SETTINGS
#         #***********************************
#         case "CW_ADC_ST_FROM"|"CW_ADC_ST_TO"|"CW_ADC_DOT_FROM"|"CW_ADC_DOT_TO":
#             print("need work:", userSettingName)
#             #     upperBitsByte = XML_Get_Byte_FromEEPROM(EEPROMroot, "CW_ADC_MOST_BIT1", EEPROMBuffer)  #get byte with upper two bits
#             #
#             #     memContents: int = get_Byte_FromEEPROM(EEPROMBuffer, memLocation)               #now get the lower 8 bits
#             #     match settingName:
#             #         case "CW_ADC_ST_FROM":
#             #             value.text = str(memContents | ((upperBitsByte &0x03)  << 8))           #4 sets of 2 bits, find them, put them to the left
#             #         case "CW_ADC_ST_TO":
#             #             value.text = str(memContents | ((upperBitsByte & 0x0C) << 6))
#             #         case "CW_ADC_DOT_FROM":
#             #             value.text = str(memContents | ((upperBitsByte & 0x30) << 4))
#             #         case "CW_ADC_DOT_TO":
#             #             value.text = str(memContents | ((upperBitsByte & 0xC0) << 2))
#             #
#         case "CW_ADC_DASH_FROM" | "CW_ADC_DASH_TO" | "CW_ADC_BOTH_FROM" | "CW_ADC_BOTH_TO":
#             print("need work:", userSettingName)
#             #     upperBitsByte = XML_Get_Byte_FromEEPROM(EEPROMroot, "CW_ADC_MOST_BIT2", EEPROMBuffer)       #get byte with upper 2 bits
#             #
#             #     memContents: int = get_Byte_FromEEPROM(EEPROMBuffer, memLocation)  # now get the lower 8 bits
#             #     match settingName:
#             #         case "CW_ADC_DASH_FROM":
#             #             value.text = str(memContents | ((upperBitsByte & 0x03) << 8))           # 4 sets of 2 bits, find them, put them to the left
#             #         case "CW_ADC_DASH_TO":
#             #             value.text = str(memContents | ((upperBitsByte & 0x0C) << 6))
#             #         case "CW_ADC_BOTH_FROM":
#             #             value.text = str(memContents | ((upperBitsByte & 0x30) << 4))
#             #         case "CW_ADC_BOTH_TO":
#             #             value.text = str(memContents | ((upperBitsByte & 0xC0) << 2))
#             #
#

#         #***********************************
#         #   HAM BANDS
#         #***********************************
#             #
#         case "TUNING_RESTICTIONS":
#             print("need work:", userSettingName)
#             #     if (get_Byte_FromEEPROM(EEPROMBuffer, memLocation) & 0x02):
#             #         value.text = "BAND"  # Restriction are placed on Tuning (although not clear enforced)
#             #     else:
#             #         value.text = "NONE"  # No restrictions on how and where you can tune
#         case "TX_RESTRICTIONS":
#             print("need work:", userSettingName)
#             #     if (get_Byte_FromEEPROM(EEPROMBuffer, memLocation) >=100):
#             #         value.text = "HAM"              #Restriction of TX to only HAM bands
#             #     else:
#             #         value.text = "NONE"              #Restrictions on TX
#             #
#


#         # ***********************************
#         #   WSPR SETTINGS
#         # ***********************************
#
#         case ("WSPR_MESSAGE1_NAME" | "WSPR_MESSAGE2_NAME" | "WSPR_MESSAGE3_NAME" | "WSPR_MESSAGE4_NAME" ):
#             print("need work:", userSettingName)
#
#         case ("WSPR_MESSAGE1" | "WSPR_MESSAGE2" |"WSPR_MESSAGE3" | "WSPR_MESSAGE4"):
#             print("need work:", userSettingName)
#             #     j: int = 0
#             #     msgStr: str = ''
#             #
#             #     while j < SIZEOFWSPRMESSAGES:
#             #         msgStr+='{:02X}'.format(get_Byte_FromEEPROM(EEPROMBuffer, memLocation + j))+':'
#             #         j += 1
#             #     value.text = msgStr.rstrip(':')                 #strip off extra : on right
#             #
#
#         # ***********************************
#         #   HARDWARE SETTINGS
#         # ***********************************
#         case "S_METER_LEVELS":
#             print("need work:", userSettingName)
#         #     if ((get_Byte_FromEEPROM(EEPROMBuffer, memLocation)) & 0x08):  # a 0x08 bit pattern indicates s-meter on
#         #         value.text = BOOL_SELECT[1]
#         #     else:
#         #         value.text = BOOL_SELECT[0]
#         #
#         case ("S_METER_LEVEL1" | "S_METER_LEVEL2" | "S_METER_LEVEL3" | "S_METER_LEVEL4" | "S_METER_LEVEL5"|
#             "S_METER_LEVEL6" | "S_METER_LEVEL7" | "S_METER_LEVEL8"):
#             print("need work:", userSettingName)
#         #     value.text = str(4 * get_Byte_FromEEPROM(EEPROMBuffer, memLocation))
#
#         case ("I2C_LCD_MASTER" | "I2C_LCD_SECOND"):
#             set_Byte_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue,16))
#
#         case "I2C_ADDR_SI5351":
#             set_Byte_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue,16))
#
#         # ***********************************
#         #   ADVANCED UX SETTINGS
#         # ***********************************
#
#         case "MESSAGE_LINE":
#             print("need work:", userSettingName)
# #         value.text = BOOL_SELECT[(get_Byte_FromEEPROM(EEPROMBuffer, memLocation) >>4)&0x01]
# #
#         case "SCROLLING_DISPLAY":
#             print("need work:", userSettingName)
# #         value.text = BOOL_SELECT[(get_Byte_FromEEPROM(EEPROMBuffer, memLocation) >> 2) & 0x01]
# #
#         case "One_Two_Line_Toggle":
#             print("need work:", userSettingName)
#         #         value.text = BOOL_SELECT[get_Byte_FromEEPROM(EEPROMBuffer, memLocation)  & 0x01]
#
#         case "MAIN_SCREEN_FORMAT":
#             set_Byte_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, MAIN_MENU_SELECT.index(userSettingValue) )
#
#         case "NEXTION_DISPLAY_CALL_SIGN":
#             print("need work:", userSettingName)
#         #         value.text = BOOL_SELECT[(get_Byte_FromEEPROM(EEPROMBuffer, memLocation) >> 1) & 0x01]
# #
#
#         case "Stored_IF_Shift":
#             print("need work:", userSettingName)
#
# #         value.text = BOOL_SELECT[(get_Byte_FromEEPROM(EEPROMBuffer, memLocation) >> 6) & 0x01]
#         case "IF_SHIFTVALUE":
#             print("need work:", userSettingName)
# #tmpInt = get_uint16_FromEEPROM(EEPROMBuffer, memLocation)
# #         if tmpInt & 0x8000:                                         #We have a negative number
# #             value.text = "-" + str((~tmpInt+1)& 0xffff)             #convert from 2's complement
# #         else:
# #             value.text = str(tmpInt)
#         case "CW_DISPLAY_FREQ":
#             print("need work:", userSettingName)
#
# #         shiftDisplay = (get_Byte_FromEEPROM(EEPROMBuffer, memLocation) >>7) & 0x01
# #         enableAdjustCWFreq = (get_Byte_FromEEPROM(EEPROMBuffer, memLocation+1) >>7) & 0x01
# #
# #         if shiftDisplay & ~enableAdjustCWFreq:      #By definition means display shows RX freq
# #             value.text = "RX"
# #         else:
# #             value.text = "TX"                       #Shows TX Freq seems to be the preferred option
#         case "CW_Frequency_Adjustment":
#             print("need work:", userSettingName)
# #         value.text = str((get_Byte_FromEEPROM(EEPROMBuffer, memLocation) &  0x3f)*10)
#
#         # ***********************************
#         #   EXTENDED KEYS
#         # ***********************************
#
#         #
#         case ("EXTENDED_KEY1_START" |"EXTENDED_KEY2_START"|"EXTENDED_KEY3_START"|                #saved as ADC/4.
#               "EXTENDED_KEY4_START" | "EXTENDED_KEY5_START"|"EXTENDED_KEY6_START"):              #x4 to make it user easier
#             print("need work:", userSettingName)
#         #     value.text = str(get_Byte_FromEEPROM(EEPROMBuffer, memLocation)*4)
#         case ("EXTENDED_KEY1_END" | "EXTENDED_KEY2_END" | "EXTENDED_KEY3_END" | "EXTENDED_KEY4_END" |
#               "EXTENDED_KEY5_END"  | "EXTENDED_KEY6_END"):
#             print("need work:", userSettingName)
#     #     value.text = str(get_Byte_FromEEPROM(EEPROMBuffer, memLocation)*4)
#
#         case ("EXTENDED_KEY1_FUNC" | "EXTENDED_KEY2_FUNC" | "EXTENDED_KEY3_FUNC" | "EXTENDED_KEY4_FUNC" |
#                "EXTENDED_KEY5_FUNC" | "EXTENDED_KEY6_FUNC" ):
#             set_Byte_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, FTN_KEY_SELECT.index(userSettingValue))
#
#         # ***********************************
#         #   CUSTOM LPF FILTERS
#         # ***********************************
#
#         case "CUST_LPF_ENABLED":
#             print("need work:", userSettingName)
#         #      if ((((get_Byte_FromEEPROM(EEPROMBuffer, memLocation)) & 0x5F)==0x57)|
#         #          (((get_Byte_FromEEPROM(EEPROMBuffer, memLocation)) & 0x5F) == 0x58)):  # a 0x57 or 0x58 bit pattern enables custom lpf
#         #             value.text = BOOL_SELECT[1]
#         #      else:
#         #             value.text = BOOL_SELECT[0]
#         #
#         case "CUST_LPF_USE_D10-D13":
#             print("need work:", userSettingName)
#         #      if (((get_Byte_FromEEPROM(EEPROMBuffer, memLocation)) & 0x5F) == 0x58):  # a 0x58 bit pattern enables use of D10-D13 too
#         #          value.text = BOOL_SELECT[1]
#         #      else:
#         #          value.text = BOOL_SELECT[0]
#         #
#         case ("CUST_LPF_FILTER1_ENDFREQ" | "CUST_LPF_FILTER2_ENDFREQ" | "CUST_LPF_FILTER3_ENDFREQ" |
#                "CUST_LPF_FILTER4_ENDFREQ" | "CUST_LPF_FILTER5_ENDFREQ" | "CUST_LPF_FILTER6_ENDFREQ" |
#                "CUST_LPF_FILTER7_ENDFREQ"):
#             set_Byte_InEEPROMBuffer(EEPROMBuffer, EEPROMBufferDirty, memLocation, int(userSettingValue))
#
#         case ("CUST_LPF_FILTER1_CONTROL" | "CUST_LPF_FILTER2_CONTROL" | "CUST_LPF_FILTER3_CONTROL" |
#              "CUST_LPF_FILTER4_CONTROL" | "CUST_LPF_FILTER5_CONTROL" | "CUST_LPF_FILTER6_CONTROL" |
#              "CUST_LPF_FILTER7_CONTROL"):
#             print("need work:", userSettingName)
#   #              j = 0
#             #     tmpStr = ""
#             #     LPFControlByte = get_Byte_FromEEPROM(EEPROMBuffer, memLocation)
#             #     while j < 7:
#             #         if ((LPFControlByte>>j)&0x01):
#             #             tmpStr += (LPF_CTRL_SELECT[j] + ",")
#             #         j += 1
#             #     value.text = tmpStr.rstrip(',')
#
        # case _:
        #    print("Special processing still required for:", userSettingName)


print("In memory EEPROM copy updated. Now updating actual EEPROM")

# write out eeprom and specific locations updated based on dirty bits


if(updateEEPROM( RS232, EEPROMBuffer, EEPROMBufferDirty  )==0):
    print("All done!")
else:
    print("Error, see message above")





