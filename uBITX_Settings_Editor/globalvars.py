import os
import sys
import time
import tkinter as tk

VERSION="Release Candidate 1"

# default window size
DEFAULT_ROOT_WINDOW_WIDTH = 1280
DEFAULT_ROOT_WINDOW_HEIGHT = 900

#ENUMS#####################################################
INTERNAL_FIRMWARE_VERSION = ["NA", "V1.061", "V1.07", "V1.08", "V1.09", "V2.0"]
MODE_SELECT = ["DEFAULT","xxx","LSB","USB","CWL","CWU"]
BOOL_SELECT = ["NO","YES"]
TUNE_RESTRICT_SELECT = ["200Khz","BAND"]
TX_RESTRICT_SELECT = ["NONE", "HAM"]
TX_RESTRICT_MINIMUM = 100
CW_KEY_SELECT = ["STRAIGHT","IAMBICA","IAMBICB"]
MAIN_MENU_SELECT = ["DEFAULT","CW"]
BOOT_MODE = ["NORMAL", "SDR"]
SDR_OFFSET_MODE = ["NONE","FIXED", "MHZ", "KHZ"]
SHOW_CHANNEL_NAME = 0x03
HIDE_CHANNEL_NAME = 0x00
FTN_KEY_SELECT = ["NONE", "MODE", "BAND-UP", "BAND-DN", "TUNE-STEP", "VFO-A/B", "SPLIT", "TX", "SDR-MODE", "RIT"]
LPF_MODE_SELECT = ["OFF", "STANDARD", "EXTENDED"]
LPF_MODE_SETTING = [0x00, 0x57, 0x58]
LPF_CTRL_SELECT = ["TX_LPF_A", "TX_LPF_B", "TX_LPF_C", "D10", "D11", "D12", "D13","NONE"]
CW_MSG_TOTAL = 25
CW_MSG_LABEL = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H",
                "I", "J", "K", "L", "M", "N", "O"]

# For extended EEPROM

EXT_UBITX_BOARD_VERSION_SELECT =    ["Data Not Available","V1","V2","V3","V4","V5","V6"]
EXT_PROCESSOR_TYPE_SELECT =         ["Data Not Available","Arduino Nano V3","Arduino Nano Every","Arduino Nano 33 IoT","Arduino Nano BLE",
                                        "Arduino RP2040", "Teensy 4.0", "Raspberry Pi Pico"]
EXT_DISPLAY_TYPE_SELECT =           ["Data Not Available","LCD 16x2 (Parallel)","LCD 16x2 (I2C)","LCD 20x4 (Parallel)", "Dual LCD 16x2 (I2C)",
                                        "LCD 20x4 (I2C)", "Nextion"]
EXT_FUNCTIONALITY_SET_SELECT =      ["Data Not Available","All Functions","Test Functionality","Suggested for LCD", "For Expanded Nano V3.0/Nextion",
                                    "None - Old Nanos/Nextion", "Suggested for Processors/Newton"]

EXT_SMETER_SELECTION_SELECT =       ["Data Not Available","I2C S-Meter/2nd Nano","On board Sensor","None"]

EXT_SERIAL_TYPE_SELECT =            ["Data Not Available", "Tiny SoftwareSerial", "Hardware", "Std SoftwareSerial"]

EXT_EEPROM_TYPE_SELECT =            ["Data Not Available", "On Processor", "External I2C"]

EXT_ENCODER_TYPE_SELECT =            ["Data Not Available", "Analog", "Digital"]

MONTH3CHARS = ["Data Not Available", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ]


#
#            Band       Dial Freq   Low         Mid         High
#
WSPRBANDS ={ '600m':     (474200,    475600,    475700,     475800 ),
            '160m':     (1836600,   1838000,   1838100,    1838200),
            '80m':      (3592600,   3594000,    3594100,    3594200),
            '60m':      (5287200,   5288600,    5288700,    5288800),
            '40m':      (7038600,   7040000,    7040100,    7040200),
            '30m':      (10138700,  10140100,   10140200,   10140300),
            '20m':      (1495600,   14097000,   14097100,   14097200),
            '17m':      (18104600,  18106000,   18106100,   18106200),
            '15m':      (21094600,  21096000,   21096100,   21096200),
            '12m':      (24924600,  24926000,   24926100,   24926200),
            '10m':      (28124600,  28126000,   28126100,   28126200),
            '6m':       (50293000,  50294400,   50294500,   50294600),
            '4m':       (70091000,  70092400,   70092500,   70092600),
            '2m':       (144489000, 144490400,  144490500,  144490600)
        }
DEFAULTWSPRBAND = '20m'
DEFAULTWSPRTONE = 100

#   Default "reasonable" ADC Values
#
CW_KEY_PRESSED_START = '0'
CW_KEY_PRESSED_END = '50'

CW_DOT_KEY_PRESSSED_START = '301'
CW_DOT_KEY_PRESSSED_END = '600'

CW_DASH_KEY_PRESSSED_START = '601'
CW_DASH_KEY_PRESSSED_END = '700'

CW_BOTH_KEY_PRESSSED_START = '51'
CW_BOTH_KEY_PRESSSED_END = '300'


#
#   end ENUMS#################################################

READCOMMAND=0xDB
WRITECOMMAND=0xDC
READADCDATA=0xDD

READVFO=0xC5

SETMODE = 0x07          #CatSetMode function
CAT_MODE_CW = 0x02
CAT_MODE_USB = 0x01


READCALINMEMORY= 0xC0

WRITEMASTERCALINMEMORY = 0xC1
WRITEUSBCALINMEMORY = 0xC2
WRITECWCALINMEMORY = 0xC3

WRITECALVALUESTOEEPROM =0xC4

GETSIZECOMMAND=0xDF

OK=0x77
ACK = 0x00
RETRIES=3



VERSION_ADDRESS = 779   # this is the address in the EEPROM of the version. If < 5, then orginal KD8CEC
                        # 5 or more means KD8CEC V2 with ability to get the eepromsize through CAT
KD8CEC_V2_INTERNAL_VERSION_NUM = 5
EXT_FIRMWARE_ID_ADDR1 = 1024
EXT_FIRMWARE_ID_ADDR2 = 1025
EXT_FIRMWARE_ID_ADDR3 = 1026

# Magic numbers used for validation of EEPROM
MAGIC_VALID_EEPROM_1 = 0x59
MAGIC_VALID_EEPROM_2 = 0x58
MAGIC_VALID_EEPROM_3 = 0x68

MAGIC_USER_CALLSIGN_KEY = 0x59
MAGIC_CW_AUTO_MAGIC_KEY = 0x73

VALID_BFO_VALUES = { 'V56':     (11048000, 11060000, 11052000 ),
                     'V34':   (11990000, 12010000, 11997000 )
                     }
LOW_BFO_VALUE = 0          # enum for low value
HIGH_BFO_VALUE = 1          # enum for high value
DEFAULT_BFO_VALUE = 2       # enum for default value if out of range


EEPROMSIZE=2048                              # default to large EEPROM, but check later and reset to right number
DEFAULT_EEPROM_SIZE=1024                     # used as the default value when EEPROM size is unknown
MAXEEPROMSIZE=2048
MAXWRITETOEEPROM=1024
BACKUPFILESIZE=2048

STARTFACTOREYRESTORE=64
ENDFACTORYRESTORE=100

CW_MEMORY_KEYER_BUFFER_START = 803              #  Magic - Location of the CW_AUTO_DATA pointer
CW_MEMORY_KEYER_BUFFER_END = 1023


VREFMAXVALUE=1023
# Index's of PIN Function to ADC Value in KD8CEC
ANALOGPINS = {"ENC A":0, "ENC B": 1, "ENC SW":2, "PTT":3, "CW Keyer":6, "S Meter":7  } # A4 and A5 are used for I2C on Some platforms
#SMETERPIN=7


CHANNELNAMELENGTH = 5                               #Number of characters in the Channel Name
WSPRNAMELENGTH = 5                                  #Number of characters in the Channel Name
WSPRREG1LENGTH = 5
WSPRREG2LENGTH = 3
TOTALCWMESSAGES=10                                  #assumption on number of CW message elements to be provided
SIZEOFWSPRMESSAGES=41                               #size in bytes of wspr messages
MAXCALLSIGNLEN = 18                                 #Max length of callsign and alt callsign

DEFAULTCWSPEED = '10'

BAUD = 38400

#application required files################################################

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# to use pyinstaller we need to get the resource not the path
# resource_path is in globalvars
#

def copyLogToClipboard(textToClip):
        tmpTK = tk.Text()
        tmpTK.clipboard_clear()
        tmpTK.clipboard_append(textToClip)
        tmpTK.update()

def setEEPROM_SIZE (newSize):
    global EEPROMSIZE
    EEPROMSIZE = newSize


def getEEPROM_SIZE ():
    global EEPROMSIZE
    return EEPROMSIZE

def millis():
    return (time.time_ns()// 1000000)



SERIALTIMEOUT = 5000


EEPROMMEMORYMAP=resource_path("eeprommemorymap.xml")               #Maps EEPROM locations to settings
USERMODFILETEMPLACE=resource_path("usermodfiletemplate.xml")       #Template file used to fill in with data from EEPROM

HELPFILE = resource_path("help.xml")
ABOUTFILE = resource_path("about.xml")

WINDOWMANAGERICON = resource_path("settingseditor.gif")

LEFTCOPYARROW = resource_path("img_red-arrow-pointing-left59x36.png")
RIGHTCOPYARROW = resource_path("img_red-arrow-pointing-right59x36.png")

SAMPLE1ICON = resource_path("img_sample1-125x80.png")
SAMPLE2ICON = resource_path("img_sample2-125x80.png")
SAMPLE3ICON = resource_path("img_sample3-125x80.png")
SAMPLE4ICON = resource_path("img_sample4-125x80.png")
SAMPLE5ICON = resource_path("img_sample5-125x80.png")
SAMPLE6ICON = resource_path("img_sample6-125x80.png")
SAMPLE7ICON = resource_path("img_sample7-125x80.png")
CUSTOMICON = resource_path("img_Custom-125x80.png")

RELOADICON = resource_path("img_Reload-24x24.png")
COPYICON = resource_path("img_copy_icon25x25.png")

MOVELEFTARROWICON = resource_path("img_plain_red-arrow-pointing-left59x36.png")
MOVERIGHTARROWICON = resource_path("img_plain_red-arrow-pointing-right59x36.png")




USERMODFILE="Select Saved File"                       #Output of process - file that User can customize

#HOMEDIRECTORY="c:/Users/markj/Documents/backups/usermodfiles"                      #Initial directory for file selector
HOMEDIRECTORY="~"                      #Initial directory for file selector


DEBUGAPP=False




