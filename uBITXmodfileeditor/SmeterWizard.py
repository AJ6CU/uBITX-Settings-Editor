# import pygubu.widgets.simpletooltip as tooltip

from smeterwizardwidget import SmeterwizardWidget
from com_portManager import com_portManager
from globalvars import *
from time import sleep

class SmeterWizard(SmeterwizardWidget):

    sample1 = [0, 0.137, 0.277, 0.417, 0.557, 0.697, 0.847, 1]
    sample2 = [0, 0.098, 0.198, 0.348, 0.498, 0.598, 0.748, 1]
    sample3 = [0, 0.038, 0.098, 0.178, 0.299, 0.568, 0.748, 1]
    sample4 = [0, 0.030, 0.078, 0.138, 0.251, 0.471, 0.647, 1]
    sample5 = [0, 0.251, 0.470, 0.647, 0.720, 0.867, 0.948, 1]
    sample6 = [0, 0.251, 0.470, 0.647, 0.801, 0.900, 0.968, 1]
    sample7 = [0.097, 0.310, 0.508, 0.699, 0.841, 0.948, 0.968, 1]


    def __init__(self, parent):
        super().__init__(parent)

        self.myparent = parent

        # create com port
        self.comPortObj = com_portManager(self.com_portManager_frame, self)

        # pre-load com ports
        self.comPortObj.updateComPorts()                # Fill in available Com Ports

        self.comPortObj.pack()                          # make com it visible

        self.resetADCAssistant()


    def resetADCAssistant(self):
        # transfer current s-meter readings to dialog
        self.smeterWizard_S1.set(self.myparent.S_METER_LEVEL1.get())
        self.smeterWizard_S2.set(self.myparent.S_METER_LEVEL2.get())
        self.smeterWizard_S3.set(self.myparent.S_METER_LEVEL3.get())
        self.smeterWizard_S4.set(self.myparent.S_METER_LEVEL4.get())
        self.smeterWizard_S5.set(self.myparent.S_METER_LEVEL5.get())
        self.smeterWizard_S6.set(self.myparent.S_METER_LEVEL6.get())
        self.smeterWizard_S7.set(self.myparent.S_METER_LEVEL7.get())
        self.smeterWizard_S8.set(self.myparent.S_METER_LEVEL8.get())

        # Initialize source of min/max
        self.minRead = 'MANUAL'
        self.maxRead = 'MANUAL'

        self.smeterWizardManualMin.set(self.myparent.S_METER_LEVEL1.get())
        self.smeterWizardManualMax.set(self.myparent.S_METER_LEVEL8.get())

        if (int(self.smeterWizardManualMax.get()) == 0) | (int(self.smeterWizardManualMax.get()) >VREFMAXVALUE) :        #guard against a uninitialized EEPROM
            self.smeterWizardManualMax.set(str(VREFMAXVALUE))

        self.highlightMe(self.adcManual_Button_frame)

    def readADCsmeter(self, highorlow):

        adcValue =[]
        if(self.comPortObj.openComPort(self.comPortObj.getSelectedComPort())):        # was able to open com port
            self.RS232 = self.comPortObj.getComPortPTR(self.comPortObj.getSelectedComPort())
            print("\n***Starting ADC Scan***")
            #print("sample size =", self.sampleSizeADC.get())
            #print("delay =", self.sampleDelayADC.get())

            for x in range(self.sampleSizeADC.get()):
                self.RS232.write(bytes([SMETERPIN, 0, 0, 0, READADC]))
                self.RS232.flush()

                i = 0

                while i < 3:
                    if self.RS232.in_waiting != 0:          # have a byte to read
                        if i == 0:          #got first byte
                            byte1 = self.RS232.read(1)
                        elif i == 1:        #got second byte
                            byte2 = self.RS232.read(1)
                        else:
                            throwaway = self.RS232.read(1)   # last byte is zero
                        i += 1

                adcValue.append((ord(byte1)<<8) + ord(byte2))
                sleep(self.sampleDelayADC.get()/1000)

            print('values found =', adcValue)
            if highorlow == 'HIGH':
                print(max(adcValue))
                return max(adcValue)
            else:
                print(min(adcValue))
                return min(adcValue)



    def enableGoButtonComPort(self):
        self.sampleADCReadMin_Button_WIDGET.configure(state='normal')
        self.sampleADCReadMax_Button_WIDGET.configure(state='normal')

    def disableGoButtonComPort(self):
        self.sampleADCReadMin_Button_WIDGET.configure(state='disabled')
        self.sampleADCReadMax_Button_WIDGET.configure(state='disabled')

    def sampleADCReadMin(self):
        print("read ubitx min")
        self.minRead = 'AUTO'
        self.ADCubitxReadMin.set(self.readADCsmeter("LOW"))

    def sampleADCReadMax(self):
        print("read ubitx max")
        self.maxRead = 'AUTO'
        self.ADCubitxReadMax.set(self.readADCsmeter("HIGH"))


    def validate_smeterWizardManualMin(self, p_entry_value, v_condition):
        self.minRead = 'MANUAL'

    def validate_smeterWizardManualMax(self, p_entry_value, v_condition):
        self.maxRead = 'MANUAL'

    def apply_Sample(self, minValue, range, sample):

        self.smeterWizard_S1.set(str(round(((sample[0]*range)+minValue),0)).replace('.0',''))
        self.smeterWizard_S2.set(str(round(((sample[1]*range)+minValue),0)).replace('.0',''))
        self.smeterWizard_S3.set(str(round(((sample[2]*range)+minValue),0)).replace('.0',''))
        self.smeterWizard_S4.set(str(round(((sample[3]*range)+minValue),0)).replace('.0',''))
        self.smeterWizard_S5.set(str(round(((sample[4]*range)+minValue),0)).replace('.0',''))
        self.smeterWizard_S6.set(str(round(((sample[5]*range)+minValue),0)).replace('.0',''))
        self.smeterWizard_S7.set(str(round(((sample[6]*range)+minValue),0)).replace('.0',''))
        self.smeterWizard_S8.set(str(round(((sample[7]*range)+minValue),0)).replace('.0',''))

    def setSampleMaxMin (self):
        if self.minRead == "MANUAL":
            self.minADC = int(self.smeterWizardManualMin.get())
        elif self.minRead == "AUTO":
            self.minADC = int(self.ADCubitxReadMin.get())
        else:
            print("need error log here")
            return False

        if self.maxRead == "MANUAL":
            self.maxADC = int(self.smeterWizardManualMax.get())
        elif self.minRead == "AUTO":
            self.maxADC = int(self.ADCubitxReadMax.get())
        else:
            print("need error log here")
            return False

        return True         # found valid values

    def highlightMe(self, me):
        self.adcCurve1_Button_frame.configure(style='Normal.TFrame')
        self.adcCurve2_Button_frame.configure(style='Normal.TFrame')
        self.adcCurve3_Button_frame.configure(style='Normal.TFrame')
        self.adcCurve4_Button_frame.configure(style='Normal.TFrame')
        self.adcCurve5_Button_frame.configure(style='Normal.TFrame')
        self.adcCurve6_Button_frame.configure(style='Normal.TFrame')
        self.adcCurve7_Button_frame.configure(style='Normal.TFrame')
        self.adcManual_Button_frame.configure(style='Normal.TFrame')

        me.configure(style='Highlight.TFrame')

    def apply_Sample1(self):
        if self.setSampleMaxMin() == True:
            self.apply_Sample(self.minADC, self.maxADC-self.minADC, SmeterWizard.sample1)
            self.highlightMe(self.adcCurve1_Button_frame)


    def apply_Sample2(self):
        if self.setSampleMaxMin() == True:
            self.apply_Sample(self.minADC, self.maxADC-self.minADC, SmeterWizard.sample2)
            self.highlightMe(self.adcCurve2_Button_frame)

    def apply_Sample3(self):
        if self.setSampleMaxMin() == True:
            self.apply_Sample(self.minADC, self.maxADC-self.minADC, SmeterWizard.sample3)
            self.highlightMe(self.adcCurve3_Button_frame)

    def apply_Sample4(self):
        if self.setSampleMaxMin() == True:
            self.apply_Sample(self.minADC, self.maxADC-self.minADC, SmeterWizard.sample4)
            self.highlightMe(self.adcCurve4_Button_frame)

    def apply_Sample5(self):
        if self.setSampleMaxMin() == True:
            self.apply_Sample(self.minADC, self.maxADC-self.minADC, SmeterWizard.sample5)
            self.highlightMe(self.adcCurve5_Button_frame)

    def apply_Sample6(self):
        if self.setSampleMaxMin() == True:
            self.apply_Sample(self.minADC, self.maxADC-self.minADC, SmeterWizard.sample6)
            self.highlightMe(self.adcCurve6_Button_frame)

    def apply_Sample7(self):
        if self.setSampleMaxMin() == True:
            self.apply_Sample(self.minADC, self.maxADC-self.minADC, SmeterWizard.sample7)
            self.highlightMe(self.adcCurve7_Button_frame)

    def apply_Custom(self, *args):
        self.highlightMe(self.adcManual_Button_frame)



    def smeterWizard_Apply_Button(self):
        # Clicking the Apply button means we need to update the original ADC values

        self.myparent.S_METER_LEVEL1.set(self.smeterWizard_S1.get())
        self.myparent.S_METER_LEVEL2.set(self.smeterWizard_S2.get())
        self.myparent.S_METER_LEVEL3.set(self.smeterWizard_S3.get())
        self.myparent.S_METER_LEVEL4.set(self.smeterWizard_S4.get())
        self.myparent.S_METER_LEVEL5.set(self.smeterWizard_S5.get())
        self.myparent.S_METER_LEVEL6.set(self.smeterWizard_S6.get())
        self.myparent.S_METER_LEVEL7.set(self.smeterWizard_S7.get())
        self.myparent.S_METER_LEVEL8.set(self.smeterWizard_S8.get())
        # close the window
        self.destroy()


    def smeterWizard_Cancel_Button(self):
        self.destroy()

