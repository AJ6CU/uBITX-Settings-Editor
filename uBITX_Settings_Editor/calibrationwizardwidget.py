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
            text='IMPORANT: Record the calibration numbers above or take a photo before the next step. This allows you to manually reset them if necessary.',
            width=300)
        self.message3.grid(
            column=0,
            columnspan=2,
            pady="15 0",
            row=3,
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
            text='The frequency calibration of the uBITX depends on your ability to "zero-beat" against a known signal. To do that you must be able to hear that signal. This step will help you initially calibrate your BFO.\n\nDo not worry if you do not get it optimal at this point, we will fine tune it after we calibrate the frequency.\n\nIf you have not watched it, you should watch the youtube video below by the designer of uBITX, Ashhar Farhan, where he walks thru calibrating a V6 uBITX.  (You can copy and paste this link.)\n',
            width=300)
        self.message13.pack(expand="true", fill="both", pady=10, side="top")
        self.frame21 = ttk.Frame(self.frame20)
        self.frame21.configure(height=200, width=200)
        self.entry3 = ttk.Entry(self.frame21)
        self.entry3.configure(
            state="readonly",
            style="NoBorder.TEntry",
            width=30)
        _text_ = 'https://youtu.be/t6LGXhS4_O8'
        self.entry3["state"] = "normal"
        self.entry3.delete("0", "end")
        self.entry3.insert("0", _text_)
        self.entry3["state"] = "readonly"
        self.entry3.pack(pady="0 10", side="top")
        self.frame21.pack(side="top")
        self.message14 = tk.Message(self.frame20)
        self.message14.configure(
            text='After viewing the video, go to the link below to access the HF Signals BFO Tuning Aid. Follow the setup directions. (You can also copy and paste this link too.)\n',
            width=300)
        self.message14.pack(pady="0 10", side="top")
        self.frame22 = ttk.Frame(self.frame20)
        self.frame22.configure(height=200, width=200)
        self.entry4 = ttk.Entry(self.frame22)
        self.entry4.configure(
            state="readonly",
            style="NoBorder.TEntry",
            width=50)
        _text_ = 'https://www.hfsignals.com/index.php/bfo-tuning-aid/'
        self.entry4["state"] = "normal"
        self.entry4.delete("0", "end")
        self.entry4.insert("0", _text_)
        self.entry4["state"] = "readonly"
        self.entry4.pack(expand="true", fill="x", side="top")
        self.frame22.pack(side="top")
        self.frame20.pack(padx=5, pady="0 10", side="top")
        self.calibrationWizardStep2_Frame.grid()
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
