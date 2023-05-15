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
            text='This wizard will help you to Calibrate your uBITX.\n\nDO NOT use this Wizard unless your radio is not receiving or is off frequency!!! \n\nAlways record your Master Calibration# SSB BFO# (also  known as (USB Calibration) and CW BFO# before using this wizard. \n\nFill in requested information and then click save when done. You can click Save at any time and it will save to you Raduino the calibration numbers you have created so far.\n\nYou can quit at any time and the original calibration numbers will be restored.')
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
        self.com_portManager_frame = ttk.Frame(
            self.com_portManager_Enclosing_frame)
        self.com_portManager_frame.pack(side="left")
        self.button1 = ttk.Button(self.com_portManager_Enclosing_frame)
        self.button1.configure(style="Normal.TButton", text='Read')
        self.button1.pack(padx=15, side="right")
        self.com_portManager_Enclosing_frame.pack(
            expand="true", fill="both", pady=25, side="top")
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
        self.currentMasterCal = tk.StringVar()
        self.label3.configure(
            style="Normal.TLabel",
            textvariable=self.currentMasterCal)
        self.label3.grid(column=1, padx="10 0", row=0, sticky="w")
        self.label4 = ttk.Label(self.calibrationWizardExistingValue_Frame)
        self.label4.configure(
            anchor="n",
            style="Normal.TLabel",
            text='SSB BFO:')
        self.label4.grid(column=0, row=1, sticky="e")
        self.label6 = ttk.Label(self.calibrationWizardExistingValue_Frame)
        self.currentSSBBFO = tk.StringVar()
        self.label6.configure(
            style="Normal.TLabel",
            textvariable=self.currentSSBBFO)
        self.label6.grid(column=1, padx="10 0", row=1, sticky="w")
        self.copyExistingCalibrationToClipboard_Button = ttk.Button(
            self.calibrationWizardExistingValue_Frame)
        self.img_copy_icon25x25 = tk.PhotoImage(file="copy_icon25x25.png")
        self.copyExistingCalibrationToClipboard_Button.configure(
            image=self.img_copy_icon25x25)
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
        self.currentCWBFO = tk.StringVar()
        self.label8.configure(
            style="Normal.TLabel",
            textvariable=self.currentCWBFO)
        self.label8.grid(column=1, padx="10 0", row=2, sticky="w")
        self.message3 = tk.Message(self.calibrationWizardExistingValue_Frame)
        self.message3.configure(
            borderwidth=2,
            justify="left",
            relief="ridge",
            takefocus=False,
            text='IMPORANT: Click the Copy icon to copy the existing calibration values to the clipboard or take a photo before the next step. This allows you to manually reset them if necessary.',
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
        self.CalVideoCopy_Button.configure(image=self.img_copy_icon25x25)
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
        self.hfsiganlsBFOTuningAidCopy_Button = ttk.Button(self.frame22)
        self.hfsiganlsBFOTuningAidCopy_Button.configure(
            image=self.img_copy_icon25x25, style="Symbol1.TButton")
        self.hfsiganlsBFOTuningAidCopy_Button.pack(
            padx=10, pady="0 10", side="right")
        self.hfsiganlsBFOTuningAidCopy_Button.configure(
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
            takefocus=False,
            text='The frequency calibration of the uBITX depends on your ability to "zero-beat" against a known signal. To do that you must be able to hear that signal. This step will help you initially calibrate your BFO.\n\nDo not worry if you do not get it optimal at this point, we will fine tune it after we calibrate the frequency.\n\nIf you have not watched it, you should watch the youtube video below by the designer of uBITX, Ashhar Farhan, where he walks thru calibrating a V6 uBITX.\n',
            width=300)
        self.message15.pack(expand="true", fill="both", pady=10, side="top")
        self.frame27 = ttk.Frame(self.frame26)
        self.frame27.configure(height=200, width=200)
        self.label30 = ttk.Label(self.frame27)
        self.label30.configure(
            text='https://youtu.be/t6LGXhS4_O8',
            textvariable=self.hfsignalsCalVideoLink)
        self.label30.pack(side="left")
        self.button6 = ttk.Button(self.frame27)
        self.button6.configure(image=self.img_copy_icon25x25)
        self.button6.pack(padx=10, side="right")
        self.button6.configure(command=self.copyCalVideoToClipboard)
        self.frame27.pack(pady=10, side="top")
        self.message16 = tk.Message(self.frame26)
        self.message16.configure(
            text='After viewing the video, go to the link below to access the HF Signals BFO Tuning Aid. Follow the setup directions.\n',
            width=300)
        self.message16.pack(pady="0 10", side="top")
        self.frame28 = ttk.Frame(self.frame26)
        self.frame28.configure(height=200, width=200)
        self.label31 = ttk.Label(self.frame28)
        self.label31.configure(
            compound="top",
            cursor="arrow",
            text='https://www.hfsignals.com/index.php/bfo-tuning-aid/\n',
            textvariable=self.hfsignalsBFOTuningAid)
        self.label31.pack(side="left")
        self.button7 = ttk.Button(self.frame28)
        self.button7.configure(
            image=self.img_copy_icon25x25,
            style="Symbol1.TButton")
        self.button7.pack(padx=10, pady="0 10", side="right")
        self.button7.configure(command=self.copyTuningAidLinkToClipboard)
        self.frame28.pack(padx=10, side="top")
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
            takefocus=False,
            text='The frequency calibration of the uBITX depends on your ability to "zero-beat" against a known signal. To do that you must be able to hear that signal. This step will help you initially calibrate your BFO.\n\nDo not worry if you do not get it optimal at this point, we will fine tune it after we calibrate the frequency.\n\nIf you have not watched it, you should watch the youtube video below by the designer of uBITX, Ashhar Farhan, where he walks thru calibrating a V6 uBITX.\n',
            width=300)
        self.message17.pack(expand="true", fill="both", pady=10, side="top")
        self.frame32 = ttk.Frame(self.frame31)
        self.frame32.configure(height=200, width=200)
        self.label33 = ttk.Label(self.frame32)
        self.label33.configure(
            text='https://youtu.be/t6LGXhS4_O8',
            textvariable=self.hfsignalsCalVideoLink)
        self.label33.pack(side="left")
        self.button8 = ttk.Button(self.frame32)
        self.button8.configure(image=self.img_copy_icon25x25)
        self.button8.pack(padx=10, side="right")
        self.button8.configure(command=self.copyCalVideoToClipboard)
        self.frame32.pack(pady=10, side="top")
        self.message18 = tk.Message(self.frame31)
        self.message18.configure(
            text='After viewing the video, go to the link below to access the HF Signals BFO Tuning Aid. Follow the setup directions.\n',
            width=300)
        self.message18.pack(pady="0 10", side="top")
        self.frame33 = ttk.Frame(self.frame31)
        self.frame33.configure(height=200, width=200)
        self.label34 = ttk.Label(self.frame33)
        self.label34.configure(
            compound="top",
            cursor="arrow",
            text='https://www.hfsignals.com/index.php/bfo-tuning-aid/\n',
            textvariable=self.hfsignalsBFOTuningAid)
        self.label34.pack(side="left")
        self.button9 = ttk.Button(self.frame33)
        self.button9.configure(
            image=self.img_copy_icon25x25,
            style="Symbol1.TButton")
        self.button9.pack(padx=10, pady="0 10", side="right")
        self.button9.configure(command=self.copyTuningAidLinkToClipboard)
        self.frame33.pack(padx=10, side="top")
        self.frame31.pack(padx=5, pady="0 10", side="top")
        self.calibrationWizardStep4_Frame.grid()
        self.calibrationWizardStep5_Frame = ttk.Frame(self)
        self.calibrationWizardStep5_Frame.configure(height=200, width=200)
        self.separator15 = ttk.Separator(self.calibrationWizardStep5_Frame)
        self.separator15.configure(orient="horizontal")
        self.separator15.pack(expand="true", fill="x", side="top")
        self.frame35 = ttk.Frame(self.calibrationWizardStep5_Frame)
        self.frame35.configure(height=25)
        self.label41 = ttk.Label(self.frame35)
        self.label41.configure(
            state="normal",
            style="Heading4.TLabel",
            text='Final Adjustment of the SSB BFO')
        self.label41.pack(padx=5, side="top")
        self.frame35.pack(expand="true", fill="x", pady=10, side="top")
        self.frame36 = ttk.Frame(self.calibrationWizardStep5_Frame)
        self.frame36.configure(height=200, width=350)
        self.message19 = tk.Message(self.frame36)
        self.message19.configure(
            borderwidth=0,
            justify="left",
            takefocus=False,
            text='The frequency calibration of the uBITX depends on your ability to "zero-beat" against a known signal. To do that you must be able to hear that signal. This step will help you initially calibrate your BFO.\n\nDo not worry if you do not get it optimal at this point, we will fine tune it after we calibrate the frequency.\n\nIf you have not watched it, you should watch the youtube video below by the designer of uBITX, Ashhar Farhan, where he walks thru calibrating a V6 uBITX.\n',
            width=300)
        self.message19.pack(expand="true", fill="both", pady=10, side="top")
        self.frame37 = ttk.Frame(self.frame36)
        self.frame37.configure(height=200, width=200)
        self.label36 = ttk.Label(self.frame37)
        self.label36.configure(
            text='https://youtu.be/t6LGXhS4_O8',
            textvariable=self.hfsignalsCalVideoLink)
        self.label36.pack(side="left")
        self.button10 = ttk.Button(self.frame37)
        self.button10.configure(image=self.img_copy_icon25x25)
        self.button10.pack(padx=10, side="right")
        self.button10.configure(command=self.copyCalVideoToClipboard)
        self.frame37.pack(pady=10, side="top")
        self.message20 = tk.Message(self.frame36)
        self.message20.configure(
            text='After viewing the video, go to the link below to access the HF Signals BFO Tuning Aid. Follow the setup directions.\n',
            width=300)
        self.message20.pack(pady="0 10", side="top")
        self.frame38 = ttk.Frame(self.frame36)
        self.frame38.configure(height=200, width=200)
        self.label37 = ttk.Label(self.frame38)
        self.label37.configure(
            compound="top",
            cursor="arrow",
            text='https://www.hfsignals.com/index.php/bfo-tuning-aid/\n',
            textvariable=self.hfsignalsBFOTuningAid)
        self.label37.pack(side="left")
        self.button11 = ttk.Button(self.frame38)
        self.button11.configure(
            image=self.img_copy_icon25x25,
            style="Symbol1.TButton")
        self.button11.pack(padx=10, pady="0 10", side="right")
        self.button11.configure(command=self.copyTuningAidLinkToClipboard)
        self.frame38.pack(padx=10, side="top")
        self.frame36.pack(padx=5, pady="0 10", side="top")
        self.calibrationWizardStep5_Frame.grid()
        self.calibrationWizardStep6_Frame = ttk.Frame(self)
        self.calibrationWizardStep6_Frame.configure(height=200, width=200)
        self.separator16 = ttk.Separator(self.calibrationWizardStep6_Frame)
        self.separator16.configure(orient="horizontal")
        self.separator16.pack(expand="true", fill="x", side="top")
        self.frame40 = ttk.Frame(self.calibrationWizardStep6_Frame)
        self.frame40.configure(height=25)
        self.label38 = ttk.Label(self.frame40)
        self.label38.configure(
            state="normal",
            style="Heading4.TLabel",
            text='Preparing for CW BFO Calibration')
        self.label38.pack(padx=5, side="top")
        self.frame40.pack(expand="true", fill="x", pady=10, side="top")
        self.frame41 = ttk.Frame(self.calibrationWizardStep6_Frame)
        self.frame41.configure(height=200, width=350)
        self.message21 = tk.Message(self.frame41)
        self.message21.configure(
            borderwidth=0,
            justify="left",
            takefocus=False,
            text='The frequency calibration of the uBITX depends on your ability to "zero-beat" against a known signal. To do that you must be able to hear that signal. This step will help you initially calibrate your BFO.\n\nDo not worry if you do not get it optimal at this point, we will fine tune it after we calibrate the frequency.\n\nIf you have not watched it, you should watch the youtube video below by the designer of uBITX, Ashhar Farhan, where he walks thru calibrating a V6 uBITX.\n',
            width=300)
        self.message21.pack(expand="true", fill="both", pady=10, side="top")
        self.frame42 = ttk.Frame(self.frame41)
        self.frame42.configure(height=200, width=200)
        self.label39 = ttk.Label(self.frame42)
        self.label39.configure(
            text='https://youtu.be/t6LGXhS4_O8',
            textvariable=self.hfsignalsCalVideoLink)
        self.label39.pack(side="left")
        self.button12 = ttk.Button(self.frame42)
        self.button12.configure(image=self.img_copy_icon25x25)
        self.button12.pack(padx=10, side="right")
        self.button12.configure(command=self.copyCalVideoToClipboard)
        self.frame42.pack(pady=10, side="top")
        self.message22 = tk.Message(self.frame41)
        self.message22.configure(
            text='After viewing the video, go to the link below to access the HF Signals BFO Tuning Aid. Follow the setup directions.\n',
            width=300)
        self.message22.pack(pady="0 10", side="top")
        self.frame43 = ttk.Frame(self.frame41)
        self.frame43.configure(height=200, width=200)
        self.label40 = ttk.Label(self.frame43)
        self.label40.configure(
            compound="top",
            cursor="arrow",
            text='https://www.hfsignals.com/index.php/bfo-tuning-aid/\n',
            textvariable=self.hfsignalsBFOTuningAid)
        self.label40.pack(side="left")
        self.button13 = ttk.Button(self.frame43)
        self.button13.configure(
            image=self.img_copy_icon25x25,
            style="Symbol1.TButton")
        self.button13.pack(padx=10, pady="0 10", side="right")
        self.button13.configure(command=self.copyTuningAidLinkToClipboard)
        self.frame43.pack(padx=10, side="top")
        self.frame41.pack(padx=5, pady="0 10", side="top")
        self.calibrationWizardStep6_Frame.grid()
        self.calibrationWizardStep7_Frame = ttk.Frame(self)
        self.calibrationWizardStep7_Frame.configure(height=200, width=200)
        self.separator17 = ttk.Separator(self.calibrationWizardStep7_Frame)
        self.separator17.configure(orient="horizontal")
        self.separator17.pack(expand="true", fill="x", side="top")
        self.frame45 = ttk.Frame(self.calibrationWizardStep7_Frame)
        self.frame45.configure(height=25)
        self.label42 = ttk.Label(self.frame45)
        self.label42.configure(
            state="normal",
            style="Heading4.TLabel",
            text='Calibrating the CW BFO')
        self.label42.pack(padx=5, side="top")
        self.frame45.pack(expand="true", fill="x", pady=10, side="top")
        self.frame46 = ttk.Frame(self.calibrationWizardStep7_Frame)
        self.frame46.configure(height=200, width=350)
        self.message23 = tk.Message(self.frame46)
        self.message23.configure(
            borderwidth=0,
            justify="left",
            takefocus=False,
            text='The frequency calibration of the uBITX depends on your ability to "zero-beat" against a known signal. To do that you must be able to hear that signal. This step will help you initially calibrate your BFO.\n\nDo not worry if you do not get it optimal at this point, we will fine tune it after we calibrate the frequency.\n\nIf you have not watched it, you should watch the youtube video below by the designer of uBITX, Ashhar Farhan, where he walks thru calibrating a V6 uBITX.\n',
            width=300)
        self.message23.pack(expand="true", fill="both", pady=10, side="top")
        self.frame47 = ttk.Frame(self.frame46)
        self.frame47.configure(height=200, width=200)
        self.label43 = ttk.Label(self.frame47)
        self.label43.configure(
            text='https://youtu.be/t6LGXhS4_O8',
            textvariable=self.hfsignalsCalVideoLink)
        self.label43.pack(side="left")
        self.button14 = ttk.Button(self.frame47)
        self.button14.configure(image=self.img_copy_icon25x25)
        self.button14.pack(padx=10, side="right")
        self.button14.configure(command=self.copyCalVideoToClipboard)
        self.frame47.pack(pady=10, side="top")
        self.message24 = tk.Message(self.frame46)
        self.message24.configure(
            text='After viewing the video, go to the link below to access the HF Signals BFO Tuning Aid. Follow the setup directions.\n',
            width=300)
        self.message24.pack(pady="0 10", side="top")
        self.frame48 = ttk.Frame(self.frame46)
        self.frame48.configure(height=200, width=200)
        self.label44 = ttk.Label(self.frame48)
        self.label44.configure(
            compound="top",
            cursor="arrow",
            text='https://www.hfsignals.com/index.php/bfo-tuning-aid/\n',
            textvariable=self.hfsignalsBFOTuningAid)
        self.label44.pack(side="left")
        self.button15 = ttk.Button(self.frame48)
        self.button15.configure(
            image=self.img_copy_icon25x25,
            style="Symbol1.TButton")
        self.button15.pack(padx=10, pady="0 10", side="right")
        self.button15.configure(command=self.copyTuningAidLinkToClipboard)
        self.frame48.pack(padx=10, side="top")
        self.frame46.pack(padx=5, pady="0 10", side="top")
        self.calibrationWizardStep7_Frame.grid()
        self.calibrationWizardStep8_Frame = ttk.Frame(self)
        self.calibrationWizardStep8_Frame.configure(height=200, width=200)
        self.separator18 = ttk.Separator(self.calibrationWizardStep8_Frame)
        self.separator18.configure(orient="horizontal")
        self.separator18.pack(expand="true", fill="x", side="top")
        self.frame50 = ttk.Frame(self.calibrationWizardStep8_Frame)
        self.frame50.configure(height=25)
        self.label45 = ttk.Label(self.frame50)
        self.label45.configure(
            state="normal",
            style="Heading4.TLabel",
            text='Final Review of Calibration Values')
        self.label45.pack(padx=5, side="top")
        self.frame50.pack(expand="true", fill="x", pady=10, side="top")
        self.frame51 = ttk.Frame(self.calibrationWizardStep8_Frame)
        self.frame51.configure(height=200, width=350)
        self.message25 = tk.Message(self.frame51)
        self.message25.configure(
            borderwidth=0,
            justify="left",
            takefocus=False,
            text='The frequency calibration of the uBITX depends on your ability to "zero-beat" against a known signal. To do that you must be able to hear that signal. This step will help you initially calibrate your BFO.\n\nDo not worry if you do not get it optimal at this point, we will fine tune it after we calibrate the frequency.\n\nIf you have not watched it, you should watch the youtube video below by the designer of uBITX, Ashhar Farhan, where he walks thru calibrating a V6 uBITX.\n',
            width=300)
        self.message25.pack(expand="true", fill="both", pady=10, side="top")
        self.frame52 = ttk.Frame(self.frame51)
        self.frame52.configure(height=200, width=200)
        self.label46 = ttk.Label(self.frame52)
        self.label46.configure(
            text='https://youtu.be/t6LGXhS4_O8',
            textvariable=self.hfsignalsCalVideoLink)
        self.label46.pack(side="left")
        self.button16 = ttk.Button(self.frame52)
        self.button16.configure(image=self.img_copy_icon25x25)
        self.button16.pack(padx=10, side="right")
        self.button16.configure(command=self.copyCalVideoToClipboard)
        self.frame52.pack(pady=10, side="top")
        self.message26 = tk.Message(self.frame51)
        self.message26.configure(
            text='After viewing the video, go to the link below to access the HF Signals BFO Tuning Aid. Follow the setup directions.\n',
            width=300)
        self.message26.pack(pady="0 10", side="top")
        self.frame53 = ttk.Frame(self.frame51)
        self.frame53.configure(height=200, width=200)
        self.label47 = ttk.Label(self.frame53)
        self.label47.configure(
            compound="top",
            cursor="arrow",
            text='https://www.hfsignals.com/index.php/bfo-tuning-aid/\n',
            textvariable=self.hfsignalsBFOTuningAid)
        self.label47.pack(side="left")
        self.button17 = ttk.Button(self.frame53)
        self.button17.configure(
            image=self.img_copy_icon25x25,
            style="Symbol1.TButton")
        self.button17.pack(padx=10, pady="0 10", side="right")
        self.button17.configure(command=self.copyTuningAidLinkToClipboard)
        self.frame53.pack(padx=10, side="top")
        self.frame51.pack(padx=5, pady="0 10", side="top")
        self.calibrationWizardStep8_Frame.grid()
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
        self.saveButton.configure(text='Save')
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
