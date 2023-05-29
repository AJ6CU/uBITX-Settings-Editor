#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class CalibrationWizardWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(CalibrationWizardWidget, self).__init__(master, **kw)
        self.calibrationWizardStep0_Frame = ttk.Frame(self)
        self.calibrationWizardStep0_Frame.configure(height=200, width=200)
        self.calibrationWizardTitle_Frame = ttk.Frame(
            self.calibrationWizardStep0_Frame)
        self.calibrationWizardTitle_Frame.configure(height=25)
        self.calibrationWizardTitle_Label = ttk.Label(
            self.calibrationWizardTitle_Frame)
        self.calibrationWizardTitle_Label.configure(
            state="normal", style="Heading4.TLabel", text='uBITX Calibration Wizard')
        self.calibrationWizardTitle_Label.pack(padx=5, side="top")
        self.calibrationWizardTitle_Frame.pack(
            expand="true", fill="x", pady=10, side="top")
        self.separator2 = ttk.Separator(self.calibrationWizardStep0_Frame)
        self.separator2.configure(orient="horizontal")
        self.separator2.pack(expand="true", fill="x", side="top")
        self.calibrationWizardFirstStep_Frame = ttk.Frame(
            self.calibrationWizardStep0_Frame)
        self.calibrationWizardFirstStep_Frame.configure(height=200, width=350)
        self.message1 = tk.Message(self.calibrationWizardFirstStep_Frame)
        self.message1.configure(
            borderwidth=0,
            justify="left",
            takefocus=False,
            text='This wizard will help you Calibrate your uBITX.\n\nDO NOT use this Wizard unless your radio is not receiving or is off frequency!!! \n\nAlways record your Master Calibration#, SSB BFO# (also  known as (USB Calibration) and CW BFO# before using this wizard. \n\nFill in requested information and then click Save when done. You can click Save at any time and it will save to you Raduino the calibration numbers you have created so far.\n\nYou can Cancel at any time and the original calibration numbers will be restored.')
        self.message1.pack(expand="true", fill="both", pady=10, side="left")
        self.calibrationWizardFirstStep_Frame.pack(
            padx=5, pady="0 10", side="top")
        self.separator1 = ttk.Separator(self.calibrationWizardStep0_Frame)
        self.separator1.configure(orient="horizontal")
        self.separator1.pack(expand="true", fill="x", side="top")
        self.calibrationWizardStep0_Frame.grid(column=0, row=0, sticky="ew")
        self.calibrationWizardStep1_Frame = ttk.Frame(self)
        self.calibrationWizardStep1_Frame.configure(height=200, width=200)
        self.frame10 = ttk.Frame(self.calibrationWizardStep1_Frame)
        self.frame10.configure(height=25)
        self.label5 = ttk.Label(self.frame10)
        self.label5.configure(
            state="normal",
            style="Heading4.TLabel",
            text='Acquire Existing Calibration Data')
        self.label5.pack(padx=5, side="top")
        self.frame10.pack(expand="true", fill="x", pady=10, side="top")
        self.separator9 = ttk.Separator(self.calibrationWizardStep1_Frame)
        self.separator9.configure(orient="horizontal")
        self.separator9.pack(expand="true", fill="x", side="top")
        self.com_portManager_Enclosing_frame = ttk.Frame(
            self.calibrationWizardStep1_Frame)
        self.com_portManager_Enclosing_frame.pack(side="top")
        self.calibrationWizardExistingValue_Frame = ttk.Frame(
            self.calibrationWizardStep1_Frame)
        self.calibrationWizardExistingValue_Frame.configure(height=200)
        self.label2 = ttk.Label(self.calibrationWizardExistingValue_Frame)
        self.label2.configure(
            anchor="n",
            style="Normal.TLabel",
            text='Master Calibration:')
        self.label2.grid(column=0, row=0, sticky="e")
        self.label3 = ttk.Label(self.calibrationWizardExistingValue_Frame)
        self.currentMASTER_CAL = tk.StringVar()
        self.label3.configure(
            style="Normal.TLabel",
            textvariable=self.currentMASTER_CAL)
        self.label3.grid(column=1, padx="10 0", row=0, sticky="w")
        self.label4 = ttk.Label(self.calibrationWizardExistingValue_Frame)
        self.label4.configure(
            anchor="n",
            style="Normal.TLabel",
            text='SSB BFO:')
        self.label4.grid(column=0, row=1, sticky="e")
        self.label6 = ttk.Label(self.calibrationWizardExistingValue_Frame)
        self.currentUSB_CAL = tk.StringVar()
        self.label6.configure(
            style="Normal.TLabel",
            textvariable=self.currentUSB_CAL)
        self.label6.grid(column=1, padx="10 0", row=1, sticky="w")
        self.copyExistingCalibrationToClipboard_Button = ttk.Button(
            self.calibrationWizardExistingValue_Frame)
        self.copyExistingCalibrationToClipboard_Button.grid(
            column=2, row=1, sticky="e")
        self.copyExistingCalibrationToClipboard_Button.configure(
            command=self.copyExistingCalibrationToClipboard)
        self.label7 = ttk.Label(self.calibrationWizardExistingValue_Frame)
        self.label7.configure(
            anchor="n",
            style="Normal.TLabel",
            text='CW BFO:')
        self.label7.grid(column=0, row=2, sticky="e")
        self.label8 = ttk.Label(self.calibrationWizardExistingValue_Frame)
        self.currentCW_CAL = tk.StringVar()
        self.label8.configure(
            state="normal",
            style="Normal.TLabel",
            textvariable=self.currentCW_CAL)
        self.label8.grid(column=1, padx="10 0", row=2, sticky="w")
        self.message3 = tk.Message(self.calibrationWizardExistingValue_Frame)
        self.message3.configure(
            borderwidth=2,
            justify="left",
            relief="ridge",
            takefocus=False,
            text='IMPORANT: Click the Copy icon to copy the existing calibration values to the clipboard or take a photo before the next step. This allows you to manually reset them if necessary.\n\nAlso note that these values may differ from the Calibration values reported on the Calibration Tab. The Calibration Tab shows what is stored in EEPROM. The values reported  above are what the radio is using *right now* and would reflect any prior calibration work since the *last power cycle* of your radio. \n\nIf you want to restart this wizard with the EEPROM values, exit the Settings Editor, unplug the USB connection to your radio, and power cycle it. You can then restore the connections and start the Settings Editor again and navigate back to this wizard.',
            width=300)
        self.message3.grid(
            column=0,
            columnspan=3,
            pady="15 0",
            row=4,
            sticky="ew")
        self.calibrationWizardExistingValue_Frame.pack(
            expand="true", fill="both", pady=25, side="top")
        self.separator5 = ttk.Separator(self.calibrationWizardStep1_Frame)
        self.separator5.configure(orient="horizontal")
        self.separator5.pack(expand="true", fill="x", side="top")
        self.calibrationWizardStep1_Frame.grid(column=0, row=0, sticky="ew")
        self.calibrationWizardStep2_Frame = ttk.Frame(self)
        self.calibrationWizardStep2_Frame.configure(height=200, width=200)
        self.separator12 = ttk.Separator(self.calibrationWizardStep2_Frame)
        self.separator12.configure(orient="horizontal")
        self.separator12.pack(expand="true", fill="x", side="top")
        self.frame19 = ttk.Frame(self.calibrationWizardStep2_Frame)
        self.frame19.configure(height=25)
        self.label26 = ttk.Label(self.frame19)
        self.label26.configure(
            state="normal",
            style="Heading4.TLabel",
            text='Preparing for Initial BFO Setting')
        self.label26.pack(padx=5, side="top")
        self.frame19.pack(expand="true", fill="x", pady=10, side="top")
        self.frame20 = ttk.Frame(self.calibrationWizardStep2_Frame)
        self.frame20.configure(height=200, width=350)
        self.message13 = tk.Message(self.frame20)
        self.message13.configure(
            borderwidth=0,
            justify="left",
            takefocus=False,
            text='The frequency calibration of the uBITX depends on your ability to "zero-beat" against a known signal. To do that you must be able to hear that signal. This step will help you initially calibrate your BFO.\n\nDo not worry if you do not get it optimal at this point, we will fine tune it after we calibrate the frequency.\n\nIf you have not watched it, you should watch the youtube video below by the designer of uBITX, Ashhar Farhan, where he walks thru calibrating a V6 uBITX.\n',
            width=300)
        self.message13.pack(expand="true", fill="both", pady=10, side="top")
        self.frame23 = ttk.Frame(self.frame20)
        self.frame23.configure(height=200, width=200)
        self.hfsignalsCalVideoLink_Widget = ttk.Label(self.frame23)
        self.hfsignalsCalVideoLink = tk.StringVar(
            value='https://youtu.be/t6LGXhS4_O8')
        self.hfsignalsCalVideoLink_Widget.configure(
            text='https://youtu.be/t6LGXhS4_O8',
            textvariable=self.hfsignalsCalVideoLink)
        self.hfsignalsCalVideoLink_Widget.pack(side="left")
        self.CalVideoCopy_Button = ttk.Button(self.frame23)
        self.CalVideoCopy_Button.pack(padx=10, side="right")
        self.CalVideoCopy_Button.configure(
            command=self.copyCalVideoToClipboard)
        self.frame23.pack(pady=10, side="top")
        self.message14 = tk.Message(self.frame20)
        self.message14.configure(
            text='After viewing the video, go to the link below to access the HF Signals BFO Tuning Aid. Follow the setup directions.\n',
            width=300)
        self.message14.pack(pady="0 10", side="top")
        self.frame22 = ttk.Frame(self.frame20)
        self.frame22.configure(height=200, width=200)
        self.hfsignalsBFOTuningAid_Label = ttk.Label(self.frame22)
        self.hfsignalsBFOTuningAid = tk.StringVar(
            value='https://www.hfsignals.com/index.php/bfo-tuning-aid/\n')
        self.hfsignalsBFOTuningAid_Label.configure(
            compound="top",
            cursor="arrow",
            text='https://www.hfsignals.com/index.php/bfo-tuning-aid/\n',
            textvariable=self.hfsignalsBFOTuningAid)
        self.hfsignalsBFOTuningAid_Label.pack(side="left")
        self.hfsignalsBFOTuningAidCopy_Button = ttk.Button(self.frame22)
        self.hfsignalsBFOTuningAidCopy_Button.configure(
            style="Symbol1.TButton")
        self.hfsignalsBFOTuningAidCopy_Button.pack(
            padx=10, pady="0 10", side="right")
        self.hfsignalsBFOTuningAidCopy_Button.configure(
            command=self.copyTuningAidLinkToClipboard)
        self.frame22.pack(padx=10, side="top")
        self.frame20.pack(padx=5, pady="0 10", side="top")
        self.calibrationWizardStep2_Frame.grid()
        self.calibrationWizardStep3_Frame = ttk.Frame(self)
        self.calibrationWizardStep3_Frame.configure(height=200, width=200)
        self.separator13 = ttk.Separator(self.calibrationWizardStep3_Frame)
        self.separator13.configure(orient="horizontal")
        self.separator13.pack(expand="true", fill="x", side="top")
        self.frame25 = ttk.Frame(self.calibrationWizardStep3_Frame)
        self.frame25.configure(height=25)
        self.label29 = ttk.Label(self.frame25)
        self.label29.configure(
            state="normal",
            style="Heading4.TLabel",
            text='Setting BFO')
        self.label29.pack(padx=5, side="top")
        self.frame25.pack(expand="true", fill="x", pady=10, side="top")
        self.frame26 = ttk.Frame(self.calibrationWizardStep3_Frame)
        self.frame26.configure(height=200, width=350)
        self.message15 = tk.Message(self.frame26)
        self.message15.configure(
            borderwidth=0,
            justify="left",
            relief="flat",
            takefocus=False,
            text='Go to the webpage for the HF Signals BFO Tuning Aid. Follow the directions there for the hardware setup. Make sure you remember to connect your radio to your antenna!\n\nThis step automatically sets your radio Mode to USB.\n\nIf you want to move the spectrum left (down frequency) click the left arrow. Click the right arrow to move the spectrum to the right.\n\nYou can also select the speed mulitple using the menu in the center.\n\nAfter you have the waveform aligned with the left, you can click Next>>.',
            width=300)
        self.message15.pack(expand="true", fill="both", pady=10, side="top")
        self.frame54 = ttk.Frame(self.frame26)
        self.frame54.configure(height=200, width=200)
        self.label49 = ttk.Label(self.frame54)
        self.label49.configure(
            justify="left",
            style="Heading4.TLabel",
            text='Move Lower')
        self.label49.grid(column=0, padx="0 20", row=0, sticky="w")
        self.label50 = ttk.Label(self.frame54)
        self.label50.configure(style="Heading4.TLabel", text='Speed')
        self.label50.grid(column=1, padx="0 20", row=0)
        self.label51 = ttk.Label(self.frame54)
        self.label51.configure(style="Heading4.TLabel", text='Move Higher')
        self.label51.grid(column=2, row=0, sticky="e")
        self.moveFreqLower_Button = ttk.Button(self.frame54)
        self.moveFreqLower_Button.grid(
            column=0, padx="0 20", row=1, sticky="w")
        self.moveFreqLower_Button.configure(command=self.moveFreqLower_CB)
        self.bfo_speed_multiplier = tk.StringVar(value='X    5')
        __values = [
            'X    1',
            'X    2',
            'X    5',
            'X  10',
            'X  25',
            'X  50',
            'X100']
        self.bfo_speed_multiplier_OptionMenu = ttk.OptionMenu(
            self.frame54, self.bfo_speed_multiplier, "X    5", *__values, command=None)
        self.bfo_speed_multiplier_OptionMenu.grid(column=1, padx="0 20", row=1)
        self.moveFreqHigher_Button = ttk.Button(self.frame54)
        self.moveFreqHigher_Button.grid(column=2, row=1, sticky="e")
        self.moveFreqHigher_Button.configure(command=self.moveFreqLHigher_CB)
        self.frame54.pack(side="top")
        self.frame28 = ttk.Frame(self.frame26)
        self.frame28.configure(height=200, width=200)
        self.label48 = ttk.Label(self.frame28)
        self.label48.configure(
            justify="left",
            style="Heading4.TLabel",
            text='BFO Setting:')
        self.label48.pack(padx="0 10", side="left")
        self.currentBFOSetting_Entry = ttk.Entry(self.frame28)
        self.newUSB_CAL = tk.StringVar()
        self.currentBFOSetting_Entry.configure(
            state="readonly",
            style="NoBorder.TEntry",
            textvariable=self.newUSB_CAL)
        self.currentBFOSetting_Entry.pack(side="left")
        self.frame28.pack(pady=15, side="top")
        self.frame26.pack(padx=5, pady="0 10", side="top")
        self.calibrationWizardStep3_Frame.grid()
        self.calibrationWizardStep4_Frame = ttk.Frame(self)
        self.calibrationWizardStep4_Frame.configure(height=200, width=200)
        self.separator14 = ttk.Separator(self.calibrationWizardStep4_Frame)
        self.separator14.configure(orient="horizontal")
        self.separator14.pack(expand="true", fill="x", side="top")
        self.frame30 = ttk.Frame(self.calibrationWizardStep4_Frame)
        self.frame30.configure(height=25)
        self.label32 = ttk.Label(self.frame30)
        self.label32.configure(
            state="normal",
            style="Heading4.TLabel",
            text='Calibrate Frequency - "Master Calibration"')
        self.label32.pack(padx=5, side="top")
        self.frame30.pack(expand="true", fill="x", pady=10, side="top")
        self.frame31 = ttk.Frame(self.calibrationWizardStep4_Frame)
        self.frame31.configure(height=200, width=350)
        self.message17 = tk.Message(self.frame31)
        self.message17.configure(
            borderwidth=0,
            justify="left",
            relief="raised",
            takefocus=False,
            text='The easiest process to calibrate the frequency of the uBITX is to "zero-beat" against a known signal. This is a 3 step process:\n\n1. Select source with known frequency.\n2. Zero-beat this source. This step automatically puts your radio in USB mode.\n3. Click "Calculate" to generate the new calibration value.',
            width=300)
        self.message17.pack(expand="true", fill="both", pady=10, side="top")
        self.frame1 = ttk.Frame(self.frame31)
        self.frame1.configure(height=200, width=200)
        self.label33 = ttk.Label(self.frame1)
        self.label33.configure(
            state="normal",
            style="Heading3.TLabel",
            text='Step1: Select signal source:')
        self.label33.pack()
        self.frame1.pack(anchor="w", pady="10 0", side="top")
        self.frame32 = ttk.Frame(self.frame31)
        self.frame32.configure(height=200, width=200)
        self.label23 = ttk.Label(self.frame32)
        self.label23.configure(style="Normal.TLabel", text='WWV')
        self.label23.grid(column=0, columnspan=4, row=0, sticky="w")
        self.calibrationFreqWWV5MHz_RadioButton = ttk.Radiobutton(self.frame32)
        self.freqSelectButton = tk.StringVar(value='WWV5')
        self.calibrationFreqWWV5MHz_RadioButton.configure(
            style="RadioButton4.TRadiobutton",
            text='5MHz',
            value="WWV5",
            variable=self.freqSelectButton)
        self.calibrationFreqWWV5MHz_RadioButton.grid(
            column=0, padx="25 15", row=1, sticky="w")
        self.calibrationFreqWWV10MHz_RadioButton = ttk.Radiobutton(
            self.frame32)
        self.calibrationFreqWWV10MHz_RadioButton.configure(
            text='10MHz', value="WWV10", variable=self.freqSelectButton)
        self.calibrationFreqWWV10MHz_RadioButton.grid(
            column=1, padx="0 15", row=1, sticky="w")
        self.calibrationFreqWWV15MHz_RadioButton = ttk.Radiobutton(
            self.frame32)
        self.calibrationFreqWWV15MHz_RadioButton.configure(
            text='15 MHz', value="WWV15", variable=self.freqSelectButton)
        self.calibrationFreqWWV15MHz_RadioButton.grid(
            column=2, padx="0 15", row=1, sticky="w")
        self.calibrationFreqWWV20MHz_RadioButton = ttk.Radiobutton(
            self.frame32)
        self.calibrationFreqWWV20MHz_RadioButton.configure(
            text='20 MHz', value="WWV20", variable=self.freqSelectButton)
        self.calibrationFreqWWV20MHz_RadioButton.grid(
            column=3, row=1, sticky="w")
        self.label25 = ttk.Label(self.frame32)
        self.label25.configure(
            relief="flat",
            style="Normal.TLabel",
            text='Custom')
        self.label25.grid(column=0, columnspan=4, row=2, sticky="w")
        self.calibrationFreqCustom_RadioButton = ttk.Radiobutton(self.frame32)
        self.calibrationFreqCustom_RadioButton.configure(
            text='Freq', value="CUSTOM", variable=self.freqSelectButton)
        self.calibrationFreqCustom_RadioButton.grid(
            column=0, padx="25 10", row=3, sticky="w")
        self.calibrationFreqCustomSource_Entry = ttk.Entry(self.frame32)
        self.customSourceFreq = tk.StringVar(value='0')
        self.calibrationFreqCustomSource_Entry.configure(
            style="NoBorder.TEntry", textvariable=self.customSourceFreq, width=12)
        _text_ = '0'
        self.calibrationFreqCustomSource_Entry.delete("0", "end")
        self.calibrationFreqCustomSource_Entry.insert("0", _text_)
        self.calibrationFreqCustomSource_Entry.grid(
            column=1, columnspan=2, row=3, sticky="w")
        self.label27 = ttk.Label(self.frame32)
        self.label27.configure(text='Hz')
        self.label27.grid(column=2, padx=5, row=3, sticky="w")
        self.frame24 = ttk.Frame(self.frame32)
        self.frame24.configure(height=200, width=200)
        self.badFreqEnteredError_Message = tk.Message(self.frame24)
        self.badFreqEnteredError_Message.configure(
            font="TkTextFont",
            foreground="#ff0000",
            text='Invalid frequency!',
            width=400)
        self.badFreqEnteredError_Message.pack()
        self.frame24.grid(column=0, columnspan=4, row=4, sticky="ew")
        self.frame32.pack(expand="true", fill="x", pady=10, side="top")
        self.frame6 = ttk.Frame(self.frame31)
        self.frame6.configure(height=200, width=200)
        self.label28 = ttk.Label(self.frame6)
        self.label28.configure(
            relief="flat",
            state="normal",
            style="Heading3.TLabel",
            text='Step2: Zero-Beat frequency on VFO')
        self.label28.pack()
        self.frame6.pack(anchor="w", pady="25 0", side="top")
        self.frame13 = ttk.Frame(self.frame31)
        self.frame13.configure(height=200, width=200)
        self.label30 = ttk.Label(self.frame13)
        self.label30.configure(
            justify="left",
            relief="flat",
            state="normal",
            style="Heading3.TLabel",
            text='Step3: ')
        self.label30.pack(side="left")
        self.calculateMASTER_CAL_Button = ttk.Button(self.frame13)
        self.calculateMASTER_CAL_Button.configure(
            style="Button4.TButton", text='Calculate')
        self.calculateMASTER_CAL_Button.pack(padx="10 20", side="left")
        self.calculateMASTER_CAL_Button.configure(
            command=self.calculateMASTER_CAL)
        self.label35 = ttk.Label(self.frame13)
        self.label35.configure(text='VFO:')
        self.label35.pack(side="left")
        self.currentRadioVFO_Label = ttk.Label(self.frame13)
        self.currentVFOFreq = tk.StringVar(value='55.555.555')
        self.currentRadioVFO_Label.configure(
            text='55.555.555', textvariable=self.currentVFOFreq, width=10)
        self.currentRadioVFO_Label.pack(padx="0 2", side="left")
        self.label34 = ttk.Label(self.frame13)
        self.label34.configure(text='Hz')
        self.label34.pack(side="left")
        self.frame13.pack(
            anchor="w",
            expand="true",
            fill="x",
            pady="25 0",
            side="top")
        self.frame17 = ttk.Frame(self.frame31)
        self.frame17.configure(height=200, width=200)
        self.label31 = ttk.Label(self.frame17)
        self.label31.configure(
            justify="left",
            relief="flat",
            state="normal",
            style="Heading3.TLabel",
            text='Master Calibration Values')
        self.label31.pack(side="left")
        self.frame17.pack(anchor="w", pady="25 0", side="top")
        self.frame21 = ttk.Frame(self.frame31)
        self.frame21.configure(height=200, width=200)
        self.label42 = ttk.Label(self.frame21)
        self.label42.configure(style="Normal.TLabel", text='Current:')
        self.label42.grid(column=0, row=2, sticky="e")
        self.currentMASTER_CAL_Label = ttk.Label(self.frame21)
        self.currentMASTER_CAL_Label.configure(
            text='label43', textvariable=self.currentMASTER_CAL)
        self.currentMASTER_CAL_Label.grid(column=1, row=2)
        self.label44 = ttk.Label(self.frame21)
        self.label44.configure(style="Normal.TLabel", text='New:')
        self.label44.grid(column=0, row=3, sticky="e")
        self.newMASTER_CAL_Label = ttk.Label(self.frame21)
        self.newMASTER_CAL = tk.StringVar(value='label45')
        self.newMASTER_CAL_Label.configure(
            text='label45', textvariable=self.newMASTER_CAL)
        self.newMASTER_CAL_Label.grid(column=1, row=3)
        self.frame21.pack(
            expand="true",
            fill="x",
            padx=25,
            pady="10 0",
            side="top")
        self.frame31.pack(padx=5, pady="0 10", side="top")
        self.calibrationWizardStep4_Frame.grid()
        self.calibrationWizardStep5_Frame = ttk.Frame(self)
        self.calibrationWizardStep5_Frame.configure(height=200, width=200)
        self.separator3 = ttk.Separator(self.calibrationWizardStep5_Frame)
        self.separator3.configure(orient="horizontal")
        self.separator3.pack(expand="true", fill="x", side="top")
        self.frame2 = ttk.Frame(self.calibrationWizardStep5_Frame)
        self.frame2.configure(height=25)
        self.label1 = ttk.Label(self.frame2)
        self.label1.configure(
            state="normal",
            style="Heading4.TLabel",
            text='Final BFO Tuning')
        self.label1.pack(padx=5, side="top")
        self.frame2.pack(expand="true", fill="x", pady=10, side="top")
        self.frame3 = ttk.Frame(self.calibrationWizardStep5_Frame)
        self.frame3.configure(height=200, width=350)
        self.message2 = tk.Message(self.frame3)
        self.message2.configure(
            borderwidth=0,
            justify="left",
            relief="flat",
            takefocus=False,
            text='Your BFO should be pretty close. But it is worth checking again here and fine tuning it if necessary. Again, start the HF Signals BFO Tuning Aid and then adjust the BFO. A link to this tuning aid is provided below.',
            width=300)
        self.message2.pack(expand="true", fill="both", pady=10, side="top")
        self.frame12 = ttk.Frame(self.frame3)
        self.frame12.configure(height=200, width=200)
        self.label18 = ttk.Label(self.frame12)
        self.label18.configure(
            compound="top",
            cursor="arrow",
            text='https://www.hfsignals.com/index.php/bfo-tuning-aid/\n',
            textvariable=self.hfsignalsBFOTuningAid)
        self.label18.pack(side="left")
        self.fineTunehfsignalsBFOTuningAidCopy_Button = ttk.Button(
            self.frame12)
        self.fineTunehfsignalsBFOTuningAidCopy_Button.configure(
            style="Symbol1.TButton")
        self.fineTunehfsignalsBFOTuningAidCopy_Button.pack(
            padx=10, pady="0 10", side="right")
        self.fineTunehfsignalsBFOTuningAidCopy_Button.configure(
            command=self.copyTuningAidLinkToClipboard)
        self.frame12.pack(padx=10, side="top")
        self.frame4 = ttk.Frame(self.frame3)
        self.frame4.configure(height=200, width=200)
        self.label9 = ttk.Label(self.frame4)
        self.label9.configure(
            justify="left",
            style="Heading4.TLabel",
            text='Move Lower')
        self.label9.grid(column=0, padx="0 20", row=0, sticky="w")
        self.label10 = ttk.Label(self.frame4)
        self.label10.configure(style="Heading4.TLabel", text='Speed')
        self.label10.grid(column=1, padx="0 20", row=0)
        self.label11 = ttk.Label(self.frame4)
        self.label11.configure(style="Heading4.TLabel", text='Move Higher')
        self.label11.grid(column=2, row=0, sticky="e")
        self.fineTuneMoveFreqLower_Button = ttk.Button(self.frame4)
        self.fineTuneMoveFreqLower_Button.grid(
            column=0, padx="0 20", row=1, sticky="w")
        self.fineTuneMoveFreqLower_Button.configure(
            command=self.moveFreqLower_CB)
        self.bfo_speed_mulitpier = tk.StringVar(value='X    5')
        __values = [
            'X    1',
            'X    2',
            'X    5',
            'X  10',
            'X  25',
            'X  50',
            'X100']
        self.fineTuneBFOMultiplier_OptionMenu = ttk.OptionMenu(
            self.frame4, self.bfo_speed_mulitpier, "X    5", *__values, command=None)
        self.fineTuneBFOMultiplier_OptionMenu.grid(
            column=1, padx="0 20", row=1)
        self.fineTuneMoveFreqHigher_Button = ttk.Button(self.frame4)
        self.fineTuneMoveFreqHigher_Button.grid(column=2, row=1, sticky="e")
        self.fineTuneMoveFreqHigher_Button.configure(
            command=self.moveFreqLHigher_CB)
        self.frame4.pack(side="top")
        self.frame5 = ttk.Frame(self.frame3)
        self.frame5.configure(height=200, width=200)
        self.label12 = ttk.Label(self.frame5)
        self.label12.configure(
            justify="left",
            style="Heading4.TLabel",
            text='BFO Setting:')
        self.label12.pack(padx="0 10", side="left")
        self.newBFOSetting_Entry = ttk.Entry(self.frame5)
        self.newBFOSetting_Entry.configure(
            state="readonly",
            style="NoBorder.TEntry",
            textvariable=self.newUSB_CAL)
        self.newBFOSetting_Entry.pack(side="left")
        self.frame5.pack(pady=15, side="top")
        self.frame3.pack(padx=5, pady="0 10", side="top")
        self.calibrationWizardStep5_Frame.grid()
        self.calibrationWizardStep6_Frame = ttk.Frame(self)
        self.calibrationWizardStep6_Frame.configure(height=200, width=200)
        self.separator4 = ttk.Separator(self.calibrationWizardStep6_Frame)
        self.separator4.configure(orient="horizontal")
        self.separator4.pack(expand="true", fill="x", side="top")
        self.frame7 = ttk.Frame(self.calibrationWizardStep6_Frame)
        self.frame7.configure(height=25)
        self.label13 = ttk.Label(self.frame7)
        self.label13.configure(
            state="normal",
            style="Heading4.TLabel",
            text='Setting CW BFO')
        self.label13.pack(padx=5, side="top")
        self.frame7.pack(expand="true", fill="x", pady=10, side="top")
        self.frame8 = ttk.Frame(self.calibrationWizardStep6_Frame)
        self.frame8.configure(height=200, width=350)
        self.message4 = tk.Message(self.frame8)
        self.message4.configure(
            borderwidth=0,
            justify="left",
            relief="flat",
            takefocus=True,
            text='The process for setting the CW BFO is similar to that of the SSB BFO. As previously, this step sets your radio mode to the proper value (CWL).\n\nNow start the HF Signals BFO Tuning Aid, and then adjust the spectrum so that it is inbetween the two red borders. \n\nA link to the HF Signals BFO Tuning Aid is also provided below.',
            width=300)
        self.message4.pack(expand="true", fill="both", pady=10, side="top")
        self.frame18 = ttk.Frame(self.frame8)
        self.frame18.configure(height=200, width=200)
        self.label24 = ttk.Label(self.frame18)
        self.label24.configure(
            compound="top",
            cursor="arrow",
            text='https://www.hfsignals.com/index.php/bfo-tuning-aid/\n',
            textvariable=self.hfsignalsBFOTuningAid)
        self.label24.pack(side="left")
        self.CWTunehfsignalsBFOTuningAidCopy_Button = ttk.Button(self.frame18)
        self.CWTunehfsignalsBFOTuningAidCopy_Button.configure(
            style="Symbol1.TButton")
        self.CWTunehfsignalsBFOTuningAidCopy_Button.pack(
            padx=10, pady="0 10", side="right")
        self.CWTunehfsignalsBFOTuningAidCopy_Button.configure(
            command=self.copyTuningAidLinkToClipboard)
        self.frame18.pack(padx=10, side="top")
        self.frame9 = ttk.Frame(self.frame8)
        self.frame9.configure(height=200, width=200)
        self.label14 = ttk.Label(self.frame9)
        self.label14.configure(
            justify="left",
            style="Heading4.TLabel",
            text='Move Lower')
        self.label14.grid(column=0, padx="0 20", row=0, sticky="w")
        self.label15 = ttk.Label(self.frame9)
        self.label15.configure(style="Heading4.TLabel", text='Speed')
        self.label15.grid(column=1, padx="0 20", row=0)
        self.label16 = ttk.Label(self.frame9)
        self.label16.configure(style="Heading4.TLabel", text='Move Higher')
        self.label16.grid(column=2, row=0, sticky="e")
        self.moveCWBFOFreqLower_Button = ttk.Button(self.frame9)
        self.moveCWBFOFreqLower_Button.grid(
            column=0, padx="0 20", row=1, sticky="w")
        self.moveCWBFOFreqLower_Button.configure(
            command=self.moveCWBFOFreqLower_CB)
        self.CWbfo_speed_mulitpier = tk.StringVar(value='X    5')
        __values = [
            'X    1',
            'X    2',
            'X    5',
            'X  10',
            'X  25',
            'X  50',
            'X100']
        self.CWspeedMultiplier_OptionMenu = ttk.OptionMenu(
            self.frame9, self.CWbfo_speed_mulitpier, "X    5", *__values, command=None)
        self.CWspeedMultiplier_OptionMenu.grid(column=1, padx="0 20", row=1)
        self.moveCWBFOFreqHigher_Button = ttk.Button(self.frame9)
        self.moveCWBFOFreqHigher_Button.grid(column=2, row=1, sticky="e")
        self.moveCWBFOFreqHigher_Button.configure(
            command=self.moveCWBFOFreqLHigher_CB)
        self.frame9.pack(side="top")
        self.frame11 = ttk.Frame(self.frame8)
        self.frame11.configure(height=200, width=200)
        self.label17 = ttk.Label(self.frame11)
        self.label17.configure(
            justify="left",
            style="Heading4.TLabel",
            text='CW BFO Setting:')
        self.label17.pack(padx="0 10", side="left")
        self.newCWBFOSetting_Entry = ttk.Entry(self.frame11)
        self.newCW_CAL = tk.StringVar()
        self.newCWBFOSetting_Entry.configure(
            state="readonly",
            style="NoBorder.TEntry",
            textvariable=self.newCW_CAL)
        self.newCWBFOSetting_Entry.pack(side="left")
        self.frame11.pack(pady=15, side="top")
        self.frame8.pack(padx=5, pady="0 10", side="top")
        self.calibrationWizardStep6_Frame.grid()
        self.calibrationWizardStep7_Frame = ttk.Frame(self)
        self.calibrationWizardStep7_Frame.configure(height=200, width=200)
        self.separator6 = ttk.Separator(self.calibrationWizardStep7_Frame)
        self.separator6.configure(orient="horizontal")
        self.separator6.pack(expand="true", fill="x", side="top")
        self.frame14 = ttk.Frame(self.calibrationWizardStep7_Frame)
        self.frame14.configure(height=25)
        self.label19 = ttk.Label(self.frame14)
        self.label19.configure(
            state="normal",
            style="Heading4.TLabel",
            text='Final Review!')
        self.label19.pack(padx=5, side="top")
        self.frame14.pack(expand="true", fill="x", pady=10, side="top")
        self.frame15 = ttk.Frame(self.calibrationWizardStep7_Frame)
        self.frame15.configure(height=200, width=350)
        self.message5 = tk.Message(self.frame15)
        self.message5.configure(
            borderwidth=0,
            justify="left",
            relief="flat",
            takefocus=False,
            text='You are just about done! The initial and final numbers are provided below.\n\nIf you are OK with the new values, click the "Save and Exit" button. Your uBITX will also be automatically rebooted to ensure that you are using the new values stored in EEPROM.\n\nNotes: \n1. Items in Bold indicate a change in value. \n2. This step "guesses" that you want to be in USB mode after completing this wizard. You may want to change that to another mode.',
            width=300)
        self.message5.pack(expand="true", fill="both", pady=10, side="top")
        self.frame16 = ttk.Frame(self.frame15)
        self.frame16.configure(height=200, width=200)
        self.label20 = ttk.Label(self.frame16)
        self.label20.configure(
            justify="left",
            style="Heading4.TLabel",
            text='Parameter')
        self.label20.grid(column=0, padx="0 20", row=0, sticky="w")
        self.label21 = ttk.Label(self.frame16)
        self.label21.configure(style="Heading4.TLabel", text='Initial Value')
        self.label21.grid(column=1, padx="0 20", row=0, sticky="w")
        self.label22 = ttk.Label(self.frame16)
        self.label22.configure(style="Heading4.TLabel", text='New Value')
        self.label22.grid(column=2, row=0, sticky="e")
        self.Master_Cal_Label = ttk.Label(self.frame16)
        self.Master_Cal_Label.configure(
            justify="left",
            style="Normal.TLabel",
            text='Master Cal')
        self.Master_Cal_Label.grid(row=1, sticky="w")
        self.finalReviewMasterCalInitial_Label = ttk.Label(self.frame16)
        self.finalReviewMasterCalInitial_Label.configure(
            justify="left", style="Normal.TLabel", textvariable=self.currentMASTER_CAL)
        self.finalReviewMasterCalInitial_Label.grid(
            column=1, row=1, sticky="w")
        self.finalReviewMasterCalNew_Label = ttk.Label(self.frame16)
        self.finalReviewMasterCalNew_Label.configure(
            justify="left", style="Normal.TLabel", textvariable=self.newMASTER_CAL)
        self.finalReviewMasterCalNew_Label.grid(column=2, row=1, sticky="w")
        self.SSB_BFO_Label = ttk.Label(self.frame16)
        self.SSB_BFO_Label.configure(
            justify="left",
            style="Normal.TLabel",
            text='SSB BFO')
        self.SSB_BFO_Label.grid(row=2, sticky="w")
        self.finalReviewBFOCalInitial_Label = ttk.Label(self.frame16)
        self.finalReviewBFOCalInitial_Label.configure(
            justify="left",
            relief="flat",
            style="Normal.TLabel",
            textvariable=self.currentUSB_CAL)
        self.finalReviewBFOCalInitial_Label.grid(column=1, row=2, sticky="w")
        self.finalReviewBFOCalNew_Label = ttk.Label(self.frame16)
        self.finalReviewBFOCalNew_Label.configure(
            justify="left", style="Normal.TLabel", textvariable=self.newUSB_CAL)
        self.finalReviewBFOCalNew_Label.grid(column=2, row=2, sticky="w")
        self.CW_BFO_Label = ttk.Label(self.frame16)
        self.CW_BFO_Label.configure(
            justify="left",
            style="Normal.TLabel",
            text='CW BFO')
        self.CW_BFO_Label.grid(row=3, sticky="w")
        self.finalReviewCWCalInitial_Label = ttk.Label(self.frame16)
        self.finalReviewCWCalInitial_Label.configure(
            justify="left", style="Normal.TLabel", textvariable=self.currentCW_CAL)
        self.finalReviewCWCalInitial_Label.grid(column=1, row=3, sticky="w")
        self.finalReviewCWCalNew_Label = ttk.Label(self.frame16)
        self.finalReviewCWCalNew_Label.configure(
            justify="left", style="Normal.TLabel", textvariable=self.newCW_CAL)
        self.finalReviewCWCalNew_Label.grid(column=2, row=3, sticky="w")
        self.frame16.pack(side="top")
        self.frame15.pack(padx=5, pady="0 10", side="top")
        self.calibrationWizardStep7_Frame.grid()
        self.calibrationWizardButton_Frame = ttk.Frame(self)
        self.calibrationWizardButton_Frame.configure(height=50, width=200)
        self.calibration_wizard_button_frame = ttk.Frame(
            self.calibrationWizardButton_Frame)
        self.calibration_wizard_button_frame.configure(height=200, width=200)
        self.backButton = ttk.Button(self.calibration_wizard_button_frame)
        self.backButton.configure(text='<<Back')
        self.backButton.pack(padx=10, pady=10, side="left")
        self.backButton.configure(command=self.wizardBack)
        self.nextButton = ttk.Button(self.calibration_wizard_button_frame)
        self.nextButton.configure(text='Next>>')
        self.nextButton.pack(padx="0 10", pady=10, side="left")
        self.nextButton.configure(command=self.wizardNext)
        self.saveButton = ttk.Button(self.calibration_wizard_button_frame)
        self.saveButton.configure(text='Save and Exit')
        self.saveButton.pack(padx="0 10", pady=10, side="left")
        self.saveButton.configure(command=self.wizardSave)
        self.cancelButton = ttk.Button(self.calibration_wizard_button_frame)
        self.cancelButton.configure(text='Cancel')
        self.cancelButton.pack(padx="0 10", pady=10, side="left")
        self.cancelButton.configure(command=self.wizardCancel)
        self.calibration_wizard_button_frame.pack(anchor="center", side="top")
        self.calibrationWizardButton_Frame.grid(column=0, row=3, sticky="ew")
        self.configure(height=350, width=500)
        self.title("uBITX Calibration Wizard")

        self.setup_ttk_styles()

    def setup_ttk_styles(self):
        # ttk styles configuration
        self.style = style = ttk.Style()
        optiondb = style.master
        # --------------------
        # This file is used for defining Ttk styles.
        # Use the 'style' object to define styles.

        # Pygubu Designer will need to know which style definition file
        # you wish to use in your project.

        # To specify a style definition file in Pygubu Designer:
        # Go to: Edit -> Preferences -> Ttk Styles -> Browse (button)

        # In Pygubu Designer:
        # Assuming that you have specified a style definition file,
        # - Use the 'style' combobox drop-down menu in Pygubu Designer
        #   to select a style that you have defined.
        # - Changes made to the chosen style definition file will be
        #   automatically reflected in Pygubu Designer.
        # --------------------

        # Example code:
        fontList = {'Heading1': ('Times New Roman', 24, 'bold', 'italic'),
                    'Heading2': ('Arial', 18, 'bold'),
                    'Heading3': ('Arial', 12, 'bold'),
                    'Heading4': ('Arial', 10, 'bold'),
                    'Normal': ('Default', 10),
                    'Emphasis': ('Default', 12, 'bold'),
                    'Symbol1': ('Symbol', 18, 'bold'),
                    'Symbol3': ('Symbol', 12, 'bold')}

        style.configure(
            'Heading1.TLabel',
            font=fontList['Heading1'],
            background='blue',
            foreground='white')
        style.configure('Heading2.TLabel', font=fontList['Heading2'])
        style.configure('Heading3.TLabel', font=fontList['Heading3'])
        style.configure('Heading4.TLabel', font=fontList['Heading4'])
        style.configure('Normal.TLabel', font=fontList['Normal'])
        style.configure('Symbol1.TLabel', font=fontList['Symbol1'])
        style.configure('Button3.TButton', font=fontList['Heading3'])
        style.configure('Button4.TButton', font=fontList['Heading4'])
        style.configure(
            'Button3Blue.TButton',
            font=fontList['Heading3'],
            foreground='blue')
        style.configure('Normal.TButton', font=fontList['Normal'])
        style.configure('Symbol1.TButton', font=fontList['Symbol1'])
        style.configure('Symbol3.TButton', font=fontList['Symbol3'])
        style.configure('ButtonEmphasis.TButton', font=fontList['Emphasis'])
        style.configure('RadioButton3.TRadiobutton', font=fontList['Heading3'])
        style.configure('RadioButton4.TRadiobutton', font=fontList['Heading4'])
        style.configure(
            'RadioButtonNormal.TRadiobutton',
            font=fontList['Normal'])
        style.configure(
            'RadioButtonEmphasis.TRadiobutton',
            font=fontList['Emphasis'])
        style.configure('Checkbox3.TCheckbutton', font=fontList['Heading3'])
        style.configure('Checkbox4.TCheckbutton', font=fontList['Heading4'])
        style.configure('CheckboxNormal.TCheckbutton', font=fontList['Normal'])
        style.configure(
            'CheckboxNormalNoBorder.TCheckbutton',
            font=fontList['Normal'],
            highlightthickness=0,
            borderwidth=0,
            bd=0)
        style.configure(
            'CheckboxEmphasis.TCheckbutton',
            font=fontList['Emphasis'])
        style.configure('ComboBox3.TCombobox', font=fontList['Heading3'])
        style.configure('ComboBox4.TCombobox', font=fontList['Heading4'])
        style.configure(
            'ComboBox4White.TCombobox',
            font=fontList['Heading4'],
            foreground='white')
        style.configure('Normal.TEntry', font=fontList['Normal'])
        style.configure(
            'NoBorder.TEntry',
            font=fontList['Normal'],
            highlightthickness=0,
            borderwidth=0,
            bd=0)
        style.configure('Title.TFrame', background='blue', foreground='white')
        style.configure(
            'Heading2.TLabelframe.Label',
            font=fontList['Heading3'])
        style.configure('Heading2.TLabelframe')
        style.configure('Normal.TText', font=fontList['Heading3'])

        style.configure('Highlight.TFrame', background='blue', bd=4)
        style.configure('Normal.TFrame', background='gray', bd=4)

        style.configure('Fixed.TNotebook')
        style.configure('Fixed.TNotebook.Tab', padding=[5, 2])

    def copyExistingCalibrationToClipboard(self):
        pass

    def copyCalVideoToClipboard(self):
        pass

    def copyTuningAidLinkToClipboard(self):
        pass

    def moveFreqLower_CB(self):
        pass

    def moveFreqLHigher_CB(self):
        pass

    def calculateMASTER_CAL(self):
        pass

    def moveCWBFOFreqLower_CB(self):
        pass

    def moveCWBFOFreqLHigher_CB(self):
        pass

    def wizardBack(self):
        pass

    def wizardNext(self):
        pass

    def wizardSave(self):
        pass

    def wizardCancel(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = CalibrationWizardWidget(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
