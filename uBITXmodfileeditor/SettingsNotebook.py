from tkinter import *
from settingsnotebookwidget import SettingsnotebookWidget

class SettingsNotebook(SettingsnotebookWidget):
    #   Class variables
    #
    #   error message will be set when ever validation fails
    validationErrorMsg = ''

    #   Error messages common to all validation
    error_Msgs = {
        "NOTINMIDDLE":"Value must be {:,} to {:,}, prior value restored",
        "NOTANUMBER":"{} is not a valid number, prior value restored",
        "NOTLOWER":"Value must be lower than {:,}, prior value restored",
        "NOTHIGHER":"Value must be higher than {:,}, prior value restored",
        "STRINGTOOLONG": "Entry longer than {}, prior value restored"
    }

    # Value Constraints
    ADC = {'LOW':0, 'HIGH':1023}            # Min/Max for Analog to Digital read - used for cw keys, etc.
    FREQ ={'LOW':0, 'HIGH':60000000}            # Min/Max for valid frequencies.
    FREQKHZ = {'LOW':0, 'HIGH':60000}
    MASTER_CAL_BOUNDS = {'LOW':-500000, 'HIGH': 500000}
    USB_CAL_BOUNDS = {'LOW':0, 'HIGH': 20000000}
    CW_CAL_BOUNDS = {'LOW':0, 'HIGH': 20000000}
    CW_SIDETONE_BOUNDS = {'LOW':100, 'HIGH': 2000}
    CW_SPEED_WPM_BOUNDS = {'LOW':1, 'HIGH': 250}
    CW_START_MS_BOUNDS = {'LOW':0, 'HIGH': 5000}
    CW_DELAY_MS_BOUNDS = {'LOW':0, 'HIGH': 10000}
    CHANNEL_WSPR_NAME_MAX = 5
    USER_CALLSIGN_BOUNDS = {'HIGH':18 }
    HAM_BAND_COUNT_BOUNDS = {'LOW':0, 'HIGH':10}

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
                if (self.getNumber(x) <= int(target )):          # Target is supposed to be greater than X
                    return True
                else:
                    SettingsNotebook.validationErrorMsg = SettingsNotebook.error_Msgs["NOTLOWER"].format(int(target))
                    return False
            elif (self.getNumber(x) >= int(target)):             # Target is supposed to be less than X
                return True
            else:
                SettingsNotebook.validationErrorMsg = SettingsNotebook.error_Msgs["NOTHIGHER"].format(int(target))
                return False
        else:
            return False            # Error message already set by validateNumber


    ##############################
    #  Validation functions
    ##############################

    def validate_MASTER_CAL(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if(self.validateNumber(p_entry_value,  SettingsNotebook.MASTER_CAL_BOUNDS['LOW'],  SettingsNotebook.MASTER_CAL_BOUNDS['HIGH'])):
            self.MASTER_CAL_INVALID_WIDGET.forget()
            return True
        else:
            self.MASTER_CAL_INVALID.set(SettingsNotebook.validationErrorMsg)
            self.MASTER_CAL_INVALID_WIDGET.pack()
            self.MASTER_CAL.set(self.priorValue)
            return False

    def validate_USB_CAL(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if(self.validateNumber(p_entry_value, SettingsNotebook.USB_CAL_BOUNDS['LOW'], SettingsNotebook.USB_CAL_BOUNDS['HIGH'])):
            self.USB_CAL_INVALID_WIDGET.forget()
            return True
        else:
            self.USB_CAL_INVALID.set(SettingsNotebook.validationErrorMsg)
            self.USB_CAL_INVALID_WIDGET.pack()
            self.USB_CAL.set(self.priorValue)
            return False

    def validate_CW_CAL(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if(self.validateNumber(p_entry_value,SettingsNotebook.CW_CAL_BOUNDS['LOW'], SettingsNotebook.CW_CAL_BOUNDS['HIGH'])):
            self.CW_CAL_INVALID_WIDGET.forget()
            return True
        else:
            self.CW_CAL_INVALID.set(SettingsNotebook.validationErrorMsg)
            self.CW_CAL_INVALID_WIDGET.pack()
            self.CW_CAL.set(self.priorValue)
            return False

    def validate_CW_SIDETONE(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if(self.validateNumber(p_entry_value,SettingsNotebook.CW_SIDETONE_BOUNDS['LOW'], SettingsNotebook.CW_SIDETONE_BOUNDS['HIGH'])):
            self.CW_SIDETONE_INVALID_WIDGET.forget()
            return True
        else:
            self.CW_SIDETONE_INVALID.set(SettingsNotebook.validationErrorMsg)
            self.CW_SIDETONE_INVALID_WIDGET.pack()
            self.CW_SIDETONE.set(self.priorValue)
            return False

    def validate_CW_SPEED_WPM(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if(self.validateNumber(p_entry_value,SettingsNotebook.CW_SPEED_WPM_BOUNDS['LOW'], SettingsNotebook.CW_SPEED_WPM_BOUNDS['HIGH'])):
            self.CW_SPEED_WPM_INVALID_WIDGET.forget()
            return True
        else:
            self.CW_SPEED_WPM_INVALID.set(SettingsNotebook.validationErrorMsg)
            self.CW_SPEED_WPM_INVALID_WIDGET.pack()
            self.CW_SPEED_WPM.set(self.priorValue)
            return False

    def validate_CW_DELAY_MS(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if(self.validateNumber(p_entry_value,SettingsNotebook.CW_DELAY_MS_BOUNDS['LOW'], SettingsNotebook.CW_DELAY_MS_BOUNDS['HIGH'])):
            self.CW_DELAY_MS_INVALID_WIDGET.forget()
            return True
        else:
            self.CW_DELAY_MS_INVALID.set(SettingsNotebook.validationErrorMsg)
            self.CW_DELAY_MS_INVALID_WIDGET.pack()
            self.CW_DELAY_MS.set(self.priorValue)
            return False

    def validate_CW_START_MS(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if(self.validateNumber(p_entry_value,SettingsNotebook.CW_START_MS_BOUNDS['LOW'], SettingsNotebook.CW_START_MS_BOUNDS['HIGH'])):
            self.CW_START_MS_INVALID_WIDGET.forget()
            return True
        else:
            self.CW_START_MS_INVALID.set(SettingsNotebook.validationErrorMsg)
            self.CW_START_MS_INVALID_WIDGET.pack()
            self.CW_START_MS.set(self.priorValue)
            return False

    def validate_USER_CALLSIGN(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if(self.checkLength(p_entry_value, SettingsNotebook.USER_CALLSIGN_BOUNDS['HIGH']) ):
            self.USER_CALLSIGN_INVALID_WIDGET.forget()
            return True
        else:
            self.USER_CALLSIGN_INVALID.set(SettingsNotebook.validationErrorMsg)
            self.USER_CALLSIGN_INVALID_WIDGET.pack()
            self.USER_CALLSIGN.set(self.priorValue)
            return False


    def validate_CW_ADC_ST_FROM(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if (self.validateADC(p_entry_value, 'HIGH', self.CW_ADC_ST_TO.get())):
            self.CW_ADC_ST_INVALID_WIDGET.forget()
            return True

        # if we reach this point, there is an error...
        self.CW_ADC_ST_INVALID.set(SettingsNotebook.validationErrorMsg)
        self.CW_ADC_ST_INVALID_WIDGET.pack()
        self.CW_ADC_ST_FROM.set(self.priorValue)
        return False

    def validate_CW_ADC_ST_TO_WIDGET(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if (self.validateADC(p_entry_value, 'LOW', self.CW_ADC_ST_FROM.get())):
                self.CW_ADC_ST_INVALID_WIDGET.forget()
                return True

        # if we reach this point, there is an error...
        self.CW_ADC_ST_INVALID.set(SettingsNotebook.validationErrorMsg)
        self.CW_ADC_ST_INVALID_WIDGET.pack()
        self.CW_ADC_ST_TO.set(self.priorValue)
        return False


    def validate_CW_ADC_DOT_FROM(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if (self.validateADC(p_entry_value, 'HIGH', self.CW_ADC_DOT_TO.get())):
            self.CW_ADC_DOT_INVALID_WIDGET.forget()
            return True

        # if we reach this point, there is an error...
        self.CW_ADC_DOT_INVALID.set(SettingsNotebook.validationErrorMsg)
        self.CW_ADC_DOT_INVALID_WIDGET.pack()
        self.CW_ADC_DOT_FROM.set(self.priorValue)
        return False


    def validate_CW_ADC_DOT_TO(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if (self.validateADC(p_entry_value, 'LOW', self.CW_ADC_DOT_FROM.get())):
            self.CW_ADC_DOT_INVALID_WIDGET.forget()
            return True

        # if we reach this point, there is an error...
        self.CW_ADC_DOT_INVALID.set(SettingsNotebook.validationErrorMsg)
        self.CW_ADC_DOT_INVALID_WIDGET.pack()
        self.CW_ADC_DOT_TO.set(self.priorValue)
        return False

    def validate_CW_ADC_DASH_FROM(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if (self.validateADC(p_entry_value, 'HIGH', self.CW_ADC_DASH_TO.get())):
            self.CW_ADC_DASH_INVALID_WIDGET.forget()
            return True

        # if we reach this point, there is an error...
        self.CW_ADC_DASH_INVALID.set(SettingsNotebook.validationErrorMsg)
        self.CW_ADC_DASH_INVALID_WIDGET.pack()
        self.CW_ADC_DASH_FROM.set(self.priorValue)
        return False

    def validate_CW_ADC_DASH_TO(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if (self.validateADC(p_entry_value, 'LOW', self.CW_ADC_DASH_FROM.get())):
            self.CW_ADC_DASH_INVALID_WIDGET.forget()
            return True

        # if we reach this point, there is an error...
        self.CW_ADC_DASH_INVALID.set(SettingsNotebook.validationErrorMsg)
        self.CW_ADC_DASH_INVALID_WIDGET.pack()
        self.CW_ADC_DASH_TO.set(self.priorValue)
        return False

    def validate_CW_ADC_BOTH_FROM(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if (self.validateADC(p_entry_value, 'HIGH', self.CW_ADC_BOTH_TO.get())):
            self.CW_ADC_BOTH_INVALID_WIDGET.forget()
            return True

        # if we reach this point, there is an error...
        self.CW_ADC_BOTH_INVALID.set(SettingsNotebook.validationErrorMsg)
        self.CW_ADC_BOTH_INVALID_WIDGET.pack()
        self.CW_ADC_BOTH_FROM.set(self.priorValue)
        return False

    def validate_CW_ADC_BOTH_TO(self, p_entry_value, v_condition):

        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if (self.validateADC(p_entry_value, 'LOW', self.CW_ADC_BOTH_FROM.get())):
            self.CW_ADC_BOTH_INVALID_WIDGET.forget()
            return True

        # if we reach this point, there is an error...
        self.CW_ADC_BOTH_INVALID.set(SettingsNotebook.validationErrorMsg)
        self.CW_ADC_BOTH_INVALID_WIDGET.pack()
        self.CW_ADC_BOTH_TO.set(self.priorValue)
        return False

    def validate_CHANNEL_FREQ(self, p_entry_value, v_condition, bandName):
        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if (self.validateNumber(p_entry_value, SettingsNotebook.FREQ['LOW'], SettingsNotebook.FREQ['HIGH'])):
            getattr(self, "CHANNEL_"+bandName+"_INVALID_WIDGET").forget()
            return True

        # if we reach this point, there is an error...
        getattr(self, "CHANNEL_"+bandName+"_INVALID").set(SettingsNotebook.validationErrorMsg)
        getattr(self, "CHANNEL_"+bandName+"_INVALID_WIDGET").pack()
        getattr(self, "CHANNEL_"+bandName).set(self.priorValue)
        return False

    def validate_CHANNEL_NAME(self, p_entry_value, v_condition, bandName):

        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
            getattr(self, "CHANNEL_"+bandName+"_NAME").set(self.priorValue.strip())
        if(self.checkLength(p_entry_value.strip(), SettingsNotebook.CHANNEL_WSPR_NAME_MAX) ):
            getattr(self, "CHANNEL_"+bandName+"_NAME").set(p_entry_value.strip())
            getattr(self, "CHANNEL_"+bandName+"_INVALID_WIDGET").forget()
            return True

        getattr(self, "CHANNEL_"+bandName+"_INVALID").set(SettingsNotebook.validationErrorMsg)
        getattr(self, "CHANNEL_"+bandName+"_INVALID_WIDGET").pack()
        getattr(self, "CHANNEL_"+bandName+"_NAME").set(self.priorValue)
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

    def clearHAM_BAND_Error_MSGS(self):
        self.HAM_BAND_COUNT_INVALID_WIDGET.forget()
        for i in range(1,11):
            getattr(self, "HAM_BAND_RANGE"+str(i)+"_INVALID_WIDGET").forget()

    def validate_HAM_BAND_COUNT(self, p_entry_value, v_condition):
        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if (self.validateNumberRange (p_entry_value, SettingsNotebook.HAM_BAND_COUNT_BOUNDS['LOW'],
                                 SettingsNotebook.HAM_BAND_COUNT_BOUNDS['HIGH'], 'HIGH',
                                 SettingsNotebook.HAM_BAND_COUNT_BOUNDS['HIGH']+1)):
            self.HAM_BAND_COUNT_INVALID_WIDGET.forget()
            return True

        # if we reach this point, there is an error...
        self.HAM_BAND_COUNT_INVALID.set(SettingsNotebook.validationErrorMsg)
        self.HAM_BAND_COUNT_INVALID_WIDGET.pack()
        self.HAM_BAND_COUNT.set(self.priorValue)
        return False

    def validate_HAM_BAND_START(self, p_entry_value, v_condition, bandName):
        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if (self.validateFREQKHZ(p_entry_value, 'HIGH', getattr(self, "HAM_BAND_"+bandName+"_END").get())):
            getattr(self, "HAM_BAND_"+bandName+"_INVALID_WIDGET").forget()
            return True

        # if we reach this point, there is an error...
        getattr(self, "HAM_BAND_"+bandName+"_INVALID").set(SettingsNotebook.validationErrorMsg)
        getattr(self, "HAM_BAND_"+bandName+"_INVALID_WIDGET").pack()
        getattr(self, "HAM_BAND_"+bandName+"_START").set(self.priorValue)
        return False

    def validate_HAM_BAND_END(self, p_entry_value, v_condition, bandName):
        if (v_condition == "focusin"):
            self.priorValue = p_entry_value
        if (self.validateFREQKHZ(p_entry_value, 'LOW', getattr(self, "HAM_BAND_"+bandName+"_START").get())):
            getattr(self, "HAM_BAND_"+bandName+"_INVALID_WIDGET").forget()
            return True

        # if we reach this point, there is an error...
        getattr(self, "HAM_BAND_"+bandName+"_INVALID").set(SettingsNotebook.validationErrorMsg)
        getattr(self, "HAM_BAND_"+bandName+"_INVALID_WIDGET").pack()
        getattr(self, "HAM_BAND_"+bandName+"_END").set(self.priorValue)
        return False

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


    ##############################
    #  Functional Callbacks
    ##############################


    def Reset_Master_Cal_To_Factory(self):
        self.MASTER_CAL.set(self.FACTORY_VALUES_MASTER_CAL.get())

    def Reset_SSB_BFO_To_Factory(self):
        self.USB_CAL.set(self.FACTORY_VALUES_USB_CAL.get())

    def toggleExtendedChannels(self):
        if self.toggleExtendedChannelsCheckBox.get() == "1":
            self.Extended_Channel_Frame.pack(anchor="w", side="top")
        else:
            self.Extended_Channel_Frame.forget()

    def autoInputRegion1(self):
        self.clearHAM_BAND_Error_MSGS()

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
        self.clearHAM_BAND_Error_MSGS()

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
        self.clearHAM_BAND_Error_MSGS()

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
