from lxml import etree as ET

from typing import Any
import serial
import functools
from time import sleep
import sys

#definitions################################################
COM_PORT = "COM24"
BAUD = 38400

READCOMMAND=0xDB

EEPROMSIZE=1024
BACKUPFILESIZE=2048

EEPROMMEMORYMAP="eeprommemorymap.xml"               #Maps EEPROM locations to settings
USERMODFILETEMPLACE="usermodfiletemplate.xml"       #Template file used to fill in with data from EEPROM

USERMODFILE="usermodfile.xml"                       #Output of process - file that User can customize


#end definitions############################################

#ENUMS#####################################################
MODE_SELECT = ["DEFAULT","xxx","LSB","USB","CWL","CWU"]
BOOL_SELECT = ["NO","YES"]
CW_KEY_SELECT = ["STRAIGHT","IAMBICA","IAMBICB"]
FTN_KEY_SELECT = ["NONE", "MODE", "BAND-UP", "BAND-DN", "TUNE-STEP", "VFO-A/B", "SPLIT", "TX", "SDR-MODE", "RIT"]
LPF_CTRL_SELECT = ["TX_LPF_A", "TX_LPF_B", "TX_LPF_C", "D10", "D11", "D12", "D13"]
#end ENUMS#################################################


def readEEPROMData(portdesc: object, memlocation: int, numBytesToRead: int) -> bytearray:

    LSB = memlocation & 0xff
    MSB = (memlocation >> 8) & 0xff

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

def get_Byte_FromEEPROM(memBuffer:bytearray, memlocation: int) -> int:
    #return int.from_bytes(memBuffer[memlocation],"little",signed=False)
    return(memBuffer[memlocation])

def get_uint16_FromEEPROM(memBuffer:bytearray, memlocation: int) -> int:
    return memBuffer[memlocation] + (memBuffer[memlocation+1]<<8)

def get_uint32_FromEEPROM(memBuffer:bytearray, memlocation: int) -> int:
    return memBuffer[memlocation] + (memBuffer[memlocation+1]<<8) +(memBuffer[memlocation+2]<<16) +(memBuffer[memlocation+3]<<24)


#####################################
#Start Main Progrm
#####################################
print("Opening connection to radio")
RS232 = serial.Serial(COM_PORT, BAUD, timeout=0, stopbits=1, parity=serial.PARITY_NONE, xonxoff=0, rtscts=0)
sleep(3)  #this is required to allow Nano to reset after open

print("reading EEPROM")
EEPROMBuffer=readEEPROMData(RS232, 0, EEPROMSIZE)       #Read the EEPROM into memory

print("opening template files")
EEPROMtree = ET.parse(EEPROMMEMORYMAP)
EEPROMroot = EEPROMtree.getroot()


UserModtree = ET.parse(USERMODFILETEMPLACE)
UserModroot = UserModtree.getroot()


print("Creating User Mod File from EEPROM data...")

# first step is to take the "easy" ones from the EEPROM buffer and write to the corresponding <value></value>
# in the usermod template file
#
for setting in EEPROMroot.findall('.//SETTING'):


    #get name, location in eeprom buffer, number of bytes, and type of data
    settingName = setting.get("NAME")
    memLocation = int(setting.find("EEPROMStart").text)
    numBytes = setting.find("sizeInBytes").text
    dataType = setting.find("displayFormat").text

#    print("processing=",settingName, "\tmemLocation=", memLocation, "\tMemcontents=", str(EEPROMBuffer[memLocation]), "\tnumber of bytes=", numBytes,"\tdatatype=",dataType)

    if(setting.find("SPECIAL_PROCESSING").text!="skip"):          #skip means no entry on modtemplate, so skip it!
        #find the pointer within the usermod file to stuff the value
        # this use of the "format" modifier is required because if we replaced the "{}" with settingName
        # it would not recognize it as a variable. So we use the format modifier to evaluate the variable
        # and replace it where the "{}" is. Note also that it is important that the {} are enclosed in
        # quote marks since the format is @attrib="foo". So the {} are replaced with the value of
        # setting name and the quote marks remain. I could have swapped the single and double quotes and
        # all would have worked.
        valueElement = UserModroot.find('.//SETTING[@NAME="{}"]'.format(settingName))
#        print("valueElement=",valueElement)
#        print(valueElement.get("NAME"))
        value=valueElement.find("value")

        #    if (setting.find("SPECIAL_PROCESSING").text=="no"):
        if (setting.find("SPECIAL_PROCESSING").text=="no"):
            match numBytes:
                case '1':
                    memContents: int = get_Byte_FromEEPROM(EEPROMBuffer, memLocation)
                    match dataType:
                        case "selection_mode":
                            value.text = MODE_SELECT[memContents]
                        case "selection_cw_key":
                            value.text = CW_KEY_SELECT[memContents]
                        case "selection_ftn_key":
                            value.text = FTN_KEY_SELECT[memContents]
                        case "bool":
                            value.text = BOOL_SELECT[memContents]
                        case "hex":
                            value.text = hex(memContents)
                        case _:
                            value.text = str(memContents)
                case '2':
                    value.text = str(get_uint16_FromEEPROM(EEPROMBuffer, memLocation))
                case '4':
                    value.text = str(get_uint32_FromEEPROM(EEPROMBuffer, memLocation))
                case _:
                    i: int =0
                    tmpStr: str = ''
                    while i<int(numBytes):
                        match dataType:
                            case "int":
                                tmpStr += str(get_Byte_FromEEPROM(EEPROMBuffer, memLocation+i))
                            case "str":
                                tmpStr += str(chr((get_Byte_FromEEPROM(EEPROMBuffer, memLocation+i))))
                            case "hex":
                                tmpStr += str(hex(get_Byte_FromEEPROM(EEPROMBuffer, memLocation+i)))
                            case _:
                                tmpStr += str(get_Byte_FromEEPROM(EEPROMBuffer, memLocation+i))
                        i += 1
                    if tmpStr.isprintable():
                        value.text = tmpStr
        else:                   # the many special cases that require individual specialized processing
            match settingName:
                case "CW_SPEED_WPM":
                    value.text = str(round(1200/get_Byte_FromEEPROM(EEPROMBuffer, memLocation)))
                case "CW_DELAY_MS":
                    value.text = str(10* get_Byte_FromEEPROM(EEPROMBuffer, memLocation))
                case "CW_START_MS":
                    value.text = str(2 * get_Byte_FromEEPROM(EEPROMBuffer, memLocation))
                case "CW_ADC_ST_FROM"|"CW_ADC_ST_TO"|"CW_ADC_DOT_FROM"|"CW_ADC_DOT_TO":
                    upperBits=EEPROMroot.find('.//SETTING[@NAME="CW_ADC_MOST_BIT1"]')               #must go back to eeprom memory tree
                    upperBitsMemLocation = int(upperBits.find("EEPROMStart").text)                  #to find byte holding top 2 bits of each ADC byte
                    upperBitsByte = get_Byte_FromEEPROM(EEPROMBuffer, upperBitsMemLocation)

                    memContents: int = get_Byte_FromEEPROM(EEPROMBuffer, memLocation)               #now get the lower 8 bits
                    match settingName:
                        case "CW_ADC_ST_FROM":
                            value.text = str(memContents | ((upperBitsByte &0x03)  << 8))           #4 sets of 2 bits, find them, put them to the left
                        case "CW_ADC_ST_TO":
                            value.text = str(memContents | ((upperBitsByte & 0x0C) << 6))
                        case "CW_ADC_DOT_FROM":
                            value.text = str(memContents | ((upperBitsByte & 0x30) << 4))
                        case "CW_ADC_DOT_TO":
                            value.text = str(memContents | ((upperBitsByte & 0xC0) << 2))
                case "CW_ADC_DASH_FROM" | "CW_ADC_DASH_TO" | "CW_ADC_BOTH_FROM" | "CW_ADC_BOTH_TO":
                    upperBits = EEPROMroot.find('.//SETTING[@NAME="CW_ADC_MOST_BIT2"]')             # must go back to eeprom memory tree
                    upperBitsMemLocation = int(upperBits.find("EEPROMStart").text)                  # to find byte holding top 2 bits of each ADC byte
                    upperBitsByte = get_Byte_FromEEPROM(EEPROMBuffer, upperBitsMemLocation)

                    memContents: int = get_Byte_FromEEPROM(EEPROMBuffer, memLocation)  # now get the lower 8 bits
                    match settingName:
                        case "CW_ADC_DASH_FROM":
                            value.text = str(memContents | ((upperBitsByte & 0x03) << 8))           # 4 sets of 2 bits, find them, put them to the left
                        case "CW_ADC_DASH_TO":
                            value.text = str(memContents | ((upperBitsByte & 0x0C) << 6))
                        case "CW_ADC_BOTH_FROM":
                            value.text = str(memContents | ((upperBitsByte & 0x30) << 4))
                        case "CW_ADC_BOTH_TO":
                            value.text = str(memContents | ((upperBitsByte & 0xC0) << 2))
                case ("CHANNEL_FREQ1" | "CHANNEL_FREQ2" | "CHANNEL_FREQ3" | "CHANNEL_FREQ4" | "CHANNEL_FREQ5"|
                    "CHANNEL_FREQ6" | "CHANNEL_FREQ7" | "CHANNEL_FREQ8" | "CHANNEL_FREQ9" | "CHANNEL_FREQ10" |
                    "CHANNEL_FREQ11" |"CHANNEL_FREQ12" | "CHANNEL_FREQ13" | "CHANNEL_FREQ14" | "CHANNEL_FREQ15" |
                    "CHANNEL_FREQ16" |"CHANNEL_FREQ17" | "CHANNEL_FREQ18" | "CHANNEL_FREQ19" | "CHANNEL_FREQ20"):
                    value.text = str((get_uint32_FromEEPROM(EEPROMBuffer, memLocation)&0x1FFFFFFF))     #upper 3 bits are the mode must mask off
                case ("CHANNEL_FREQ1_MODE" | "CHANNEL_FREQ2_MODE" | "CHANNEL_FREQ3_MODE" | "CHANNEL_FREQ4_MODE" |
                      "CHANNEL_FREQ5_MODE" | "CHANNEL_FREQ6_MODE" | "CHANNEL_FREQ7_MODE" | "CHANNEL_FREQ8_MODE" |
                      "CHANNEL_FREQ9_MODE" | "CHANNEL_FREQ10_MODE" | "CHANNEL_FREQ11_MODE" | "CHANNEL_FREQ12_MODE" |
                      "CHANNEL_FREQ13_MODE" | "CHANNEL_FREQ14_MODE" | "CHANNEL_FREQ15_MODE" | "CHANNEL_FREQ16_MODE" |
                      "CHANNEL_FREQ17_MODE" | "CHANNEL_FREQ18_MODE" | "CHANNEL_FREQ19_MODE" | "CHANNEL_FREQ20_MODE"):
                    value.text = str(MODE_SELECT[((get_Byte_FromEEPROM(EEPROMBuffer, memLocation)) >>5)])
                case("CHANNEL_FREQ1_SHOW_NAME" | "CHANNEL_FREQ2_SHOW_NAME" | "CHANNEL_FREQ3_SHOW_NAME" |
                     "CHANNEL_FREQ4_SHOW_NAME" | "CHANNEL_FREQ5_SHOW_NAME" | "CHANNEL_FREQ6_SHOW_NAME" |
                     "CHANNEL_FREQ7_SHOW_NAME" | "CHANNEL_FREQ8_SHOW_NAME" | "CHANNEL_FREQ9_SHOW_NAME" |
                     "CHANNEL_FREQ10_SHOW_NAME" ):
                    if((get_Byte_FromEEPROM(EEPROMBuffer, memLocation))== 0x03):        #0x03 is a flag for "yes"
                        value.text = BOOL_SELECT[1]
                    else:
                        value.text = BOOL_SELECT[0]
                case ("EXTENDED_KEY1_START"|"EXTENDED_KEY1_END"|"EXTENDED_KEY2_START"|"EXTENDED_KEY2_END"|    #saved as ADC/4.
                      "EXTENDED_KEY3_START" | "EXTENDED_KEY3_END" |"EXTENDED_KEY4_START"|"EXTENDED_KEY4_END"| #x4 to make it user easier
                      "EXTENDED_KEY5_START" | "EXTENDED_KEY5_END" |"EXTENDED_KEY6_START"|"EXTENDED_KEY6_END"):
                    value.text = str(get_Byte_FromEEPROM(EEPROMBuffer, memLocation)*4)
                case "CUST_LPF_ENABLED":
                     if ((((get_Byte_FromEEPROM(EEPROMBuffer, memLocation)) & 0x5F)==0x57)|
                         (((get_Byte_FromEEPROM(EEPROMBuffer, memLocation)) & 0x5F) == 0x58)):  # a 0x57 or 0x58 bit pattern enables custom lpf
                            value.text = BOOL_SELECT[1]
                     else:
                            value.text = BOOL_SELECT[0]
                case "CUST_LPF_USE_D10-D13":
                     if (((get_Byte_FromEEPROM(EEPROMBuffer, memLocation)) & 0x5F) == 0x58):  # a 0x58 bit pattern enables use of D10-D13 too
                         value.text = BOOL_SELECT[1]
                     else:
                         value.text = BOOL_SELECT[0]
                case ("CUST_LPF_FILTER1_CONTROL" | "CUST_LPF_FILTER2_CONTROL" | "CUST_LPF_FILTER3_CONTROL" |
                     "CUST_LPF_FILTER4_CONTROL" | "CUST_LPF_FILTER5_CONTROL" | "CUST_LPF_FILTER6_CONTROL" |
                     "CUST_LPF_FILTER7_CONTROL"):
                    j = 0
                    tmpStr = ""
                    LPFControlByte = get_Byte_FromEEPROM(EEPROMBuffer, memLocation)
                    while j < 7:
                        if ((LPFControlByte>>j)&0x01):
                            tmpStr += (LPF_CTRL_SELECT[j] + ",")
                        j += 1
                    value.text = tmpStr.rstrip(',')

                case _:
                    print("Special processing still required for:", settingName)



UserModtree.write(USERMODFILE,method="html")
print("All done!")

