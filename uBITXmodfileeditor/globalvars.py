#ENUMS#####################################################
INTERNAL_FIRMWARE_VERSION = ["NA", "V1.061", "V1.07", "V1.08", "V1.09", "V2.0"]
MODE_SELECT = ["DEFAULT","xxx","LSB","USB","CWL","CWU"]
BOOL_SELECT = ["NO","YES"]
TUNE_RESTRICT_SELECT = ["NONE","BAND"]
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
#end ENUMS#################################################

READCOMMAND=0xDB
WRITECOMMAND=0xDC
READADC=0xDD

OK=0x77
ACK = 0x00
RETRIES=3


EEPROMSIZE=1024
BACKUPFILESIZE=2048


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


EEPROMMEMORYMAP="eeprommemorymap.xml"               #Maps EEPROM locations to settings
USERMODFILETEMPLACE="usermodfiletemplate.xml"       #Template file used to fill in with data from EEPROM


USERMODFILE="Select Saved File"                       #Output of process - file that User can customize
USERMODFILE="c:/Users/markj/Documents/backups/usermodfiles"                        #Output of process - file that User can customize
HOMEDIRECTORY="c:/Users/markj/Documents/backups/usermodfiles"                                     #Initial directory for file selector

# #   Dictionary to hold current values of usermodfile and whether dirty or not
# userModFileValues = {}
# userModFileDirty = {}
# userModFileToolTips = {}




