from lxml import etree as ET
from globalvars import *



class getters(object):
    # utility functions
    def get_Byte_FromEEPROM(self, memBuffer: bytearray, memlocation: int) -> int:
        return (memBuffer[memlocation])

    def get_uint16_FromEEPROM(self, memBuffer: bytearray, memlocation: int) -> int:
        return memBuffer[memlocation] + (memBuffer[memlocation + 1] << 8)

    def get_uint32_FromEEPROM(self, memBuffer: bytearray, memlocation: int) -> int:
        return memBuffer[memlocation] + (memBuffer[memlocation + 1] << 8) + (memBuffer[memlocation + 2] << 16) + (
                    memBuffer[memlocation + 3] << 24)


#         #***********************************
#         #   RADIO CALIBRATION SETTINGS
#         #***********************************

    def MASTER_CAL(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        print("Getter Called:" SettingName)

    def USB_CAL(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        print("Getter Called:" SettingName)

    def CW_CAL(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        print("Getter Called:" SettingName)

    def F1_CAL_ON_OFF_SWITCH(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        print("Getter Called:" SettingName)

    def IF1_CAL(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        print("Getter Called:" SettingName)

    def IF1_CAL_ADD_SUB(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        print("Getter Called:" SettingName)

#
#         #***********************************
#         #   VFO SETTING FOR ON BOOT
#         #***********************************
#

    def VFO_A (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        value.text = str(self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation))

    def VFO_B(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        value.text = str(self.get_uint32_FromEEPROM(EEPROMBuffer, memLocation))

    def VFO_A_MODE (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        value.text = MODE_SELECT[self.get_Byte_FromEEPROM(EEPROMBuffer, memLocation)]

    def VFO_B_MODE (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        value.text = MODE_SELECT[self.get_Byte_FromEEPROM(EEPROMBuffer, memLocation)]

    def TUNING_STEP_INDEX (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        print("Getter Called:", SettingName)

    def TUNING_STEP1 (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        print("Getter Called:", SettingName)

    def TUNING_STEP2 (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        print("Getter Called:", SettingName)

    def TUNING_STEP3 (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        print("Getter Called:", SettingName)

    def TUNING_STEP4 (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        print("Getter Called:", SettingName)

    def TUNING_STEP5 (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        print("Getter Called:", SettingName)

#
#         #***********************************
#         #   COMMON CW SETTINGS
#         #***********************************
#

    def CW_KEY_TYPE (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        print("Getter Called:", SettingName)

    def CW_SIDETONE(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        print("Getter Called:", SettingName)

    def CW_SPEED_WPM (self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        print("Getter Called:", SettingName)

    def CW_DELAY_MS(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        print("Getter Called:", SettingName)

    def CW_START_MS(self, SettingName, EEPROMBuffer, memLocation, value, _unused, _unused1):
        print("Getter Called:", SettingName)










    def defaultFunc(self, *args):
        print ("Command not recognised:", args[0])

    def get(self, cmd, *args):
        return getattr(self, cmd, self.defaultFunc)(*args)