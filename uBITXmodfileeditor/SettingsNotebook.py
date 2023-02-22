import pygubu.widgets.simpletooltip as tooltip
import tkinter as tk

from settingsnotebookwidget import SettingsnotebookWidget
from I2cscanner import I2Cscanner
from ADCscanner import ADCscanner
from SmeterWizard import SmeterWizard
from globalvars import *

class SettingsNotebook(SettingsnotebookWidget):
    def __init__(self, parent):
        #   Save root (parent)
        self.root = parent

        #   Set up image files first
        self.img_img_redarrowpointingleft59x36 = tk.PhotoImage(file=LEFTCOPYARROW)
        self.img_img_redarrowpointingright59x36 = tk.PhotoImage(file=RIGHTCOPYARROW)



        super().__init__(parent)

        #   now configure the buttons to display the arrows.
        self.MASTER_CAL_COPY_BUTTON.configure(image=self.img_img_redarrowpointingleft59x36)
        self.MASTER_CAL_COPY_FACTORY_BUTTON.configure(image=self.img_img_redarrowpointingright59x36)

        self.USB_CAL_COPY_BUTTON.configure(image=self.img_img_redarrowpointingleft59x36)
        self.USB_CAL_COPY_FACTORY_BUTTON.configure(image=self.img_img_redarrowpointingright59x36)

        #   Initialize maximum available bytes to 0
        self.CW_AUTO_BYTES_USED.set('0')


    #   temp to control what is processed
    readyToGo = ['VERSION_ADDRESS', 'FACTORY_VALUES_MASTER_CAL', 'FACTORY_VALUES_USB_CAL',
             'MASTER_CAL', 'USB_CAL', 'CW_CAL', 'VFO_A', 'VFO_A_MODE', 'VFO_B', 'VFO_B_MODE',
             'TUNING_STEP_INDEX', 'TUNING_STEP1', 'TUNING_STEP2', 'TUNING_STEP3', 'TUNING_STEP4', 'TUNING_STEP5',
             'CW_KEY_TYPE',
            'CW_SIDETONE',  'CW_SPEED_WPM', 'CW_DELAY_MS','CW_START_MS', 'USER_CALLSIGN', 'QSO_CALLSIGN', 'CW_ADC_ST_FROM', 'CW_ADC_ST_TO',
            'CW_ADC_DOT_FROM', 'CW_ADC_DOT_TO', 'CW_ADC_DASH_FROM', 'CW_ADC_DASH_TO', 'CW_ADC_BOTH_FROM', 'CW_ADC_BOTH_TO',
            'CW_AUTO_MAGIC_KEY', 'USER_CALLSIGN_KEY',
            'CW_MEMORY_KEYER_MSG0', 'CW_MEMORY_KEYER_MSG1', 'CW_MEMORY_KEYER_MSG2', 'CW_MEMORY_KEYER_MSG3', 'CW_MEMORY_KEYER_MSG4',
            'CW_MEMORY_KEYER_MSG5', 'CW_MEMORY_KEYER_MSG6', 'CW_MEMORY_KEYER_MSG7', 'CW_MEMORY_KEYER_MSG8', 'CW_MEMORY_KEYER_MSG9',
            'CW_MEMORY_KEYER_MSGA', 'CW_MEMORY_KEYER_MSGB', 'CW_MEMORY_KEYER_MSGC', 'CW_MEMORY_KEYER_MSGD', 'CW_MEMORY_KEYER_MSGE',
            'CW_MEMORY_KEYER_MSGF', 'CW_MEMORY_KEYER_MSGG', 'CW_MEMORY_KEYER_MSGH', 'CW_MEMORY_KEYER_MSGI', 'CW_MEMORY_KEYER_MSGJ',
            'CW_MEMORY_KEYER_MSGK', 'CW_MEMORY_KEYER_MSGL', 'CW_MEMORY_KEYER_MSGM', 'CW_MEMORY_KEYER_MSGN', 'CW_MEMORY_KEYER_MSGO',
            'CHANNEL_FREQ1', 'CHANNEL_FREQ1_MODE', 'CHANNEL_FREQ1_SHOW_NAME', 'CHANNEL_FREQ1_NAME',
            'CHANNEL_FREQ1', 'CHANNEL_FREQ1_MODE', 'CHANNEL_FREQ1_SHOW_NAME', 'CHANNEL_FREQ1_NAME',
            'CHANNEL_FREQ2', 'CHANNEL_FREQ2_MODE', 'CHANNEL_FREQ2_SHOW_NAME', 'CHANNEL_FREQ2_NAME',
            'CHANNEL_FREQ3', 'CHANNEL_FREQ3_MODE', 'CHANNEL_FREQ3_SHOW_NAME', 'CHANNEL_FREQ3_NAME',
            'CHANNEL_FREQ4', 'CHANNEL_FREQ4_MODE', 'CHANNEL_FREQ4_SHOW_NAME', 'CHANNEL_FREQ4_NAME',
            'CHANNEL_FREQ5', 'CHANNEL_FREQ5_MODE', 'CHANNEL_FREQ5_SHOW_NAME', 'CHANNEL_FREQ5_NAME',
            'CHANNEL_FREQ6', 'CHANNEL_FREQ6_MODE', 'CHANNEL_FREQ6_SHOW_NAME', 'CHANNEL_FREQ6_NAME',
            'CHANNEL_FREQ7', 'CHANNEL_FREQ7_MODE', 'CHANNEL_FREQ7_SHOW_NAME', 'CHANNEL_FREQ7_NAME',
            'CHANNEL_FREQ8', 'CHANNEL_FREQ8_MODE', 'CHANNEL_FREQ8_SHOW_NAME', 'CHANNEL_FREQ8_NAME',
            'CHANNEL_FREQ9', 'CHANNEL_FREQ9_MODE', 'CHANNEL_FREQ9_SHOW_NAME', 'CHANNEL_FREQ9_NAME',
            'CHANNEL_FREQ10', 'CHANNEL_FREQ10_MODE', 'CHANNEL_FREQ10_SHOW_NAME', 'CHANNEL_FREQ10_NAME',
            'CHANNEL_FREQ11', 'CHANNEL_FREQ11_MODE',  'CHANNEL_FREQ12', 'CHANNEL_FREQ12_MODE',
            'CHANNEL_FREQ13', 'CHANNEL_FREQ13_MODE',  'CHANNEL_FREQ14', 'CHANNEL_FREQ14_MODE',
            'CHANNEL_FREQ15', 'CHANNEL_FREQ15_MODE',  'CHANNEL_FREQ16', 'CHANNEL_FREQ16_MODE',
            'CHANNEL_FREQ17', 'CHANNEL_FREQ17_MODE',  'CHANNEL_FREQ18', 'CHANNEL_FREQ18_MODE',
            'CHANNEL_FREQ19', 'CHANNEL_FREQ19_MODE',  'CHANNEL_FREQ20', 'CHANNEL_FREQ20_MODE',
            'HAM_BAND_COUNT', 'HAM_BAND_RANGE1_START', 'HAM_BAND_RANGE1_END', 'HAM_BAND_RANGE2_START', 'HAM_BAND_RANGE2_END',
            'HAM_BAND_RANGE3_START', 'HAM_BAND_RANGE3_END', 'HAM_BAND_RANGE4_START', 'HAM_BAND_RANGE4_END', 'HAM_BAND_RANGE5_START',
            'HAM_BAND_RANGE5_END', 'HAM_BAND_RANGE6_START', 'HAM_BAND_RANGE6_END', 'HAM_BAND_RANGE7_START', 'HAM_BAND_RANGE7_END',
            'HAM_BAND_RANGE8_START', 'HAM_BAND_RANGE8_END', 'HAM_BAND_RANGE9_START', 'HAM_BAND_RANGE9_END', 'HAM_BAND_RANGE10_START',
            'HAM_BAND_RANGE10_END',  'HAM_BAND_FREQS1', 'HAM_BAND_FREQS2','HAM_BAND_FREQS3','HAM_BAND_FREQS4','HAM_BAND_FREQS5',
            'HAM_BAND_FREQS6','HAM_BAND_FREQS7','HAM_BAND_FREQS8','HAM_BAND_FREQS9','HAM_BAND_FREQS10', 'HAM_BAND_FREQS1_MODE',
            'HAM_BAND_FREQS2_MODE', 'HAM_BAND_FREQS3_MODE', 'HAM_BAND_FREQS4_MODE', 'HAM_BAND_FREQS5_MODE', 'HAM_BAND_FREQS6_MODE',
            'HAM_BAND_FREQS7_MODE', 'HAM_BAND_FREQS8_MODE', 'HAM_BAND_FREQS9_MODE', 'HAM_BAND_FREQS10_MODE',
            'BOOT_INTO_SDR_MODE', 'SDR_OFFSET_MODE', 'SDR_FREQUENCY',
            'I2C_LCD_MASTER', 'TUNING_RESTICTIONS', 'TX_RESTRICTIONS',
            'I2C_LCD_SECOND', 'I2C_ADDR_SI5351','ONE_TWO_LINE_TOGGLE', 'SCROLLING_DISPLAY', 'MESSAGE_LINE', 'S_METER_LEVELS', 'S_METER_LEVEL1',
            'S_METER_LEVEL2', 'S_METER_LEVEL3', 'S_METER_LEVEL4', 'S_METER_LEVEL5', 'S_METER_LEVEL6', 'S_METER_LEVEL7', 'S_METER_LEVEL8',
            'EXTENDED_KEY1_FUNC', 'EXTENDED_KEY1_START', 'EXTENDED_KEY1_END', 'EXTENDED_KEY2_FUNC', 'EXTENDED_KEY2_START', 'EXTENDED_KEY2_END',
            'EXTENDED_KEY3_FUNC', 'EXTENDED_KEY3_START', 'EXTENDED_KEY3_END', 'EXTENDED_KEY4_FUNC', 'EXTENDED_KEY4_START', 'EXTENDED_KEY4_END',
            'EXTENDED_KEY5_FUNC', 'EXTENDED_KEY5_START', 'EXTENDED_KEY5_END', 'EXTENDED_KEY6_FUNC', 'EXTENDED_KEY6_START', 'EXTENDED_KEY6_END',
            'CW_MEMORY_KEYER_MSG01', 'CW_MEMORY_KEYER_MSG02', 'CW_MEMORY_KEYER_MSG03', 'CW_MEMORY_KEYER_MSG04',
            'CW_MEMORY_KEYER_MSG05', 'CW_MEMORY_KEYER_MSG06', 'CW_MEMORY_KEYER_MSG07', 'CW_MEMORY_KEYER_MSG08',
            'CW_MEMORY_KEYER_MSG09', 'CW_MEMORY_KEYER_MSG10', 'CW_AUTO_COUNT', 'WSPR_COUNT',
            'WSPR_BAND1_TXFREQ', 'WSPR_BAND2_TXFREQ', 'WSPR_BAND3_TXFREQ', 'WSPR_MESSAGE1_NAME', 'WSPR_MESSAGE2_NAME',
            'WSPR_MESSAGE3_NAME', 'WSPR_MESSAGE4_NAME', 'WSPR_MESSAGE1', 'WSPR_MESSAGE2', 'WSPR_MESSAGE3', 'WSPR_MESSAGE4',
            'CUST_LPF_ENABLED', 'CUST_LPF_FILTER1_ENDFREQ', 'CUST_LPF_FILTER2_ENDFREQ', 'CUST_LPF_FILTER3_ENDFREQ',
            'CUST_LPF_FILTER4_ENDFREQ', 'CUST_LPF_FILTER5_ENDFREQ', 'CUST_LPF_FILTER6_ENDFREQ', 'CUST_LPF_FILTER7_ENDFREQ',
            'CUST_LPF_FILTER1_CONTROL', 'CUST_LPF_FILTER2_CONTROL', 'CUST_LPF_FILTER3_CONTROL', 'CUST_LPF_FILTER4_CONTROL',
            'CUST_LPF_FILTER5_CONTROL', 'CUST_LPF_FILTER6_CONTROL', 'CUST_LPF_FILTER7_CONTROL'
             ]

    #   this needs to be moved somewhere else too
    hideOnStartup = ['Extended_Channel_Frame', "TUNING_STEP_INDEX_VALUE_WIDGET", "TUNING_STEP_INDEX_WIDGET",
                    'CW_AUTO_MAGIC_KEY_WIDGET',  'USER_CALLSIGN_KEY_WIDGET']

    #   Class variables
    #
    newTuningSteps = ()
    #   error message will be set when ever validation fails
    validationErrorMsg = ''

    #   Error messages common to all validation
    error_Msgs = {
        "NOTINMIDDLE":"must be between {:,} and {:,}, prior value restored",
        "NOTANUMBER":"{} is not a valid number, prior value restored",
        "NOTLOWER":"must be lower than {:,}, prior value restored",
        "NOTHIGHER":"must be higher than {:,}, prior value restored",
        "STRINGTOOLONG": "longer than {} characters, prior value restored",
        "NOTVALIDTUNINGSTEP": "Left most two digits of any tuning step must be {:,} to {:,}, prior value restored",
        "TOOMANYCWCHARS": "Required {:,} bytes for CW Message but ony {:,} available, prior message restored"
    }

    priorValues={}

    # Value Constraints
    ADC = {'LOW':0, 'HIGH':1023}            # Min/Max for Analog to Digital read - used for cw keys, etc.
    FREQ ={'LOW':0, 'HIGH':60000000}            # Min/Max for valid frequencies.
    FREQKHZ = {'LOW':0, 'HIGH':60000}
    MASTER_CAL_BOUNDS = {'LOW':-500000, 'HIGH': 500000}
    USB_CAL_BOUNDS = {'LOW':0, 'HIGH': 20000000}
    CW_CAL_BOUNDS = {'LOW':0, 'HIGH': 20000000}
    PREDEFINED_TUNING_STEPS = {'0': [1,5,10,50,100], '1': [10,20,50,100,1000], '2': [1,10,100,1000,10000],
                               '3': [10,50,500,5000,10000], '4': [10,50,100,2000,50000] }
    TUNING_STEPS_BOUNDS = {'LOW':1, 'HIGH': 60}
    CW_SIDETONE_BOUNDS = {'LOW':100, 'HIGH': 2000}
    CW_SPEED_WPM_BOUNDS = {'LOW':1, 'HIGH': 250}
    CW_START_MS_BOUNDS = {'LOW':0, 'HIGH': 5000}
    CW_DELAY_MS_BOUNDS = {'LOW':0, 'HIGH': 10000}
    CHANNEL_WSPR_NAME_MAX = 5
    USER_CALLSIGN_BOUNDS = {'HIGH':18 }
    HAM_BAND_COUNT_BOUNDS = {'LOW':0, 'HIGH':10}

    errorMsgPersistFlag = 0         #This is a hack to keep error messages around thru the next entry/selection
                                    #When an error message is displayed, this flag is incremented.
                                    #When a good entry is validated, this error message is set to zero
                                    #On the next valid entry, the errormessage is unpacked and is no longer visible

    ##############################
    #  Validation helper functions
    ##############################

    def getNumber (self,x):
        valueToTest = int(x.translate({ord(c): None for c in"-.,+"}))       #   eliminate periods, commas, and leading sign
        if (x.lstrip()[0] == "-"):                                          #   check if first character is a minus in original string
            valueToTest = -valueToTest
        return valueToTest

    def checkLength (self,x, maxChars):
        if (len(x) <= maxChars):                                          #   check if first character is a minus in original string
            return True
        else:
            SettingsNotebook.validationErrorMsg = SettingsNotebook.error_Msgs["STRINGTOOLONG"].format(maxChars)
            return False

    def validateNumber (self, x, lowValue, highValue):
        try:
            valueToTest = int(x.translate({ord(c): None for c in"-.,+"}))       #   eliminate periods, commas, and leading signs
        except:                                                             #   if it fails the conversion to number, must not be a number
            SettingsNotebook.validationErrorMsg = SettingsNotebook.error_Msgs["NOTANUMBER"].format(x)
            return False

        if (x.lstrip()[0] == "-"):                                          #   check if first character is a minus in original string
            valueToTest = -valueToTest

        if ((lowValue <= valueToTest) & (highValue >= valueToTest)):        #   confirm that it meets upper/lower bounds
            return True
        else:
            SettingsNotebook.validationErrorMsg = SettingsNotebook.error_Msgs["NOTINMIDDLE"].format(lowValue, highValue)
            return False
    def validateADC(self, x, highOrLow, target):
        return self.validateNumberRange(x,SettingsNotebook.ADC['LOW'], SettingsNotebook.ADC['HIGH'],highOrLow, target )

    def validateFREQ(self, x, highOrLow, target):
        return self.validateNumberRange(x,SettingsNotebook.FREQ['LOW'], SettingsNotebook.FREQ['HIGH'],highOrLow, target)

    def validateFREQKHZ(self, x, highOrLow, target):
        return self.validateNumberRange(x,SettingsNotebook.FREQKHZ['LOW'], SettingsNotebook.FREQKHZ['HIGH'],highOrLow, target)

    def validateNumberRange (self, x, lowValue, highValue, highOrLow, target):
        #   X = string of digits we are validating
        #   lowValue = absolute lowest value it can be
        #   highValue = absolute highest value it cane be
        #   highOrLow = "HIGH" target should be higher than X, "LOW"= target should be lower
        #   returns =   True if it passes validation tests
        #               False if one of the tests fails
        if(self.validateNumber(x,lowValue, highValue)):
            if (highOrLow == "HIGH"):
                if (self.getNumber(x) <= int(self.getNumber(target) )):          # Target is supposed to be greater than X
                    return True
                else:
                    SettingsNotebook.validationErrorMsg = SettingsNotebook.error_Msgs["NOTLOWER"].format(int(self.getNumber(target)))
                    return False
            elif (self.getNumber(x) >= int(self.getNumber(target))):             # Target is supposed to be less than X
                return True
            else:
                SettingsNotebook.validationErrorMsg = SettingsNotebook.error_Msgs["NOTHIGHER"].format(int(self.getNumber(target)))
                return False
        else:
            return False            # Error message already set by validateNumber
    def clearErrorMsgPersistFlag(self):
        errorMsgPersistFlag = 0

    ##############################
    #  Validation functions
    ##############################

    def validate_MASTER_CAL(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValues["MASTER_CAL"] = p_entry_value
        if(self.validateNumber(p_entry_value,  SettingsNotebook.MASTER_CAL_BOUNDS['LOW'],  SettingsNotebook.MASTER_CAL_BOUNDS['HIGH'])):
            return True
        else:
            self.log.printerror("timestamp", "Master Calibration " + SettingsNotebook.validationErrorMsg)
            self.MASTER_CAL.set(self.priorValues["MASTER_CAL"])
            return False

    def validate_USB_CAL(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValues["USB_CAL"] = p_entry_value
        if(self.validateNumber(p_entry_value, SettingsNotebook.USB_CAL_BOUNDS['LOW'], SettingsNotebook.USB_CAL_BOUNDS['HIGH'])):
            return True
        else:
            self.log.printerror("timestamp", "SSB BFO Calibration " + SettingsNotebook.validationErrorMsg)
            self.USB_CAL.set(self.priorValues["USB_CAL"])
            return False

    def validate_CW_CAL(self, p_entry_value, v_condition):
        if (v_condition == "focusin"):
            self.priorValues["CW_CAL"] = p_entry_value
        if(self.validateNumber(p_entry_value, SettingsNotebook.CW_CAL_BOUNDS['LOW'], SettingsNotebook.CW_CAL_BOUNDS['HIGH'])):
            return True
        else:
            self.log.printerror("timestamp", "CW BFO Calibration " + SettingsNotebook.validationErrorMsg)
            self.CW_CAL.set(self.priorValues["CW_CAL"])
            return False



    def validate_TUNING_STEP(self, p_entry_value, v_condition, currentStep):

        if (v_condition == "focusin"):
            self.priorValues["TUNING_"+currentStep] = p_entry_value

        # Make sure we have a number here
        try:
            valueToTest = int(p_entry_value)
        except:                                   #   if it fails the conversion to number, must not be a number
            self.log.printerror("timestamp",  SettingsNotebook.error_Msgs["NOTANUMBER"].format(p_entry_value))

        else:
            # We have a real number, now need to look at first (left most) digits to make sure they are 1-60
            noSpacesString = p_entry_value.strip()
            stepLength= len(noSpacesString)

            if stepLength >= 2:
                testValue = int(noSpacesString[:2])
            elif stepLength > 1:
                testValue = int(noSpacesString[:1])
            else:
                testValue = 0

            if((testValue >= SettingsNotebook.TUNING_STEPS_BOUNDS['LOW']) & (SettingsNotebook.TUNING_STEPS_BOUNDS['HIGH'] >= testValue)):
                return True
            else:
                # Reaching here means that a step's left most digits are out of the range of 1-60
                SettingsNotebook.validationErrorMsg = \
                    SettingsNotebook.error_Msgs["NOTVALIDTUNINGSTEP"].format(SettingsNotebook.TUNING_STEPS_BOUNDS['LOW'],
                                                                             SettingsNotebook.TUNING_STEPS_BOUNDS['HIGH'])

        # if we reach this point, there is an error...
        SettingsNotebook.validationErrorMsg = SettingsNotebook.error_Msgs["STRINGTOOLONG"].format(maxChars)
        self.log.printerror("timestamp",  SettingsNotebook.validationErrorMsg)
        getattr(self, "TUNING_"+currentStep).set(self.priorValues["TUNING_"+currentStep])
        return False


    def validate_TUNING_STEP1(self, p_entry_value, v_condition):
        return self.validate_TUNING_STEP(p_entry_value, v_condition, "STEP1")

    def validate_TUNING_STEP2(self, p_entry_value, v_condition):
        return self.validate_TUNING_STEP(p_entry_value, v_condition, "STEP2")

    def validate_TUNING_STEP3(self, p_entry_value, v_condition):
        return self.validate_TUNING_STEP(p_entry_value, v_condition, "STEP3")

    def validate_TUNING_STEP4(self, p_entry_value, v_condition):
        return self.validate_TUNING_STEP(p_entry_value, v_condition, "STEP4")

    def validate_TUNING_STEP5(self, p_entry_value, v_condition):
        return self.validate_TUNING_STEP(p_entry_value, v_condition, "STEP5")




    def validate_CW_SIDETONE(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValues["CW_SIDETONE"] = p_entry_value
        if(self.validateNumber(p_entry_value,SettingsNotebook.CW_SIDETONE_BOUNDS['LOW'], SettingsNotebook.CW_SIDETONE_BOUNDS['HIGH'])):
            return True
        else:
            self.log.printerror("timestamp",  "CW Sidetone " + SettingsNotebook.validationErrorMsg)
            self.CW_SIDETONE.set(self.priorValues["CW_SIDETONE"])
            return False

    def validate_CW_SPEED_WPM(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValues["CW_SPEED_WPM"] = p_entry_value
        if(self.validateNumber(p_entry_value,SettingsNotebook.CW_SPEED_WPM_BOUNDS['LOW'], SettingsNotebook.CW_SPEED_WPM_BOUNDS['HIGH'])):
            return True
        else:
            self.log.printerror("timestamp",  "CW Keyer speed " + SettingsNotebook.validationErrorMsg)
            self.CW_SPEED_WPM.set(self.priorValues["CW_SPEED_WPM"])
            return False

    def validate_CW_DELAY_MS(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValues["CW_DELAY_MS"] = p_entry_value
        if(self.validateNumber(p_entry_value,SettingsNotebook.CW_DELAY_MS_BOUNDS['LOW'], SettingsNotebook.CW_DELAY_MS_BOUNDS['HIGH'])):
            return True
        else:
            self.log.printerror("timestamp",  "CW delay after ending TX  " + SettingsNotebook.validationErrorMsg)
            self.CW_DELAY_MS.set(self.priorValues["CW_DELAY_MS"])
            return False

    def validate_CW_START_MS(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValues["CW_START_MS"] = p_entry_value
        if(self.validateNumber(p_entry_value,SettingsNotebook.CW_START_MS_BOUNDS['LOW'], SettingsNotebook.CW_START_MS_BOUNDS['HIGH'])):
            return True
        else:
            self.log.printerror("timestamp", "CW delay before going into TX " + SettingsNotebook.validationErrorMsg)
            self.CW_START_MS.set(self.priorValues["CW_START_MS"] )
            return False

    def validate_USER_CALLSIGN(self, p_entry_value, v_condition):
        if (v_condition == "focusin"):
            self.priorValues["USER_CALLSIGN"] = p_entry_value
        if(self.checkLength(p_entry_value, SettingsNotebook.USER_CALLSIGN_BOUNDS['HIGH']) ):
            return True
        else:
            self.log.printerror("timestamp",  "Callsign is " + SettingsNotebook.validationErrorMsg)
            self.USER_CALLSIGN.set(self.priorValues["USER_CALLSIGN"])
            return False

    def validate_QSO_CALLSIGN(self, p_entry_value, v_condition):
        if (v_condition == "focusin"):
            self.priorValues["QSO_CALLSIGN"] = p_entry_value
        if(self.checkLength(p_entry_value, SettingsNotebook.USER_CALLSIGN_BOUNDS['HIGH']) ):
            # Update maximum available bytes
            self.CW_AUTO_REMAINING_BYTES.set(str(EEPROMSIZE - 1 - len(p_entry_value) - CW_MEMORY_KEYER_BUFFER_START - int(self.CW_AUTO_BYTES_USED.get())))

            return True
        else:
            self.log.printerror("timestamp",  "QSO Callsign is " + SettingsNotebook.validationErrorMsg)
            self.QSO_CALLSIGN.set(self.priorValues["QSO_CALLSIGN"])
            return False

    def validate_CW_ADC_ST_FROM(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValues["CW_ADC_ST_FROM"] = p_entry_value
        elif (v_condition == "focusout"):
            if (self.getNumber(p_entry_value) == '0') | \
                    (self.validateADC(p_entry_value, 'HIGH', str(self.ADC['HIGH']))):
                return True

            # if we reach this point, there is an error...
            self.log.printerror("timestamp","CW Straight Key ADC beginning value "+SettingsNotebook.validationErrorMsg)
            getattr(self, "CW_ADC_ST_FROM").set(self.priorValues["CW_ADC_ST_FROM"])
            return False
        return True

    def validate_CW_ADC_ST_TO(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValues["CW_ADC_ST_TO"] = p_entry_value
        elif (v_condition == "focusout"):
            if (self.getNumber(p_entry_value) == '0') | (self.validateADC(p_entry_value, 'LOW', getattr(self, "CW_ADC_ST_FROM").get())):
                return True

            # if we reach this point, there is an error...
            print(self.getNumber(p_entry_value) )
            print("lower is", getattr(self, "CW_ADC_ST_FROM").get())
            self.log.printerror("timestamp", "CW Straight Key ADC ending value "+SettingsNotebook.validationErrorMsg)
            getattr(self, "CW_ADC_ST_TO").set(self.priorValues["CW_ADC_ST_TO"])
            return False
        return True


    def validate_CW_ADC_DOT_FROM(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValues["CW_ADC_DOT_FROM"] = p_entry_value
        elif (v_condition == "focusout"):
            if (self.getNumber(p_entry_value) == '0') | self.validateADC(p_entry_value, 'HIGH', str(self.ADC['HIGH'])):
                return True

            # if we reach this point, there is an error...
            self.log.printerror("timestamp", "CW DOT ADC beginning value "+SettingsNotebook.validationErrorMsg)
            getattr(self,"CW_ADC_DOT_FROM").set(self.priorValues["CW_ADC_DOT_FROM"])
            return False
        return True


    def validate_CW_ADC_DOT_TO(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValues["CW_ADC_DOT_TO"]  = p_entry_value
        elif (v_condition == "focusout"):
            if (self.getNumber(p_entry_value) == '0') | (self.validateADC(p_entry_value, 'LOW', self.CW_ADC_DOT_FROM.get())):
                return True

            # if we reach this point, there is an error...
            self.log.printerror("timestamp", "CW DOT ADC ending value "+SettingsNotebook.validationErrorMsg)
            getattr(self,"CW_ADC_DOT_TO").set(self.priorValues["CW_ADC_DOT_TO"])
            return False
        return True

    def validate_CW_ADC_DASH_FROM(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValues["CW_ADC_DASH_FROM"] = p_entry_value
        elif (v_condition == "focusout"):
            if (self.getNumber(p_entry_value) == '0') | (self.validateADC(p_entry_value, 'HIGH', str(self.ADC['HIGH']))):
                return True

            # if we reach this point, there is an error...
            self.log.printerror("timestamp", "CW DASH ADC beginning value "+SettingsNotebook.validationErrorMsg)
            getattr(self, "CW_ADC_DASH_FROM").set(self.priorValues["CW_ADC_DASH_FROM"])
            return False
        return True

    def validate_CW_ADC_DASH_TO(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValues["CW_ADC_DASH_TO"] = p_entry_value
        elif (v_condition == "focusout"):
            if (self.getNumber(p_entry_value) == '0') | (self.validateADC(p_entry_value, 'LOW', self.CW_ADC_DASH_FROM.get())):
                return True

            # if we reach this point, there is an error...
            self.log.printerror("timestamp", "CW DASH Key ADC ending value " + SettingsNotebook.validationErrorMsg)
            getattr(self, "CW_ADC_DASH_TO").set(self.priorValues["CW_ADC_DASH_TO"])
            return False
        return True

    def validate_CW_ADC_BOTH_FROM(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValues["CW_ADC_BOTH_FROM"] = p_entry_value
        elif (v_condition == "focusout"):
            if (self.getNumber(p_entry_value) == '0') | (self.validateADC(p_entry_value, 'HIGH', str(self.ADC['HIGH']))):
                return True

            # if we reach this point, there is an error...
            self.log.printerror("timestamp", "CW BOTH keys pressed ADC beginning value "+SettingsNotebook.validationErrorMsg)
            getattr(self, "CW_ADC_BOTH_FROM").set(self.priorValues["CW_ADC_BOTH_FROM"])
            return False
        return True

    def validate_CW_ADC_BOTH_TO(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValues["CW_ADC_BOTH_TO"] = p_entry_value
        elif (v_condition == "focusout"):
            if (self.getNumber(p_entry_value) == '0') | (self.validateADC(p_entry_value, 'LOW', self.CW_ADC_BOTH_FROM.get())):
                return True

            # if we reach this point, there is an error...
            self.log.printerror("timestamp", "CW BOTH keys pressed ADC ending value "+SettingsNotebook.validationErrorMsg)()
            getattr(self, "CW_ADC_BOTH_TO").set(self.priorValues["CW_ADC_BOTH_TO"])
            return False
        return True


    def validate_CW_Message_Change(self, p_entry_value, v_condition, w_entry_name):

        widgetHandle = self.root.nametowidget(w_entry_name)             # get pointer to the actual widget
        stringVarHandle = widgetHandle.cget("textvariable")             # use the widget ptr to get to the strvar
                                                                        # The symbol table entry for the stringvar
                                                                        # is used to save the prior value

        if v_condition == "focusin":
            self.priorValues[stringVarHandle] = p_entry_value.upper()        #   save the focus in value
            return True
        else:
            #
            #   we have a focus out condition
            #


            if (self.priorValues[stringVarHandle] == '') & (p_entry_value != ''):         #  New msg added


                newBytesUsed = len(p_entry_value) + 2
                #
                #   confirm that we have these bytes available
                #
                if int(self.CW_AUTO_REMAINING_BYTES.get()) >= newBytesUsed:

                    # Increment number of message count and make next message widget visible
                    self.CW_AUTO_COUNT.set(str(int(self.CW_AUTO_COUNT.get())+1))

                    # Increment number of bytes used - the + 2 is result of the added beg/end pointer for a new entry
                    # Then update remaining available bytes
                    self.CW_AUTO_BYTES_USED.set(str(int(self.CW_AUTO_BYTES_USED.get()) + newBytesUsed))
                    self.CW_AUTO_REMAINING_BYTES.set(str(int(self.CW_AUTO_REMAINING_BYTES.get()) - newBytesUsed))


                    # upperCase = widgetHandle.getvar(stringVarHandle).upper()        # get upper upper case version
                    upperCase = p_entry_value.upper()
                    widgetHandle.setvar(stringVarHandle, upperCase)                 # replace mixed case with upper

                    #if we don't have 25 messages, enable the next one too
                    if int(self.CW_AUTO_COUNT.get()) < CW_MSG_TOTAL :
                        getattr(self, "CW_MEMORY_KEYER_MSG" + CW_MSG_LABEL[int(self.CW_AUTO_COUNT.get())] + "_WIDGET").configure (state="enabled")
                    #
                    #   updated byte oounts, so can return True
                    #
                    return True

            else:                           # message modified, update used count
                # Increment number of bytes used - the + 2 is result of the added beg/end pointer for a new entry
                # Then update remaining available bytes

                newBytesUsed = len(p_entry_value) - len(self.priorValues[stringVarHandle])
                #
                #   confirm that we have these bytes available
                #
                if int(self.CW_AUTO_REMAINING_BYTES.get()) >= newBytesUsed:
                    self.CW_AUTO_BYTES_USED.set(str(int(self.CW_AUTO_BYTES_USED.get()) + newBytesUsed))
                    self.CW_AUTO_REMAINING_BYTES.set(str(int(self.CW_AUTO_REMAINING_BYTES.get()) - newBytesUsed))

                    upperCase = p_entry_value.upper()

                    widgetHandle.setvar(stringVarHandle, upperCase)                 # replace mixed case with upper
                    #
                    #   updated byte counts, and translated it to upper, so can return True
                    #
                    return True
            #
            #   If we have reached this point, then we did not have sufficient characters for the message. Log error message
            #   and restore original value
            #
            SettingsNotebook.validationErrorMsg = SettingsNotebook.error_Msgs["TOOMANYCWCHARS"].format(newBytesUsed,int(self.CW_AUTO_REMAINING_BYTES.get()))

            self.log.printerror("timestamp", SettingsNotebook.validationErrorMsg)
            widgetHandle.setvar(stringVarHandle, self.priorValues[stringVarHandle])                # restore prior value

            return False

    def validate_CHANNEL_FREQ(self, p_entry_value, v_condition, bandName):
        if (v_condition == "focusin"):
            self.priorValues["CHANNEL_"+ bandName] = p_entry_value
        if (self.validateNumber(p_entry_value, SettingsNotebook.FREQ['LOW'], SettingsNotebook.FREQ['HIGH'])):
            return True

        # if we reach this point, there is an error...
        self.log.printerror("timestamp", "Channel Freq " + SettingsNotebook.validationErrorMsg)
        getattr(self, "CHANNEL_"+bandName).set(self.priorValues["CHANNEL_"+bandName])
        return False

    def validate_CHANNEL_NAME(self, p_entry_value, v_condition, bandName):

        if (v_condition == "focusin"):
            self.priorValues["CHANNEL_"+bandName+"_NAME"] = p_entry_value
            getattr(self, "CHANNEL_"+bandName+"_NAME").set(p_entry_value.strip())
        if(self.checkLength(p_entry_value.strip(), SettingsNotebook.CHANNEL_WSPR_NAME_MAX) ):
            getattr(self, "CHANNEL_"+bandName+"_NAME").set(p_entry_value.strip())
            return True

        # if we reach this point, there is an error...
        self.log.printerror("timestamp", "Channel Name " + SettingsNotebook.validationErrorMsg)
        getattr(self, "CHANNEL_"+bandName+"_NAME").set(self.priorValues["CHANNEL_"+bandName+"_NAME"])
        return False

    def validate_CHANNEL_FREQ1_NAME(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_NAME(p_entry_value, v_condition, "FREQ1")

    def validate_CHANNEL_FREQ1(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ1")

    def validate_CHANNEL_FREQ2_NAME(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_NAME(p_entry_value, v_condition, "FREQ2")

    def validate_CHANNEL_FREQ2(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ2")

    def validate_CHANNEL_FREQ3_NAME(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_NAME(p_entry_value, v_condition, "FREQ3")

    def validate_CHANNEL_FREQ3(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ3")

    def validate_CHANNEL_FREQ4_NAME(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_NAME(p_entry_value, v_condition, "FREQ4")

    def validate_CHANNEL_FREQ4(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ4")

    def validate_CHANNEL_FREQ5_NAME(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_NAME(p_entry_value, v_condition, "FREQ5")

    def validate_CHANNEL_FREQ5(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ5")

    def validate_CHANNEL_FREQ6_NAME(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_NAME(p_entry_value, v_condition, "FREQ6")

    def validate_CHANNEL_FREQ6(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ6")

    def validate_CHANNEL_FREQ7_NAME(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_NAME(p_entry_value, v_condition, "FREQ7")

    def validate_CHANNEL_FREQ7(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ7")

    def validate_CHANNEL_FREQ8_NAME(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_NAME(p_entry_value, v_condition, "FREQ8")

    def validate_CHANNEL_FREQ8(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ8")

    def validate_CHANNEL_FREQ9_NAME(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_NAME(p_entry_value, v_condition, "FREQ9")

    def validate_CHANNEL_FREQ9(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ9")

    def validate_CHANNEL_FREQ10_NAME(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_NAME(p_entry_value, v_condition, "FREQ10")

    def validate_CHANNEL_FREQ10(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ10")

    def validate_CHANNEL_FREQ11(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ11")

    def validate_CHANNEL_FREQ12(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ12")

    def validate_CHANNEL_FREQ13(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ13")

    def validate_CHANNEL_FREQ14(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ14")

    def validate_CHANNEL_FREQ15(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ15")

    def validate_CHANNEL_FREQ16(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ16")

    def validate_CHANNEL_FREQ17(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ17")

    def validate_CHANNEL_FREQ18(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ18")

    def validate_CHANNEL_FREQ19(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ19")

    def validate_CHANNEL_FREQ20(self, p_entry_value, v_condition):
        return self.validate_CHANNEL_FREQ(p_entry_value, v_condition, "FREQ20")

    def validate_HAM_BAND_COUNT(self, p_entry_value, v_condition):
        if (v_condition == "focusin"):
            self.priorValues["HAM_BAND_COUNT"] = p_entry_value
        if (self.validateNumberRange (p_entry_value, SettingsNotebook.HAM_BAND_COUNT_BOUNDS['LOW'],
                                 SettingsNotebook.HAM_BAND_COUNT_BOUNDS['HIGH'], 'HIGH',
                                 str(SettingsNotebook.HAM_BAND_COUNT_BOUNDS['HIGH']+1))):
            return True

        # if we reach this point, there is an error...
        self.log.printerror("timestamp", "Number of Ham Bands must be between" + SettingsNotebook.validationErrorMsg)
        self.HAM_BAND_COUNT.set(self.priorValues["HAM_BAND_COUNT"])

        return False

    def validate_HAM_BAND_START(self, p_entry_value, v_condition, bandName):
        if (v_condition == "focusin"):
            self.priorValues["HAM_BAND_"+bandName+"_START"] = p_entry_value
        elif (v_condition == "focusout"):
            if (self.getNumber(p_entry_value) == '0') | (self.validateFREQKHZ(p_entry_value, 'HIGH', str(SettingsNotebook.FREQKHZ['HIGH']))):
                return True

            # if we reach this point, there is an error...
            self.log.printerror("timestamp", "Ham Band start freq " + SettingsNotebook.validationErrorMsg)
            getattr(self, "HAM_BAND_"+bandName+"_START").set(self.priorValues["HAM_BAND_"+bandName+"_START"])
            return False
        return True

    def validate_HAM_BAND_END(self, p_entry_value, v_condition, bandName):
        if (v_condition == "focusin"):
            self.priorValues["HAM_BAND_"+bandName+"_END"] = p_entry_value
        elif (v_condition == "focusout"):
            if (self.getNumber(p_entry_value) == '0') | (self.validateFREQKHZ(p_entry_value, 'LOW', getattr(self, "HAM_BAND_"+bandName+"_START").get())):
                return True

            # if we reach this point, there is an error...
            self.log.printerror("timestamp", "Ham Band end freq " + SettingsNotebook.validationErrorMsg)
            getattr(self, "HAM_BAND_"+bandName+"_END").set(self.priorValues["HAM_BAND_"+bandName+"_END"])
            return False
        return True

    def validate_HAM_BAND_RANGE1_START(self, p_entry_value, v_condition):
        return self.validate_HAM_BAND_START(p_entry_value, v_condition, "RANGE1")

    def validate_HAM_BAND_RANGE1_END(self, p_entry_value, v_condition):
        return self.validate_HAM_BAND_END(p_entry_value, v_condition, "RANGE1")


    def validate_HAM_BAND_RANGE2_START(self, p_entry_value, v_condition):
        return self.validate_HAM_BAND_START(p_entry_value, v_condition, "RANGE2")

    def validate_HAM_BAND_RANGE2_END(self, p_entry_value, v_condition):
        return self.validate_HAM_BAND_END(p_entry_value, v_condition, "RANGE2")


    def validate_HAM_BAND_RANGE3_START(self, p_entry_value, v_condition):
        return self.validate_HAM_BAND_START(p_entry_value, v_condition, "RANGE3")

    def validate_HAM_BAND_RANGE3_END(self, p_entry_value, v_condition):
        return self.validate_HAM_BAND_END(p_entry_value, v_condition, "RANGE3")


    def validate_HAM_BAND_RANGE4_START(self, p_entry_value, v_condition):
        return self.validate_HAM_BAND_START(p_entry_value, v_condition, "RANGE4")

    def validate_HAM_BAND_RANGE4_END(self, p_entry_value, v_condition):
        return self.validate_HAM_BAND_END(p_entry_value, v_condition, "RANGE4")


    def validate_HAM_BAND_RANGE5_START(self, p_entry_value, v_condition):
        return self.validate_HAM_BAND_START(p_entry_value, v_condition, "RANGE5")

    def validate_HAM_BAND_RANGE5_END(self, p_entry_value, v_condition):
        return self.validate_HAM_BAND_END(p_entry_value, v_condition, "RANGE5")


    def validate_HAM_BAND_RANGE6_START(self, p_entry_value, v_condition):
        return self.validate_HAM_BAND_START(p_entry_value, v_condition, "RANGE6")

    def validate_HAM_BAND_RANGE6_END(self, p_entry_value, v_condition):
        return self.validate_HAM_BAND_END(p_entry_value, v_condition, "RANGE6")


    def validate_HAM_BAND_RANGE7_START(self, p_entry_value, v_condition):
        return self.validate_HAM_BAND_START(p_entry_value, v_condition, "RANGE7")

    def validate_HAM_BAND_RANGE7_END(self, p_entry_value, v_condition):
        return self.validate_HAM_BAND_END(p_entry_value, v_condition, "RANGE7")


    def validate_HAM_BAND_RANGE8_START(self, p_entry_value, v_condition):
        return self.validate_HAM_BAND_START(p_entry_value, v_condition, "RANGE8")

    def validate_HAM_BAND_RANGE8_END(self, p_entry_value, v_condition):
         return self.validate_HAM_BAND_END(p_entry_value, v_condition, "RANGE8")


    def validate_HAM_BAND_RANGE9_START(self, p_entry_value, v_condition):
        return self.validate_HAM_BAND_START(p_entry_value, v_condition, "RANGE9")

    def validate_HAM_BAND_RANGE9_END(self, p_entry_value, v_condition):
        return self.validate_HAM_BAND_END(p_entry_value, v_condition, "RANGE9")


    def validate_HAM_BAND_RANGE10_START(self, p_entry_value, v_condition):
        return self.validate_HAM_BAND_START(p_entry_value, v_condition, "RANGE10")

    def validate_HAM_BAND_RANGE10_END(self, p_entry_value, v_condition):
        return self.validate_HAM_BAND_END(p_entry_value, v_condition, "RANGE10")

    def CUST_LPF_SELECTION_CB(self, *args):
        if (self.CUST_LPF_ENABLED.get() == 'OFF'):
            self.CUSTOM_BANDPASS_FILTER_Frame.forget()
        elif (self.CUST_LPF_ENABLED.get() == 'STANDARD'):
            self.CUSTOM_BANDPASS_EXTENDED_Frame.forget()
            self.CUSTOM_BANDPASS_FILTER_Frame.pack()
        else:
            self.CUSTOM_BANDPASS_EXTENDED_Frame.pack()
            self.CUSTOM_BANDPASS_FILTER_Frame.pack()


    def validate_CUST_LPF_FILTER1_ENDFREQ(self, p_entry_value, v_condition):
        if ( p_entry_value != '') & (p_entry_value != '0'):
            self.CUST_LPF_FILTER2_BEGFREQ.set(str(int(p_entry_value)))
            if (self.CUST_LPF_FILTER2_BEGFREQ.get() > self.CUST_LPF_FILTER2_ENDFREQ.get()):
                self.CUST_LPF_FILTER2_ENDFREQ.set(str(int(p_entry_value)-1))
        return True

    def validate_CUST_LPF_FILTER2_ENDFREQ(self, p_entry_value, v_condition):
        if ( p_entry_value == ''):
            self.CUST_LPF_FILTER2_BEGFREQ.set("")
        elif (p_entry_value != '0'):
            self.CUST_LPF_FILTER3_BEGFREQ.set(str(int(p_entry_value)))
            if (self.CUST_LPF_FILTER3_BEGFREQ.get() > self.CUST_LPF_FILTER3_ENDFREQ.get()):
                self.CUST_LPF_FILTER3_ENDFREQ.set(str(int(p_entry_value)-1))

        return True


    def validate_CUST_LPF_FILTER3_ENDFREQ(self, p_entry_value, v_condition):
        if ( p_entry_value == ''):
            self.CUST_LPF_FILTER3_BEGFREQ.set("")
        elif (p_entry_value != '0'):
            self.CUST_LPF_FILTER4_BEGFREQ.set(str(int(p_entry_value)))
            if (self.CUST_LPF_FILTER4_BEGFREQ.get() > self.CUST_LPF_FILTER4_ENDFREQ.get()):
                self.CUST_LPF_FILTER4_ENDFREQ.set(str(int(p_entry_value)-1))

        return True

    def validate_CUST_LPF_FILTER4_ENDFREQ(self, p_entry_value, v_condition):
        if ( p_entry_value == ''):
            self.CUST_LPF_FILTER4_BEGFREQ.set("")
        elif (p_entry_value != '0'):
            self.CUST_LPF_FILTER5_BEGFREQ.set(str(int(p_entry_value)))
            if (self.CUST_LPF_FILTER5_BEGFREQ.get() > self.CUST_LPF_FILTER5_ENDFREQ.get()):
                self.CUST_LPF_FILTER5_ENDFREQ.set(str(int(p_entry_value)-1))

        return True

    def validate_CUST_LPF_FILTER5_ENDFREQ(self, p_entry_value, v_condition):
        if ( p_entry_value == ''):
            self.CUST_LPF_FILTER5_BEGFREQ.set("")
        elif (p_entry_value != '0'):
            self.CUST_LPF_FILTER6_BEGFREQ.set(str(int(p_entry_value)))
            if (self.CUST_LPF_FILTER6_BEGFREQ.get() > self.CUST_LPF_FILTER6_ENDFREQ.get()):
                self.CUST_LPF_FILTER6_ENDFREQ.set(str(int(p_entry_value)-1))

        return True

    def validate_CUST_LPF_FILTER6_ENDFREQ(self, p_entry_value, v_condition):
        if ( p_entry_value == ''):
            self.CUST_LPF_FILTER6_BEGFREQ.set("")
        elif  (p_entry_value != '0'):
            self.CUST_LPF_FILTER7_BEGFREQ.set(str(int(p_entry_value)))
            if (self.CUST_LPF_FILTER7_BEGFREQ.get() > self.CUST_LPF_FILTER7_ENDFREQ.get()):
                self.CUST_LPF_FILTER7_ENDFREQ.set(str(int(p_entry_value)-1))
        return True

    def validate_CUST_LPF_FILTER7_ENDFREQ(self, p_entry_value, v_condition):
        if ( p_entry_value == ''):
            self.CUST_LPF_FILTER7_BEGFREQ.set("")
        return True


    ##############################
    #  Functional Callbacks
    ##############################


    def Reset_Master_Cal_To_Factory(self):
        self.MASTER_CAL.set(self.FACTORY_VALUES_MASTER_CAL.get())

    def Copy_Master_Cal_Over_Factory_Value(self):
        self.FACTORY_VALUES_MASTER_CAL.set(self.MASTER_CAL.get())

    def Reset_SSB_BFO_To_Factory(self):
        self.USB_CAL.set(self.FACTORY_VALUES_USB_CAL.get())

    def Copy_SSB_BFO_Over_Factory_Value(self):
        self.FACTORY_VALUES_USB_CAL.set(self.USB_CAL.get())

    def toggleExtendedChannels(self):
        if self.toggleExtendedChannelsCheckBox.get() == "1":
            self.Extended_Channel_Frame.pack(anchor="w", side="top")
        else:
            self.Extended_Channel_Frame.forget()

    def CW_Auto_Msg_Cleanup_CB(self):
        # this function just deletes empty CW Autokey Messages and frees up space
        #
        #   save starting positions to adjust used characters and disable extra messages

        msgCount = int(self.CW_AUTO_COUNT.get())
        numEmptyMsgsFound=0

        i = 0
        # Primary loop to go thru all active messages
        while i < msgCount:
            if (getattr(self, "CW_MEMORY_KEYER_MSG" + CW_MSG_LABEL[i]).get() == ''):
                #   Found an empty messsage, start moving the rest up
                numEmptyMsgsFound += 1

                j=i
                while (j < msgCount) & (j < CW_MSG_TOTAL-1) :               # J<CW_MSG_TOTAL-1 is boundary condition for last msg in list
                    getattr(self, "CW_MEMORY_KEYER_MSG" + CW_MSG_LABEL[j]).set(getattr(self, "CW_MEMORY_KEYER_MSG" + CW_MSG_LABEL[j+1]).get())
                    j +=1
                #
                #   zap contents of last message as it has been moved down
                #   for now set it to disable, will enable the last one at the end of processing
                #
                getattr(self, "CW_MEMORY_KEYER_MSG" + CW_MSG_LABEL[j]).set('')
                getattr(self, "CW_MEMORY_KEYER_MSG" + CW_MSG_LABEL[j]+"_WIDGET").configure(state='disabled')

                msgCount -= 1                       # one fewer message to look at
            else:
                i+=1            # not incremented in case of a move down. Only bump the pointer if the message is non-empty

        #   At this point, we have moved up all the non-empty messages and we just need to do some cleanup
        #   First delete 2 bytes used (and add 2 more available) for every empty slot we processed

        i = 0
        while i < numEmptyMsgsFound:
            # j = int(self.CW_AUTO_COUNT.get()) - i
#            print(CW_MSG_LABEL[j], j, i)

            #   Update count of bytes used (2 fewer since we recovered an empty slot and dont need beg end pointers)
            self.CW_AUTO_BYTES_USED.set(str(int(self.CW_AUTO_BYTES_USED.get()) - 2))
            self.CW_AUTO_REMAINING_BYTES.set(str(int(self.CW_AUTO_REMAINING_BYTES.get()) + 2))
            i += 1
        #
        #   Update message count
        #
        self.CW_AUTO_COUNT.set(str(int(self.CW_AUTO_COUNT.get()) - numEmptyMsgsFound))

        #
        #   Finally, (re)enable last location for input
        #
        getattr(self, "CW_MEMORY_KEYER_MSG" + CW_MSG_LABEL[int(self.CW_AUTO_COUNT.get())]+"_WIDGET").configure(state='enabled')


    def autoInputRegion1(self):

        self.HAM_BAND_COUNT.set(9)

        self.HAM_BAND_RANGE1_START.set("1.810")
        self.HAM_BAND_RANGE1_END.set("2.000")

        self.HAM_BAND_RANGE2_START.set("3.500")
        self.HAM_BAND_RANGE2_END.set("3.800")

        self.HAM_BAND_RANGE3_START.set("7.000")
        self.HAM_BAND_RANGE3_END.set("7.200")

        self.HAM_BAND_RANGE4_START.set("10.100")
        self.HAM_BAND_RANGE4_END.set("10.150")

        self.HAM_BAND_RANGE5_START.set("14.000")
        self.HAM_BAND_RANGE5_END.set("14.350")

        self.HAM_BAND_RANGE6_START.set("18.068")
        self.HAM_BAND_RANGE6_END.set("18.168")

        self.HAM_BAND_RANGE7_START.set("21.000")
        self.HAM_BAND_RANGE7_END.set("21.450")

        self.HAM_BAND_RANGE8_START.set("24.850")
        self.HAM_BAND_RANGE8_END.set("24.990")

        self.HAM_BAND_RANGE9_START.set("28.000")
        self.HAM_BAND_RANGE9_END.set("29.700")

        self.HAM_BAND_RANGE10_START.set('')
        self.HAM_BAND_RANGE10_END.set('')


    def autoInputRegion2(self):

        self.HAM_BAND_COUNT.set(10)

        self.HAM_BAND_RANGE1_START.set("1.810")
        self.HAM_BAND_RANGE1_END.set("2.000")

        self.HAM_BAND_RANGE2_START.set("3.500")
        self.HAM_BAND_RANGE2_END.set("4.000")

        self.HAM_BAND_RANGE3_START.set("5.330")
        self.HAM_BAND_RANGE3_END.set("5.404")

        self.HAM_BAND_RANGE4_START.set("7.000")
        self.HAM_BAND_RANGE4_END.set("7.300")

        self.HAM_BAND_RANGE5_START.set("10.100")
        self.HAM_BAND_RANGE5_END.set("10.150")

        self.HAM_BAND_RANGE6_START.set("14.000")
        self.HAM_BAND_RANGE6_END.set("14.350")

        self.HAM_BAND_RANGE7_START.set("18.068")
        self.HAM_BAND_RANGE7_END.set("18.168")

        self.HAM_BAND_RANGE8_START.set("21.000")
        self.HAM_BAND_RANGE8_END.set(21450)

        self.HAM_BAND_RANGE9_START.set("24.850")
        self.HAM_BAND_RANGE9_END.set("24.990")

        self.HAM_BAND_RANGE10_START.set("28.000")
        self.HAM_BAND_RANGE10_END.set("29.700")

    def autoInputRegion3(self):

        self.HAM_BAND_COUNT.set(10)

        self.HAM_BAND_RANGE1_START.set("1.800")
        self.HAM_BAND_RANGE1_END.set("1.825")

        self.HAM_BAND_RANGE2_START.set("3.500")
        self.HAM_BAND_RANGE2_END.set("3.550")

        self.HAM_BAND_RANGE3_START.set("3.790")
        self.HAM_BAND_RANGE3_END.set("3.800")

        self.HAM_BAND_RANGE4_START.set("7.000")
        self.HAM_BAND_RANGE4_END.set("7.200")

        self.HAM_BAND_RANGE5_START.set("10.100")
        self.HAM_BAND_RANGE5_END.set("10.150")

        self.HAM_BAND_RANGE6_START.set("14.000")
        self.HAM_BAND_RANGE6_END.set("14.350")

        self.HAM_BAND_RANGE7_START.set("18.068")
        self.HAM_BAND_RANGE7_END.set("18.168")

        self.HAM_BAND_RANGE8_START.set("21.000")
        self.HAM_BAND_RANGE8_END.set("21.450")

        self.HAM_BAND_RANGE9_START.set("24.850")
        self.HAM_BAND_RANGE9_END.set("24.990")

        self.HAM_BAND_RANGE10_START.set("28.000")
        self.HAM_BAND_RANGE10_END.set("29.700")

    def CUST_LPF_FILTER_CONTROL(self, filter):

        theFilter = getattr(self,"CUST_LPF_"+filter+"_CONTROL")
        theFilter.set('')

        for dataline in LPF_CTRL_SELECT:
            if (dataline != '0') & (dataline != "NONE"):
                checkBoxValue = getattr(self,"CUST_LPF_"+filter+"_CONTROL_"+dataline).get()
                if (checkBoxValue != '0') & (checkBoxValue != '') :
                    theFilter.set(theFilter.get() + "," + checkBoxValue)
        if (len(theFilter.get()) == 0):
            theFilter.set("NONE")
        elif (theFilter.get()[0] == ','):
            theFilter.set(theFilter.get()[1:])      #delete leading comma
        print(filter, " CB called=", theFilter.get() )

    def CUST_LPF_FILTER1_CONTROL_CB(self):
        self.CUST_LPF_FILTER_CONTROL("FILTER1")

    def CUST_LPF_FILTER2_CONTROL_CB(self):
        self.CUST_LPF_FILTER_CONTROL("FILTER2")

    def CUST_LPF_FILTER3_CONTROL_CB(self):
        self.CUST_LPF_FILTER_CONTROL("FILTER3")

    def CUST_LPF_FILTER4_CONTROL_CB(self):
        self.CUST_LPF_FILTER_CONTROL("FILTER4")

    def CUST_LPF_FILTER5_CONTROL_CB(self):
        self.CUST_LPF_FILTER_CONTROL("FILTER5")

    def CUST_LPF_FILTER6_CONTROL_CB(self):
        self.CUST_LPF_FILTER_CONTROL("FILTER6")

    def CUST_LPF_FILTER7_CONTROL_CB(self):
        self.CUST_LPF_FILTER_CONTROL("FILTER7")

    def new_Default_Tuning_Step(self, *args):
        self.TUNING_STEP_INDEX.set(SettingsNotebook.newTuningSteps.index(self.TUNING_STEP_INDEX_VALUE.get())+1)

    def Refresh_Tuning_Steps(self):
        SettingsNotebook.newTuningSteps = (self.TUNING_STEP1.get(), self.TUNING_STEP2.get(), self.TUNING_STEP3.get(), self.TUNING_STEP4.get(), self.TUNING_STEP5.get())
        self.TUNING_STEP_INDEX_VALUE_WIDGET['values'] = SettingsNotebook.newTuningSteps

        if (int(self.TUNING_STEP_INDEX.get()) <1) | (int(self.TUNING_STEP_INDEX.get()) > 5):        # protect against bad data
            self.TUNING_STEP_INDEX_VALUE_WIDGET.current(3)
        else:

            self.TUNING_STEP_INDEX_VALUE_WIDGET.current(int(self.TUNING_STEP_INDEX.get())-1)
        self.new_Default_Tuning_Step()

    def Tuning_Steps_Set_Common(self):
        i = self.Tuning_Steps_Common.get()
        if int(i) < 5:
            self.TUNING_STEP1.set(SettingsNotebook.PREDEFINED_TUNING_STEPS[i][0])
            self.TUNING_STEP2.set(SettingsNotebook.PREDEFINED_TUNING_STEPS[i][1])
            self.TUNING_STEP3.set(SettingsNotebook.PREDEFINED_TUNING_STEPS[i][2])
            self.TUNING_STEP4.set(SettingsNotebook.PREDEFINED_TUNING_STEPS[i][3])
            self.TUNING_STEP5.set(SettingsNotebook.PREDEFINED_TUNING_STEPS[i][4])

            self.TUNING_STEP1_WIDGET.configure(state='disabled')
            self.TUNING_STEP2_WIDGET.configure(state='disabled')
            self.TUNING_STEP3_WIDGET.configure(state='disabled')
            self.TUNING_STEP4_WIDGET.configure(state='disabled')
            self.TUNING_STEP5_WIDGET.configure(state='disabled')
        else:
            self.TUNING_STEP1_WIDGET.configure(state='normal')
            self.TUNING_STEP2_WIDGET.configure(state='normal')
            self.TUNING_STEP3_WIDGET.configure(state='normal')
            self.TUNING_STEP4_WIDGET.configure(state='normal')
            self.TUNING_STEP5_WIDGET.configure(state='normal')

        self.Refresh_Tuning_Steps()
    def Set_LPF_Beginning_Freq(self):
        if (self.CUST_LPF_FILTER1_ENDFREQ.get() != None) & (self.CUST_LPF_FILTER1_ENDFREQ.get() != ''):
            self.CUST_LPF_FILTER2_BEGFREQ.set(str(int(self.CUST_LPF_FILTER1_ENDFREQ.get())))

        if (self.CUST_LPF_FILTER2_ENDFREQ.get() != None) & (self.CUST_LPF_FILTER2_ENDFREQ.get() != ''):
            self.CUST_LPF_FILTER3_BEGFREQ.set(str(int(self.CUST_LPF_FILTER2_ENDFREQ.get())))

        if (self.CUST_LPF_FILTER3_ENDFREQ.get() != None) & (self.CUST_LPF_FILTER3_ENDFREQ.get() != ''):
            self.CUST_LPF_FILTER4_BEGFREQ.set(str(int(self.CUST_LPF_FILTER3_ENDFREQ.get())))

        if (self.CUST_LPF_FILTER4_ENDFREQ.get() != None) & (self.CUST_LPF_FILTER4_ENDFREQ.get() != ''):
            self.CUST_LPF_FILTER5_BEGFREQ.set(str(int(self.CUST_LPF_FILTER4_ENDFREQ.get())))

        if (self.CUST_LPF_FILTER5_ENDFREQ.get() != None) & (self.CUST_LPF_FILTER5_ENDFREQ.get() != ''):
            self.CUST_LPF_FILTER6_BEGFREQ.set(str(int(self.CUST_LPF_FILTER5_ENDFREQ.get())))

        if (self.CUST_LPF_FILTER6_ENDFREQ.get() != None) & (self.CUST_LPF_FILTER6_ENDFREQ.get() != ''):
            self.CUST_LPF_FILTER7_BEGFREQ.set(str(int(self.CUST_LPF_FILTER6_ENDFREQ.get())))

    def Set_LPF_Control_Lines(self):
        # loop thru all control lines and set checkboxes
        i=1
        while i<8:
            theControlLine=getattr(self,"CUST_LPF_FILTER"+str(i)+"_CONTROL").get()
            for dataline in LPF_CTRL_SELECT:
                if dataline != "NONE":
                    if dataline in theControlLine:
                        getattr(self, "CUST_LPF_FILTER" + str(i) +"_CONTROL_" + dataline).set(dataline)
            i += 1

    def enable_CW_Widgets(self):
        i = 0

        while i < int(self.CW_AUTO_COUNT.get()):
            #   Enable associate entry field
            getattr(self, "CW_MEMORY_KEYER_MSG" + CW_MSG_LABEL[i]  + "_WIDGET").configure (state="enabled")
            #   Calculate initial bytes used + 2 is for the bytes used to set begin/end
            self.CW_AUTO_BYTES_USED.set(str(int(self.CW_AUTO_BYTES_USED.get()) +
                                       len(getattr(self, "CW_MEMORY_KEYER_MSG" + CW_MSG_LABEL[i]).get())
                                       + 2))
            i+=1

        #if we don't have 25 messages, enable the next one too
        if i < CW_MSG_TOTAL :
            getattr(self, "CW_MEMORY_KEYER_MSG" + str(i) + "_WIDGET").configure (state="enabled")



    def load_Recommended_ADC_CW_Values(self):
        pass
    #st start 0, 50
    #dot start 301, 600
    #dash start 601, 700
    #both start  51, 300


    def setNotebook(self, valueTree):

        self.userModroot = valueTree

        for userSetting in self.userModroot.findall('.//SETTING'):
            name = userSetting.get("NAME")

            if name in SettingsNotebook.readyToGo:
                if userSetting.find("value").text != None:
                    getattr(self, name).set(userSetting.find("value").text)
                else:
                    getattr(self, name).set("")

                toolTip = userSetting.find("tooltip").text

                if toolTip != None:
                    tooltip.create(getattr(self, name + "_WIDGET"), toolTip)
                    # Check for special processing
            else:
                if(DEBUGAPP):
                    print("Not ready=",  name)


        # Post process some special cases

        # Tuning steps prep
        self.TUNING_STEP_INDEX_VALUE.trace_add('write',self.new_Default_Tuning_Step)
        self.Refresh_Tuning_Steps()
        self.TUNING_STEP_INDEX_WIDGET.grid_forget()
        self.TUNING_STEP1_WIDGET.configure(state='normal')
        self.TUNING_STEP2_WIDGET.configure(state='normal')
        self.TUNING_STEP3_WIDGET.configure(state='normal')
        self.TUNING_STEP4_WIDGET.configure(state='normal')
        self.TUNING_STEP5_WIDGET.configure(state='normal')

        # Enable CW Message Widgets
        self.enable_CW_Widgets()

        # LPF Beginning Frequencies
        self.Set_LPF_Beginning_Freq()

        # LPF Control Lines
        self.Set_LPF_Control_Lines()



        # Set maximum available bytes
        # Length of QSO call sign
        self.CW_AUTO_REMAINING_BYTES.set(str(EEPROMSIZE - 1 - len(self.QSO_CALLSIGN.get())
                                             - CW_MEMORY_KEYER_BUFFER_START - int(self.CW_AUTO_BYTES_USED.get())))



        #   Clear hidden widgets
        for widget in SettingsNotebook.hideOnStartup:
            getattr(self, widget).forget()

        self.enableNotebook()

    def getNotebook(self):

        for userSetting in self.userModroot.findall('.//SETTING'):
            name = userSetting.get("NAME")

            if name in SettingsNotebook.readyToGo:
                if(DEBUGAPP):
                    print("name=", name)
                userSetting.find("value").text=getattr(self, name).get()
            else:
                if(DEBUGAPP):
                    print("Not ready=",  name)

        return self.userModroot

    def setLog(self, log ):                     # this method is called to tell object where to write the log
        self.log = log

    def enableNotebook(self):
        self.root.grid(row=2, column=0, padx=15, sticky='ewns')

    def disableNotebook(self):
        self.root.forget()

    def runI2CScanner(self):
        i2cScanner = I2Cscanner(self)

    def runADCScanner(self):
        adcScanner = ADCscanner (self)

    def runSmeterAssistant(self):
        smeterAssistant = SmeterWizard(self)





