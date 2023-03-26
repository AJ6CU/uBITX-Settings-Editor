#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.scrolledframe import ScrolledFrame


class SettingsnotebookWidget(ttk.Frame):
    def __init__(self, master=None, **kw):
        super(SettingsnotebookWidget, self).__init__(master, **kw)
        self.settingsNotebook = ttk.Notebook(self)
        self.settingsNotebook.configure(
            height=800, style="Fixed.TNotebook", width=800)
        self.General_SF = ScrolledFrame(
            self.settingsNotebook, scrolltype="both")
        self.General_SF.configure(usemousewheel=True)
        self.frame15 = ttk.Frame(self.General_SF.innerframe)
        self.frame15.configure(height=200, width=200)
        self.General_Setting_Title_Frame = ttk.Frame(self.frame15)
        self.General_Setting_Title_Frame.configure(height=200, width=200)
        self.General_Settings_Label = ttk.Label(
            self.General_Setting_Title_Frame)
        self.General_Settings_Label.configure(
            justify="center",
            style="Heading2.TLabel",
            text='General Settings')
        self.General_Settings_Label.pack(anchor="w", padx=5, pady="15 25")
        self.General_Setting_Title_Frame.pack(anchor="w", fill="x", side="top")
        self.General_Frame = ttk.Frame(self.frame15)
        self.General_Operator_Frame = ttk.Frame(self.General_Frame)
        self.General_Operator_Frame.configure(height=200, width=200)
        self.General_Operator_Title_Frame = ttk.Frame(
            self.General_Operator_Frame)
        self.General_Operator_Title_Frame.configure(height=200, width=200)
        self.General_Settings_Operator_Label = ttk.Label(
            self.General_Operator_Title_Frame)
        self.General_Settings_Operator_Label.configure(
            justify="left", style="Heading3.TLabel", text='Operator')
        self.General_Settings_Operator_Label.pack()
        self.General_Operator_Title_Frame.pack(anchor="w", side="top")
        self.General_Operator_Settings_Frame = ttk.Frame(
            self.General_Operator_Frame)
        self.General_Operator_Settings_Frame.configure(height=200, width=200)
        self.USER_CALLSIGN_LABEL = ttk.Label(
            self.General_Operator_Settings_Frame)
        self.USER_CALLSIGN_LABEL.configure(
            style="Heading4.TLabel", text='Callsign')
        self.USER_CALLSIGN_LABEL.grid(column=0, padx="0 10", row=0, sticky="w")
        self.USER_CALLSIGN_WIDGET = ttk.Entry(
            self.General_Operator_Settings_Frame)
        self.USER_CALLSIGN = tk.StringVar()
        self.USER_CALLSIGN_WIDGET.configure(
            justify="left",
            textvariable=self.USER_CALLSIGN,
            validate="focus",
            width=18)
        self.USER_CALLSIGN_WIDGET.grid(column=1, padx="0 10", row=0)
        _validatecmd = (
            self.USER_CALLSIGN_WIDGET.register(
                self.validate_USER_CALLSIGN), "%P", "%V")
        self.USER_CALLSIGN_WIDGET.configure(validatecommand=_validatecmd)
        self.General_Operator_Settings_Frame.pack(padx="50 0", side="top")
        self.General_Operator_Frame.pack(anchor="w", side="top")
        self.frame4 = ttk.Frame(self.General_Frame)
        self.frame4.configure(height=200, width=200)
        self.separator2 = ttk.Separator(self.frame4)
        self.separator2.configure(orient="horizontal")
        self.separator2.pack(
            anchor="center",
            expand="true",
            fill="x",
            pady=10,
            side="top")
        self.frame4.pack(anchor="w", expand="true", fill="x", side="top")
        self.General_Tuning_Steps_Frame = ttk.Frame(self.General_Frame)
        self.General_Tuning_Steps_Frame.configure(height=200, width=200)
        self.Tuning_Steps_Title_Frame = ttk.Frame(
            self.General_Tuning_Steps_Frame)
        self.Tuning_Steps_Title_Frame.configure(height=200, width=200)
        self.General_Tuning_Steps_Label = ttk.Label(
            self.Tuning_Steps_Title_Frame)
        self.General_Tuning_Steps_Label.configure(
            style="Heading3.TLabel", text='Tuning Steps')
        self.General_Tuning_Steps_Label.pack(
            anchor="w", expand="true", fill="x")
        self.Tuning_Steps_Title_Frame.pack(
            anchor="w", expand="true", fill="x", pady="10 0", side="top")
        self.General_Tuning_Steps_Settings_Frame = ttk.Frame(
            self.General_Tuning_Steps_Frame)
        self.General_Tuning_Steps_Settings_Frame.configure(
            height=200, width=200)
        self.frame10 = ttk.Frame(self.General_Tuning_Steps_Settings_Frame)
        self.frame10.configure(width=200)
        self.label105 = ttk.Label(self.frame10)
        self.label105.configure(
            style="Heading4.TLabel",
            text='Step#\t1\t2\t3\t4\t5')
        self.label105.grid(column=0, row=0, sticky="w")
        self.Tuning_Steps_RadioButton5 = ttk.Radiobutton(self.frame10)
        self.Tuning_Steps_Common = tk.StringVar(value='5')
        self.Tuning_Steps_RadioButton5.configure(
            style="RadioButtonNormal.TRadiobutton",
            text='Custom',
            value=5,
            variable=self.Tuning_Steps_Common)
        self.Tuning_Steps_RadioButton5.grid(
            column=0, padx=38, pady=10, row=6, sticky="w")
        self.Tuning_Steps_RadioButton5.configure(
            command=self.Tuning_Steps_Set_Common)
        self.Tuning_Steps_RadioButton0 = ttk.Radiobutton(self.frame10)
        self.Tuning_Steps_RadioButton0.configure(
            style="RadioButtonNormal.TRadiobutton",
            text='1\t5\t10\t50\t100 Hz',
            value=0,
            variable=self.Tuning_Steps_Common)
        self.Tuning_Steps_RadioButton0.grid(
            column=0, padx=38, row=1, sticky="w")
        self.Tuning_Steps_RadioButton0.configure(
            command=self.Tuning_Steps_Set_Common)
        self.Tuning_Steps_RadioButton1 = ttk.Radiobutton(self.frame10)
        self.Tuning_Steps_RadioButton1.configure(
            style="RadioButtonNormal.TRadiobutton",
            text='10\t20\t50\t100\t1000 Hz',
            value=1,
            variable=self.Tuning_Steps_Common)
        self.Tuning_Steps_RadioButton1.grid(
            column=0, padx=38, row=2, sticky="w")
        self.Tuning_Steps_RadioButton1.configure(
            command=self.Tuning_Steps_Set_Common)
        self.Tuning_Steps_RadioButton2 = ttk.Radiobutton(self.frame10)
        self.Tuning_Steps_RadioButton2.configure(
            style="RadioButtonNormal.TRadiobutton",
            text='1\t10\t100\t1000\t10000 Hz',
            value=2,
            variable=self.Tuning_Steps_Common)
        self.Tuning_Steps_RadioButton2.grid(
            column=0, padx=38, row=3, sticky="w")
        self.Tuning_Steps_RadioButton2.configure(
            command=self.Tuning_Steps_Set_Common)
        self.Tuning_Steps_RadioButton3 = ttk.Radiobutton(self.frame10)
        self.Tuning_Steps_RadioButton3.configure(
            style="RadioButtonNormal.TRadiobutton",
            text='10\t50\t500\t5000\t10000 Hz',
            value=3,
            variable=self.Tuning_Steps_Common)
        self.Tuning_Steps_RadioButton3.grid(
            column=0, padx=38, row=4, sticky="w")
        self.Tuning_Steps_RadioButton3.configure(
            command=self.Tuning_Steps_Set_Common)
        self.Tuning_Steps_RadioButton4 = ttk.Radiobutton(self.frame10)
        self.Tuning_Steps_RadioButton4.configure(
            style="RadioButtonNormal.TRadiobutton",
            text='10\t50\t100\t2000\t50000 Hz',
            value=4,
            variable=self.Tuning_Steps_Common)
        self.Tuning_Steps_RadioButton4.grid(
            column=0, padx=38, row=5, sticky="w")
        self.Tuning_Steps_RadioButton4.configure(
            command=self.Tuning_Steps_Set_Common)
        self.frame10.pack(anchor="w", pady="20 0", side="top")
        self.frame6 = ttk.Frame(self.General_Tuning_Steps_Settings_Frame)
        self.frame6.configure(width=200)
        self.label20 = ttk.Label(self.frame6)
        self.label20.configure(style="Heading4.TLabel", text='Step#')
        self.label20.grid(column=0, padx="0 20", row=0, sticky="e")
        self.label19 = ttk.Label(self.frame6)
        self.label19.configure(style="Heading4.TLabel", text='1\t2\t3\t4\t5')
        self.label19.grid(
            column=1,
            columnspan=8,
            padx="0 20",
            row=0,
            sticky="w")
        self.label84 = ttk.Label(self.frame6)
        self.label84.configure(style="Heading4.TLabel", text='Steps (HZ)')
        self.label84.grid(column=0, padx="0 20", row=1, sticky="e")
        self.TUNING_STEP1_WIDGET = ttk.Entry(self.frame6)
        self.TUNING_STEP1 = tk.StringVar()
        self.TUNING_STEP1_WIDGET.configure(
            justify="right",
            state="disabled",
            style="Normal.TEntry",
            textvariable=self.TUNING_STEP1,
            validate="focus",
            width=7)
        self.TUNING_STEP1_WIDGET.grid(column=2, padx="0 8", row=1)
        _validatecmd = (
            self.TUNING_STEP1_WIDGET.register(
                self.validate_TUNING_STEP1), "%P", "%V")
        self.TUNING_STEP1_WIDGET.configure(validatecommand=_validatecmd)
        self.TUNING_STEP2_WIDGET = ttk.Entry(self.frame6)
        self.TUNING_STEP2 = tk.StringVar()
        self.TUNING_STEP2_WIDGET.configure(
            justify="right",
            state="disabled",
            style="Normal.TEntry",
            textvariable=self.TUNING_STEP2,
            validate="focus",
            width=7)
        self.TUNING_STEP2_WIDGET.grid(column=3, padx="0 8", row=1)
        _validatecmd = (
            self.TUNING_STEP2_WIDGET.register(
                self.validate_TUNING_STEP2), "%P", "%V")
        self.TUNING_STEP2_WIDGET.configure(validatecommand=_validatecmd)
        self.TUNING_STEP3_WIDGET = ttk.Entry(self.frame6)
        self.TUNING_STEP3 = tk.StringVar()
        self.TUNING_STEP3_WIDGET.configure(
            justify="right",
            state="disabled",
            style="Normal.TEntry",
            textvariable=self.TUNING_STEP3,
            validate="focus",
            width=7)
        self.TUNING_STEP3_WIDGET.grid(column=4, padx="0 8", row=1)
        _validatecmd = (
            self.TUNING_STEP3_WIDGET.register(
                self.validate_TUNING_STEP3), "%P", "%V")
        self.TUNING_STEP3_WIDGET.configure(validatecommand=_validatecmd)
        self.TUNING_STEP4_WIDGET = ttk.Entry(self.frame6)
        self.TUNING_STEP4 = tk.StringVar()
        self.TUNING_STEP4_WIDGET.configure(
            justify="right",
            state="disabled",
            style="Normal.TEntry",
            textvariable=self.TUNING_STEP4,
            validate="focus",
            width=7)
        self.TUNING_STEP4_WIDGET.grid(column=5, padx="0 8", row=1)
        _validatecmd = (
            self.TUNING_STEP4_WIDGET.register(
                self.validate_TUNING_STEP4), "%P", "%V")
        self.TUNING_STEP4_WIDGET.configure(validatecommand=_validatecmd)
        self.TUNING_STEP5_WIDGET = ttk.Entry(self.frame6)
        self.TUNING_STEP5 = tk.StringVar()
        self.TUNING_STEP5_WIDGET.configure(
            justify="right",
            state="disabled",
            style="Normal.TEntry",
            textvariable=self.TUNING_STEP5,
            validate="focus",
            width=7)
        self.TUNING_STEP5_WIDGET.grid(column=6, row=1)
        _validatecmd = (
            self.TUNING_STEP5_WIDGET.register(
                self.validate_TUNING_STEP5), "%P", "%V")
        self.TUNING_STEP5_WIDGET.configure(validatecommand=_validatecmd)
        self.frame6.pack(anchor="w", padx=50, side="top")
        self.frame1 = ttk.Frame(self.General_Tuning_Steps_Settings_Frame)
        self.frame1.configure(height=200, width=200)
        self.label21 = ttk.Label(self.frame1)
        self.label21.configure(style="Heading4.TLabel", text='Default Step:')
        self.label21.grid(column=0, padx=5, row=0)
        self.TUNING_STEP_INDEX_VALUE_WIDGET = ttk.Combobox(self.frame1)
        self.TUNING_STEP_INDEX_VALUE = tk.StringVar()
        self.TUNING_STEP_INDEX_VALUE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox4.TCombobox",
            textvariable=self.TUNING_STEP_INDEX_VALUE,
            validate="all",
            values='10 20 50 100 1000',
            width=5)
        self.TUNING_STEP_INDEX_VALUE_WIDGET.grid(column=1, row=0)
        self.TUNING_STEP_HIDDEN_Frame = ttk.Frame(self.frame1)
        self.TUNING_STEP_HIDDEN_Frame.configure(height=200, width=200)
        self.TUNING_STEP_INDEX_WIDGET = ttk.Label(
            self.TUNING_STEP_HIDDEN_Frame)
        self.TUNING_STEP_INDEX = tk.StringVar()
        self.TUNING_STEP_INDEX_WIDGET.configure(
            textvariable=self.TUNING_STEP_INDEX)
        self.TUNING_STEP_INDEX_WIDGET.pack()
        self.TUNING_STEP_HIDDEN_Frame.grid(column=0, row=2)
        self.frame1.pack(anchor="w", pady="10 0", side="top")
        self.General_Tuning_Steps_Settings_Frame.pack(padx="50 0", side="top")
        self.General_Tuning_Steps_Frame.pack(anchor="w", side="top")
        self.frame7 = ttk.Frame(self.General_Frame)
        self.frame7.configure(height=200, width=200)
        self.separator4 = ttk.Separator(self.frame7)
        self.separator4.configure(orient="horizontal")
        self.separator4.pack(
            anchor="center",
            expand="true",
            fill="x",
            side="top")
        self.frame7.pack(anchor="w", expand="true", fill="x", side="top")
        self.General_CW_Frame = ttk.Frame(self.General_Frame)
        self.General_CW_Frame.configure(height=200, width=200)
        self.Operator_CW_Title_Frame = ttk.Frame(self.General_CW_Frame)
        self.Operator_CW_Title_Frame.configure(height=200, width=200)
        self.General_Settings_CW_Label = ttk.Label(
            self.Operator_CW_Title_Frame)
        self.General_Settings_CW_Label.configure(
            style="Heading3.TLabel", text='CW')
        self.General_Settings_CW_Label.pack(
            anchor="w", expand="true", fill="x", pady="20 0")
        self.Operator_CW_Title_Frame.pack(
            anchor="w", expand="true", fill="x", side="top")
        self.General_CW_Settings_Frame = ttk.Frame(self.General_CW_Frame)
        self.General_CW_Settings_Frame.configure(height=200, width=200)
        self.CW_KEY_TYPE_LABEL = ttk.Label(self.General_CW_Settings_Frame)
        self.CW_KEY_TYPE_LABEL.configure(
            style="Heading4.TLabel", text='Key Type')
        self.CW_KEY_TYPE_LABEL.grid(column=0, pady="0 10", row=0)
        self.CW_KEY_TYPE = tk.StringVar(value='STRAIGHT')
        __values = ['STRAIGHT', 'IAMBICA', 'IAMBICB']
        self.CW_KEY_TYPE_WIDGET = tk.OptionMenu(
            self.General_CW_Settings_Frame,
            self.CW_KEY_TYPE,
            *__values,
            command=None)
        self.CW_KEY_TYPE_WIDGET.grid(column=1, row=0, sticky="w")
        self.CW_SIDETONE_LABEL = ttk.Label(self.General_CW_Settings_Frame)
        self.CW_SIDETONE_LABEL.configure(
            style="Heading4.TLabel", text='Sidetone (HZ)')
        self.CW_SIDETONE_LABEL.grid(column=0, row=2, sticky="w")
        self.CW_SIDETONE_WIDGET = ttk.Entry(self.General_CW_Settings_Frame)
        self.CW_SIDETONE = tk.StringVar()
        self.CW_SIDETONE_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CW_SIDETONE,
            validate="focus",
            width=10)
        self.CW_SIDETONE_WIDGET.grid(column=1, row=2)
        _validatecmd = (
            self.CW_SIDETONE_WIDGET.register(
                self.validate_CW_SIDETONE), "%P", "%V")
        self.CW_SIDETONE_WIDGET.configure(validatecommand=_validatecmd)
        self.CW_SPEED_WPM_LABEL = ttk.Label(self.General_CW_Settings_Frame)
        self.CW_SPEED_WPM_LABEL.configure(
            style="Heading4.TLabel", text='Speed (WPM)')
        self.CW_SPEED_WPM_LABEL.grid(column=0, row=6, sticky="w")
        self.CW_SPEED_WPM_WIDGET = ttk.Entry(self.General_CW_Settings_Frame)
        self.CW_SPEED_WPM = tk.StringVar()
        self.CW_SPEED_WPM_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CW_SPEED_WPM,
            validate="focus",
            width=10)
        self.CW_SPEED_WPM_WIDGET.grid(column=1, row=6)
        _validatecmd = (
            self.CW_SPEED_WPM_WIDGET.register(
                self.validate_CW_SPEED_WPM), "%P", "%V")
        self.CW_SPEED_WPM_WIDGET.configure(validatecommand=_validatecmd)
        self.CW_START_MS_LABEL = ttk.Label(self.General_CW_Settings_Frame)
        self.CW_START_MS_LABEL.configure(
            style="Heading4.TLabel",
            text='Delay Starting TX (ms)')
        self.CW_START_MS_LABEL.grid(column=0, row=10, sticky="w")
        self.CW_START_MS_WIDGET = ttk.Entry(self.General_CW_Settings_Frame)
        self.CW_START_MS = tk.StringVar()
        self.CW_START_MS_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CW_START_MS,
            validate="focus",
            width=10)
        self.CW_START_MS_WIDGET.grid(column=1, row=10)
        _validatecmd = (
            self.CW_START_MS_WIDGET.register(
                self.validate_CW_START_MS), "%P", "%V")
        self.CW_START_MS_WIDGET.configure(validatecommand=_validatecmd)
        self.CW_DELAY_MS_LABEL = ttk.Label(self.General_CW_Settings_Frame)
        self.CW_DELAY_MS_LABEL.configure(
            style="Heading4.TLabel",
            text='Delay Returning to RX (ms)')
        self.CW_DELAY_MS_LABEL.grid(column=0, row=14, sticky="w")
        self.CW_DELAY_MS_WIDGET = ttk.Entry(self.General_CW_Settings_Frame)
        self.CW_DELAY_MS = tk.StringVar()
        self.CW_DELAY_MS_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CW_DELAY_MS,
            validate="focus",
            width=10)
        self.CW_DELAY_MS_WIDGET.grid(column=1, row=14)
        _validatecmd = (
            self.CW_DELAY_MS_WIDGET.register(
                self.validate_CW_DELAY_MS), "%P", "%V")
        self.CW_DELAY_MS_WIDGET.configure(validatecommand=_validatecmd)
        self.label209 = ttk.Label(self.General_CW_Settings_Frame)
        self.label209.configure(
            style="Heading4.TLabel",
            text='VFO Freq displays')
        self.label209.grid(column=0, pady="0 10", row=15)
        self.CW_DISPLAY_FREQ = tk.StringVar(value='TX')
        __values = ['TX', 'RX']
        self.CW_DISPLAY_FREQ_WIDGET = tk.OptionMenu(
            self.General_CW_Settings_Frame, self.CW_DISPLAY_FREQ, *__values, command=None)
        self.CW_DISPLAY_FREQ_WIDGET.grid(column=1, pady=10, row=15)
        self.message8 = tk.Message(self.General_CW_Settings_Frame)
        self.message8.configure(
            borderwidth=2,
            font="TkTextFont",
            justify="left",
            pady=5,
            relief="ridge",
            takefocus=False,
            text='When in CW mode, your VFO can display either your TX or RX frequency. TX seems to be generally the preferred choice. For more details, see:\nhttp://www.hamskey.com/2018/07/cw-frequency-in-ubitx.html',
            width=350)
        self.message8.grid(column=2, padx=10, row=15)
        self.General_CW_Settings_Frame.pack(padx="50 0", side="top")
        self.General_CW_Frame.pack(anchor="w", side="top")
        self.frame48 = ttk.Frame(self.General_Frame)
        self.frame48.configure(height=200, width=200)
        self.separator5 = ttk.Separator(self.frame48)
        self.separator5.configure(orient="horizontal")
        self.separator5.pack(
            anchor="center",
            expand="true",
            fill="x",
            pady=10,
            side="top")
        self.frame48.pack(anchor="w", expand="true", fill="x", side="top")
        self.IF_CUSTOMIZATION_Frame = ttk.Frame(self.General_Frame)
        self.IF_CUSTOMIZATION_Frame.configure(height=200, width=200)
        self.frame61 = ttk.Frame(self.IF_CUSTOMIZATION_Frame)
        self.frame61.configure(height=200, width=200)
        self.label207 = ttk.Label(self.frame61)
        self.label207.configure(
            style="Heading3.TLabel",
            text='Personalized IF Shift')
        self.label207.grid(column=0, row=0)
        self.frame61.pack(anchor="w", expand="true", fill="x", side="top")
        self.frame62 = ttk.Frame(self.IF_CUSTOMIZATION_Frame)
        self.frame62.configure(height=200, width=200)
        self.STORED_IF_SHIFT_WIDGET = ttk.Checkbutton(self.frame62)
        self.STORED_IF_SHIFT = tk.StringVar()
        self.STORED_IF_SHIFT_WIDGET.configure(
            offvalue="NO",
            onvalue="YES",
            style="Checkbox4.TCheckbutton",
            text='Preserve IF Shift',
            variable=self.STORED_IF_SHIFT)
        self.STORED_IF_SHIFT_WIDGET.pack(anchor="w", side="top")
        self.STORED_IF_SHIFT_WIDGET.configure(
            command=self.toggle_IF1_Calibration_Frame)
        self.frame63 = ttk.Frame(self.frame62)
        self.frame63.configure(height=200, width=200)
        self.label208 = ttk.Label(self.frame63)
        self.label208.configure(
            style="Heading4.TLabel",
            text='Amount to Shift IF:')
        self.label208.grid(column=0, row=0)
        self.IF_SHIFTVALUE_WIDGET = ttk.Entry(self.frame63)
        self.IF_SHIFTVALUE = tk.StringVar()
        self.IF_SHIFTVALUE_WIDGET.configure(
            textvariable=self.IF_SHIFTVALUE, validate="focus")
        self.IF_SHIFTVALUE_WIDGET.grid(column=1, row=0)
        _validatecmd = (
            self.IF_SHIFTVALUE_WIDGET.register(
                self.validate_IF_SHIFTVALUE), "%P", "%V")
        self.IF_SHIFTVALUE_WIDGET.configure(validatecommand=_validatecmd)
        self.frame63.pack(anchor="e", padx=70, side="top")
        self.frame62.pack(anchor="w", padx="50 0", side="top")
        self.IF_CUSTOMIZATION_Frame.pack(anchor="w", side="top")
        self.General_Frame.pack(
            expand="true",
            fill="both",
            padx=20,
            pady=5,
            side="top")
        self.frame15.pack(
            anchor="center",
            expand="true",
            fill="both",
            padx=5,
            pady=5,
            side="top")
        self.General_SF.pack(
            anchor="center",
            expand="true",
            fill="both",
            side="top")
        self.settingsNotebook.add(self.General_SF, text='General')
        self.Autokeyer_SF = ScrolledFrame(
            self.settingsNotebook, scrolltype="both")
        self.Autokeyer_SF.configure(usemousewheel=True)
        self.Autokeyer_Frame = ttk.Frame(self.Autokeyer_SF.innerframe)
        self.CW_Autokeyer_Titlle_Frame = ttk.Frame(self.Autokeyer_Frame)
        self.CW_Autokeyer_Titlle_Frame.configure(height=200, width=200)
        self.label3 = ttk.Label(self.CW_Autokeyer_Titlle_Frame)
        self.label3.configure(
            justify="center",
            style="Heading2.TLabel",
            text='CW Autokeyer Settings')
        self.label3.pack(anchor="w", padx=5)
        self.CW_Autokeyer_Titlle_Frame.pack(
            anchor="center", fill="x", pady="15 25", side="top")
        self.CW_Autokeyer_Callsign_Frame = ttk.Frame(self.Autokeyer_Frame)
        self.CW_Autokeyer_Callsign_Frame.configure(height=200, width=200)
        self.CW_Autokeyer_Callsigns_Label_Frame = ttk.Frame(
            self.CW_Autokeyer_Callsign_Frame)
        self.CW_Autokeyer_Callsigns_Label_Frame.configure(
            height=200, width=200)
        self.CW_Autokeyer_Callsign_Title_Label = ttk.Label(
            self.CW_Autokeyer_Callsigns_Label_Frame)
        self.CW_Autokeyer_Callsign_Title_Label.configure(
            justify="left", style="Heading3.TLabel", text='Callsigns')
        self.CW_Autokeyer_Callsign_Title_Label.pack()
        self.CW_Autokeyer_Callsigns_Label_Frame.pack(anchor="w", side="top")
        self.CW_Autokeyer_Callsigns_Frame = ttk.Frame(
            self.CW_Autokeyer_Callsign_Frame)
        self.CW_Autokeyer_Callsigns_Frame.configure(height=200, width=200)
        self.CW_Autokeyer_Callsign_Label = ttk.Label(
            self.CW_Autokeyer_Callsigns_Frame)
        self.CW_Autokeyer_Callsign_Label.configure(
            style="Heading4.TLabel", text='Callsign')
        self.CW_Autokeyer_Callsign_Label.grid(
            column=0, padx="0 10", row=0, sticky="w")
        self.USER_CALLSIGN_WIDGET_2 = ttk.Entry(
            self.CW_Autokeyer_Callsigns_Frame)
        self.USER_CALLSIGN_WIDGET_2.configure(
            justify="left",
            textvariable=self.USER_CALLSIGN,
            validate="focus",
            width=18)
        self.USER_CALLSIGN_WIDGET_2.grid(
            column=1, padx="0 10", row=0, sticky="w")
        _validatecmd = (
            self.USER_CALLSIGN_WIDGET_2.register(
                self.validate_USER_CALLSIGN), "%P", "%V")
        self.USER_CALLSIGN_WIDGET_2.configure(validatecommand=_validatecmd)
        self.CW_Autokeyer_Alt_Callsign_Label = ttk.Label(
            self.CW_Autokeyer_Callsigns_Frame)
        self.CW_Autokeyer_Alt_Callsign_Label.configure(
            style="Heading4.TLabel", text='Alternate QSO Callsign')
        self.CW_Autokeyer_Alt_Callsign_Label.grid(
            column=0, padx="0 10", row=1, sticky="w")
        self.QSO_CALLSIGN_WIDGET = ttk.Entry(self.CW_Autokeyer_Callsigns_Frame)
        self.QSO_CALLSIGN = tk.StringVar()
        self.QSO_CALLSIGN_WIDGET.configure(
            justify="left",
            textvariable=self.QSO_CALLSIGN,
            validate="focus",
            width=18)
        self.QSO_CALLSIGN_WIDGET.grid(column=1, padx="0 10", row=1, sticky="w")
        _validatecmd = (
            self.QSO_CALLSIGN_WIDGET.register(
                self.validate_QSO_CALLSIGN), "%P", "%V")
        self.QSO_CALLSIGN_WIDGET.configure(validatecommand=_validatecmd)
        self.label164 = ttk.Label(self.CW_Autokeyer_Callsigns_Frame)
        self.QSO_CALLSIGN_LENGTH = tk.StringVar()
        self.label164.configure(
            justify="left",
            textvariable=self.QSO_CALLSIGN_LENGTH)
        self.label164.grid(column=0, row=2)
        self.CW_Autokeyer_Callsigns_Frame.pack(
            anchor="w", padx="50 0", side="top")
        self.CW_Autokeyer_Callsign_Frame.pack(anchor="w", padx=20, side="top")
        self.frame5 = ttk.Frame(self.Autokeyer_Frame)
        self.frame5.configure(height=200, width=200)
        self.frame31 = ttk.Frame(self.frame5)
        self.frame31.configure(height=200, width=200)
        self.frame32 = ttk.Frame(self.frame31)
        self.frame32.configure(height=200, width=200)
        self.label25 = ttk.Label(self.frame32)
        self.label25.configure(
            compound="top",
            justify="left",
            style="Heading3.TLabel",
            text='CW Keyer Messages')
        self.label25.pack()
        self.frame32.pack(anchor="w", side="top")
        self.frame20 = ttk.Frame(self.frame31)
        self.frame20.configure(height=200, width=200)
        self.CW_AUTO_COUNT_LABEL = ttk.Label(self.frame20)
        self.CW_AUTO_COUNT_LABEL.configure(
            style="Heading4.TLabel", text='Total Msgs (max 25)')
        self.CW_AUTO_COUNT_LABEL.pack(padx="10 10", side="left")
        self.CW_AUTO_COUNT_WIDGET = ttk.Entry(self.frame20)
        self.CW_AUTO_COUNT = tk.StringVar()
        self.CW_AUTO_COUNT_WIDGET.configure(
            justify="left",
            state="readonly",
            textvariable=self.CW_AUTO_COUNT,
            validate="none",
            width=3)
        self.CW_AUTO_COUNT_WIDGET.pack(anchor="w", side="left")
        self.label53 = ttk.Label(self.frame20)
        self.label53.configure(
            relief="flat",
            style="Heading4.TLabel",
            text='Total Bytes Used:')
        self.label53.pack(padx="20 10", side="left")
        self.CW_AUTO_BYTES_USED_WIDGET = ttk.Entry(self.frame20)
        self.CW_AUTO_BYTES_USED = tk.StringVar()
        self.CW_AUTO_BYTES_USED_WIDGET.configure(
            justify="left",
            state="readonly",
            style="Normal.TEntry",
            takefocus=False,
            textvariable=self.CW_AUTO_BYTES_USED,
            validate="none",
            width=3)
        self.CW_AUTO_BYTES_USED_WIDGET.pack(anchor="w", side="left")
        self.label163 = ttk.Label(self.frame20)
        self.label163.configure(
            relief="flat",
            style="Heading4.TLabel",
            takefocus=False,
            text='Remaining Bytes')
        self.label163.pack(padx="20 10", side="left")
        self.CW_AUTO_REMAINING_BYTES_WIDGET = ttk.Entry(self.frame20)
        self.CW_AUTO_REMAINING_BYTES = tk.StringVar()
        self.CW_AUTO_REMAINING_BYTES_WIDGET.configure(
            justify="left",
            state="readonly",
            takefocus=False,
            textvariable=self.CW_AUTO_REMAINING_BYTES,
            validate="none",
            width=3)
        self.CW_AUTO_REMAINING_BYTES_WIDGET.pack(anchor="w", side="left")
        self.frame20.pack(anchor="center", padx="10 0", pady="10 20")
        self.frame33 = ttk.Frame(self.frame31)
        self.frame33.configure(height=200, width=200)
        self.label54 = ttk.Label(self.frame33)
        self.label54.configure(style="Heading4.TLabel", text='Msg#')
        self.label54.grid(column=0, padx="0 10", row=0, sticky="e")
        self.label57 = ttk.Label(self.frame33)
        self.label57.configure(style="Heading4.TLabel", text='Message Content')
        self.label57.grid(column=1, padx="0 10", row=0)
        self.label26 = ttk.Label(self.frame33)
        self.label26.configure(style="Heading4.TLabel", text='0')
        self.label26.grid(column=0, padx="0 10", row=1, sticky="e")
        self.CW_MEMORY_KEYER_MSG0_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSG0 = tk.StringVar()
        self.CW_MEMORY_KEYER_MSG0_WIDGET.configure(
            justify="left",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSG0,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSG0_WIDGET.grid(
            column=1, padx="0 10", row=1, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSG0_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSG0_WIDGET.configure(
            validatecommand=_validatecmd)
        self.CW_MEMORY_KEYER_MSG01_LABEL = ttk.Label(self.frame33)
        self.CW_MEMORY_KEYER_MSG01_LABEL.configure(
            style="Heading4.TLabel", text='1')
        self.CW_MEMORY_KEYER_MSG01_LABEL.grid(
            column=0, padx="0 10", row=2, sticky="e")
        self.CW_MEMORY_KEYER_MSG1_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSG1 = tk.StringVar()
        self.CW_MEMORY_KEYER_MSG1_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSG1,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSG1_WIDGET.grid(
            column=1, padx="0 10", row=2, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSG1_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSG1_WIDGET.configure(
            validatecommand=_validatecmd)
        self.CW_MEMORY_KEYER_MSG02_LABEL = ttk.Label(self.frame33)
        self.CW_MEMORY_KEYER_MSG02_LABEL.configure(
            style="Heading4.TLabel", text='2')
        self.CW_MEMORY_KEYER_MSG02_LABEL.grid(
            column=0, padx="0 10", row=3, sticky="e")
        self.CW_MEMORY_KEYER_MSG2_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSG2 = tk.StringVar()
        self.CW_MEMORY_KEYER_MSG2_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSG2,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSG2_WIDGET.grid(
            column=1, padx="0 10", row=3, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSG2_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSG2_WIDGET.configure(
            validatecommand=_validatecmd)
        self.CW_MEMORY_KEYER_MSG03_LABEL = ttk.Label(self.frame33)
        self.CW_MEMORY_KEYER_MSG03_LABEL.configure(
            style="Heading4.TLabel", text='3')
        self.CW_MEMORY_KEYER_MSG03_LABEL.grid(
            column=0, padx="0 10", row=4, sticky="e")
        self.CW_MEMORY_KEYER_MSG3_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSG3 = tk.StringVar()
        self.CW_MEMORY_KEYER_MSG3_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSG3,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSG3_WIDGET.grid(
            column=1, padx="0 10", row=4, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSG3_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSG3_WIDGET.configure(
            validatecommand=_validatecmd)
        self.CW_MEMORY_KEYER_MSG04_LABEL = ttk.Label(self.frame33)
        self.CW_MEMORY_KEYER_MSG04_LABEL.configure(
            style="Heading4.TLabel", text='4')
        self.CW_MEMORY_KEYER_MSG04_LABEL.grid(
            column=0, padx="0 10", row=5, sticky="e")
        self.CW_MEMORY_KEYER_MSG4_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSG4 = tk.StringVar()
        self.CW_MEMORY_KEYER_MSG4_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSG4,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSG4_WIDGET.grid(
            column=1, padx="0 10", row=5, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSG4_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSG4_WIDGET.configure(
            validatecommand=_validatecmd)
        self.CW_MEMORY_KEYER_MSG05_LABEL = ttk.Label(self.frame33)
        self.CW_MEMORY_KEYER_MSG05_LABEL.configure(
            style="Heading4.TLabel", text='5')
        self.CW_MEMORY_KEYER_MSG05_LABEL.grid(
            column=0, padx="0 10", row=6, sticky="e")
        self.CW_MEMORY_KEYER_MSG5_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSG5 = tk.StringVar()
        self.CW_MEMORY_KEYER_MSG5_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSG5,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSG5_WIDGET.grid(
            column=1, padx="0 10", row=6, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSG5_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSG5_WIDGET.configure(
            validatecommand=_validatecmd)
        self.CW_MEMORY_KEYER_MSG06_LABEL = ttk.Label(self.frame33)
        self.CW_MEMORY_KEYER_MSG06_LABEL.configure(
            style="Heading4.TLabel", text='6')
        self.CW_MEMORY_KEYER_MSG06_LABEL.grid(
            column=0, padx="0 10", row=7, sticky="e")
        self.CW_MEMORY_KEYER_MSG6_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSG6 = tk.StringVar()
        self.CW_MEMORY_KEYER_MSG6_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSG6,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSG6_WIDGET.grid(
            column=1, padx="0 10", row=7, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSG6_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSG6_WIDGET.configure(
            validatecommand=_validatecmd)
        self.CW_MEMORY_KEYER_MSG07_LABEL = ttk.Label(self.frame33)
        self.CW_MEMORY_KEYER_MSG07_LABEL.configure(
            style="Heading4.TLabel", text='7')
        self.CW_MEMORY_KEYER_MSG07_LABEL.grid(
            column=0, padx="0 10", row=8, sticky="e")
        self.CW_MEMORY_KEYER_MSG7_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSG7 = tk.StringVar()
        self.CW_MEMORY_KEYER_MSG7_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSG7,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSG7_WIDGET.grid(
            column=1, padx="0 10", row=8, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSG7_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSG7_WIDGET.configure(
            validatecommand=_validatecmd)
        self.CW_MEMORY_KEYER_MSG08_LABEL = ttk.Label(self.frame33)
        self.CW_MEMORY_KEYER_MSG08_LABEL.configure(
            style="Heading4.TLabel", text='8')
        self.CW_MEMORY_KEYER_MSG08_LABEL.grid(
            column=0, padx="0 10", row=9, sticky="e")
        self.CW_MEMORY_KEYER_MSG8_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSG8 = tk.StringVar()
        self.CW_MEMORY_KEYER_MSG8_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSG8,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSG8_WIDGET.grid(
            column=1, padx="0 10", row=9, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSG8_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSG8_WIDGET.configure(
            validatecommand=_validatecmd)
        self.CW_MEMORY_KEYER_MSG09_LABEL = ttk.Label(self.frame33)
        self.CW_MEMORY_KEYER_MSG09_LABEL.configure(
            style="Heading4.TLabel", text='9')
        self.CW_MEMORY_KEYER_MSG09_LABEL.grid(
            column=0, padx="0 10", row=10, sticky="e")
        self.CW_MEMORY_KEYER_MSG9_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSG9 = tk.StringVar()
        self.CW_MEMORY_KEYER_MSG9_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSG9,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSG9_WIDGET.grid(
            column=1, padx="0 10", row=10, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSG9_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSG9_WIDGET.configure(
            validatecommand=_validatecmd)
        self.CW_MEMORY_KEYER_MSG10_LABEL = ttk.Label(self.frame33)
        self.CW_MEMORY_KEYER_MSG10_LABEL.configure(
            style="Heading4.TLabel", text='A')
        self.CW_MEMORY_KEYER_MSG10_LABEL.grid(
            column=0, padx="0 10", row=11, sticky="e")
        self.CW_MEMORY_KEYER_MSGA_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSGA = tk.StringVar()
        self.CW_MEMORY_KEYER_MSGA_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSGA,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSGA_WIDGET.grid(
            column=1, padx="0 10", row=11, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSGA_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSGA_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label56 = ttk.Label(self.frame33)
        self.label56.configure(style="Heading4.TLabel", text='B')
        self.label56.grid(column=0, padx="0 10", row=12, sticky="e")
        self.CW_MEMORY_KEYER_MSGB_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSGB = tk.StringVar()
        self.CW_MEMORY_KEYER_MSGB_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSGB,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSGB_WIDGET.grid(
            column=1, padx="0 10", row=12, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSGB_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSGB_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label59 = ttk.Label(self.frame33)
        self.label59.configure(style="Heading4.TLabel", text='C')
        self.label59.grid(column=0, padx="0 10", row=13, sticky="e")
        self.CW_MEMORY_KEYER_MSGC_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSGC = tk.StringVar()
        self.CW_MEMORY_KEYER_MSGC_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSGC,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSGC_WIDGET.grid(
            column=1, padx="0 10", row=13, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSGC_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSGC_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label60 = ttk.Label(self.frame33)
        self.label60.configure(style="Heading4.TLabel", text='D')
        self.label60.grid(column=0, padx="0 10", row=14, sticky="e")
        self.CW_MEMORY_KEYER_MSGD_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSGD = tk.StringVar()
        self.CW_MEMORY_KEYER_MSGD_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSGD,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSGD_WIDGET.grid(
            column=1, padx="0 10", row=14, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSGD_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSGD_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label63 = ttk.Label(self.frame33)
        self.label63.configure(style="Heading4.TLabel", text='E')
        self.label63.grid(column=0, padx="0 10", row=15, sticky="e")
        self.CW_MEMORY_KEYER_MSGE_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSGE = tk.StringVar()
        self.CW_MEMORY_KEYER_MSGE_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSGE,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSGE_WIDGET.grid(
            column=1, padx="0 10", row=15, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSGE_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSGE_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label67 = ttk.Label(self.frame33)
        self.label67.configure(style="Heading4.TLabel", text='F')
        self.label67.grid(column=0, padx="0 10", row=16, sticky="e")
        self.CW_MEMORY_KEYER_MSGF_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSGF = tk.StringVar()
        self.CW_MEMORY_KEYER_MSGF_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSGF,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSGF_WIDGET.grid(
            column=1, padx="0 10", row=16, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSGF_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSGF_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label154 = ttk.Label(self.frame33)
        self.label154.configure(style="Heading4.TLabel", text='G')
        self.label154.grid(column=0, padx="0 10", row=17, sticky="e")
        self.CW_MEMORY_KEYER_MSGG_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSGG = tk.StringVar()
        self.CW_MEMORY_KEYER_MSGG_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSGG,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSGG_WIDGET.grid(
            column=1, padx="0 10", row=17, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSGG_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSGG_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label155 = ttk.Label(self.frame33)
        self.label155.configure(style="Heading4.TLabel", text='H')
        self.label155.grid(column=0, padx="0 10", row=18, sticky="e")
        self.CW_MEMORY_KEYER_MSGH_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSGH = tk.StringVar()
        self.CW_MEMORY_KEYER_MSGH_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSGH,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSGH_WIDGET.grid(
            column=1, padx="0 10", row=18, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSGH_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSGH_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label156 = ttk.Label(self.frame33)
        self.label156.configure(style="Heading4.TLabel", text='I')
        self.label156.grid(column=0, padx="0 10", row=19, sticky="e")
        self.CW_MEMORY_KEYER_MSGI_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSGI = tk.StringVar()
        self.CW_MEMORY_KEYER_MSGI_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSGI,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSGI_WIDGET.grid(
            column=1, padx="0 10", row=19, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSGI_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSGI_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label157 = ttk.Label(self.frame33)
        self.label157.configure(style="Heading4.TLabel", text='J')
        self.label157.grid(column=0, padx="0 10", row=20, sticky="e")
        self.CW_MEMORY_KEYER_MSGJ_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSGJ = tk.StringVar()
        self.CW_MEMORY_KEYER_MSGJ_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSGJ,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSGJ_WIDGET.grid(
            column=1, padx="0 10", row=20, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSGJ_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSGJ_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label158 = ttk.Label(self.frame33)
        self.label158.configure(style="Heading4.TLabel", text='K')
        self.label158.grid(column=0, padx="0 10", row=21, sticky="e")
        self.CW_MEMORY_KEYER_MSGK_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSGK = tk.StringVar()
        self.CW_MEMORY_KEYER_MSGK_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSGK,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSGK_WIDGET.grid(
            column=1, padx="0 10", row=21, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSGK_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSGK_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label159 = ttk.Label(self.frame33)
        self.label159.configure(style="Heading4.TLabel", text='L')
        self.label159.grid(column=0, padx="0 10", row=22, sticky="e")
        self.CW_MEMORY_KEYER_MSGL_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSGL = tk.StringVar()
        self.CW_MEMORY_KEYER_MSGL_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSGL,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSGL_WIDGET.grid(
            column=1, padx="0 10", row=22, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSGL_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSGL_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label160 = ttk.Label(self.frame33)
        self.label160.configure(style="Heading4.TLabel", text='M')
        self.label160.grid(column=0, padx="0 10", row=23, sticky="e")
        self.CW_MEMORY_KEYER_MSGM_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSGM = tk.StringVar()
        self.CW_MEMORY_KEYER_MSGM_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSGM,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSGM_WIDGET.grid(
            column=1, padx="0 10", row=23, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSGM_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSGM_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label161 = ttk.Label(self.frame33)
        self.label161.configure(style="Heading4.TLabel", text='N')
        self.label161.grid(column=0, padx="0 10", row=24, sticky="e")
        self.CW_MEMORY_KEYER_MSGN_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSGN = tk.StringVar()
        self.CW_MEMORY_KEYER_MSGN_WIDGET.configure(
            justify="left",
            state="disabled",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSGN,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSGN_WIDGET.grid(
            column=1, padx="0 10", row=24, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSGN_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSGN_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label162 = ttk.Label(self.frame33)
        self.label162.configure(style="Heading4.TLabel", text='O')
        self.label162.grid(column=0, padx="0 10", row=25, sticky="e")
        self.CW_MEMORY_KEYER_MSGO_WIDGET = ttk.Entry(self.frame33)
        self.CW_MEMORY_KEYER_MSGO = tk.StringVar()
        self.CW_MEMORY_KEYER_MSGO_WIDGET.configure(
            justify="left",
            state="readonly",
            takefocus=True,
            textvariable=self.CW_MEMORY_KEYER_MSGO,
            validate="focus",
            width=50)
        self.CW_MEMORY_KEYER_MSGO_WIDGET.grid(
            column=1, padx="0 10", row=25, sticky="w")
        _validatecmd = (self.CW_MEMORY_KEYER_MSGO_WIDGET.register(
            self.validate_CW_Message_Change), "%P", "%V", "%W")
        self.CW_MEMORY_KEYER_MSGO_WIDGET.configure(
            validatecommand=_validatecmd)
        self.CW_Auto_Msg_Cleanup_Button_WIDGET = ttk.Button(self.frame33)
        self.CW_Auto_Msg_Cleanup_Button_WIDGET.configure(
            style="Button4.TButton", text='Cleanup')
        self.CW_Auto_Msg_Cleanup_Button_WIDGET.grid(column=2, padx=10, row=0)
        self.CW_Auto_Msg_Cleanup_Button_WIDGET.configure(
            command=self.CW_Auto_Msg_Cleanup_CB)
        self.frame33.pack(anchor="n", padx="50 0", side="left")
        self.frame31.grid(column=0, row=0)
        self.frame23 = ttk.Frame(self.frame5)
        self.frame23.configure(height=200, width=200)
        self.label86 = ttk.Label(self.frame23)
        self.label86.configure(style="Heading3.TLabel", text='CW Macros:')
        self.label86.grid(column=0, pady="0 5", row=0)
        self.message2 = tk.Message(self.frame23)
        self.message2.configure(
            borderwidth=2,
            font="TkTextFont",
            justify="left",
            pady=5,
            relief="ridge",
            takefocus=False,
            text='>\tCallsign\n<\tQSO Callsign\n#\tAR\n[\tAS\n]\tSK\n~\tBT\n^\tKN\n\'\tStart\n"\tEnd',
            width=200)
        self.message2.grid(column=0, row=2, sticky="ew")
        self.label88 = ttk.Label(self.frame23)
        self.label88.configure(
            style="Heading4.TLabel",
            text='Chr\tReplacement')
        self.label88.grid(column=0, row=1, sticky="ew")
        self.frame23.grid(column=1, padx="20 0", pady=80, row=0, sticky="n")
        self.CW_Autokeyer_Hidden_Frame = ttk.Frame(self.frame5)
        self.CW_Autokeyer_Hidden_Frame.configure(height=200, width=200)
        self.CW_AUTO_MAGIC_KEY_WIDGET = ttk.Label(
            self.CW_Autokeyer_Hidden_Frame)
        self.CW_AUTO_MAGIC_KEY = tk.StringVar()
        self.CW_AUTO_MAGIC_KEY_WIDGET.configure(
            state="disabled", textvariable=self.CW_AUTO_MAGIC_KEY)
        self.CW_AUTO_MAGIC_KEY_WIDGET.pack(side="top")
        self.USER_CALLSIGN_KEY_WIDGET = ttk.Label(
            self.CW_Autokeyer_Hidden_Frame)
        self.USER_CALLSIGN_KEY = tk.StringVar()
        self.USER_CALLSIGN_KEY_WIDGET.configure(
            state="disabled", textvariable=self.USER_CALLSIGN_KEY)
        self.USER_CALLSIGN_KEY_WIDGET.pack(side="top")
        self.CW_AUTO_DATA_WIDGET = ttk.Label(self.CW_Autokeyer_Hidden_Frame)
        self.CW_AUTO_DATA = tk.StringVar()
        self.CW_AUTO_DATA_WIDGET.configure(
            state="disabled",
            takefocus=False,
            textvariable=self.CW_AUTO_DATA)
        self.CW_AUTO_DATA_WIDGET.pack(padx="10 0", side="top")
        self.CW_Autokeyer_Hidden_Frame.grid(row=1)
        self.frame5.pack(expand="true", fill="both", side="top")
        self.Autokeyer_Frame.pack(
            anchor="center",
            expand="true",
            fill="both",
            padx=5,
            pady=5,
            side="top")
        self.Autokeyer_SF.pack(side="top")
        self.settingsNotebook.add(self.Autokeyer_SF, text='CW Keyer')
        self.Bands_SF = ScrolledFrame(self.settingsNotebook, scrolltype="both")
        self.Bands_SF.configure(usemousewheel=True)
        self.frame16 = ttk.Frame(self.Bands_SF.innerframe)
        self.frame16.configure(height=200, width=200)
        self.Bands_Setting_Title_Frame = ttk.Frame(self.frame16)
        self.Bands_Setting_Title_Frame.configure(height=200, width=200)
        self.Bands_Settings_Label = ttk.Label(self.Bands_Setting_Title_Frame)
        self.Bands_Settings_Label.configure(
            justify="center",
            style="Heading2.TLabel",
            text='Bands Settings')
        self.Bands_Settings_Label.pack(anchor="w", padx=5, pady="15 25")
        self.Bands_Setting_Title_Frame.pack(fill="x", side="top")
        self.frame19 = ttk.Frame(self.frame16)
        self.frame19.configure(height=200, width=200)
        self.frame46 = ttk.Frame(self.frame19)
        self.label104 = ttk.Label(self.frame46)
        self.label104.configure(
            style="Heading4.TLabel",
            text='# of Bands Defined')
        self.label104.grid(
            column=1,
            columnspan=3,
            padx="0 15",
            row=7,
            sticky="w")
        self.HAM_BAND_COUNT_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_COUNT = tk.StringVar()
        self.HAM_BAND_COUNT_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_COUNT,
            validate="focus",
            width=3)
        self.HAM_BAND_COUNT_WIDGET.grid(
            column=4, padx="0 5", row=7, sticky="w")
        _validatecmd = (
            self.HAM_BAND_COUNT_WIDGET.register(
                self.validate_HAM_BAND_COUNT), "%P", "%V")
        self.HAM_BAND_COUNT_WIDGET.configure(validatecommand=_validatecmd)
        self.label100 = ttk.Label(self.frame46)
        self.label100.configure(
            justify="center",
            style="Heading4.TLabel",
            text='Frequency Range')
        self.label100.grid(column=3, columnspan=3, pady="20 0", row=8)
        self.label101 = ttk.Label(self.frame46)
        self.label101.configure(style="Heading4.TLabel", text='Start')
        self.label101.grid(column=3, row=9, sticky="s")
        self.label102 = ttk.Label(self.frame46)
        self.label102.configure(style="Heading4.TLabel", text='End')
        self.label102.grid(column=5, row=9, sticky="s")
        self.label106 = ttk.Label(self.frame46)
        self.label106.configure(style="Heading4.TLabel", text='Band 1')
        self.label106.grid(column=1, pady="0 5", row=10, sticky="w")
        self.HAM_BAND_RANGE1_START_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE1_START = tk.StringVar()
        self.HAM_BAND_RANGE1_START_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE1_START,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE1_START_WIDGET.grid(
            column=3, padx="0 2", pady="0 5", row=10, sticky="w")
        _validatecmd = (self.HAM_BAND_RANGE1_START_WIDGET.register(
            self.validate_HAM_BAND_RANGE1_START), "%P", "%V")
        self.HAM_BAND_RANGE1_START_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label116 = ttk.Label(self.frame46)
        self.label116.configure(text='KHz')
        self.label116.grid(column=4, padx="0 10", row=10, sticky="w")
        self.HAM_BAND_RANGE1_END_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE1_END = tk.StringVar()
        self.HAM_BAND_RANGE1_END_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE1_END,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE1_END_WIDGET.grid(
            column=5, padx="0 2", pady="0 5", row=10)
        _validatecmd = (self.HAM_BAND_RANGE1_END_WIDGET.register(
            self.validate_HAM_BAND_RANGE1_END), "%P", "%V")
        self.HAM_BAND_RANGE1_END_WIDGET.configure(validatecommand=_validatecmd)
        self.label117 = ttk.Label(self.frame46)
        self.label117.configure(text='KHz')
        self.label117.grid(column=6, padx="0 5", row=10)
        self.label107 = ttk.Label(self.frame46)
        self.label107.configure(style="Heading4.TLabel", text='Band 2')
        self.label107.grid(column=1, pady="0 5", row=11, sticky="w")
        self.HAM_BAND_RANGE2_START_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE2_START = tk.StringVar()
        self.HAM_BAND_RANGE2_START_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE2_START,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE2_START_WIDGET.grid(
            column=3, pady="0 5", row=11, sticky="w")
        _validatecmd = (self.HAM_BAND_RANGE2_START_WIDGET.register(
            self.validate_HAM_BAND_RANGE2_START), "%P", "%V")
        self.HAM_BAND_RANGE2_START_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label118 = ttk.Label(self.frame46)
        self.label118.configure(text='KHz')
        self.label118.grid(column=4, padx="0 10", row=11, sticky="w")
        self.HAM_BAND_RANGE2_END_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE2_END = tk.StringVar()
        self.HAM_BAND_RANGE2_END_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE2_END,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE2_END_WIDGET.grid(
            column=5, padx="0 5", pady="0 5", row=11)
        _validatecmd = (self.HAM_BAND_RANGE2_END_WIDGET.register(
            self.validate_HAM_BAND_RANGE2_END), "%P", "%V")
        self.HAM_BAND_RANGE2_END_WIDGET.configure(validatecommand=_validatecmd)
        self.label119 = ttk.Label(self.frame46)
        self.label119.configure(text='KHz')
        self.label119.grid(column=6, padx="0 5", row=11)
        self.label108 = ttk.Label(self.frame46)
        self.label108.configure(style="Heading4.TLabel", text='Band 3')
        self.label108.grid(column=1, pady="0 5", row=12, sticky="w")
        self.HAM_BAND_RANGE3_START_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE3_START = tk.StringVar()
        self.HAM_BAND_RANGE3_START_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE3_START,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE3_START_WIDGET.grid(
            column=3, pady="0 5", row=12, sticky="w")
        _validatecmd = (self.HAM_BAND_RANGE3_START_WIDGET.register(
            self.validate_HAM_BAND_RANGE3_START), "%P", "%V")
        self.HAM_BAND_RANGE3_START_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label120 = ttk.Label(self.frame46)
        self.label120.configure(text='KHz')
        self.label120.grid(column=4, padx="0 10", row=12, sticky="w")
        self.HAM_BAND_RANGE3_END_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE3_END = tk.StringVar()
        self.HAM_BAND_RANGE3_END_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE3_END,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE3_END_WIDGET.grid(
            column=5, padx="0 5", pady="0 5", row=12)
        _validatecmd = (self.HAM_BAND_RANGE3_END_WIDGET.register(
            self.validate_HAM_BAND_RANGE3_END), "%P", "%V")
        self.HAM_BAND_RANGE3_END_WIDGET.configure(validatecommand=_validatecmd)
        self.label121 = ttk.Label(self.frame46)
        self.label121.configure(text='KHz')
        self.label121.grid(column=6, padx="0 5", row=12)
        self.label109 = ttk.Label(self.frame46)
        self.label109.configure(style="Heading4.TLabel", text='Band 4')
        self.label109.grid(column=1, pady="0 5", row=13, sticky="w")
        self.HAM_BAND_RANGE4_START_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE4_START = tk.StringVar()
        self.HAM_BAND_RANGE4_START_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE4_START,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE4_START_WIDGET.grid(
            column=3, pady="0 5", row=13, sticky="w")
        _validatecmd = (self.HAM_BAND_RANGE4_START_WIDGET.register(
            self.validate_HAM_BAND_RANGE4_START), "%P", "%V")
        self.HAM_BAND_RANGE4_START_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label122 = ttk.Label(self.frame46)
        self.label122.configure(text='KHz')
        self.label122.grid(column=4, padx="0 10", row=13, sticky="w")
        self.HAM_BAND_RANGE4_END_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE4_END = tk.StringVar()
        self.HAM_BAND_RANGE4_END_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE4_END,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE4_END_WIDGET.grid(
            column=5, padx="0 5", pady="0 5", row=13)
        _validatecmd = (self.HAM_BAND_RANGE4_END_WIDGET.register(
            self.validate_HAM_BAND_RANGE4_END), "%P", "%V")
        self.HAM_BAND_RANGE4_END_WIDGET.configure(validatecommand=_validatecmd)
        self.label123 = ttk.Label(self.frame46)
        self.label123.configure(text='KHz')
        self.label123.grid(column=6, padx="0 5", row=13)
        self.label110 = ttk.Label(self.frame46)
        self.label110.configure(style="Heading4.TLabel", text='Band 5')
        self.label110.grid(column=1, pady="0 5", row=14, sticky="w")
        self.HAM_BAND_RANGE5_START_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE5_START = tk.StringVar()
        self.HAM_BAND_RANGE5_START_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE5_START,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE5_START_WIDGET.grid(
            column=3, pady="0 5", row=14, sticky="w")
        _validatecmd = (self.HAM_BAND_RANGE5_START_WIDGET.register(
            self.validate_HAM_BAND_RANGE5_START), "%P", "%V")
        self.HAM_BAND_RANGE5_START_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label124 = ttk.Label(self.frame46)
        self.label124.configure(text='KHz')
        self.label124.grid(column=4, padx="0 10", row=14, sticky="w")
        self.HAM_BAND_RANGE5_END_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE5_END = tk.StringVar()
        self.HAM_BAND_RANGE5_END_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE5_END,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE5_END_WIDGET.grid(
            column=5, padx="0 5", pady="0 5", row=14)
        _validatecmd = (self.HAM_BAND_RANGE5_END_WIDGET.register(
            self.validate_HAM_BAND_RANGE5_END), "%P", "%V")
        self.HAM_BAND_RANGE5_END_WIDGET.configure(validatecommand=_validatecmd)
        self.label125 = ttk.Label(self.frame46)
        self.label125.configure(text='KHz')
        self.label125.grid(column=6, padx="0 5", row=14)
        self.label111 = ttk.Label(self.frame46)
        self.label111.configure(style="Heading4.TLabel", text='Band 6')
        self.label111.grid(column=1, pady="0 5", row=15, sticky="w")
        self.HAM_BAND_RANGE6_START_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE6_START = tk.StringVar()
        self.HAM_BAND_RANGE6_START_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE6_START,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE6_START_WIDGET.grid(
            column=3, pady="0 5", row=15, sticky="w")
        _validatecmd = (self.HAM_BAND_RANGE6_START_WIDGET.register(
            self.validate_HAM_BAND_RANGE6_START), "%P", "%V")
        self.HAM_BAND_RANGE6_START_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label126 = ttk.Label(self.frame46)
        self.label126.configure(text='KHz')
        self.label126.grid(column=4, padx="0 10", row=15, sticky="w")
        self.HAM_BAND_RANGE6_END_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE6_END = tk.StringVar()
        self.HAM_BAND_RANGE6_END_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE6_END,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE6_END_WIDGET.grid(
            column=5, padx="0 5", pady="0 5", row=15)
        _validatecmd = (self.HAM_BAND_RANGE6_END_WIDGET.register(
            self.validate_HAM_BAND_RANGE6_END), "%P", "%V")
        self.HAM_BAND_RANGE6_END_WIDGET.configure(validatecommand=_validatecmd)
        self.label127 = ttk.Label(self.frame46)
        self.label127.configure(text='KHz')
        self.label127.grid(column=6, padx="0 5", row=15)
        self.label112 = ttk.Label(self.frame46)
        self.label112.configure(style="Heading4.TLabel", text='Band 7')
        self.label112.grid(column=1, pady="0 5", row=16, sticky="w")
        self.HAM_BAND_RANGE7_START_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE7_START = tk.StringVar()
        self.HAM_BAND_RANGE7_START_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE7_START,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE7_START_WIDGET.grid(
            column=3, pady="0 5", row=16, sticky="w")
        _validatecmd = (self.HAM_BAND_RANGE7_START_WIDGET.register(
            self.validate_HAM_BAND_RANGE7_START), "%P", "%V")
        self.HAM_BAND_RANGE7_START_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label128 = ttk.Label(self.frame46)
        self.label128.configure(text='KHz')
        self.label128.grid(column=4, padx="0 10", row=16, sticky="w")
        self.HAM_BAND_RANGE7_END_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE7_END = tk.StringVar()
        self.HAM_BAND_RANGE7_END_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE7_END,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE7_END_WIDGET.grid(
            column=5, padx="0 5", pady="0 5", row=16)
        _validatecmd = (self.HAM_BAND_RANGE7_END_WIDGET.register(
            self.validate_HAM_BAND_RANGE7_END), "%P", "%V")
        self.HAM_BAND_RANGE7_END_WIDGET.configure(validatecommand=_validatecmd)
        self.label129 = ttk.Label(self.frame46)
        self.label129.configure(text='KHz')
        self.label129.grid(column=6, padx="0 5", row=16)
        self.label113 = ttk.Label(self.frame46)
        self.label113.configure(style="Heading4.TLabel", text='Band 8')
        self.label113.grid(column=1, pady="0 5", row=17, sticky="w")
        self.HAM_BAND_RANGE8_START_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE8_START = tk.StringVar()
        self.HAM_BAND_RANGE8_START_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE8_START,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE8_START_WIDGET.grid(
            column=3, pady="0 5", row=17, sticky="w")
        _validatecmd = (self.HAM_BAND_RANGE8_START_WIDGET.register(
            self.validate_HAM_BAND_RANGE8_START), "%P", "%V")
        self.HAM_BAND_RANGE8_START_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label130 = ttk.Label(self.frame46)
        self.label130.configure(text='KHz')
        self.label130.grid(column=4, padx="0 10", row=17, sticky="w")
        self.HAM_BAND_RANGE8_END_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE8_END = tk.StringVar()
        self.HAM_BAND_RANGE8_END_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE8_END,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE8_END_WIDGET.grid(
            column=5, padx="0 5", pady="0 5", row=17)
        _validatecmd = (self.HAM_BAND_RANGE8_END_WIDGET.register(
            self.validate_HAM_BAND_RANGE8_END), "%P", "%V")
        self.HAM_BAND_RANGE8_END_WIDGET.configure(validatecommand=_validatecmd)
        self.label131 = ttk.Label(self.frame46)
        self.label131.configure(text='KHz')
        self.label131.grid(column=6, padx="0 5", row=17)
        self.label114 = ttk.Label(self.frame46)
        self.label114.configure(style="Heading4.TLabel", text='Band 9')
        self.label114.grid(column=1, pady="0 5", row=18, sticky="w")
        self.HAM_BAND_RANGE9_START_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE9_START = tk.StringVar()
        self.HAM_BAND_RANGE9_START_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE9_START,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE9_START_WIDGET.grid(
            column=3, pady="0 5", row=18, sticky="w")
        _validatecmd = (self.HAM_BAND_RANGE9_START_WIDGET.register(
            self.validate_HAM_BAND_RANGE9_START), "%P", "%V")
        self.HAM_BAND_RANGE9_START_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label132 = ttk.Label(self.frame46)
        self.label132.configure(text='KHz')
        self.label132.grid(column=4, padx="0 10", row=18, sticky="w")
        self.HAM_BAND_RANGE9_END_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE9_END = tk.StringVar()
        self.HAM_BAND_RANGE9_END_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE9_END,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE9_END_WIDGET.grid(
            column=5, padx="0 5", pady="0 5", row=18)
        _validatecmd = (self.HAM_BAND_RANGE9_END_WIDGET.register(
            self.validate_HAM_BAND_RANGE9_END), "%P", "%V")
        self.HAM_BAND_RANGE9_END_WIDGET.configure(validatecommand=_validatecmd)
        self.label133 = ttk.Label(self.frame46)
        self.label133.configure(text='KHz')
        self.label133.grid(column=6, padx="0 5", row=18)
        self.label115 = ttk.Label(self.frame46)
        self.label115.configure(style="Heading4.TLabel", text='Band 10')
        self.label115.grid(
            column=1,
            padx="0 5",
            pady="0 5",
            row=19,
            sticky="w")
        self.HAM_BAND_RANGE10_START_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE10_START = tk.StringVar()
        self.HAM_BAND_RANGE10_START_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE10_START,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE10_START_WIDGET.grid(
            column=3, pady="0 5", row=19, sticky="w")
        _validatecmd = (self.HAM_BAND_RANGE10_START_WIDGET.register(
            self.validate_HAM_BAND_RANGE10_START), "%P", "%V")
        self.HAM_BAND_RANGE10_START_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label134 = ttk.Label(self.frame46)
        self.label134.configure(text='KHz')
        self.label134.grid(column=4, padx="0 10", row=19, sticky="w")
        self.HAM_BAND_RANGE10_END_WIDGET = ttk.Entry(self.frame46)
        self.HAM_BAND_RANGE10_END = tk.StringVar()
        self.HAM_BAND_RANGE10_END_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.HAM_BAND_RANGE10_END,
            validate="focus",
            width=10)
        self.HAM_BAND_RANGE10_END_WIDGET.grid(
            column=5, padx="0 5", pady="0 5", row=19)
        _validatecmd = (self.HAM_BAND_RANGE10_END_WIDGET.register(
            self.validate_HAM_BAND_RANGE10_END), "%P", "%V")
        self.HAM_BAND_RANGE10_END_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label135 = ttk.Label(self.frame46)
        self.label135.configure(text='KHz')
        self.label135.grid(column=6, padx="0 5", row=19)
        self.frame46.pack(
            anchor="w",
            expand="false",
            fill="x",
            pady="20 0",
            side="top")
        self.frame46.grid_anchor("w")
        self.frame58 = ttk.Frame(self.frame19)
        self.frame58.configure(
            height=200,
            padding=10,
            relief="groove",
            width=200)
        self.autoInputRegion1_WIDGET = ttk.Button(self.frame58)
        self.autoInputRegion1_WIDGET.configure(
            style="Button4.TButton", text='Region 1')
        self.autoInputRegion1_WIDGET.grid(column=1, padx=5, row=1)
        self.autoInputRegion1_WIDGET.configure(command=self.autoInputRegion1)
        self.label136 = ttk.Label(self.frame58)
        self.label136.configure(
            style="Heading3.TLabel",
            text='Auto Input Bands For:')
        self.label136.grid(column=0, ipadx=5, padx=5, row=1)
        self.autoInputRegion2_WIDGET = ttk.Button(self.frame58)
        self.autoInputRegion2_WIDGET.configure(
            style="Button4.TButton", text='Region 2')
        self.autoInputRegion2_WIDGET.grid(column=2, padx=5, row=1)
        self.autoInputRegion2_WIDGET.configure(command=self.autoInputRegion2)
        self.autoInputRegion3_WIDGET = ttk.Button(self.frame58)
        self.autoInputRegion3_WIDGET.configure(
            style="Button4.TButton", text='Region 3')
        self.autoInputRegion3_WIDGET.grid(column=3, padx=5, row=1)
        self.autoInputRegion3_WIDGET.configure(command=self.autoInputRegion3)
        self.label92 = ttk.Label(self.frame58)
        self.label92.configure(style="Heading4.TLabel", text='Region 1:')
        self.label92.grid(column=0, pady="10 5", row=2, sticky="e")
        self.label94 = ttk.Label(self.frame58)
        self.label94.configure(style="Heading4.TLabel", text='Region 2:')
        self.label94.grid(column=0, pady="0 5", row=3, sticky="e")
        self.label96 = ttk.Label(self.frame58)
        self.label96.configure(style="Heading4.TLabel", text='Region 3:')
        self.label96.grid(column=0, row=4, sticky="e")
        self.label97 = ttk.Label(self.frame58)
        self.label97.configure(
            text='Africa, Europe, Middle East, and northern Asia')
        self.label97.grid(
            column=1,
            columnspan=3,
            padx="5 0",
            pady="10 5",
            row=2,
            sticky="w")
        self.label98 = ttk.Label(self.frame58)
        self.label98.configure(text='the Americas')
        self.label98.grid(
            column=1,
            columnspan=3,
            padx="5 0",
            pady="0 5",
            row=3,
            sticky="ew")
        self.label99 = ttk.Label(self.frame58)
        self.label99.configure(text='the rest of Asia and the Pacific')
        self.label99.grid(
            column=1,
            columnspan=3,
            padx="5 0",
            row=4,
            sticky="ew")
        self.frame58.pack(anchor="w", pady="20 0", side="top")
        self.frame58.grid_anchor("w")
        self.frame12 = ttk.Frame(self.frame19)
        self.label144 = ttk.Label(self.frame12)
        self.label144.configure(
            justify="left",
            relief="flat",
            style="Heading3.TLabel",
            text='TX/RX Restrictions')
        self.label144.grid(
            column=0,
            columnspan=2,
            padx="0 15",
            pady="10 0",
            row=1,
            sticky="w")
        self.label145 = ttk.Label(self.frame12)
        self.label145.configure(
            style="Heading4.TLabel",
            text='Tuning Restriction')
        self.label145.grid(
            column=1,
            padx="80 15",
            pady="5 10",
            row=2,
            sticky="e")
        self.TUNING_RESTICTIONS = tk.StringVar(value='NONE')
        __values = ['NONE', 'BAND']
        self.TUNING_RESTICTIONS_WIDGET = ttk.OptionMenu(
            self.frame12, self.TUNING_RESTICTIONS, "NONE", *__values, command=None)
        self.TUNING_RESTICTIONS_WIDGET.grid(column=2, pady="5 10", row=2)
        self.label146 = ttk.Label(self.frame12)
        self.label146.configure(
            style="Heading4.TLabel",
            text='Transmit Restriction')
        self.label146.grid(column=1, padx="30 15", row=3, sticky="e")
        self.TX_RESTRICTIONS = tk.StringVar(value='NONE')
        __values = ['NONE', 'HAM']
        self.TX_RESTRICTIONS_WIDGET = ttk.OptionMenu(
            self.frame12, self.TX_RESTRICTIONS, "NONE", *__values, command=None)
        self.TX_RESTRICTIONS_WIDGET.grid(column=2, row=3)
        self.frame12.pack(
            anchor="w",
            expand="false",
            fill="x",
            pady="20 0",
            side="top")
        self.frame12.grid_anchor("w")
        self.frame19.pack(anchor="w", padx=20, side="top")
        self.frame16.pack(
            anchor="center",
            expand="true",
            fill="both",
            padx=5,
            pady=5,
            side="top")
        self.Bands_SF.pack(side="top")
        self.settingsNotebook.add(self.Bands_SF, text='Bands')
        self.Channels_SF = ScrolledFrame(
            self.settingsNotebook, scrolltype="both")
        self.Channels_SF.configure(usemousewheel=True)
        self.frame45 = ttk.Frame(self.Channels_SF.innerframe)
        self.frame45.configure(height=200, width=200)
        self.frame47 = ttk.Frame(self.frame45)
        self.label199 = ttk.Label(self.frame47)
        self.label199.configure(
            justify="center",
            style="Heading2.TLabel",
            text='Channels')
        self.label199.pack(anchor="w", padx=5, pady="15 25", side="top")
        self.frame47.pack(anchor="w", side="top")
        self.Operator_Channel_Frame = ttk.Frame(self.frame45)
        self.Operator_Channel_Frame.configure(height=200, width=200)
        self.All_Channel_Frame = ttk.Frame(self.Operator_Channel_Frame)
        self.All_Channel_Frame.configure(height=200, width=200)
        self.Standard_Channel_Frame = ttk.Frame(self.All_Channel_Frame)
        self.Standard_Channel_Frame.configure(height=200, width=200)
        self.General_Channel_Title_Frame = ttk.Frame(
            self.Standard_Channel_Frame)
        self.General_Channel_Title_Frame.configure(height=200, width=200)
        self.General_Settings_Channels_Label = ttk.Label(
            self.General_Channel_Title_Frame)
        self.General_Settings_Channels_Label.configure(
            style="Heading3.TLabel", text='Channel Memory')
        self.General_Settings_Channels_Label.pack(
            anchor="w", expand="true", fill="x", pady="20 0")
        self.General_Channel_Title_Frame.pack(
            anchor="w", expand="true", fill="x", side="top")
        self.General_Channels_Settings_Frame = ttk.Frame(
            self.Standard_Channel_Frame)
        self.label70 = ttk.Label(self.General_Channels_Settings_Frame)
        self.label70.configure(style="Heading4.TLabel", text='Show')
        self.label70.grid(column=2, row=2, sticky="s")
        self.label69 = ttk.Label(self.General_Channels_Settings_Frame)
        self.label69.configure(
            justify="center",
            style="Heading4.TLabel",
            text='Operation')
        self.label69.grid(column=7, row=2)
        self.label30 = ttk.Label(self.General_Channels_Settings_Frame)
        self.label30.configure(style="Heading4.TLabel", text='Name')
        self.label30.grid(column=2, row=3)
        self.label71 = ttk.Label(self.General_Channels_Settings_Frame)
        self.label71.configure(style="Heading4.TLabel", text='Name')
        self.label71.grid(column=3, padx=5, row=3, sticky="s")
        self.label31 = ttk.Label(self.General_Channels_Settings_Frame)
        self.label31.configure(style="Heading4.TLabel", text='Frequency')
        self.label31.grid(column=4, row=3, sticky="s")
        self.label68 = ttk.Label(self.General_Channels_Settings_Frame)
        self.label68.configure(style="Heading4.TLabel", text='Mode')
        self.label68.grid(column=7, row=3, sticky="s")
        self.CHANNEL_FREQ1_Label = ttk.Label(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ1_Label.configure(
            style="Heading4.TLabel", text='CH.01')
        self.CHANNEL_FREQ1_Label.grid(
            column=0, padx="0 10", pady="5 5", row=4, sticky="w")
        self.CHANNEL_FREQ1_SHOW_NAME = tk.StringVar(value='YES')
        __values = ['YES', 'NO']
        self.CHANNEL_FREQ1_SHOW_NAME_WIDGET = tk.OptionMenu(
            self.General_Channels_Settings_Frame,
            self.CHANNEL_FREQ1_SHOW_NAME,
            *__values,
            command=None)
        self.CHANNEL_FREQ1_SHOW_NAME_WIDGET.grid(
            column=2, padx="0 5", pady="5 5", row=4)
        self.CHANNEL_FREQ1_NAME_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ1_NAME = tk.StringVar()
        self.CHANNEL_FREQ1_NAME_WIDGET.configure(
            justify="right",
            state="normal",
            style="Normal.TEntry",
            takefocus=True,
            textvariable=self.CHANNEL_FREQ1_NAME,
            validate="focus",
            width=6)
        self.CHANNEL_FREQ1_NAME_WIDGET.grid(
            column=3, padx="0 5", pady="5 5", row=4, sticky="w")
        _validatecmd = (
            self.CHANNEL_FREQ1_NAME_WIDGET.register(
                self.validate_CHANNEL_FREQ1_NAME), "%P", "%V")
        self.CHANNEL_FREQ1_NAME_WIDGET.configure(validatecommand=_validatecmd)
        self.CHANNEL_FREQ1_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ1 = tk.StringVar()
        self.CHANNEL_FREQ1_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ1,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ1_WIDGET.grid(column=4, padx="0 2", pady="5 5", row=4)
        _validatecmd = (
            self.CHANNEL_FREQ1_WIDGET.register(
                self.validate_CHANNEL_FREQ1), "%P", "%V")
        self.CHANNEL_FREQ1_WIDGET.configure(validatecommand=_validatecmd)
        self.label34 = ttk.Label(self.General_Channels_Settings_Frame)
        self.label34.configure(text='Hz')
        self.label34.grid(column=5, padx="0 10", pady="5 5", row=4)
        self.CHANNEL_FREQ1_MODE_WIDGET = ttk.Combobox(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ1_MODE = tk.StringVar()
        self.CHANNEL_FREQ1_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox3.TCombobox",
            textvariable=self.CHANNEL_FREQ1_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ1_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 5", row=4, sticky="w")
        self.CHANNEL_FREQ1_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.CHANNEL_FREQ2_Label = ttk.Label(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ2_Label.configure(
            style="Heading4.TLabel", text='CH.02')
        self.CHANNEL_FREQ2_Label.grid(column=0, pady="5 0", row=5, sticky="w")
        self.CHANNEL_FREQ2_SHOW_NAME = tk.StringVar(value='YES')
        __values = ['YES', 'NO']
        self.CHANNEL_FREQ2_SHOW_NAME_WIDGET = tk.OptionMenu(
            self.General_Channels_Settings_Frame,
            self.CHANNEL_FREQ2_SHOW_NAME,
            *__values,
            command=None)
        self.CHANNEL_FREQ2_SHOW_NAME_WIDGET.grid(
            column=2, padx="0 5", pady="5 0", row=5)
        self.CHANNEL_FREQ2_NAME_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ2_NAME = tk.StringVar()
        self.CHANNEL_FREQ2_NAME_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ2_NAME,
            validate="focus",
            width=6)
        self.CHANNEL_FREQ2_NAME_WIDGET.grid(
            column=3, padx="0 5", pady="5 0", row=5, sticky="w")
        _validatecmd = (
            self.CHANNEL_FREQ2_NAME_WIDGET.register(
                self.validate_CHANNEL_FREQ2_NAME), "%P", "%V")
        self.CHANNEL_FREQ2_NAME_WIDGET.configure(validatecommand=_validatecmd)
        self.CHANNEL_FREQ2_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ2 = tk.StringVar()
        self.CHANNEL_FREQ2_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ2,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ2_WIDGET.grid(column=4, padx="0 5", pady="5 0", row=5)
        _validatecmd = (
            self.CHANNEL_FREQ2_WIDGET.register(
                self.validate_CHANNEL_FREQ2), "%P", "%V")
        self.CHANNEL_FREQ2_WIDGET.configure(validatecommand=_validatecmd)
        self.label37 = ttk.Label(self.General_Channels_Settings_Frame)
        self.label37.configure(text='Hz')
        self.label37.grid(column=5, padx="0 10", pady="5 0", row=5)
        self.CHANNEL_FREQ2_MODE_WIDGET = ttk.Combobox(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ2_MODE = tk.StringVar()
        self.CHANNEL_FREQ2_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox4.TCombobox",
            textvariable=self.CHANNEL_FREQ2_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ2_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 0", row=5, sticky="w")
        self.CHANNEL_FREQ2_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.CHANNEL_FREQ3_Label = ttk.Label(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ3_Label.configure(
            style="Heading4.TLabel", text='CH.03')
        self.CHANNEL_FREQ3_Label.grid(column=0, pady="5 0", row=6, sticky="w")
        self.CHANNEL_FREQ3_SHOW_NAME = tk.StringVar(value='YES')
        __values = ['YES', 'NO']
        self.CHANNEL_FREQ3_SHOW_NAME_WIDGET = tk.OptionMenu(
            self.General_Channels_Settings_Frame,
            self.CHANNEL_FREQ3_SHOW_NAME,
            *__values,
            command=None)
        self.CHANNEL_FREQ3_SHOW_NAME_WIDGET.grid(
            column=2, padx="0 5", pady="5 0", row=6)
        self.CHANNEL_FREQ3_NAME_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ3_NAME = tk.StringVar()
        self.CHANNEL_FREQ3_NAME_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ3_NAME,
            validate="focus",
            width=6)
        self.CHANNEL_FREQ3_NAME_WIDGET.grid(
            column=3, padx="0 5", pady="5 0", row=6, sticky="w")
        _validatecmd = (
            self.CHANNEL_FREQ3_NAME_WIDGET.register(
                self.validate_CHANNEL_FREQ3_NAME), "%P", "%V")
        self.CHANNEL_FREQ3_NAME_WIDGET.configure(validatecommand=_validatecmd)
        self.CHANNEL_FREQ3_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ3 = tk.StringVar()
        self.CHANNEL_FREQ3_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ3,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ3_WIDGET.grid(column=4, padx="0 5", pady="5 0", row=6)
        _validatecmd = (
            self.CHANNEL_FREQ3_WIDGET.register(
                self.validate_CHANNEL_FREQ3), "%P", "%V")
        self.CHANNEL_FREQ3_WIDGET.configure(validatecommand=_validatecmd)
        self.label40 = ttk.Label(self.General_Channels_Settings_Frame)
        self.label40.configure(text='Hz')
        self.label40.grid(column=5, padx="0 10", pady="5 0", row=6)
        self.CHANNEL_FREQ3_MODE_WIDGET = ttk.Combobox(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ3_MODE = tk.StringVar()
        self.CHANNEL_FREQ3_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox3.TCombobox",
            textvariable=self.CHANNEL_FREQ3_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ3_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 0", row=6, sticky="w")
        self.CHANNEL_FREQ3_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.CHANNEL_FREQ4_Label = ttk.Label(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ4_Label.configure(
            style="Heading4.TLabel", text='CH.04')
        self.CHANNEL_FREQ4_Label.grid(column=0, pady="5 0", row=7, sticky="w")
        self.CHANNEL_FREQ4_SHOW_NAME = tk.StringVar(value='YES')
        __values = ['YES', 'NO']
        self.CHANNEL_FREQ4_SHOW_NAME_WIDGET = tk.OptionMenu(
            self.General_Channels_Settings_Frame,
            self.CHANNEL_FREQ4_SHOW_NAME,
            *__values,
            command=None)
        self.CHANNEL_FREQ4_SHOW_NAME_WIDGET.grid(
            column=2, padx="0 5", pady="5 0", row=7)
        self.CHANNEL_FREQ4_NAME_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ4_NAME = tk.StringVar()
        self.CHANNEL_FREQ4_NAME_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ4_NAME,
            validate="focus",
            width=6)
        self.CHANNEL_FREQ4_NAME_WIDGET.grid(
            column=3, padx="0 5", pady="5 0", row=7, sticky="w")
        _validatecmd = (
            self.CHANNEL_FREQ4_NAME_WIDGET.register(
                self.validate_CHANNEL_FREQ4_NAME), "%P", "%V")
        self.CHANNEL_FREQ4_NAME_WIDGET.configure(validatecommand=_validatecmd)
        self.CHANNEL_FREQ4_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ4 = tk.StringVar()
        self.CHANNEL_FREQ4_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ4,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ4_WIDGET.grid(column=4, padx="0 5", pady="5 0", row=7)
        _validatecmd = (
            self.CHANNEL_FREQ4_WIDGET.register(
                self.validate_CHANNEL_FREQ4), "%P", "%V")
        self.CHANNEL_FREQ4_WIDGET.configure(validatecommand=_validatecmd)
        self.label43 = ttk.Label(self.General_Channels_Settings_Frame)
        self.label43.configure(text='Hz')
        self.label43.grid(column=5, padx="0 10", pady="5 0", row=7)
        self.CHANNEL_FREQ4_MODE_WIDGET = ttk.Combobox(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ4_MODE = tk.StringVar()
        self.CHANNEL_FREQ4_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox3.TCombobox",
            textvariable=self.CHANNEL_FREQ4_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ4_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 0", row=7, sticky="w")
        self.CHANNEL_FREQ4_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.CHANNEL_FREQ5_Label = ttk.Label(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ5_Label.configure(
            style="Heading4.TLabel", text='CH.05')
        self.CHANNEL_FREQ5_Label.grid(column=0, pady="5 0", row=8, sticky="w")
        self.CHANNEL_FREQ5_SHOW_NAME = tk.StringVar(value='YES')
        __values = ['YES', 'NO']
        self.CHANNEL_FREQ5_SHOW_NAME_WIDGET = tk.OptionMenu(
            self.General_Channels_Settings_Frame,
            self.CHANNEL_FREQ5_SHOW_NAME,
            *__values,
            command=None)
        self.CHANNEL_FREQ5_SHOW_NAME_WIDGET.grid(
            column=2, padx="0 5", pady="5 0", row=8)
        self.CHANNEL_FREQ5_NAME_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ5_NAME = tk.StringVar()
        self.CHANNEL_FREQ5_NAME_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ5_NAME,
            validate="focus",
            width=6)
        self.CHANNEL_FREQ5_NAME_WIDGET.grid(
            column=3, padx="0 5", pady="5 0", row=8, sticky="w")
        _validatecmd = (
            self.CHANNEL_FREQ5_NAME_WIDGET.register(
                self.validate_CHANNEL_FREQ5_NAME), "%P", "%V")
        self.CHANNEL_FREQ5_NAME_WIDGET.configure(validatecommand=_validatecmd)
        self.CHANNEL_FREQ5_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ5 = tk.StringVar()
        self.CHANNEL_FREQ5_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ5,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ5_WIDGET.grid(column=4, padx="0 5", pady="5 0", row=8)
        _validatecmd = (
            self.CHANNEL_FREQ5_WIDGET.register(
                self.validate_CHANNEL_FREQ5), "%P", "%V")
        self.CHANNEL_FREQ5_WIDGET.configure(validatecommand=_validatecmd)
        self.label46 = ttk.Label(self.General_Channels_Settings_Frame)
        self.label46.configure(text='Hz')
        self.label46.grid(column=5, padx="0 10", pady="5 0", row=8)
        self.CHANNEL_FREQ5_MODE_WIDGET = ttk.Combobox(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ5_MODE = tk.StringVar()
        self.CHANNEL_FREQ5_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox3.TCombobox",
            textvariable=self.CHANNEL_FREQ5_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ5_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 0", row=8, sticky="w")
        self.CHANNEL_FREQ5_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.CHANNEL_FREQ6_Label = ttk.Label(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ6_Label.configure(
            style="Heading4.TLabel", text='CH.06')
        self.CHANNEL_FREQ6_Label.grid(column=0, pady="5 0", row=9, sticky="w")
        self.CHANNEL_FREQ6_SHOW_NAME = tk.StringVar(value='YES')
        __values = ['YES', 'NO']
        self.CHANNEL_FREQ6_SHOW_NAME_WIDGET = tk.OptionMenu(
            self.General_Channels_Settings_Frame,
            self.CHANNEL_FREQ6_SHOW_NAME,
            *__values,
            command=None)
        self.CHANNEL_FREQ6_SHOW_NAME_WIDGET.grid(
            column=2, padx="0 5", pady="5 0", row=9)
        self.CHANNEL_FREQ6_NAME_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ6_NAME = tk.StringVar()
        self.CHANNEL_FREQ6_NAME_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ6_NAME,
            validate="focus",
            width=6)
        self.CHANNEL_FREQ6_NAME_WIDGET.grid(
            column=3, padx="0 5", pady="5 0", row=9, sticky="w")
        _validatecmd = (
            self.CHANNEL_FREQ6_NAME_WIDGET.register(
                self.validate_CHANNEL_FREQ6_NAME), "%P", "%V")
        self.CHANNEL_FREQ6_NAME_WIDGET.configure(validatecommand=_validatecmd)
        self.CHANNEL_FREQ6_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ6 = tk.StringVar()
        self.CHANNEL_FREQ6_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ6,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ6_WIDGET.grid(column=4, padx="0 5", pady="5 0", row=9)
        _validatecmd = (
            self.CHANNEL_FREQ6_WIDGET.register(
                self.validate_CHANNEL_FREQ6), "%P", "%V")
        self.CHANNEL_FREQ6_WIDGET.configure(validatecommand=_validatecmd)
        self.label49 = ttk.Label(self.General_Channels_Settings_Frame)
        self.label49.configure(text='Hz')
        self.label49.grid(column=5, padx="0 10", pady="5 0", row=9)
        self.CHANNEL_FREQ6_MODE_WIDGET = ttk.Combobox(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ6_MODE = tk.StringVar()
        self.CHANNEL_FREQ6_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox3.TCombobox",
            textvariable=self.CHANNEL_FREQ6_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ6_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 0", row=9, sticky="w")
        self.CHANNEL_FREQ6_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.CHANNEL_FREQ7_Label = ttk.Label(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ7_Label.configure(
            style="Heading4.TLabel", text='CH.07')
        self.CHANNEL_FREQ7_Label.grid(column=0, pady="5 0", row=10, sticky="w")
        self.CHANNEL_FREQ7_SHOW_NAME = tk.StringVar(value='YES')
        __values = ['YES', 'NO']
        self.CHANNEL_FREQ7_SHOW_NAME_WIDGET = tk.OptionMenu(
            self.General_Channels_Settings_Frame,
            self.CHANNEL_FREQ7_SHOW_NAME,
            *__values,
            command=None)
        self.CHANNEL_FREQ7_SHOW_NAME_WIDGET.grid(
            column=2, padx="0 5", pady="5 0", row=10)
        self.CHANNEL_FREQ7_NAME_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ7_NAME = tk.StringVar()
        self.CHANNEL_FREQ7_NAME_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ7_NAME,
            validate="focus",
            width=6)
        self.CHANNEL_FREQ7_NAME_WIDGET.grid(
            column=3, padx="0 5", pady="5 0", row=10, sticky="w")
        _validatecmd = (
            self.CHANNEL_FREQ7_NAME_WIDGET.register(
                self.validate_CHANNEL_FREQ7_NAME), "%P", "%V")
        self.CHANNEL_FREQ7_NAME_WIDGET.configure(validatecommand=_validatecmd)
        self.CHANNEL_FREQ7_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ7 = tk.StringVar()
        self.CHANNEL_FREQ7_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ7,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ7_WIDGET.grid(
            column=4, padx="0 5", pady="5 0", row=10)
        _validatecmd = (
            self.CHANNEL_FREQ7_WIDGET.register(
                self.validate_CHANNEL_FREQ7), "%P", "%V")
        self.CHANNEL_FREQ7_WIDGET.configure(validatecommand=_validatecmd)
        self.label52 = ttk.Label(self.General_Channels_Settings_Frame)
        self.label52.configure(text='Hz')
        self.label52.grid(column=5, padx="0 10", pady="5 0", row=10)
        self.CHANNEL_FREQ7_MODE_WIDGET = ttk.Combobox(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ7_MODE = tk.StringVar()
        self.CHANNEL_FREQ7_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox3.TCombobox",
            textvariable=self.CHANNEL_FREQ7_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ7_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 0", row=10, sticky="w")
        self.CHANNEL_FREQ7_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.CHANNEL_FREQ8_Label = ttk.Label(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ8_Label.configure(
            style="Heading4.TLabel", text='CH.08')
        self.CHANNEL_FREQ8_Label.grid(column=0, pady="5 0", row=11, sticky="w")
        self.CHANNEL_FREQ8_SHOW_NAME = tk.StringVar(value='YES')
        __values = ['YES', 'NO']
        self.CHANNEL_FREQ8_SHOW_NAME_WIDGET = tk.OptionMenu(
            self.General_Channels_Settings_Frame,
            self.CHANNEL_FREQ8_SHOW_NAME,
            *__values,
            command=None)
        self.CHANNEL_FREQ8_SHOW_NAME_WIDGET.grid(
            column=2, padx="0 5", pady="5 0", row=11)
        self.CHANNEL_FREQ8_NAME_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ8_NAME = tk.StringVar()
        self.CHANNEL_FREQ8_NAME_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ8_NAME,
            validate="focus",
            width=6)
        self.CHANNEL_FREQ8_NAME_WIDGET.grid(
            column=3, padx="0 5", pady="5 0", row=11, sticky="w")
        _validatecmd = (
            self.CHANNEL_FREQ8_NAME_WIDGET.register(
                self.validate_CHANNEL_FREQ8_NAME), "%P", "%V")
        self.CHANNEL_FREQ8_NAME_WIDGET.configure(validatecommand=_validatecmd)
        self.CHANNEL_FREQ8_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ8 = tk.StringVar()
        self.CHANNEL_FREQ8_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ8,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ8_WIDGET.grid(
            column=4, padx="0 5", pady="5 0", row=11)
        _validatecmd = (
            self.CHANNEL_FREQ8_WIDGET.register(
                self.validate_CHANNEL_FREQ8), "%P", "%V")
        self.CHANNEL_FREQ8_WIDGET.configure(validatecommand=_validatecmd)
        self.label55 = ttk.Label(self.General_Channels_Settings_Frame)
        self.label55.configure(text='Hz')
        self.label55.grid(column=5, padx="0 10", pady="5 0", row=11)
        self.CHANNEL_FREQ8_MODE_WIDGET = ttk.Combobox(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ8_MODE = tk.StringVar()
        self.CHANNEL_FREQ8_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox3.TCombobox",
            textvariable=self.CHANNEL_FREQ8_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ8_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 0", row=11, sticky="w")
        self.CHANNEL_FREQ8_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.CHANNEL_FREQ9_Label = ttk.Label(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ9_Label.configure(
            style="Heading4.TLabel", text='CH.09')
        self.CHANNEL_FREQ9_Label.grid(column=0, pady="5 0", row=12, sticky="w")
        self.CHANNEL_FREQ9_SHOW_NAME = tk.StringVar(value='YES')
        __values = ['YES', 'NO']
        self.CHANNEL_FREQ9_SHOW_NAME_WIDGET = tk.OptionMenu(
            self.General_Channels_Settings_Frame,
            self.CHANNEL_FREQ9_SHOW_NAME,
            *__values,
            command=None)
        self.CHANNEL_FREQ9_SHOW_NAME_WIDGET.grid(
            column=2, padx="0 5", pady="5 0", row=12)
        self.CHANNEL_FREQ9_NAME_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ9_NAME = tk.StringVar()
        self.CHANNEL_FREQ9_NAME_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ9_NAME,
            validate="focus",
            width=6)
        self.CHANNEL_FREQ9_NAME_WIDGET.grid(
            column=3, padx="0 5", pady="5 0", row=12, sticky="w")
        _validatecmd = (
            self.CHANNEL_FREQ9_NAME_WIDGET.register(
                self.validate_CHANNEL_FREQ9_NAME), "%P", "%V")
        self.CHANNEL_FREQ9_NAME_WIDGET.configure(validatecommand=_validatecmd)
        self.CHANNEL_FREQ9_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ9 = tk.StringVar()
        self.CHANNEL_FREQ9_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ9,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ9_WIDGET.grid(
            column=4, padx="0 5", pady="5 0", row=12)
        _validatecmd = (
            self.CHANNEL_FREQ9_WIDGET.register(
                self.validate_CHANNEL_FREQ9), "%P", "%V")
        self.CHANNEL_FREQ9_WIDGET.configure(validatecommand=_validatecmd)
        self.label58 = ttk.Label(self.General_Channels_Settings_Frame)
        self.label58.configure(text='Hz')
        self.label58.grid(column=5, padx="0 10", pady="5 0", row=12)
        self.CHANNEL_FREQ9_MODE_WIDGET = ttk.Combobox(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ9_MODE = tk.StringVar()
        self.CHANNEL_FREQ9_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox3.TCombobox",
            textvariable=self.CHANNEL_FREQ9_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ9_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 0", row=12, sticky="w")
        self.CHANNEL_FREQ9_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.CHANNEL_FREQ10_Label = ttk.Label(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ10_Label.configure(
            style="Heading4.TLabel", text='CH.10')
        self.CHANNEL_FREQ10_Label.grid(
            column=0, padx="0 5", pady="5 0", row=13, sticky="w")
        self.CHANNEL_FREQ10_SHOW_NAME = tk.StringVar(value='YES')
        __values = ['YES', 'NO']
        self.CHANNEL_FREQ10_SHOW_NAME_WIDGET = tk.OptionMenu(
            self.General_Channels_Settings_Frame,
            self.CHANNEL_FREQ10_SHOW_NAME,
            *__values,
            command=None)
        self.CHANNEL_FREQ10_SHOW_NAME_WIDGET.grid(
            column=2, padx="0 5", pady="5 0", row=13)
        self.CHANNEL_FREQ10_NAME_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ10_NAME = tk.StringVar()
        self.CHANNEL_FREQ10_NAME_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ10_NAME,
            validate="focus",
            width=6)
        self.CHANNEL_FREQ10_NAME_WIDGET.grid(
            column=3, padx="0 5", pady="5 0", row=13, sticky="w")
        _validatecmd = (self.CHANNEL_FREQ10_NAME_WIDGET.register(
            self.validate_CHANNEL_FREQ10_NAME), "%P", "%V")
        self.CHANNEL_FREQ10_NAME_WIDGET.configure(validatecommand=_validatecmd)
        self.CHANNEL_FREQ10_WIDGET = ttk.Entry(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ10 = tk.StringVar()
        self.CHANNEL_FREQ10_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ10,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ10_WIDGET.grid(
            column=4, padx="0 5", pady="5 0", row=13)
        _validatecmd = (
            self.CHANNEL_FREQ10_WIDGET.register(
                self.validate_CHANNEL_FREQ10), "%P", "%V")
        self.CHANNEL_FREQ10_WIDGET.configure(validatecommand=_validatecmd)
        self.CHANNEL_FREQ10_MODE_WIDGET = ttk.Combobox(
            self.General_Channels_Settings_Frame)
        self.CHANNEL_FREQ10_MODE = tk.StringVar()
        self.CHANNEL_FREQ10_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox3.TCombobox",
            textvariable=self.CHANNEL_FREQ10_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ10_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 0", row=13, sticky="w")
        self.CHANNEL_FREQ10_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.label61 = ttk.Label(self.General_Channels_Settings_Frame)
        self.label61.configure(text='Hz')
        self.label61.grid(column=5, padx="0 10", pady="5 0", row=13)
        self.General_Channels_Settings_Frame.pack(
            anchor="w", expand="false", fill="x", padx="50 0", pady="20 0", side="top")
        self.General_Channels_Settings_Frame.grid_anchor("w")
        self.Standard_Channel_Frame.pack(anchor="w", side="top")
        self.show_extended_channels_frame = ttk.Frame(self.All_Channel_Frame)
        self.show_extended_channels_frame.configure(height=200, width=200)
        self.toggleExtendedChannels_WIDGET = ttk.Checkbutton(
            self.show_extended_channels_frame)
        self.toggleExtendedChannelsCheckBox = tk.StringVar()
        self.toggleExtendedChannels_WIDGET.configure(
            offvalue=0,
            onvalue=1,
            style="Checkbox4.TCheckbutton",
            text='Show Extended Channels',
            variable=self.toggleExtendedChannelsCheckBox)
        self.toggleExtendedChannels_WIDGET.pack(anchor="w", pady="10 0")
        self.toggleExtendedChannels_WIDGET.configure(
            command=self.toggleExtendedChannels)
        self.separator1 = ttk.Separator(self.show_extended_channels_frame)
        self.separator1.configure(orient="horizontal")
        self.separator1.pack(
            anchor="center",
            expand="true",
            fill="x",
            pady="10 0",
            side="top")
        self.show_extended_channels_frame.pack(
            anchor="w", expand="true", fill="x", side="top")
        self.Extended_Channel_Frame = ttk.Frame(self.All_Channel_Frame)
        self.Extended_Channel_Frame.configure(height=200, width=200)
        self.Extended_Channel_Title_Frame = ttk.Frame(
            self.Extended_Channel_Frame)
        self.Extended_Channel_Title_Frame.configure(height=200, width=200)
        self.label103 = ttk.Label(self.Extended_Channel_Title_Frame)
        self.label103.configure(
            style="Heading3.TLabel",
            text='Extended Channel Memory')
        self.label103.pack(
            anchor="w",
            expand="false",
            pady="20 0",
            side="left")
        self.Extended_Channel_Title_Frame.pack(
            anchor="w", expand="false", side="top")
        self.General_Extended_Channel_Frame = ttk.Frame(
            self.Extended_Channel_Frame)
        self.label72 = ttk.Label(self.General_Extended_Channel_Frame)
        self.label72.configure(
            justify="center",
            style="Heading4.TLabel",
            text='Operation')
        self.label72.grid(column=7, pady="20 0", row=2)
        self.label74 = ttk.Label(self.General_Extended_Channel_Frame)
        self.label74.configure(style="Heading4.TLabel", text='Frequency')
        self.label74.grid(column=4, row=3, sticky="s")
        self.label75 = ttk.Label(self.General_Extended_Channel_Frame)
        self.label75.configure(style="Heading4.TLabel", text='Mode')
        self.label75.grid(column=7, row=3, sticky="s")
        self.CHANNEL_FREQ11_Label = ttk.Label(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ11_Label.configure(
            style="Heading4.TLabel", text='CH.11')
        self.CHANNEL_FREQ11_Label.grid(
            column=0, padx="0 10", pady="5 5", row=4, sticky="w")
        self.CHANNEL_FREQ11_WIDGET = ttk.Entry(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ11 = tk.StringVar()
        self.CHANNEL_FREQ11_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ11,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ11_WIDGET.grid(
            column=4, padx="0 2", pady="5 0", row=4)
        _validatecmd = (
            self.CHANNEL_FREQ11_WIDGET.register(
                self.validate_CHANNEL_FREQ11), "%P", "%V")
        self.CHANNEL_FREQ11_WIDGET.configure(validatecommand=_validatecmd)
        self.label77 = ttk.Label(self.General_Extended_Channel_Frame)
        self.label77.configure(text='Hz')
        self.label77.grid(column=5, padx="0 10", pady="5 0", row=4)
        self.CHANNEL_FREQ11_MODE_WIDGET = ttk.Combobox(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ11_MODE = tk.StringVar()
        self.CHANNEL_FREQ11_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox3.TCombobox",
            textvariable=self.CHANNEL_FREQ11_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ11_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 5", row=4, sticky="w")
        self.CHANNEL_FREQ11_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.CHANNEL_FREQ12_Label = ttk.Label(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ12_Label.configure(
            style="Heading4.TLabel", text='CH.12')
        self.CHANNEL_FREQ12_Label.grid(column=0, pady="5 0", row=5, sticky="w")
        self.CHANNEL_FREQ12_WIDGET = ttk.Entry(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ12 = tk.StringVar()
        self.CHANNEL_FREQ12_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ12,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ12_WIDGET.grid(
            column=4, padx="0 5", pady="5 0", row=5)
        _validatecmd = (
            self.CHANNEL_FREQ12_WIDGET.register(
                self.validate_CHANNEL_FREQ12), "%P", "%V")
        self.CHANNEL_FREQ12_WIDGET.configure(validatecommand=_validatecmd)
        self.label79 = ttk.Label(self.General_Extended_Channel_Frame)
        self.label79.configure(text='Hz')
        self.label79.grid(column=5, padx="0 10", pady="5 0", row=5)
        self.CHANNEL_FREQ12_MODE_WIDGET = ttk.Combobox(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ12_MODE = tk.StringVar()
        self.CHANNEL_FREQ12_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox4.TCombobox",
            textvariable=self.CHANNEL_FREQ12_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ12_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 0", row=5, sticky="w")
        self.CHANNEL_FREQ12_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.CHANNEL_FREQ13_Label = ttk.Label(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ13_Label.configure(
            style="Heading4.TLabel", text='CH.13')
        self.CHANNEL_FREQ13_Label.grid(column=0, pady="5 0", row=6, sticky="w")
        self.CHANNEL_FREQ13_WIDGET = ttk.Entry(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ13 = tk.StringVar()
        self.CHANNEL_FREQ13_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ13,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ13_WIDGET.grid(
            column=4, padx="0 5", pady="5 0", row=6)
        _validatecmd = (
            self.CHANNEL_FREQ13_WIDGET.register(
                self.validate_CHANNEL_FREQ13), "%P", "%V")
        self.CHANNEL_FREQ13_WIDGET.configure(validatecommand=_validatecmd)
        self.label81 = ttk.Label(self.General_Extended_Channel_Frame)
        self.label81.configure(text='Hz')
        self.label81.grid(column=5, padx="0 10", pady="5 0", row=6)
        self.CHANNEL_FREQ13_MODE_WIDGET = ttk.Combobox(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ13_MODE = tk.StringVar()
        self.CHANNEL_FREQ13_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox4.TCombobox",
            textvariable=self.CHANNEL_FREQ13_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ13_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 0", row=6, sticky="w")
        self.CHANNEL_FREQ13_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.CHANNEL_FREQ14_Label = ttk.Label(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ14_Label.configure(
            style="Heading4.TLabel", text='CH.14')
        self.CHANNEL_FREQ14_Label.grid(column=0, pady="5 0", row=7, sticky="w")
        self.CHANNEL_FREQ14_WIDGET = ttk.Entry(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ14 = tk.StringVar()
        self.CHANNEL_FREQ14_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ14,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ14_WIDGET.grid(
            column=4, padx="0 5", pady="5 0", row=7)
        _validatecmd = (
            self.CHANNEL_FREQ14_WIDGET.register(
                self.validate_CHANNEL_FREQ14), "%P", "%V")
        self.CHANNEL_FREQ14_WIDGET.configure(validatecommand=_validatecmd)
        self.label83 = ttk.Label(self.General_Extended_Channel_Frame)
        self.label83.configure(text='Hz')
        self.label83.grid(column=5, padx="0 10", pady="5 0", row=7)
        self.CHANNEL_FREQ14_MODE_WIDGET = ttk.Combobox(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ14_MODE = tk.StringVar()
        self.CHANNEL_FREQ14_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox4.TCombobox",
            textvariable=self.CHANNEL_FREQ14_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ14_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 0", row=7, sticky="w")
        self.CHANNEL_FREQ14_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.CHANNEL_FREQ15_Label = ttk.Label(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ15_Label.configure(
            style="Heading4.TLabel", text='CH.15')
        self.CHANNEL_FREQ15_Label.grid(column=0, pady="5 0", row=8, sticky="w")
        self.CHANNEL_FREQ15_WIDGET = ttk.Entry(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ15 = tk.StringVar()
        self.CHANNEL_FREQ15_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ15,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ15_WIDGET.grid(
            column=4, padx="0 5", pady="5 0", row=8)
        _validatecmd = (
            self.CHANNEL_FREQ15_WIDGET.register(
                self.validate_CHANNEL_FREQ15), "%P", "%V")
        self.CHANNEL_FREQ15_WIDGET.configure(validatecommand=_validatecmd)
        self.label85 = ttk.Label(self.General_Extended_Channel_Frame)
        self.label85.configure(text='Hz')
        self.label85.grid(column=5, padx="0 10", pady="5 0", row=8)
        self.CHANNEL_FREQ15_MODE_WIDGET = ttk.Combobox(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ15_MODE = tk.StringVar()
        self.CHANNEL_FREQ15_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox4.TCombobox",
            textvariable=self.CHANNEL_FREQ15_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ15_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 0", row=8, sticky="w")
        self.CHANNEL_FREQ15_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.CHANNEL_FREQ16_Label = ttk.Label(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ16_Label.configure(
            style="Heading4.TLabel", text='CH.16')
        self.CHANNEL_FREQ16_Label.grid(column=0, pady="5 0", row=9, sticky="w")
        self.CHANNEL_FREQ16_WIDGET = ttk.Entry(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ16 = tk.StringVar()
        self.CHANNEL_FREQ16_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ16,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ16_WIDGET.grid(
            column=4, padx="0 5", pady="5 0", row=9)
        _validatecmd = (
            self.CHANNEL_FREQ16_WIDGET.register(
                self.validate_CHANNEL_FREQ16), "%P", "%V")
        self.CHANNEL_FREQ16_WIDGET.configure(validatecommand=_validatecmd)
        self.label87 = ttk.Label(self.General_Extended_Channel_Frame)
        self.label87.configure(text='Hz')
        self.label87.grid(column=5, padx="0 10", pady="5 0", row=9)
        self.CHANNEL_FREQ16_MODE_WIDGET = ttk.Combobox(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ16_MODE = tk.StringVar()
        self.CHANNEL_FREQ16_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox4.TCombobox",
            textvariable=self.CHANNEL_FREQ16_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ16_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 0", row=9, sticky="w")
        self.CHANNEL_FREQ16_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.CHANNEL_FREQ17_Label = ttk.Label(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ17_Label.configure(
            style="Heading4.TLabel", text='CH.17')
        self.CHANNEL_FREQ17_Label.grid(
            column=0, pady="5 0", row=10, sticky="w")
        self.CHANNEL_FREQ17_WIDGET = ttk.Entry(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ17 = tk.StringVar()
        self.CHANNEL_FREQ17_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ17,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ17_WIDGET.grid(
            column=4, padx="0 5", pady="5 0", row=10)
        _validatecmd = (
            self.CHANNEL_FREQ17_WIDGET.register(
                self.validate_CHANNEL_FREQ17), "%P", "%V")
        self.CHANNEL_FREQ17_WIDGET.configure(validatecommand=_validatecmd)
        self.label89 = ttk.Label(self.General_Extended_Channel_Frame)
        self.label89.configure(text='Hz')
        self.label89.grid(column=5, padx="0 10", pady="5 0", row=10)
        self.CHANNEL_FREQ17_MODE_WIDGET = ttk.Combobox(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ17_MODE = tk.StringVar()
        self.CHANNEL_FREQ17_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox4.TCombobox",
            textvariable=self.CHANNEL_FREQ17_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ17_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 0", row=10, sticky="w")
        self.CHANNEL_FREQ17_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.CHANNEL_FREQ18_Label = ttk.Label(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ18_Label.configure(
            style="Heading4.TLabel", text='CH.18')
        self.CHANNEL_FREQ18_Label.grid(
            column=0, pady="5 0", row=11, sticky="w")
        self.CHANNEL_FREQ18_WIDGET = ttk.Entry(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ18 = tk.StringVar()
        self.CHANNEL_FREQ18_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ18,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ18_WIDGET.grid(
            column=4, padx="0 5", pady="5 0", row=11)
        _validatecmd = (
            self.CHANNEL_FREQ18_WIDGET.register(
                self.validate_CHANNEL_FREQ18), "%P", "%V")
        self.CHANNEL_FREQ18_WIDGET.configure(validatecommand=_validatecmd)
        self.label91 = ttk.Label(self.General_Extended_Channel_Frame)
        self.label91.configure(text='Hz')
        self.label91.grid(column=5, padx="0 10", pady="5 0", row=11)
        self.CHANNEL_FREQ18_MODE_WIDGET = ttk.Combobox(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ18_MODE = tk.StringVar()
        self.CHANNEL_FREQ18_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox4.TCombobox",
            textvariable=self.CHANNEL_FREQ18_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ18_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 0", row=11, sticky="w")
        self.CHANNEL_FREQ18_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.CHANNEL_FREQ19_Label = ttk.Label(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ19_Label.configure(
            style="Heading4.TLabel", text='CH.19')
        self.CHANNEL_FREQ19_Label.grid(
            column=0, pady="5 0", row=12, sticky="w")
        self.CHANNEL_FREQ19_WIDGET = ttk.Entry(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ19 = tk.StringVar()
        self.CHANNEL_FREQ19_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ19,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ19_WIDGET.grid(
            column=4, padx="0 5", pady="5 0", row=12)
        _validatecmd = (
            self.CHANNEL_FREQ19_WIDGET.register(
                self.validate_CHANNEL_FREQ19), "%P", "%V")
        self.CHANNEL_FREQ19_WIDGET.configure(validatecommand=_validatecmd)
        self.label93 = ttk.Label(self.General_Extended_Channel_Frame)
        self.label93.configure(text='Hz')
        self.label93.grid(column=5, padx="0 10", pady="5 0", row=12)
        self.CHANNEL_FREQ19_MODE_WIDGET = ttk.Combobox(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ19_MODE = tk.StringVar()
        self.CHANNEL_FREQ19_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox4.TCombobox",
            textvariable=self.CHANNEL_FREQ19_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ19_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 0", row=12, sticky="w")
        self.CHANNEL_FREQ19_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.CHANNEL_FREQ20_Label = ttk.Label(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ20_Label.configure(
            style="Heading4.TLabel", text='CH.20')
        self.CHANNEL_FREQ20_Label.grid(
            column=0, padx="0 5", pady="5 0", row=13, sticky="w")
        self.CHANNEL_FREQ20_WIDGET = ttk.Entry(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ20 = tk.StringVar()
        self.CHANNEL_FREQ20_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CHANNEL_FREQ20,
            validate="focus",
            width=10)
        self.CHANNEL_FREQ20_WIDGET.grid(
            column=4, padx="0 5", pady="5 0", row=13)
        _validatecmd = (
            self.CHANNEL_FREQ20_WIDGET.register(
                self.validate_CHANNEL_FREQ20), "%P", "%V")
        self.CHANNEL_FREQ20_WIDGET.configure(validatecommand=_validatecmd)
        self.label95 = ttk.Label(self.General_Extended_Channel_Frame)
        self.label95.configure(text='Hz')
        self.label95.grid(column=5, padx="0 10", pady="5 0", row=13)
        self.CHANNEL_FREQ20_MODE_WIDGET = ttk.Combobox(
            self.General_Extended_Channel_Frame)
        self.CHANNEL_FREQ20_MODE = tk.StringVar()
        self.CHANNEL_FREQ20_MODE_WIDGET.configure(
            justify="center",
            state="readonly",
            style="ComboBox4.TCombobox",
            textvariable=self.CHANNEL_FREQ20_MODE,
            validate="focusout",
            values='DEFAULT LSB USB CWL CWU',
            width=10)
        self.CHANNEL_FREQ20_MODE_WIDGET.grid(
            column=7, padx="0 2", pady="5 0", row=13, sticky="w")
        self.CHANNEL_FREQ20_MODE_WIDGET.configure(
            validatecommand=self.clearErrorMsgPersistFlag)
        self.General_Extended_Channel_Frame.pack(
            anchor="w", expand="false", fill="x", padx="50 0", side="left")
        self.General_Extended_Channel_Frame.grid_anchor("w")
        self.Extended_Channel_Frame.pack(anchor="w")
        self.All_Channel_Frame.pack(side="top")
        self.Operator_Channel_Frame.pack(anchor="w", side="top")
        self.frame45.pack(anchor="w", expand="true", fill="both", side="top")
        self.Channels_SF.pack(side="top")
        self.settingsNotebook.add(self.Channels_SF, text='Channels')
        self.WSPR_SF = ScrolledFrame(self.settingsNotebook, scrolltype="both")
        self.WSPR_SF.configure(usemousewheel=True)
        self.frame22 = ttk.Frame(self.WSPR_SF.innerframe)
        self.frame22.configure(height=200, width=200)
        self.WSPR_Frame = ttk.Frame(self.frame22)
        self.label6 = ttk.Label(self.WSPR_Frame)
        self.label6.configure(
            justify="center",
            style="Heading2.TLabel",
            text='WSPR Settings')
        self.label6.grid(
            column=0,
            columnspan=5,
            padx=5,
            pady="15 25",
            row=0,
            sticky="n")
        self.WSPR_Frame.pack(expand="true", fill="both", side="top")
        self.frame34 = ttk.Frame(self.frame22)
        self.frame34.configure(height=200, width=200)
        self.frame35 = ttk.Frame(self.frame34)
        self.frame35.configure(height=200, width=200)
        self.label27 = ttk.Label(self.frame35)
        self.label27.configure(
            compound="top",
            justify="left",
            style="Heading3.TLabel",
            text='Messages')
        self.label27.pack()
        self.frame35.pack(anchor="w", side="top")
        self.frame36 = ttk.Frame(self.frame34)
        self.frame36.configure(height=200, width=200)
        self.label44 = ttk.Label(self.frame36)
        self.label44.configure(style="Heading4.TLabel", text='Total Msgs')
        self.label44.grid(
            column=0,
            columnspan=2,
            padx="0 10",
            pady="10 15",
            row=0,
            sticky="e")
        self.label73 = ttk.Label(self.frame36)
        self.label73.configure(style="Heading4.TLabel", text='Name')
        self.label73.grid(column=1, padx="0 10", row=1, sticky="w")
        self.label76 = ttk.Label(self.frame36)
        self.label76.configure(style="Heading4.TLabel", text='WSPR Message')
        self.label76.grid(column=3, padx="0 10", row=1, sticky="w")
        self.label47 = ttk.Label(self.frame36)
        self.label47.configure(style="Heading4.TLabel", text='1')
        self.label47.grid(column=0, padx="0 10", pady=10, row=2, sticky="e")
        self.WSPR_MESSAGE1_NAME_WIDGET = ttk.Entry(self.frame36)
        self.WSPR_MESSAGE1_NAME = tk.StringVar()
        self.WSPR_MESSAGE1_NAME_WIDGET.configure(
            style="Normal.TEntry",
            textvariable=self.WSPR_MESSAGE1_NAME,
            validate="focus",
            width=6)
        self.WSPR_MESSAGE1_NAME_WIDGET.grid(column=1, padx="0 10", row=2)
        _validatecmd = (
            self.WSPR_MESSAGE1_NAME_WIDGET.register(
                self.validate_WSPR_MESSAGE1_NAME), "%P", "%V")
        self.WSPR_MESSAGE1_NAME_WIDGET.configure(validatecommand=_validatecmd)
        self.WSPR_Msg1_WIDGET = ttk.Button(self.frame36)
        self.WSPR_Msg1_WIDGET.configure(style="Normal.TButton", text='Gen Msg')
        self.WSPR_Msg1_WIDGET.grid(column=2, padx="0 10", pady=10, row=2)
        self.WSPR_Msg1_WIDGET.configure(command=self.runWSPRMsg1Gen_CB)
        self.WSPR_MESSAGE1_WIDGET = ttk.Entry(self.frame36)
        self.WSPR_MESSAGE1 = tk.StringVar()
        self.WSPR_MESSAGE1_WIDGET.configure(
            justify="left",
            state="readonly",
            style="Normal.TEntry",
            textvariable=self.WSPR_MESSAGE1,
            validate="none",
            width=80)
        self.WSPR_MESSAGE1_WIDGET.grid(
            column=3, padx="0 10", row=2, sticky="w")
        self.label48 = ttk.Label(self.frame36)
        self.label48.configure(style="Heading4.TLabel", text='2')
        self.label48.grid(column=0, padx="0 10", row=3, sticky="e")
        self.WSPR_MESSAGE2_NAME_WIDGET = ttk.Entry(self.frame36)
        self.WSPR_MESSAGE2_NAME = tk.StringVar()
        self.WSPR_MESSAGE2_NAME_WIDGET.configure(
            style="Normal.TEntry",
            textvariable=self.WSPR_MESSAGE2_NAME,
            validate="focus",
            width=6)
        self.WSPR_MESSAGE2_NAME_WIDGET.grid(column=1, padx="0 10", row=3)
        _validatecmd = (
            self.WSPR_MESSAGE2_NAME_WIDGET.register(
                self.validate_WSPR_MESSAGE2_NAME), "%P", "%V")
        self.WSPR_MESSAGE2_NAME_WIDGET.configure(validatecommand=_validatecmd)
        self.WSPR_Msg2_WIDGET = ttk.Button(self.frame36)
        self.WSPR_Msg2_WIDGET.configure(style="Normal.TButton", text='Gen Msg')
        self.WSPR_Msg2_WIDGET.grid(column=2, padx="0 10", pady=10, row=3)
        self.WSPR_Msg2_WIDGET.configure(command=self.runWSPRMsg2Gen_CB)
        self.WSPR_MESSAGE2_WIDGET = ttk.Entry(self.frame36)
        self.WSPR_MESSAGE2 = tk.StringVar()
        self.WSPR_MESSAGE2_WIDGET.configure(
            justify="left",
            state="readonly",
            style="Normal.TEntry",
            textvariable=self.WSPR_MESSAGE2,
            validate="none",
            width=80)
        self.WSPR_MESSAGE2_WIDGET.grid(
            column=3, padx="0 10", row=3, sticky="w")
        self.label50 = ttk.Label(self.frame36)
        self.label50.configure(style="Heading4.TLabel", text='3')
        self.label50.grid(column=0, padx="0 10", row=4, sticky="e")
        self.WSPR_MESSAGE3_NAME_WIDGET = ttk.Entry(self.frame36)
        self.WSPR_MESSAGE3_NAME = tk.StringVar()
        self.WSPR_MESSAGE3_NAME_WIDGET.configure(
            style="Normal.TEntry",
            textvariable=self.WSPR_MESSAGE3_NAME,
            validate="focus",
            width=6)
        self.WSPR_MESSAGE3_NAME_WIDGET.grid(column=1, padx="0 10", row=4)
        _validatecmd = (
            self.WSPR_MESSAGE3_NAME_WIDGET.register(
                self.validate_WSPR_MESSAGE3_NAME), "%P", "%V")
        self.WSPR_MESSAGE3_NAME_WIDGET.configure(validatecommand=_validatecmd)
        self.WSPR_Msg3_WIDGET = ttk.Button(self.frame36)
        self.WSPR_Msg3_WIDGET.configure(style="Normal.TButton", text='Gen Msg')
        self.WSPR_Msg3_WIDGET.grid(column=2, padx="0 10", pady=10, row=4)
        self.WSPR_Msg3_WIDGET.configure(command=self.runWSPRMsg3Gen_CB)
        self.WSPR_MESSAGE3_WIDGET = ttk.Entry(self.frame36)
        self.WSPR_MESSAGE3 = tk.StringVar()
        self.WSPR_MESSAGE3_WIDGET.configure(
            justify="left",
            state="readonly",
            style="Normal.TEntry",
            textvariable=self.WSPR_MESSAGE3,
            validate="none",
            width=80)
        self.WSPR_MESSAGE3_WIDGET.grid(
            column=3, padx="0 10", row=4, sticky="w")
        self.label51 = ttk.Label(self.frame36)
        self.label51.configure(style="Heading4.TLabel", text='4')
        self.label51.grid(column=0, padx="0 10", row=5, sticky="e")
        self.WSPR_MESSAGE4_NAME_WIDGET = ttk.Entry(self.frame36)
        self.WSPR_MESSAGE4_NAME = tk.StringVar()
        self.WSPR_MESSAGE4_NAME_WIDGET.configure(
            style="Normal.TEntry",
            textvariable=self.WSPR_MESSAGE4_NAME,
            validate="focus",
            width=6)
        self.WSPR_MESSAGE4_NAME_WIDGET.grid(column=1, padx="0 10", row=5)
        _validatecmd = (
            self.WSPR_MESSAGE4_NAME_WIDGET.register(
                self.validate_WSPR_MESSAGE4_NAME), "%P", "%V")
        self.WSPR_MESSAGE4_NAME_WIDGET.configure(validatecommand=_validatecmd)
        self.WSPR_Msg4_WIDGET = ttk.Button(self.frame36)
        self.WSPR_Msg4_WIDGET.configure(style="Normal.TButton", text='Gen Msg')
        self.WSPR_Msg4_WIDGET.grid(column=2, padx="0 10", pady=10, row=5)
        self.WSPR_Msg4_WIDGET.configure(command=self.runWSPRMsg4Gen_CB)
        self.WSPR_MESSAGE4_WIDGET = ttk.Entry(self.frame36)
        self.WSPR_MESSAGE4 = tk.StringVar()
        self.WSPR_MESSAGE4_WIDGET.configure(
            justify="left",
            state="readonly",
            style="Normal.TEntry",
            textvariable=self.WSPR_MESSAGE4,
            validate="none",
            width=80)
        self.WSPR_MESSAGE4_WIDGET.grid(
            column=3, padx="0 10", row=5, sticky="w")
        self.WSPR_COUNT = tk.StringVar(value='0')
        __values = ['0', '1', '2', '3', '4']
        self.WSPR_COUNT_WIDGET = tk.OptionMenu(
            self.frame36, self.WSPR_COUNT, *__values, command=None)
        self.WSPR_COUNT_WIDGET.grid(column=2, row=0)
        self.frame36.pack(anchor="w", padx="20 0", side="top")
        self.frame34.pack(anchor="w", padx=20, side="top")
        self.frame37 = ttk.Frame(self.frame22)
        self.frame37.configure(height=200, width=200)
        self.frame38 = ttk.Frame(self.frame37)
        self.frame38.configure(height=200, width=200)
        self.label62 = ttk.Label(self.frame38)
        self.label62.configure(
            compound="top",
            justify="left",
            style="Heading3.TLabel",
            text='Bands')
        self.label62.pack()
        self.frame38.pack(anchor="w", side="top")
        self.frame39 = ttk.Frame(self.frame37)
        self.frame39.configure(height=200, width=200)
        self.label64 = ttk.Label(self.frame39)
        self.label64.configure(style="Heading4.TLabel", text='1')
        self.label64.grid(column=0, padx="0 10", row=1, sticky="e")
        self.WSPR_BAND1_TXFREQ_WIDGET = ttk.Entry(self.frame39)
        self.WSPR_BAND1_TXFREQ = tk.StringVar()
        self.WSPR_BAND1_TXFREQ_WIDGET.configure(
            justify="right",
            state="readonly",
            style="Normal.TEntry",
            textvariable=self.WSPR_BAND1_TXFREQ,
            validate="none",
            width=12)
        self.WSPR_BAND1_TXFREQ_WIDGET.grid(
            column=2, pady="0 10", row=1, sticky="w")
        self.label78 = ttk.Label(self.frame39)
        self.label78.configure(style="Heading4.TLabel", text='Hz')
        self.label78.grid(column=3, padx="0 10", row=1, sticky="w")
        self.button9 = ttk.Button(self.frame39)
        self.button9.configure(
            style="Button4.TButton",
            text='Select Band and Freq')
        self.button9.grid(column=4, padx="0 10", row=1)
        self.button9.configure(command=self.runWSPR_Band1_Select_Button_CB)
        self.label65 = ttk.Label(self.frame39)
        self.label65.configure(style="Heading4.TLabel", text='2')
        self.label65.grid(column=0, padx="0 10", row=2, sticky="e")
        self.WSPR_BAND2_TXFREQ_WIDGET = ttk.Entry(self.frame39)
        self.WSPR_BAND2_TXFREQ = tk.StringVar()
        self.WSPR_BAND2_TXFREQ_WIDGET.configure(
            justify="right",
            state="readonly",
            style="Normal.TEntry",
            textvariable=self.WSPR_BAND2_TXFREQ,
            validate="none",
            width=12)
        self.WSPR_BAND2_TXFREQ_WIDGET.grid(
            column=2, pady="0 10", row=2, sticky="w")
        self.label80 = ttk.Label(self.frame39)
        self.label80.configure(style="Heading4.TLabel", text='Hz')
        self.label80.grid(column=3, padx="0 10", row=2, sticky="w")
        self.button10 = ttk.Button(self.frame39)
        self.button10.configure(
            style="Button4.TButton",
            text='Select Band and Freq')
        self.button10.grid(column=4, padx="0 10", row=2)
        self.button10.configure(command=self.runWSPR_Band2_Select_Button_CB)
        self.label66 = ttk.Label(self.frame39)
        self.label66.configure(style="Heading4.TLabel", text='3')
        self.label66.grid(column=0, padx="0 10", row=3, sticky="e")
        self.WSPR_BAND3_TXFREQ_WIDGET = ttk.Entry(self.frame39)
        self.WSPR_BAND3_TXFREQ = tk.StringVar()
        self.WSPR_BAND3_TXFREQ_WIDGET.configure(
            justify="right",
            state="readonly",
            style="Normal.TEntry",
            textvariable=self.WSPR_BAND3_TXFREQ,
            validate="none",
            width=12)
        self.WSPR_BAND3_TXFREQ_WIDGET.grid(column=2, row=3, sticky="w")
        self.label82 = ttk.Label(self.frame39)
        self.label82.configure(style="Heading4.TLabel", text='Hz')
        self.label82.grid(column=3, padx="0 10", row=3, sticky="w")
        self.button11 = ttk.Button(self.frame39)
        self.button11.configure(
            style="Button4.TButton",
            text='Select Band and Freq')
        self.button11.grid(column=4, padx="0 10", row=3)
        self.button11.configure(command=self.runWSPR_Band3_Select_Button_CB)
        self.frame39.pack(anchor="w", padx="20 0", side="top")
        self.frame37.pack(anchor="w", padx=20, pady=20, side="top")
        self.WSPR_HIDDEN = ttk.Frame(self.frame22)
        self.WSPR_HIDDEN.configure(height=200, width=200)
        self.WSPR_BAND1_MULTICHAN_WIDGET = ttk.Label(self.WSPR_HIDDEN)
        self.WSPR_BAND1_MULTICHAN = tk.StringVar()
        self.WSPR_BAND1_MULTICHAN_WIDGET.configure(
            textvariable=self.WSPR_BAND1_MULTICHAN)
        self.WSPR_BAND1_MULTICHAN_WIDGET.pack(anchor="nw", side="left")
        self.WSPR_BAND1_REG1_WIDGET = ttk.Label(self.WSPR_HIDDEN)
        self.WSPR_BAND1_REG1 = tk.StringVar()
        self.WSPR_BAND1_REG1_WIDGET.configure(
            textvariable=self.WSPR_BAND1_REG1)
        self.WSPR_BAND1_REG1_WIDGET.pack(anchor="nw", side="left")
        self.WSPR_BAND1_REG2_WIDGET = ttk.Label(self.WSPR_HIDDEN)
        self.WSPR_BAND1_REG2 = tk.StringVar()
        self.WSPR_BAND1_REG2_WIDGET.configure(
            textvariable=self.WSPR_BAND1_REG2)
        self.WSPR_BAND1_REG2_WIDGET.pack(anchor="nw", side="left")
        self.WSPR_BAND2_MULTICHAN_WIDGET = ttk.Label(self.WSPR_HIDDEN)
        self.WSPR_BAND2_MULTICHAN = tk.StringVar()
        self.WSPR_BAND2_MULTICHAN_WIDGET.configure(
            textvariable=self.WSPR_BAND2_MULTICHAN)
        self.WSPR_BAND2_MULTICHAN_WIDGET.pack(anchor="w", side="left")
        self.WSPR_BAND2_REG1_WIDGET = ttk.Label(self.WSPR_HIDDEN)
        self.WSPR_BAND2_REG1 = tk.StringVar()
        self.WSPR_BAND2_REG1_WIDGET.configure(
            textvariable=self.WSPR_BAND2_REG1)
        self.WSPR_BAND2_REG1_WIDGET.pack(anchor="w", side="left")
        self.WSPR_BAND2_REG2_WIDGET = ttk.Label(self.WSPR_HIDDEN)
        self.WSPR_BAND2_REG2 = tk.StringVar()
        self.WSPR_BAND2_REG2_WIDGET.configure(
            textvariable=self.WSPR_BAND2_REG2)
        self.WSPR_BAND2_REG2_WIDGET.pack(anchor="w", side="left")
        self.WSPR_BAND3_MULTICHAN_WIDGET = ttk.Label(self.WSPR_HIDDEN)
        self.WSPR_BAND3_MULTICHAN = tk.StringVar()
        self.WSPR_BAND3_MULTICHAN_WIDGET.configure(
            textvariable=self.WSPR_BAND3_MULTICHAN)
        self.WSPR_BAND3_MULTICHAN_WIDGET.pack(anchor="sw", side="left")
        self.WSPR_BAND3_REG1_WIDGET = ttk.Label(self.WSPR_HIDDEN)
        self.WSPR_BAND3_REG1 = tk.StringVar()
        self.WSPR_BAND3_REG1_WIDGET.configure(
            textvariable=self.WSPR_BAND3_REG1)
        self.WSPR_BAND3_REG1_WIDGET.pack(anchor="sw", side="left")
        self.WSPR_BAND3_REG2_WIDGET = ttk.Label(self.WSPR_HIDDEN)
        self.WSPR_BAND3_REG2 = tk.StringVar()
        self.WSPR_BAND3_REG2_WIDGET.configure(
            textvariable=self.WSPR_BAND3_REG2)
        self.WSPR_BAND3_REG2_WIDGET.pack(anchor="sw", side="left")
        self.WSPR_HIDDEN.pack(side="top")
        self.frame22.pack(anchor="w", padx=5, pady=5, side="top")
        self.WSPR_SF.pack(side="top")
        self.settingsNotebook.add(self.WSPR_SF, text='WSPR')
        self.LCD_SF = ScrolledFrame(self.settingsNotebook, scrolltype="both")
        self.LCD_SF.configure(usemousewheel=True)
        self.frame24 = ttk.Frame(self.LCD_SF.innerframe)
        self.frame24.configure(height=200, width=200)
        self.LCD_Frame = ttk.Frame(self.frame24)
        self.label8 = ttk.Label(self.LCD_Frame)
        self.label8.configure(
            justify="center",
            style="Heading2.TLabel",
            text='Settings for LCD Displays')
        self.label8.grid(column=0, padx="0 20", pady=10, row=0, sticky="nw")
        self.LCD_Frame.pack(anchor="w", side="top")
        self.frame25 = ttk.Frame(self.frame24)
        self.frame25.configure(height=200, width=200)
        self.frame2 = ttk.Frame(self.frame25)
        self.label22 = ttk.Label(self.frame2)
        self.label22.configure(
            relief="flat",
            style="Heading3.TLabel",
            text='LCD Addresses (I2C attached only)')
        self.label22.grid(column=0, columnspan=2, padx=5, row=2, sticky="ew")
        self.label90 = ttk.Label(self.frame2)
        self.label90.grid(column=4, row=2)
        self.label28 = ttk.Label(self.frame2)
        self.label28.configure(style="Normal.TLabel", text='Master I2C LCD')
        self.label28.grid(column=1, padx="75 5", row=4, sticky="w")
        self.I2C_LCD_MASTER_WIDGET = ttk.Entry(self.frame2)
        self.I2C_LCD_MASTER = tk.StringVar()
        self.I2C_LCD_MASTER_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.I2C_LCD_MASTER,
            validate="focus",
            width=10)
        self.I2C_LCD_MASTER_WIDGET.grid(
            column=3, padx="0 5", row=4, sticky="w")
        _validatecmd = (
            self.I2C_LCD_MASTER_WIDGET.register(
                self.validate_I2C_LCD_MASTER), "%P", "%V")
        self.I2C_LCD_MASTER_WIDGET.configure(validatecommand=_validatecmd)
        self.label137 = ttk.Label(self.frame2)
        self.label137.configure(
            state="normal",
            style="Normal.TLabel",
            text='(Valid: 0x00 - 0x7f)')
        self.label137.grid(column=4, pady="0 5", row=4)
        self.runI2CScanner_WIDGET = ttk.Button(self.frame2)
        self.runI2CScanner_WIDGET.configure(
            style="Button4.TButton", text='I2C Scanner')
        self.runI2CScanner_WIDGET.grid(
            column=4, padx=25, pady=10, row=5, sticky="e")
        self.runI2CScanner_WIDGET.configure(command=self.runI2CScanner)
        self.label32 = ttk.Label(self.frame2)
        self.label32.configure(
            style="Normal.TLabel",
            text='Secondary I2C LCD\nDual LCD Config')
        self.label32.grid(column=1, padx="75 10", row=6, sticky="w")
        self.I2C_LCD_SECOND_WIDGET = ttk.Entry(self.frame2)
        self.I2C_LCD_SECOND = tk.StringVar()
        self.I2C_LCD_SECOND_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.I2C_LCD_SECOND,
            validate="focus",
            width=10)
        self.I2C_LCD_SECOND_WIDGET.grid(column=3, row=6, sticky="w")
        _validatecmd = (
            self.I2C_LCD_SECOND_WIDGET.register(
                self.validate_I2C_LCD_SECOND), "%P", "%V")
        self.I2C_LCD_SECOND_WIDGET.configure(validatecommand=_validatecmd)
        self.label138 = ttk.Label(self.frame2)
        self.label138.configure(
            state="normal",
            style="Normal.TLabel",
            text='(Valid: 0x00 - 0x7f)')
        self.label138.grid(column=4, pady="0 5", row=6)
        self.frame2.pack(anchor="w", side="top")
        self.frame2.grid_anchor("nw")
        self.frame11 = ttk.Frame(self.frame25)
        self.label9 = ttk.Label(self.frame11)
        self.label9.configure(
            relief="flat",
            style="Heading3.TLabel",
            text='LCD User Interface Customization (all LCDs)')
        self.label9.grid(
            column=0,
            columnspan=2,
            padx=5,
            pady="20 0",
            row=2,
            sticky="ew")
        self.SCROLLING_DISPLAY_WIDGET = ttk.Checkbutton(self.frame11)
        self.SCROLLING_DISPLAY = tk.StringVar()
        self.SCROLLING_DISPLAY_WIDGET.configure(
            offvalue="NO",
            onvalue="YES",
            style="CheckboxNormal.TCheckbutton",
            text='When displayed, continuously scroll VFO-B line left to display more info',
            variable=self.SCROLLING_DISPLAY)
        self.SCROLLING_DISPLAY_WIDGET.grid(
            column=0, padx=75, row=5, sticky="w")
        self.MESSAGE_LINE_WIDGET = ttk.Checkbutton(self.frame11)
        self.MESSAGE_LINE = tk.StringVar()
        self.MESSAGE_LINE_WIDGET.configure(
            offvalue="NO",
            onvalue="YES",
            style="CheckboxNormal.TCheckbutton",
            text='Do not display VFO-B. Reserve its line for messages (e.g., CW Keyer). Overides above scrolling option.',
            variable=self.MESSAGE_LINE)
        self.MESSAGE_LINE_WIDGET.grid(column=0, padx=75, row=6, sticky="w")
        self.ONE_TWO_LINE_TOGGLE_WIDGET = ttk.Checkbutton(self.frame11)
        self.ONE_TWO_LINE_TOGGLE = tk.StringVar()
        self.ONE_TWO_LINE_TOGGLE_WIDGET.configure(
            offvalue="NO",
            onvalue="YES",
            style="CheckboxNormal.TCheckbutton",
            text='Put VFO-A on top line',
            variable=self.ONE_TWO_LINE_TOGGLE)
        self.ONE_TWO_LINE_TOGGLE_WIDGET.grid(
            column=0, padx=75, row=4, sticky="w")
        self.label11 = ttk.Label(self.frame11)
        self.label11.configure(
            relief="flat",
            state="normal",
            style="Normal.TLabel",
            text='The default display is for VFO-A and its Mode to be on second line and the top line is used for VFO-B and other info. These checkboxes allow you to customize this display.',
            wraplength=550)
        self.label11.grid(column=0, padx=50, pady="5 10", row=3, sticky="w")
        self.frame11.pack(anchor="w", pady=5, side="top")
        self.frame11.grid_anchor("nw")
        self.frame25.pack(anchor="w", padx=20, side="top")
        self.frame24.pack(
            anchor="n",
            expand="true",
            fill="both",
            padx=5,
            pady=5,
            side="top")
        self.LCD_HIDDEN = ttk.Frame(self.LCD_SF.innerframe)
        self.LCD_HIDDEN.configure(height=200, width=200)
        self.MAIN_SCREEN_FORMAT_WIDGET = ttk.Label(self.LCD_HIDDEN)
        self.MAIN_SCREEN_FORMAT = tk.StringVar()
        self.MAIN_SCREEN_FORMAT_WIDGET.configure(
            textvariable=self.MAIN_SCREEN_FORMAT)
        self.MAIN_SCREEN_FORMAT_WIDGET.pack(side="top")
        self.NEXTION_DISPLAY_CALL_SIGN_WIDGET = ttk.Label(self.LCD_HIDDEN)
        self.NEXTION_DISPLAY_CALL_SIGN = tk.StringVar()
        self.NEXTION_DISPLAY_CALL_SIGN_WIDGET.configure(
            textvariable=self.NEXTION_DISPLAY_CALL_SIGN)
        self.NEXTION_DISPLAY_CALL_SIGN_WIDGET.pack(side="top")
        self.LCD_HIDDEN.pack(side="top")
        self.LCD_SF.pack(side="top")
        self.settingsNotebook.add(self.LCD_SF, text='Displays')
        self.SDR_SF = ScrolledFrame(self.settingsNotebook, scrolltype="both")
        self.SDR_SF.configure(usemousewheel=True)
        self.frame13 = ttk.Frame(self.SDR_SF.innerframe)
        self.frame13.configure(height=200, width=200)
        self.SDR_Label_Frame = ttk.Frame(self.frame13)
        self.label7 = ttk.Label(self.SDR_Label_Frame)
        self.label7.configure(
            justify="center",
            style="Heading2.TLabel",
            text='SDR Settings')
        self.label7.pack(anchor="w", padx=5, pady="15 25", side="top")
        self.SDR_Label_Frame.pack(
            anchor="n",
            expand="true",
            fill="x",
            padx=5,
            pady=5,
            side="top")
        self.frame14 = ttk.Frame(self.frame13)
        self.label23 = ttk.Label(self.frame14)
        self.label23.configure(
            style="Heading4.TLabel",
            text='SDR Frequency Mode')
        self.label23.grid(
            column=1,
            columnspan=2,
            padx=10,
            pady="0 5",
            row=4,
            sticky="e")
        self.SDR_OFFSET_MODE = tk.StringVar(value='NONE')
        __values = ['NONE', 'FIXED', 'MHZ', 'KHZ']
        self.SDR_OFFSET_MODE_WIDGET = ttk.OptionMenu(
            self.frame14, self.SDR_OFFSET_MODE, "NONE", *__values, command=None)
        self.SDR_OFFSET_MODE_WIDGET.grid(
            column=3, padx="0 20", pady="0 5", row=4)
        self.message1 = tk.Message(self.frame14)
        self.message1.configure(justify="left", relief="raised", text="NONE:\tNo offset is provided to the data send to the \n\tSDR\n\nFIXED:\tThe SDR offset frequency is added to the\n\tfrequency on the display and sent to the SDR\n\nMHZ:\tThe single MHZ digit of the radio's frequency is\n\tadded. For example, if the radio was at\n\t14.032.000, and the offset was at 30.000.000,\n\tthe resulting frequency would be 43.032.000.\n\nKHZ:\tSimilar to MHZ_OFFSET, but using the KHZ\n\tnumber. So with a 30.000.000 offset and and \n\ta 14.032.000 radio setting, the SDR will see \n\ta 30.032.000 frequency.", width=500)
        self.message1.grid(column=2, columnspan=3, padx="100 0", row=5)
        self.label24 = ttk.Label(self.frame14)
        self.label24.configure(
            justify="left",
            style="Heading4.TLabel",
            text='Offset Frequency (mhz)')
        self.label24.grid(
            column=1,
            columnspan=2,
            padx=10,
            pady="20 0",
            row=6,
            sticky="e")
        self.SDR_FREQUENCY_WIDGET = ttk.Entry(self.frame14)
        self.SDR_FREQUENCY = tk.StringVar()
        self.SDR_FREQUENCY_WIDGET.configure(
            justify="right",
            state="normal",
            style="Normal.TEntry",
            textvariable=self.SDR_FREQUENCY,
            validate="focus",
            width=10)
        self.SDR_FREQUENCY_WIDGET.grid(
            column=3, pady="20 0", row=6, sticky="w")
        _validatecmd = (
            self.SDR_FREQUENCY_WIDGET.register(
                self.validate_SDR_FREQUENCY), "%P", "%V")
        self.SDR_FREQUENCY_WIDGET.configure(validatecommand=_validatecmd)
        self.BOOT_INTO_SDR_MODE_WIDGET = ttk.Checkbutton(self.frame14)
        self.BOOT_INTO_SDR_MODE = tk.StringVar()
        self.BOOT_INTO_SDR_MODE_WIDGET.configure(
            offvalue="NORMAL",
            onvalue="SDR",
            style="Checkbox4.TCheckbutton",
            text='Boot into SDR Mode',
            variable=self.BOOT_INTO_SDR_MODE)
        self.BOOT_INTO_SDR_MODE_WIDGET.grid(
            column=1, columnspan=4, padx=8, pady=20, row=7, sticky="w")
        self.frame14.pack(
            anchor="center",
            expand="false",
            fill="x",
            padx=20,
            side="top")
        self.frame14.grid_anchor("nw")
        self.frame13.pack(
            anchor="n",
            expand="true",
            fill="x",
            padx=5,
            pady=5,
            side="top")
        self.SDR_SF.pack(side="top")
        self.settingsNotebook.add(self.SDR_SF, text='SDR')
        self.Extensions_SF = ScrolledFrame(
            self.settingsNotebook, scrolltype="both")
        self.Extensions_SF.configure(usemousewheel=True)
        self.Extensions_Frame = ttk.Frame(self.Extensions_SF.innerframe)
        self.frame17 = ttk.Frame(self.Extensions_Frame)
        self.frame17.configure(height=200, width=200)
        self.label5 = ttk.Label(self.frame17)
        self.label5.configure(
            justify="center",
            style="Heading2.TLabel",
            text='KD8CEC Extentions')
        self.label5.pack(anchor="w", padx=5)
        self.frame17.pack(anchor="w", expand="false", padx=5, side="top")
        self.frame29 = ttk.Frame(self.Extensions_Frame)
        self.frame55 = ttk.Frame(self.frame29)
        self.frame55.configure(height=200, width=200)
        self.label4 = ttk.Label(self.frame55)
        self.label4.configure(
            justify="left",
            style="Heading3.TLabel",
            text='Extended Keys')
        self.label4.grid(column=0, row=0)
        self.message6 = tk.Message(self.frame55)
        self.message6.configure(
            borderwidth=2,
            font="TkTextFont",
            justify="left",
            pady=5,
            relief="ridge",
            takefocus=False,
            text='Supports attachment and control of an external button box. \n\nNOTE: Does NOT work with rotary encodes driven off digital pins. This is specific to the Pico, but depending on how KD8CEC is configured, my apply to other boards too.\n\nFor details, on the original design see: \nhttp://www.hamskey.com/2018/04/add-extended-switchs-to-ubitx-with.html',
            width=500)
        self.message6.grid(column=2, padx=10, row=0)
        self.frame55.grid(column=0, columnspan=10, pady="10 5", row=0)
        self.label14 = ttk.Label(self.frame29)
        self.label14.configure(style="Heading4.TLabel", text='ADC Range')
        self.label14.grid(column=4, columnspan=2, row=5)
        self.label16 = ttk.Label(self.frame29)
        self.label16.configure(style="Heading4.TLabel", text='Function')
        self.label16.grid(column=2, columnspan=2, row=6, sticky="s")
        self.label17 = ttk.Label(self.frame29)
        self.label17.configure(style="Heading4.TLabel", text='Start', width=7)
        self.label17.grid(column=4, padx="18 0", row=6, sticky="s")
        self.label18 = ttk.Label(self.frame29)
        self.label18.configure(style="Heading4.TLabel", text='End\t', width=7)
        self.label18.grid(column=5, padx="20 0", row=6, sticky="s")
        self.EXTENDED_KEY1_FUNC_LABEL = ttk.Label(self.frame29)
        self.EXTENDED_KEY1_FUNC_LABEL.configure(
            style="Heading4.TLabel", text='Key 1')
        self.EXTENDED_KEY1_FUNC_LABEL.grid(
            column=1, padx="0 15", pady="0 5", row=7, sticky="w")
        self.EXTENDED_KEY1_FUNC_WIDGET = ttk.Combobox(self.frame29)
        self.EXTENDED_KEY1_FUNC = tk.StringVar()
        self.EXTENDED_KEY1_FUNC_WIDGET.configure(
            textvariable=self.EXTENDED_KEY1_FUNC,
            values='NONE MODE BAND-UP BAND-DN TUNE-STEP VFO-A/B SPLIT TX SDR-MODE RIT',
            width=10)
        self.EXTENDED_KEY1_FUNC_WIDGET.grid(column=2, row=7)
        self.EXTENDED_KEY1_START_WIDGET = ttk.Entry(self.frame29)
        self.EXTENDED_KEY1_START = tk.StringVar()
        self.EXTENDED_KEY1_START_WIDGET.configure(
            justify="right",
            style="NoBorder.TEntry",
            textvariable=self.EXTENDED_KEY1_START,
            validate="focus",
            width=5)
        self.EXTENDED_KEY1_START_WIDGET.grid(column=4, pady="0 5", row=7)
        _validatecmd = (self.EXTENDED_KEY1_START_WIDGET.register(
            self.validate_EXTENDED_KEY1_START), "%P", "%V")
        self.EXTENDED_KEY1_START_WIDGET.configure(validatecommand=_validatecmd)
        self.EXTENDED_KEY1_END_WIDGET = ttk.Entry(self.frame29)
        self.EXTENDED_KEY1_END = tk.StringVar()
        self.EXTENDED_KEY1_END_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.EXTENDED_KEY1_END,
            validate="focus",
            width=5)
        self.EXTENDED_KEY1_END_WIDGET.grid(column=5, pady="0 5", row=7)
        _validatecmd = (
            self.EXTENDED_KEY1_END_WIDGET.register(
                self.validate_EXTENDED_KEY1_END), "%P", "%V")
        self.EXTENDED_KEY1_END_WIDGET.configure(validatecommand=_validatecmd)
        self.EXTENDED_KEY2_FUNC_LABEL = ttk.Label(self.frame29)
        self.EXTENDED_KEY2_FUNC_LABEL.configure(
            style="Heading4.TLabel", text='Key 2')
        self.EXTENDED_KEY2_FUNC_LABEL.grid(
            column=1, pady="0 5", row=8, sticky="w")
        self.EXTENDED_KEY2_FUNC_WIDGET = ttk.Combobox(self.frame29)
        self.EXTENDED_KEY2_FUNC = tk.StringVar()
        self.EXTENDED_KEY2_FUNC_WIDGET.configure(
            textvariable=self.EXTENDED_KEY2_FUNC,
            values='NONE MODE BAND-UP BAND-DN TUNE-STEP VFO-A/B SPLIT TX SDR-MODE RIT',
            width=10)
        self.EXTENDED_KEY2_FUNC_WIDGET.grid(column=2, row=8)
        self.EXTENDED_KEY2_START_WIDGET = ttk.Entry(self.frame29)
        self.EXTENDED_KEY2_START = tk.StringVar()
        self.EXTENDED_KEY2_START_WIDGET.configure(
            justify="right",
            style="NoBorder.TEntry",
            textvariable=self.EXTENDED_KEY2_START,
            validate="focus",
            width=5)
        self.EXTENDED_KEY2_START_WIDGET.grid(column=4, pady="0 5", row=8)
        _validatecmd = (self.EXTENDED_KEY2_START_WIDGET.register(
            self.validate_EXTENDED_KEY2_START), "%P", "%V")
        self.EXTENDED_KEY2_START_WIDGET.configure(validatecommand=_validatecmd)
        self.EXTENDED_KEY2_END_WIDGET = ttk.Entry(self.frame29)
        self.EXTENDED_KEY2_END = tk.StringVar()
        self.EXTENDED_KEY2_END_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.EXTENDED_KEY2_END,
            validate="focus",
            width=5)
        self.EXTENDED_KEY2_END_WIDGET.grid(column=5, pady="0 5", row=8)
        _validatecmd = (
            self.EXTENDED_KEY2_END_WIDGET.register(
                self.validate_EXTENDED_KEY2_END), "%P", "%V")
        self.EXTENDED_KEY2_END_WIDGET.configure(validatecommand=_validatecmd)
        self.EXTENDED_KEY3_FUNC_LABEL = ttk.Label(self.frame29)
        self.EXTENDED_KEY3_FUNC_LABEL.configure(
            style="Heading4.TLabel", text='Key 3')
        self.EXTENDED_KEY3_FUNC_LABEL.grid(
            column=1, pady="0 5", row=10, sticky="w")
        self.EXTENDED_KEY3_FUNC_WIDGET = ttk.Combobox(self.frame29)
        self.EXTENDED_KEY3_FUNC = tk.StringVar()
        self.EXTENDED_KEY3_FUNC_WIDGET.configure(
            textvariable=self.EXTENDED_KEY3_FUNC,
            values='NONE MODE BAND-UP BAND-DN TUNE-STEP VFO-A/B SPLIT TX SDR-MODE RIT',
            width=10)
        self.EXTENDED_KEY3_FUNC_WIDGET.grid(column=2, row=10)
        self.EXTENDED_KEY3_START_WIDGET = ttk.Entry(self.frame29)
        self.EXTENDED_KEY3_START = tk.StringVar()
        self.EXTENDED_KEY3_START_WIDGET.configure(
            justify="right",
            style="NoBorder.TEntry",
            textvariable=self.EXTENDED_KEY3_START,
            validate="focus",
            width=5)
        self.EXTENDED_KEY3_START_WIDGET.grid(column=4, pady="0 5", row=10)
        _validatecmd = (self.EXTENDED_KEY3_START_WIDGET.register(
            self.validate_EXTENDED_KEY3_START), "%P", "%V")
        self.EXTENDED_KEY3_START_WIDGET.configure(validatecommand=_validatecmd)
        self.EXTENDED_KEY3_END_WIDGET = ttk.Entry(self.frame29)
        self.EXTENDED_KEY3_END = tk.StringVar()
        self.EXTENDED_KEY3_END_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.EXTENDED_KEY3_END,
            validate="focus",
            width=5)
        self.EXTENDED_KEY3_END_WIDGET.grid(column=5, pady="0 5", row=10)
        _validatecmd = (
            self.EXTENDED_KEY3_END_WIDGET.register(
                self.validate_EXTENDED_KEY3_END), "%P", "%V")
        self.EXTENDED_KEY3_END_WIDGET.configure(validatecommand=_validatecmd)
        self.EXTENDED_KEY4_FUNC_LABEL = ttk.Label(self.frame29)
        self.EXTENDED_KEY4_FUNC_LABEL.configure(
            style="Heading4.TLabel", text='Key 4')
        self.EXTENDED_KEY4_FUNC_LABEL.grid(
            column=1, padx="0 5", pady="0 5", row=11, sticky="w")
        self.EXTENDED_KEY4_FUNC_WIDGET = ttk.Combobox(self.frame29)
        self.EXTENDED_KEY4_FUNC = tk.StringVar()
        self.EXTENDED_KEY4_FUNC_WIDGET.configure(
            textvariable=self.EXTENDED_KEY4_FUNC,
            values='NONE MODE BAND-UP BAND-DN TUNE-STEP VFO-A/B SPLIT TX SDR-MODE RIT',
            width=10)
        self.EXTENDED_KEY4_FUNC_WIDGET.grid(column=2, row=11)
        self.EXTENDED_KEY4_START_WIDGET = ttk.Entry(self.frame29)
        self.EXTENDED_KEY4_START = tk.StringVar()
        self.EXTENDED_KEY4_START_WIDGET.configure(
            justify="right",
            style="NoBorder.TEntry",
            textvariable=self.EXTENDED_KEY4_START,
            validate="focus",
            width=5)
        self.EXTENDED_KEY4_START_WIDGET.grid(column=4, pady="0 5", row=11)
        _validatecmd = (self.EXTENDED_KEY4_START_WIDGET.register(
            self.validate_EXTENDED_KEY4_START), "%P", "%V")
        self.EXTENDED_KEY4_START_WIDGET.configure(validatecommand=_validatecmd)
        self.EXTENDED_KEY4_END_WIDGET = ttk.Entry(self.frame29)
        self.EXTENDED_KEY4_END = tk.StringVar()
        self.EXTENDED_KEY4_END_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.EXTENDED_KEY4_END,
            validate="focus",
            width=5)
        self.EXTENDED_KEY4_END_WIDGET.grid(column=5, pady="0 5", row=11)
        _validatecmd = (
            self.EXTENDED_KEY4_END_WIDGET.register(
                self.validate_EXTENDED_KEY4_END), "%P", "%V")
        self.EXTENDED_KEY4_END_WIDGET.configure(validatecommand=_validatecmd)
        self.EXTENDED_KEY5_FUNC_LABEL = ttk.Label(self.frame29)
        self.EXTENDED_KEY5_FUNC_LABEL.configure(
            style="Heading4.TLabel", text='Key 5')
        self.EXTENDED_KEY5_FUNC_LABEL.grid(
            column=1, padx="0 5", pady="0 5", row=13, sticky="w")
        self.frame30 = ttk.Frame(self.frame29)
        self.frame30.configure(height=200, width=200)
        self.runADCScanner_WIDGET = ttk.Button(self.frame30)
        self.runADCScanner_WIDGET.configure(
            style="Button4.TButton", text='ADC Scanner')
        self.runADCScanner_WIDGET.grid(column=0, row=0)
        self.runADCScanner_WIDGET.configure(command=self.runADCScanner)
        self.frame30.grid(column=1, columnspan=5, pady=15, row=16, sticky="ew")
        self.EXTENDED_KEY6_FUNC_LABEL = ttk.Label(self.frame29)
        self.EXTENDED_KEY6_FUNC_LABEL.configure(
            style="Heading4.TLabel", text='Key 6')
        self.EXTENDED_KEY6_FUNC_LABEL.grid(
            column=1, padx="0 5", pady="0 5", row=14, sticky="w")
        self.EXTENDED_KEY5_FUNC_WIDGET = ttk.Combobox(self.frame29)
        self.EXTENDED_KEY5_FUNC = tk.StringVar()
        self.EXTENDED_KEY5_FUNC_WIDGET.configure(
            textvariable=self.EXTENDED_KEY5_FUNC,
            values='NONE MODE BAND-UP BAND-DN TUNE-STEP VFO-A/B SPLIT TX SDR-MODE RIT',
            width=10)
        self.EXTENDED_KEY5_FUNC_WIDGET.grid(column=2, row=13)
        self.EXTENDED_KEY5_START_WIDGET = ttk.Entry(self.frame29)
        self.EXTENDED_KEY5_START = tk.StringVar()
        self.EXTENDED_KEY5_START_WIDGET.configure(
            justify="right",
            style="NoBorder.TEntry",
            textvariable=self.EXTENDED_KEY5_START,
            validate="focus",
            width=5)
        self.EXTENDED_KEY5_START_WIDGET.grid(column=4, pady="0 5", row=13)
        _validatecmd = (self.EXTENDED_KEY5_START_WIDGET.register(
            self.validate_EXTENDED_KEY5_START), "%P", "%V")
        self.EXTENDED_KEY5_START_WIDGET.configure(validatecommand=_validatecmd)
        self.EXTENDED_KEY5_END_WIDGET = ttk.Entry(self.frame29)
        self.EXTENDED_KEY5_END = tk.StringVar()
        self.EXTENDED_KEY5_END_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.EXTENDED_KEY5_END,
            validate="focus",
            width=5)
        self.EXTENDED_KEY5_END_WIDGET.grid(column=5, pady="0 5", row=13)
        _validatecmd = (
            self.EXTENDED_KEY5_END_WIDGET.register(
                self.validate_EXTENDED_KEY5_END), "%P", "%V")
        self.EXTENDED_KEY5_END_WIDGET.configure(validatecommand=_validatecmd)
        self.EXTENDED_KEY6_FUNC_WIDGET = ttk.Combobox(self.frame29)
        self.EXTENDED_KEY6_FUNC = tk.StringVar()
        self.EXTENDED_KEY6_FUNC_WIDGET.configure(
            textvariable=self.EXTENDED_KEY6_FUNC,
            values='NONE MODE BAND-UP BAND-DN TUNE-STEP VFO-A/B SPLIT TX SDR-MODE RIT',
            width=10)
        self.EXTENDED_KEY6_FUNC_WIDGET.grid(column=2, row=14)
        self.EXTENDED_KEY6_START_WIDGET = ttk.Entry(self.frame29)
        self.EXTENDED_KEY6_START = tk.StringVar()
        self.EXTENDED_KEY6_START_WIDGET.configure(
            justify="right",
            style="NoBorder.TEntry",
            textvariable=self.EXTENDED_KEY6_START,
            validate="focus",
            width=5)
        self.EXTENDED_KEY6_START_WIDGET.grid(column=4, pady="0 5", row=14)
        _validatecmd = (self.EXTENDED_KEY6_START_WIDGET.register(
            self.validate_EXTENDED_KEY6_START), "%P", "%V")
        self.EXTENDED_KEY6_START_WIDGET.configure(validatecommand=_validatecmd)
        self.EXTENDED_KEY6_END_WIDGET = ttk.Entry(self.frame29)
        self.EXTENDED_KEY6_END = tk.StringVar()
        self.EXTENDED_KEY6_END_WIDGET.configure(
            justify="right",
            style="NoBorder.TEntry",
            textvariable=self.EXTENDED_KEY6_END,
            validate="focus",
            width=5)
        self.EXTENDED_KEY6_END_WIDGET.grid(column=5, pady="0 5", row=14)
        _validatecmd = (
            self.EXTENDED_KEY6_END_WIDGET.register(
                self.validate_EXTENDED_KEY6_END), "%P", "%V")
        self.EXTENDED_KEY6_END_WIDGET.configure(validatecommand=_validatecmd)
        self.frame29.pack(fill="x", padx="20 0", side="top")
        self.frame29.grid_anchor("nw")
        self.frame57 = ttk.Frame(self.Extensions_Frame)
        self.frame57.configure(height=200, width=200)
        self.separator7 = ttk.Separator(self.frame57)
        self.separator7.configure(orient="horizontal")
        self.separator7.pack(
            anchor="center",
            expand="true",
            fill="x",
            side="top")
        self.frame57.pack(anchor="w", expand="true", fill="x", side="top")
        self.frame8 = ttk.Frame(self.Extensions_Frame)
        self.frame56 = ttk.Frame(self.frame8)
        self.frame56.configure(height=200, width=200)
        self.label10 = ttk.Label(self.frame56)
        self.label10.configure(
            justify="left",
            style="Heading3.TLabel",
            text='Low Pass Filters')
        self.label10.grid(column=0, row=0, sticky="w")
        self.message4 = tk.Message(self.frame56)
        self.message4.configure(
            borderwidth=2,
            font="TkTextFont",
            justify="left",
            pady=5,
            relief="ridge",
            takefocus=False,
            text="Provides customization of uBITX's LPF as well as external LPF attached to PA.\n\nNOTE: The EXTENDED option Does NOT work on configurations with LCD's using parallel data connections. \n\nFor details, see: \nhttp://www.hamskey.com/2018/09/ubitx-setting-for-custmizedhacked-or.html",
            width=500)
        self.message4.grid(column=1, padx=10, row=0, sticky="w")
        self.frame56.grid(column=0, pady="5 0", row=0)
        self.frame18 = ttk.Frame(self.frame8)
        self.frame18.configure(height=200, width=200)
        self.CUST_LPF_ENABLED_Label = ttk.Label(self.frame18)
        self.CUST_LPF_ENABLED_Label.configure(
            style="Heading4.TLabel", text='Filter control')
        self.CUST_LPF_ENABLED_Label.grid(column=0, padx=10, row=0)
        self.CUST_LPF_ENABLED = tk.StringVar(value='OFF')
        __values = ['OFF', 'STANDARD', 'EXTENDED']
        self.CUST_LPF_ENABLED_WIDGET = ttk.OptionMenu(
            self.frame18,
            self.CUST_LPF_ENABLED,
            "OFF",
            *__values,
            command=self.CUST_LPF_SELECTION_CB)
        self.CUST_LPF_ENABLED_WIDGET.grid(column=1, row=0)
        self.frame18.grid(column=0, pady=10, row=2, sticky="w")
        self.CUST_LPF_ENABLED_Frame = ttk.Frame(self.frame8)
        self.CUST_LPF_ENABLED_Frame.configure(height=200, width=200)
        self.CUSTOM_BANDPASS_FILTER_Frame = ttk.Frame(
            self.CUST_LPF_ENABLED_Frame)
        self.CUSTOM_BANDPASS_FILTER_Frame.configure(height=200, width=200)
        self.CUSTOM_BANDPASS_STANDARD_Frame = ttk.Frame(
            self.CUSTOM_BANDPASS_FILTER_Frame)
        self.CUSTOM_BANDPASS_STANDARD_Frame.configure(height=200, width=200)
        self.CUStOM_BANDPASS_STANDARD_LABELS_Frame = ttk.Frame(
            self.CUSTOM_BANDPASS_STANDARD_Frame)
        self.CUStOM_BANDPASS_STANDARD_LABELS_Frame.configure(
            height=200, width=200)
        self.label172 = ttk.Label(self.CUStOM_BANDPASS_STANDARD_LABELS_Frame)
        self.label172.configure(style="Heading4.TLabel", text='High Freq')
        self.label172.grid(column=0, row=0, sticky="w")
        self.label174 = ttk.Label(self.CUStOM_BANDPASS_STANDARD_LABELS_Frame)
        self.label174.configure(style="Heading4.TLabel", text='    ')
        self.label174.grid(column=1, row=0)
        self.label173 = ttk.Label(self.CUStOM_BANDPASS_STANDARD_LABELS_Frame)
        self.label173.configure(style="Heading4.TLabel", text='Low Freq')
        self.label173.grid(column=2, row=0, sticky="w")
        self.label175 = ttk.Label(self.CUStOM_BANDPASS_STANDARD_LABELS_Frame)
        self.label175.configure(style="Heading4.TLabel", text='    ')
        self.label175.grid(column=3, row=0)
        self.label176 = ttk.Label(self.CUStOM_BANDPASS_STANDARD_LABELS_Frame)
        self.label176.configure(
            style="Heading4.TLabel",
            text='TXA(D5)',
            width=7)
        self.label176.grid(column=4, row=0, sticky="w")
        self.label177 = ttk.Label(self.CUStOM_BANDPASS_STANDARD_LABELS_Frame)
        self.label177.configure(
            style="Heading4.TLabel",
            text='TXB(D4)',
            width=7)
        self.label177.grid(column=5, padx="5 0", row=0, sticky="w")
        self.label178 = ttk.Label(self.CUStOM_BANDPASS_STANDARD_LABELS_Frame)
        self.label178.configure(
            style="Heading4.TLabel",
            text='TXC(D3)',
            width=7)
        self.label178.grid(column=6, padx="5 0", row=0, sticky="w")
        self.CUStOM_BANDPASS_STANDARD_LABELS_Frame.pack(anchor="w", side="top")
        self.CUSTOM_BANDPASS_STANDARD_DATA_Frame = ttk.Frame(
            self.CUSTOM_BANDPASS_STANDARD_Frame)
        self.CUSTOM_BANDPASS_STANDARD_DATA_Frame.configure(
            height=200, width=200)
        self.entry52 = ttk.Entry(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER1_BEGFREQ = tk.StringVar(value='200')
        self.entry52.configure(
            justify="right",
            state="readonly",
            style="Normal.TEntry",
            textvariable=self.CUST_LPF_FILTER1_BEGFREQ,
            width=5)
        _text_ = '200'
        self.entry52["state"] = "normal"
        self.entry52.delete("0", "end")
        self.entry52.insert("0", _text_)
        self.entry52["state"] = "readonly"
        self.entry52.grid(column=0, row=0)
        self.label12 = ttk.Label(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.label12.configure(style="Normal.TLabel", text='MHz -  ')
        self.label12.grid(column=1, row=0)
        self.CUST_LPF_FILTER1_ENDFREQ_WIDGET = ttk.Entry(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER1_ENDFREQ = tk.StringVar()
        self.CUST_LPF_FILTER1_ENDFREQ_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CUST_LPF_FILTER1_ENDFREQ,
            validate="focusout",
            width=5)
        self.CUST_LPF_FILTER1_ENDFREQ_WIDGET.grid(column=2, row=0)
        _validatecmd = (self.CUST_LPF_FILTER1_ENDFREQ_WIDGET.register(
            self.validate_CUST_LPF_FILTER1_ENDFREQ), "%P", "%V")
        self.CUST_LPF_FILTER1_ENDFREQ_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label13 = ttk.Label(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.label13.configure(style="Normal.TLabel", text=' MHz')
        self.label13.grid(column=3, row=0)
        self.checkbutton4 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER1_CONTROL_TX_LPF_A = tk.StringVar()
        self.checkbutton4.configure(
            onvalue="TX_LPF_A",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER1_CONTROL_TX_LPF_A,
            width=0)
        self.checkbutton4.grid(column=4, padx="35 0", row=0, sticky="w")
        self.checkbutton4.configure(command=self.CUST_LPF_FILTER1_CONTROL_CB)
        self.checkbutton5 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER1_CONTROL_TX_LPF_B = tk.StringVar()
        self.checkbutton5.configure(
            onvalue="TX_LPF_B",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER1_CONTROL_TX_LPF_B,
            width=0)
        self.checkbutton5.grid(column=5, padx="35 0", row=0, sticky="w")
        self.checkbutton5.configure(command=self.CUST_LPF_FILTER1_CONTROL_CB)
        self.checkbutton6 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER1_CONTROL_TX_LPF_C = tk.StringVar()
        self.checkbutton6.configure(
            onvalue="TX_LPF_C",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER1_CONTROL_TX_LPF_C,
            width=0)
        self.checkbutton6.grid(column=6, row=0, sticky="w")
        self.checkbutton6.configure(command=self.CUST_LPF_FILTER1_CONTROL_CB)
        self.entry10 = ttk.Entry(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER2_BEGFREQ = tk.StringVar()
        self.entry10.configure(
            justify="right",
            state="readonly",
            style="Normal.TEntry",
            textvariable=self.CUST_LPF_FILTER2_BEGFREQ,
            width=5)
        self.entry10.grid(column=0, row=1)
        self.label139 = ttk.Label(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.label139.configure(style="Normal.TLabel", text='MHz -  ')
        self.label139.grid(column=1, row=1)
        self.CUST_LPF_FILTER2_ENDFREQ_WIDGET = ttk.Entry(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER2_ENDFREQ = tk.StringVar()
        self.CUST_LPF_FILTER2_ENDFREQ_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CUST_LPF_FILTER2_ENDFREQ,
            validate="focusout",
            width=5)
        self.CUST_LPF_FILTER2_ENDFREQ_WIDGET.grid(column=2, row=1)
        _validatecmd = (self.CUST_LPF_FILTER2_ENDFREQ_WIDGET.register(
            self.validate_CUST_LPF_FILTER2_ENDFREQ), "%P", "%V")
        self.CUST_LPF_FILTER2_ENDFREQ_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label140 = ttk.Label(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.label140.configure(style="Normal.TLabel", text=' MHz')
        self.label140.grid(column=3, row=1)
        self.checkbutton23 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER2_CONTROL_TX_LPF_A = tk.StringVar()
        self.checkbutton23.configure(
            onvalue="TX_LPF_A",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER2_CONTROL_TX_LPF_A,
            width=0)
        self.checkbutton23.grid(column=4, padx="35 0", row=1, sticky="w")
        self.checkbutton23.configure(command=self.CUST_LPF_FILTER2_CONTROL_CB)
        self.checkbutton24 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER2_CONTROL_TX_LPF_B = tk.StringVar()
        self.checkbutton24.configure(
            onvalue="TX_LPF_B",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER2_CONTROL_TX_LPF_B,
            width=5)
        self.checkbutton24.grid(column=5, padx="35 0", row=1, sticky="w")
        self.checkbutton24.configure(command=self.CUST_LPF_FILTER2_CONTROL_CB)
        self.checkbutton25 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER2_CONTROL_TX_LPF_C = tk.StringVar()
        self.checkbutton25.configure(
            onvalue="TX_LPF_C",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER2_CONTROL_TX_LPF_C,
            width=5)
        self.checkbutton25.grid(column=6, row=1, sticky="w")
        self.checkbutton25.configure(command=self.CUST_LPF_FILTER2_CONTROL_CB)
        self.entry12 = ttk.Entry(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER3_BEGFREQ = tk.StringVar()
        self.entry12.configure(
            justify="right",
            state="readonly",
            style="Normal.TEntry",
            textvariable=self.CUST_LPF_FILTER3_BEGFREQ,
            width=5)
        self.entry12.grid(column=0, row=2)
        self.label141 = ttk.Label(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.label141.configure(style="Normal.TLabel", text='MHz -  ')
        self.label141.grid(column=1, row=2)
        self.CUST_LPF_FILTER3_ENDFREQ_WIDGET = ttk.Entry(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER3_ENDFREQ = tk.StringVar()
        self.CUST_LPF_FILTER3_ENDFREQ_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CUST_LPF_FILTER3_ENDFREQ,
            validate="focusout",
            width=5)
        self.CUST_LPF_FILTER3_ENDFREQ_WIDGET.grid(column=2, row=2)
        _validatecmd = (self.CUST_LPF_FILTER3_ENDFREQ_WIDGET.register(
            self.validate_CUST_LPF_FILTER3_ENDFREQ), "%P", "%V")
        self.CUST_LPF_FILTER3_ENDFREQ_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label142 = ttk.Label(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.label142.configure(style="Normal.TLabel", text=' MHz')
        self.label142.grid(column=3, row=2)
        self.checkbutton26 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER3_CONTROL_TX_LPF_A = tk.StringVar()
        self.checkbutton26.configure(
            onvalue="TX_LPF_A",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER3_CONTROL_TX_LPF_A,
            width=0)
        self.checkbutton26.grid(column=4, padx="35 0", row=2, sticky="w")
        self.checkbutton26.configure(command=self.CUST_LPF_FILTER3_CONTROL_CB)
        self.checkbutton27 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER3_CONTROL_TX_LPF_B = tk.StringVar()
        self.checkbutton27.configure(
            onvalue="TX_LPF_B",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER3_CONTROL_TX_LPF_B,
            width=5)
        self.checkbutton27.grid(column=5, padx="35 0", row=2, sticky="w")
        self.checkbutton27.configure(command=self.CUST_LPF_FILTER3_CONTROL_CB)
        self.checkbutton28 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER3_CONTROL_TX_LPF_C = tk.StringVar()
        self.checkbutton28.configure(
            onvalue="TX_LPF_C",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER3_CONTROL_TX_LPF_C,
            width=5)
        self.checkbutton28.grid(column=6, row=2, sticky="w")
        self.checkbutton28.configure(command=self.CUST_LPF_FILTER3_CONTROL_CB)
        self.entry14 = ttk.Entry(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER4_BEGFREQ = tk.StringVar()
        self.entry14.configure(
            justify="right",
            state="readonly",
            style="Normal.TEntry",
            textvariable=self.CUST_LPF_FILTER4_BEGFREQ,
            width=5)
        self.entry14.grid(column=0, row=3)
        self.label143 = ttk.Label(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.label143.configure(style="Normal.TLabel", text='MHz -  ')
        self.label143.grid(column=1, row=3)
        self.CUST_LPF_FILTER4_ENDFREQ_WIDGET = ttk.Entry(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER4_ENDFREQ = tk.StringVar()
        self.CUST_LPF_FILTER4_ENDFREQ_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CUST_LPF_FILTER4_ENDFREQ,
            validate="focusout",
            width=5)
        self.CUST_LPF_FILTER4_ENDFREQ_WIDGET.grid(column=2, row=3)
        _validatecmd = (self.CUST_LPF_FILTER4_ENDFREQ_WIDGET.register(
            self.validate_CUST_LPF_FILTER4_ENDFREQ), "%P", "%V")
        self.CUST_LPF_FILTER4_ENDFREQ_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label147 = ttk.Label(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.label147.configure(style="Normal.TLabel", text=' MHz')
        self.label147.grid(column=3, row=3)
        self.checkbutton29 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER4_CONTROL_TX_LPF_A = tk.StringVar()
        self.checkbutton29.configure(
            onvalue="TX_LPF_A",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER4_CONTROL_TX_LPF_A,
            width=0)
        self.checkbutton29.grid(column=4, padx="35 0", row=3, sticky="w")
        self.checkbutton29.configure(command=self.CUST_LPF_FILTER4_CONTROL_CB)
        self.checkbutton30 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER4_CONTROL_TX_LPF_B = tk.StringVar()
        self.checkbutton30.configure(
            onvalue="TX_LPF_B",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER4_CONTROL_TX_LPF_B,
            width=5)
        self.checkbutton30.grid(column=5, padx="35 0", row=3, sticky="w")
        self.checkbutton30.configure(command=self.CUST_LPF_FILTER4_CONTROL_CB)
        self.checkbutton31 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER4_CONTROL_TX_LPF_C = tk.StringVar()
        self.checkbutton31.configure(
            onvalue="TX_LPF_C",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER4_CONTROL_TX_LPF_C,
            width=5)
        self.checkbutton31.grid(column=6, row=3, sticky="w")
        self.checkbutton31.configure(command=self.CUST_LPF_FILTER4_CONTROL_CB)
        self.entry16 = ttk.Entry(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER5_BEGFREQ = tk.StringVar()
        self.entry16.configure(
            justify="right",
            state="readonly",
            style="Normal.TEntry",
            textvariable=self.CUST_LPF_FILTER5_BEGFREQ,
            width=5)
        self.entry16.grid(column=0, row=4)
        self.label148 = ttk.Label(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.label148.configure(style="Normal.TLabel", text='MHz -  ')
        self.label148.grid(column=1, row=4)
        self.CUST_LPF_FILTER5_ENDFREQ_WIDGET = ttk.Entry(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER5_ENDFREQ = tk.StringVar()
        self.CUST_LPF_FILTER5_ENDFREQ_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CUST_LPF_FILTER5_ENDFREQ,
            validate="focusout",
            width=5)
        self.CUST_LPF_FILTER5_ENDFREQ_WIDGET.grid(column=2, row=4)
        _validatecmd = (self.CUST_LPF_FILTER5_ENDFREQ_WIDGET.register(
            self.validate_CUST_LPF_FILTER5_ENDFREQ), "%P", "%V")
        self.CUST_LPF_FILTER5_ENDFREQ_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label149 = ttk.Label(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.label149.configure(style="Normal.TLabel", text=' MHz')
        self.label149.grid(column=3, row=4)
        self.checkbutton32 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER5_CONTROL_TX_LPF_A = tk.StringVar()
        self.checkbutton32.configure(
            onvalue="TX_LPF_A",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER5_CONTROL_TX_LPF_A,
            width=0)
        self.checkbutton32.grid(column=4, padx="35 0", row=4, sticky="w")
        self.checkbutton32.configure(command=self.CUST_LPF_FILTER5_CONTROL_CB)
        self.checkbutton33 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER5_CONTROL_TX_LPF_B = tk.StringVar()
        self.checkbutton33.configure(
            onvalue="TX_LPF_B",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER5_CONTROL_TX_LPF_B,
            width=5)
        self.checkbutton33.grid(column=5, padx="35 0", row=4, sticky="w")
        self.checkbutton33.configure(command=self.CUST_LPF_FILTER5_CONTROL_CB)
        self.checkbutton34 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER5_CONTROL_TX_LPF_C = tk.StringVar()
        self.checkbutton34.configure(
            onvalue="TX_LPF_C",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER5_CONTROL_TX_LPF_C,
            width=5)
        self.checkbutton34.grid(column=6, row=4, sticky="w")
        self.checkbutton34.configure(command=self.CUST_LPF_FILTER5_CONTROL_CB)
        self.entry18 = ttk.Entry(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER6_BEGFREQ = tk.StringVar()
        self.entry18.configure(
            justify="right",
            state="readonly",
            style="Normal.TEntry",
            textvariable=self.CUST_LPF_FILTER6_BEGFREQ,
            width=5)
        self.entry18.grid(column=0, row=5)
        self.label150 = ttk.Label(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.label150.configure(style="Normal.TLabel", text='MHz -  ')
        self.label150.grid(column=1, row=5)
        self.CUST_LPF_FILTER6_ENDFREQ_WIDGET = ttk.Entry(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER6_ENDFREQ = tk.StringVar()
        self.CUST_LPF_FILTER6_ENDFREQ_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CUST_LPF_FILTER6_ENDFREQ,
            validate="focusout",
            width=5)
        self.CUST_LPF_FILTER6_ENDFREQ_WIDGET.grid(column=2, row=5)
        _validatecmd = (self.CUST_LPF_FILTER6_ENDFREQ_WIDGET.register(
            self.validate_CUST_LPF_FILTER6_ENDFREQ), "%P", "%V")
        self.CUST_LPF_FILTER6_ENDFREQ_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label151 = ttk.Label(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.label151.configure(style="Normal.TLabel", text=' MHz')
        self.label151.grid(column=3, row=5)
        self.checkbutton35 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER6_CONTROL_TX_LPF_A = tk.StringVar()
        self.checkbutton35.configure(
            onvalue="TX_LPF_A",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER6_CONTROL_TX_LPF_A,
            width=0)
        self.checkbutton35.grid(column=4, padx="35 0", row=5, sticky="w")
        self.checkbutton35.configure(command=self.CUST_LPF_FILTER6_CONTROL_CB)
        self.checkbutton36 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER6_CONTROL_TX_LPF_B = tk.StringVar()
        self.checkbutton36.configure(
            onvalue="TX_LPF_B",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER6_CONTROL_TX_LPF_B,
            width=5)
        self.checkbutton36.grid(column=5, padx="35 0", row=5, sticky="w")
        self.checkbutton36.configure(command=self.CUST_LPF_FILTER6_CONTROL_CB)
        self.checkbutton37 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER6_CONTROL_TX_LPF_C = tk.StringVar()
        self.checkbutton37.configure(
            onvalue="TX_LPF_C",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER6_CONTROL_TX_LPF_C,
            width=5)
        self.checkbutton37.grid(column=6, row=5, sticky="w")
        self.checkbutton37.configure(command=self.CUST_LPF_FILTER6_CONTROL_CB)
        self.entry20 = ttk.Entry(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER7_BEGFREQ = tk.StringVar()
        self.entry20.configure(
            justify="right",
            state="readonly",
            style="Normal.TEntry",
            textvariable=self.CUST_LPF_FILTER7_BEGFREQ,
            width=5)
        self.entry20.grid(column=0, row=6)
        self.label152 = ttk.Label(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.label152.configure(style="Normal.TLabel", text='MHz -  ')
        self.label152.grid(column=1, row=6)
        self.CUST_LPF_FILTER7_ENDFREQ_WIDGET = ttk.Entry(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER7_ENDFREQ = tk.StringVar()
        self.CUST_LPF_FILTER7_ENDFREQ_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CUST_LPF_FILTER7_ENDFREQ,
            validate="focusout",
            width=5)
        self.CUST_LPF_FILTER7_ENDFREQ_WIDGET.grid(column=2, row=6)
        _validatecmd = (self.CUST_LPF_FILTER7_ENDFREQ_WIDGET.register(
            self.validate_CUST_LPF_FILTER7_ENDFREQ), "%P", "%V")
        self.CUST_LPF_FILTER7_ENDFREQ_WIDGET.configure(
            validatecommand=_validatecmd)
        self.label153 = ttk.Label(self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.label153.configure(style="Normal.TLabel", text=' MHz')
        self.label153.grid(column=3, row=6)
        self.checkbutton38 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER7_CONTROL_TX_LPF_A = tk.StringVar()
        self.checkbutton38.configure(
            onvalue="TX_LPF_A",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER7_CONTROL_TX_LPF_A,
            width=0)
        self.checkbutton38.grid(column=4, padx="35 0", row=6, sticky="w")
        self.checkbutton38.configure(command=self.CUST_LPF_FILTER7_CONTROL_CB)
        self.checkbutton39 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER7_CONTROL_TX_LPF_B = tk.StringVar()
        self.checkbutton39.configure(
            onvalue="TX_LPF_B",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER7_CONTROL_TX_LPF_B,
            width=5)
        self.checkbutton39.grid(column=5, padx="35 0", row=6, sticky="w")
        self.checkbutton39.configure(command=self.CUST_LPF_FILTER7_CONTROL_CB)
        self.checkbutton40 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_STANDARD_DATA_Frame)
        self.CUST_LPF_FILTER7_CONTROL_TX_LPF_C = tk.StringVar()
        self.checkbutton40.configure(
            onvalue="TX_LPF_C",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER7_CONTROL_TX_LPF_C,
            width=5)
        self.checkbutton40.grid(column=6, row=6, sticky="w")
        self.checkbutton40.configure(command=self.CUST_LPF_FILTER7_CONTROL_CB)
        self.CUSTOM_BANDPASS_STANDARD_DATA_Frame.pack(anchor="w", side="top")
        self.CUSTOM_BANDPASS_STANDARD_Frame.pack(anchor="n", side="left")
        self.CUSTOM_BANDPASS_EXTENDED_Frame = ttk.Frame(
            self.CUSTOM_BANDPASS_FILTER_Frame)
        self.CUSTOM_BANDPASS_EXTENDED_Frame.configure(height=200, width=200)
        self.CUSTOM_BANDPASS_EXTENDED_LABEL_Frame = ttk.Frame(
            self.CUSTOM_BANDPASS_EXTENDED_Frame)
        self.CUSTOM_BANDPASS_EXTENDED_LABEL_Frame.configure(
            height=200, width=200)
        self.label179 = ttk.Label(self.CUSTOM_BANDPASS_EXTENDED_LABEL_Frame)
        self.label179.configure(style="Heading4.TLabel", text='D10', width=7)
        self.label179.grid(column=0, row=0, sticky="w")
        self.label180 = ttk.Label(self.CUSTOM_BANDPASS_EXTENDED_LABEL_Frame)
        self.label180.configure(style="Heading4.TLabel", text='D11', width=7)
        self.label180.grid(column=1, padx="5 0", row=0, sticky="w")
        self.label181 = ttk.Label(self.CUSTOM_BANDPASS_EXTENDED_LABEL_Frame)
        self.label181.configure(style="Heading4.TLabel", text='D12', width=7)
        self.label181.grid(column=2, row=0, sticky="w")
        self.label182 = ttk.Label(self.CUSTOM_BANDPASS_EXTENDED_LABEL_Frame)
        self.label182.configure(style="Heading4.TLabel", text='D13', width=7)
        self.label182.grid(column=3, row=0, sticky="w")
        self.CUSTOM_BANDPASS_EXTENDED_LABEL_Frame.pack(anchor="w", side="top")
        self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame = ttk.Frame(
            self.CUSTOM_BANDPASS_EXTENDED_Frame)
        self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame.configure(
            height=200, width=200)
        self.checkbutton7 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER1_CONTROL_D10 = tk.StringVar()
        self.checkbutton7.configure(
            onvalue="D10",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER1_CONTROL_D10,
            width=0)
        self.checkbutton7.grid(column=0, padx="3 0", row=0, sticky="w")
        self.checkbutton7.configure(command=self.CUST_LPF_FILTER1_CONTROL_CB)
        self.checkbutton8 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER1_CONTROL_D11 = tk.StringVar()
        self.checkbutton8.configure(
            onvalue="D11",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER1_CONTROL_D11,
            width=0)
        self.checkbutton8.grid(column=1, padx="35 0", row=0, sticky="w")
        self.checkbutton8.configure(command=self.CUST_LPF_FILTER1_CONTROL_CB)
        self.checkbutton9 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER1_CONTROL_D12 = tk.StringVar()
        self.checkbutton9.configure(
            onvalue="D12",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER1_CONTROL_D12,
            width=0)
        self.checkbutton9.grid(column=2, padx="30 0", row=0, sticky="w")
        self.checkbutton9.configure(command=self.CUST_LPF_FILTER1_CONTROL_CB)
        self.checkbutton10 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER1_CONTROL_D13 = tk.StringVar()
        self.checkbutton10.configure(
            onvalue="D13",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER1_CONTROL_D13,
            width=0)
        self.checkbutton10.grid(column=3, padx="28 0", row=0, sticky="w")
        self.checkbutton10.configure(command=self.CUST_LPF_FILTER1_CONTROL_CB)
        self.checkbutton41 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER2_CONTROL_D10 = tk.StringVar()
        self.checkbutton41.configure(
            onvalue="D10",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER2_CONTROL_D10,
            width=0)
        self.checkbutton41.grid(column=0, padx="3 0", row=1, sticky="w")
        self.checkbutton41.configure(command=self.CUST_LPF_FILTER2_CONTROL_CB)
        self.checkbutton42 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER2_CONTROL_D11 = tk.StringVar()
        self.checkbutton42.configure(
            onvalue="D11",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER2_CONTROL_D11,
            width=0)
        self.checkbutton42.grid(column=1, padx="35 0", row=1, sticky="w")
        self.checkbutton42.configure(command=self.CUST_LPF_FILTER2_CONTROL_CB)
        self.checkbutton43 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER2_CONTROL_D12 = tk.StringVar()
        self.checkbutton43.configure(
            onvalue="D12",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER2_CONTROL_D12,
            width=0)
        self.checkbutton43.grid(column=2, padx="30 0", row=1, sticky="w")
        self.checkbutton43.configure(command=self.CUST_LPF_FILTER2_CONTROL_CB)
        self.checkbutton44 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER2_CONTROL_D13 = tk.StringVar()
        self.checkbutton44.configure(
            onvalue="D13",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER2_CONTROL_D13,
            width=0)
        self.checkbutton44.grid(column=3, padx="28 0", row=1, sticky="w")
        self.checkbutton44.configure(command=self.CUST_LPF_FILTER2_CONTROL_CB)
        self.checkbutton45 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER3_CONTROL_D10 = tk.StringVar()
        self.checkbutton45.configure(
            onvalue="D10",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER3_CONTROL_D10,
            width=0)
        self.checkbutton45.grid(column=0, padx="3 0", row=2, sticky="w")
        self.checkbutton45.configure(command=self.CUST_LPF_FILTER3_CONTROL_CB)
        self.checkbutton46 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER3_CONTROL_D11 = tk.StringVar()
        self.checkbutton46.configure(
            onvalue="D11",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER3_CONTROL_D11,
            width=0)
        self.checkbutton46.grid(column=1, padx="35 0", row=2, sticky="w")
        self.checkbutton46.configure(command=self.CUST_LPF_FILTER3_CONTROL_CB)
        self.checkbutton47 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER3_CONTROL_D12 = tk.StringVar()
        self.checkbutton47.configure(
            onvalue="D12",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER3_CONTROL_D12,
            width=0)
        self.checkbutton47.grid(column=2, padx="30 0", row=2, sticky="w")
        self.checkbutton47.configure(command=self.CUST_LPF_FILTER3_CONTROL_CB)
        self.checkbutton48 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER3_CONTROL_D13 = tk.StringVar()
        self.checkbutton48.configure(
            onvalue="D13",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER3_CONTROL_D13,
            width=0)
        self.checkbutton48.grid(column=3, padx="28 0", row=2, sticky="w")
        self.checkbutton48.configure(command=self.CUST_LPF_FILTER3_CONTROL_CB)
        self.checkbutton49 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER4_CONTROL_D10 = tk.StringVar()
        self.checkbutton49.configure(
            onvalue="D10",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER4_CONTROL_D10,
            width=0)
        self.checkbutton49.grid(column=0, padx="3 0", row=3, sticky="w")
        self.checkbutton49.configure(command=self.CUST_LPF_FILTER4_CONTROL_CB)
        self.checkbutton50 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER4_CONTROL_D11 = tk.StringVar()
        self.checkbutton50.configure(
            onvalue="D11",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER4_CONTROL_D11,
            width=0)
        self.checkbutton50.grid(column=1, padx="35 0", row=3, sticky="w")
        self.checkbutton50.configure(command=self.CUST_LPF_FILTER4_CONTROL_CB)
        self.checkbutton51 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER4_CONTROL_D12 = tk.StringVar()
        self.checkbutton51.configure(
            onvalue="D12",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER4_CONTROL_D12,
            width=0)
        self.checkbutton51.grid(column=2, padx="30 0", row=3, sticky="w")
        self.checkbutton51.configure(command=self.CUST_LPF_FILTER4_CONTROL_CB)
        self.checkbutton52 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER4_CONTROL_D13 = tk.StringVar()
        self.checkbutton52.configure(
            onvalue="D13",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER4_CONTROL_D13,
            width=0)
        self.checkbutton52.grid(column=3, padx="28 0", row=3, sticky="w")
        self.checkbutton52.configure(command=self.CUST_LPF_FILTER4_CONTROL_CB)
        self.checkbutton53 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER5_CONTROL_D10 = tk.StringVar()
        self.checkbutton53.configure(
            onvalue="D10",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER5_CONTROL_D10,
            width=0)
        self.checkbutton53.grid(column=0, padx="3 0", row=4, sticky="w")
        self.checkbutton53.configure(command=self.CUST_LPF_FILTER5_CONTROL_CB)
        self.checkbutton54 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER5_CONTROL_D11 = tk.StringVar()
        self.checkbutton54.configure(
            onvalue="D11",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER5_CONTROL_D11,
            width=0)
        self.checkbutton54.grid(column=1, padx="35 0", row=4, sticky="w")
        self.checkbutton54.configure(command=self.CUST_LPF_FILTER5_CONTROL_CB)
        self.checkbutton55 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER5_CONTROL_D12 = tk.StringVar()
        self.checkbutton55.configure(
            onvalue="D12",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER5_CONTROL_D12,
            width=0)
        self.checkbutton55.grid(column=2, padx="30 0", row=4, sticky="w")
        self.checkbutton55.configure(command=self.CUST_LPF_FILTER5_CONTROL_CB)
        self.checkbutton56 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER5_CONTROL_D13 = tk.StringVar()
        self.checkbutton56.configure(
            onvalue="D13",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER5_CONTROL_D13,
            width=0)
        self.checkbutton56.grid(column=3, padx="28 0", row=4, sticky="w")
        self.checkbutton56.configure(command=self.CUST_LPF_FILTER5_CONTROL_CB)
        self.checkbutton57 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER6_CONTROL_D10 = tk.StringVar()
        self.checkbutton57.configure(
            onvalue="D10",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER6_CONTROL_D10,
            width=0)
        self.checkbutton57.grid(column=0, padx="3 0", row=5, sticky="w")
        self.checkbutton57.configure(command=self.CUST_LPF_FILTER6_CONTROL_CB)
        self.checkbutton58 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER6_CONTROL_D11 = tk.StringVar()
        self.checkbutton58.configure(
            onvalue="D11",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER6_CONTROL_D11,
            width=0)
        self.checkbutton58.grid(column=1, padx="35 0", row=5, sticky="w")
        self.checkbutton58.configure(command=self.CUST_LPF_FILTER6_CONTROL_CB)
        self.checkbutton59 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER6_CONTROL_D12 = tk.StringVar()
        self.checkbutton59.configure(
            onvalue="D12",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER6_CONTROL_D12,
            width=0)
        self.checkbutton59.grid(column=2, padx="30 0", row=5, sticky="w")
        self.checkbutton59.configure(command=self.CUST_LPF_FILTER6_CONTROL_CB)
        self.checkbutton60 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER6_CONTROL_D13 = tk.StringVar()
        self.checkbutton60.configure(
            onvalue="D13",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER6_CONTROL_D13,
            width=0)
        self.checkbutton60.grid(column=3, padx="28 0", row=5, sticky="w")
        self.checkbutton60.configure(command=self.CUST_LPF_FILTER6_CONTROL_CB)
        self.checkbutton61 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER7_CONTROL_D10 = tk.StringVar()
        self.checkbutton61.configure(
            onvalue="D10",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER7_CONTROL_D10,
            width=0)
        self.checkbutton61.grid(column=0, padx="3 0", row=6, sticky="w")
        self.checkbutton61.configure(command=self.CUST_LPF_FILTER7_CONTROL_CB)
        self.checkbutton62 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER7_CONTROL_D11 = tk.StringVar()
        self.checkbutton62.configure(
            onvalue="D11",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER7_CONTROL_D11,
            width=0)
        self.checkbutton62.grid(column=1, padx="35 0", row=6, sticky="w")
        self.checkbutton62.configure(command=self.CUST_LPF_FILTER7_CONTROL_CB)
        self.checkbutton63 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER7_CONTROL_D12 = tk.StringVar()
        self.checkbutton63.configure(
            onvalue="D12",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER7_CONTROL_D12,
            width=0)
        self.checkbutton63.grid(column=2, padx="30 0", row=6, sticky="w")
        self.checkbutton63.configure(command=self.CUST_LPF_FILTER7_CONTROL_CB)
        self.checkbutton64 = ttk.Checkbutton(
            self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame)
        self.CUST_LPF_FILTER7_CONTROL_D13 = tk.StringVar()
        self.checkbutton64.configure(
            onvalue="D13",
            style="CheckboxNormal.TCheckbutton",
            variable=self.CUST_LPF_FILTER7_CONTROL_D13,
            width=0)
        self.checkbutton64.grid(column=3, padx="28 0", row=6, sticky="w")
        self.checkbutton64.configure(command=self.CUST_LPF_FILTER7_CONTROL_CB)
        self.CUSTOM_BANDPASS_EXTENDED_DATA_Frame.pack(
            anchor="w", padx=5, side="top")
        self.CUSTOM_BANDPASS_EXTENDED_Frame.pack(anchor="w", side="left")
        self.CUSTOM_BANDPASS_FILTER_Frame.pack(
            anchor="w", pady="10 0", side="top")
        self.CUST_LPF_ENABLED_Frame.grid(column=0, pady="5 0", row=5)
        self.hidden_data_items = ttk.Frame(self.frame8)
        self.hidden_data_items.configure(height=0, width=0)
        self.CUST_LPF_FILTER1_CONTROL_WIDGET = ttk.Label(
            self.hidden_data_items)
        self.CUST_LPF_FILTER1_CONTROL = tk.StringVar()
        self.CUST_LPF_FILTER1_CONTROL_WIDGET.configure(
            textvariable=self.CUST_LPF_FILTER1_CONTROL)
        self.CUST_LPF_FILTER1_CONTROL_WIDGET.pack(side="left")
        self.CUST_LPF_FILTER2_CONTROL_WIDGET = ttk.Label(
            self.hidden_data_items)
        self.CUST_LPF_FILTER2_CONTROL = tk.StringVar()
        self.CUST_LPF_FILTER2_CONTROL_WIDGET.configure(
            textvariable=self.CUST_LPF_FILTER2_CONTROL)
        self.CUST_LPF_FILTER2_CONTROL_WIDGET.pack(side="left")
        self.CUST_LPF_FILTER3_CONTROL_WIDGET = ttk.Label(
            self.hidden_data_items)
        self.CUST_LPF_FILTER3_CONTROL = tk.StringVar()
        self.CUST_LPF_FILTER3_CONTROL_WIDGET.configure(
            textvariable=self.CUST_LPF_FILTER3_CONTROL)
        self.CUST_LPF_FILTER3_CONTROL_WIDGET.pack(side="left")
        self.CUST_LPF_FILTER4_CONTROL_WIDGET = ttk.Label(
            self.hidden_data_items)
        self.CUST_LPF_FILTER4_CONTROL = tk.StringVar()
        self.CUST_LPF_FILTER4_CONTROL_WIDGET.configure(
            textvariable=self.CUST_LPF_FILTER4_CONTROL)
        self.CUST_LPF_FILTER4_CONTROL_WIDGET.pack(side="left")
        self.CUST_LPF_FILTER5_CONTROL_WIDGET = ttk.Label(
            self.hidden_data_items)
        self.CUST_LPF_FILTER5_CONTROL = tk.StringVar()
        self.CUST_LPF_FILTER5_CONTROL_WIDGET.configure(
            textvariable=self.CUST_LPF_FILTER5_CONTROL)
        self.CUST_LPF_FILTER5_CONTROL_WIDGET.pack(side="left")
        self.CUST_LPF_FILTER6_CONTROL_WIDGET = ttk.Label(
            self.hidden_data_items)
        self.CUST_LPF_FILTER6_CONTROL = tk.StringVar()
        self.CUST_LPF_FILTER6_CONTROL_WIDGET.configure(
            textvariable=self.CUST_LPF_FILTER6_CONTROL)
        self.CUST_LPF_FILTER6_CONTROL_WIDGET.pack(side="left")
        self.CUST_LPF_FILTER7_CONTROL_WIDGET = ttk.Label(
            self.hidden_data_items)
        self.CUST_LPF_FILTER7_CONTROL = tk.StringVar()
        self.CUST_LPF_FILTER7_CONTROL_WIDGET.configure(
            textvariable=self.CUST_LPF_FILTER7_CONTROL)
        self.CUST_LPF_FILTER7_CONTROL_WIDGET.pack(side="left")
        self.hidden_data_items.grid(column=0, row=13)
        self.frame8.pack(fill="x", padx="20 0", side="top")
        self.frame8.grid_anchor("nw")
        self.frame59 = ttk.Frame(self.Extensions_Frame)
        self.frame59.configure(height=200, width=200)
        self.separator8 = ttk.Separator(self.frame59)
        self.separator8.configure(orient="horizontal")
        self.separator8.pack(
            anchor="center",
            expand="true",
            fill="x",
            side="top")
        self.frame59.pack(anchor="w", expand="true", fill="x", side="top")
        self.frame49 = ttk.Frame(self.Extensions_Frame)
        self.frame49.configure(height=200, width=200)
        self.frame50 = ttk.Frame(self.frame49)
        self.frame50.configure(height=200, width=200)
        self.label200 = ttk.Label(self.frame50)
        self.label200.configure(style="Heading3.TLabel", text='IF Adjustments')
        self.label200.grid(column=0, row=0)
        self.message3 = tk.Message(self.frame50)
        self.message3.configure(
            borderwidth=2,
            font="TkTextFont",
            justify="left",
            pady=5,
            relief="ridge",
            text='Can improve receiver performance. For details, see:\nhttp://www.hamskey.com/2018/04/improves-ubitx-receive-performance-by.html',
            width=500)
        self.message3.grid(column=1, padx=10, row=0, sticky="w")
        self.frame50.pack(
            anchor="w",
            expand="true",
            fill="x",
            padx="20 0",
            side="top")
        self.frame51 = ttk.Frame(self.frame49)
        self.frame51.configure(height=200, width=200)
        self.IF1_CAL_ON_OFF_SWITCH_WIDGET = ttk.Checkbutton(self.frame51)
        self.IF1_CAL_ON_OFF_SWITCH = tk.StringVar()
        self.IF1_CAL_ON_OFF_SWITCH_WIDGET.configure(
            offvalue="NO",
            onvalue="YES",
            style="Checkbox4.TCheckbutton",
            text='Enable IF1 Calibration Value',
            variable=self.IF1_CAL_ON_OFF_SWITCH)
        self.IF1_CAL_ON_OFF_SWITCH_WIDGET.pack(anchor="w", side="top")
        self.IF1_CAL_ON_OFF_SWITCH_WIDGET.configure(
            command=self.toggle_IF1_Calibration_Frame)
        self.IF1_Calibration_Frame = ttk.Frame(self.frame51)
        self.IF1_Calibration_Frame.configure(height=200, width=200)
        self.label202 = ttk.Label(self.IF1_Calibration_Frame)
        self.label202.configure(
            style="Heading4.TLabel",
            text='IF1 (45Mhz) Calibration: ')
        self.label202.grid(column=0, row=0)
        self.IF1_CAL_ADD_SUB_WIDGET = ttk.Checkbutton(
            self.IF1_Calibration_Frame)
        self.IF1_CAL_ADD_SUB = tk.StringVar()
        self.IF1_CAL_ADD_SUB_WIDGET.configure(
            offvalue="NO",
            onvalue="YES",
            style="Checkbox4.TCheckbutton",
            text='Calibration is a Negative Value',
            variable=self.IF1_CAL_ADD_SUB)
        self.IF1_CAL_ADD_SUB_WIDGET.grid(column=1, row=1)
        self.IF1_CAL_WIDGET = ttk.Entry(self.IF1_Calibration_Frame)
        self.IF1_CAL = tk.StringVar()
        self.IF1_CAL_WIDGET.configure(
            textvariable=self.IF1_CAL, validate="focus")
        self.IF1_CAL_WIDGET.grid(column=1, row=0)
        _validatecmd = (
            self.IF1_CAL_WIDGET.register(
                self.validate_IF1_CAL), "%P", "%V")
        self.IF1_CAL_WIDGET.configure(validatecommand=_validatecmd)
        self.IF1_Calibration_Frame.pack(anchor="e", padx=70, side="top")
        self.frame51.pack(anchor="w", padx="50 0", side="top")
        self.frame49.pack(anchor="w", side="top")
        self.Extensions_Frame.pack(
            anchor="w",
            expand="true",
            fill="both",
            padx=5,
            pady="15 10",
            side="top")
        self.Extensions_SF.pack(expand="true", fill="both", side="top")
        self.settingsNotebook.add(self.Extensions_SF, text='Extensions')
        self.Calibration_SF = ScrolledFrame(
            self.settingsNotebook, scrolltype="both")
        self.Calibration_SF.configure(usemousewheel=True)
        self.Calibration_Settings_Title_Frame = ttk.Frame(
            self.Calibration_SF.innerframe)
        self.Calibration_Settings_Title_Frame.configure(height=200, width=200)
        self.Calibration_Settings_Label = ttk.Label(
            self.Calibration_Settings_Title_Frame)
        self.Calibration_Settings_Label.configure(
            justify="center", style="Heading2.TLabel", text='Calibration')
        self.Calibration_Settings_Label.pack(anchor="w", padx=5, pady="15 25")
        self.Calibration_Settings_Title_Frame.pack(anchor="w", side="top")
        self.frame21 = ttk.Frame(self.Calibration_SF.innerframe)
        self.frame21.configure(height=200, width=200)
        self.Radio_Calibration_Frame = ttk.Frame(self.frame21)
        self.Calibration_Settings_Radio_Label = ttk.Label(
            self.Radio_Calibration_Frame)
        self.Calibration_Settings_Radio_Label.configure(
            style="Heading3.TLabel", text='Radio')
        self.Calibration_Settings_Radio_Label.grid(
            column=0, padx=0, row=2, sticky="ew")
        self.Calibration_Settings_Radio_Existing_Value = ttk.Label(
            self.Radio_Calibration_Frame)
        self.Calibration_Settings_Radio_Existing_Value.configure(
            style="Heading4.TLabel", text='Existing Value')
        self.Calibration_Settings_Radio_Existing_Value.grid(
            column=3, row=3, sticky="s")
        self.Calibration_Settings_Radio_Factory_Recovery = ttk.Label(
            self.Radio_Calibration_Frame)
        self.Calibration_Settings_Radio_Factory_Recovery.configure(
            style="Heading4.TLabel", text='Factory\nRecovery')
        self.Calibration_Settings_Radio_Factory_Recovery.grid(
            column=4, columnspan=2, row=3, sticky="n")
        self.MASTER_CAL_LABEL = ttk.Label(self.Radio_Calibration_Frame)
        self.MASTER_CAL_LABEL.configure(
            style="Normal.TLabel", text='Master Cal')
        self.MASTER_CAL_LABEL.grid(column=1, padx="25 5", row=4, sticky="w")
        self.MASTER_CAL_WIDGET = ttk.Entry(self.Radio_Calibration_Frame)
        self.MASTER_CAL = tk.StringVar()
        self.MASTER_CAL_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.MASTER_CAL,
            validate="focus",
            width=10)
        self.MASTER_CAL_WIDGET.grid(column=3, padx="0 5", row=4, sticky="w")
        _validatecmd = (
            self.MASTER_CAL_WIDGET.register(
                self.validate_MASTER_CAL), "%P", "%V")
        self.MASTER_CAL_WIDGET.configure(validatecommand=_validatecmd)
        self.MASTER_CAL_COPY_BUTTON = ttk.Button(self.Radio_Calibration_Frame)
        self.MASTER_CAL_COPY_BUTTON.configure(style="Normal.TButton", width=10)
        self.MASTER_CAL_COPY_BUTTON.grid(
            column=4, padx="0 5", pady=2, row=4, sticky="w")
        self.MASTER_CAL_COPY_BUTTON.configure(
            command=self.Reset_Master_Cal_To_Factory)
        self.MASTER_CAL_COPY_FACTORY_BUTTON = ttk.Button(
            self.Radio_Calibration_Frame)
        self.MASTER_CAL_COPY_FACTORY_BUTTON.configure(
            style="Normal.TButton", width=10)
        self.MASTER_CAL_COPY_FACTORY_BUTTON.grid(
            column=5, padx="0 5", pady=2, row=4, sticky="w")
        self.MASTER_CAL_COPY_FACTORY_BUTTON.configure(
            command=self.Copy_Master_Cal_Over_Factory_Value)
        self.FACTORY_VALUES_MASTER_CAL_LABEL = ttk.Label(
            self.Radio_Calibration_Frame)
        self.FACTORY_VALUES_MASTER_CAL = tk.StringVar()
        self.FACTORY_VALUES_MASTER_CAL_LABEL.configure(
            style="Heading4.TLabel", textvariable=self.FACTORY_VALUES_MASTER_CAL)
        self.FACTORY_VALUES_MASTER_CAL_LABEL.grid(
            column=6, padx="0 5", row=4, sticky="w")
        self.USB_CAL_LABEL = ttk.Label(self.Radio_Calibration_Frame)
        self.USB_CAL_LABEL.configure(style="Normal.TLabel", text='SSB BFO')
        self.USB_CAL_LABEL.grid(column=1, padx="25 0", row=5, sticky="w")
        self.USB_CAL_WIDGET = ttk.Entry(self.Radio_Calibration_Frame)
        self.USB_CAL = tk.StringVar()
        self.USB_CAL_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.USB_CAL,
            validate="focus",
            width=10)
        self.USB_CAL_WIDGET.grid(column=3, row=5, sticky="w")
        _validatecmd = (
            self.USB_CAL_WIDGET.register(
                self.validate_USB_CAL), "%P", "%V")
        self.USB_CAL_WIDGET.configure(validatecommand=_validatecmd)
        self.USB_CAL_COPY_BUTTON = ttk.Button(self.Radio_Calibration_Frame)
        self.USB_CAL_COPY_BUTTON.configure(style="Normal.TButton", width=10)
        self.USB_CAL_COPY_BUTTON.grid(column=4, pady=2, row=5, sticky="w")
        self.USB_CAL_COPY_BUTTON.configure(
            command=self.Reset_SSB_BFO_To_Factory)
        self.USB_CAL_COPY_FACTORY_BUTTON = ttk.Button(
            self.Radio_Calibration_Frame)
        self.USB_CAL_COPY_FACTORY_BUTTON.configure(
            style="Normal.TButton", width=10)
        self.USB_CAL_COPY_FACTORY_BUTTON.grid(
            column=5, padx="0 5", pady=2, row=5, sticky="w")
        self.USB_CAL_COPY_FACTORY_BUTTON.configure(
            command=self.Copy_SSB_BFO_Over_Factory_Value)
        self.FACTORY_VALUES_USB_CAL_LABEL = ttk.Label(
            self.Radio_Calibration_Frame)
        self.FACTORY_VALUES_USB_CAL = tk.StringVar()
        self.FACTORY_VALUES_USB_CAL_LABEL.configure(
            style="Heading4.TLabel", textvariable=self.FACTORY_VALUES_USB_CAL)
        self.FACTORY_VALUES_USB_CAL_LABEL.grid(column=6, row=5, sticky="w")
        self.CW_CAL_LABEL = ttk.Label(self.Radio_Calibration_Frame)
        self.CW_CAL_LABEL.configure(style="Normal.TLabel", text='CW BFO')
        self.CW_CAL_LABEL.grid(
            column=1,
            padx="25 0",
            pady="15 00",
            row=6,
            sticky="w")
        self.CW_CAL_WIDGET = ttk.Entry(self.Radio_Calibration_Frame)
        self.CW_CAL = tk.StringVar()
        self.CW_CAL_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CW_CAL,
            validate="focus",
            width=10)
        self.CW_CAL_WIDGET.grid(column=3, pady="15 0", row=6, sticky="w")
        _validatecmd = (
            self.CW_CAL_WIDGET.register(
                self.validate_CW_CAL), "%P", "%V")
        self.CW_CAL_WIDGET.configure(validatecommand=_validatecmd)
        self.I2C_ADDR_SI5351_LABEL = ttk.Label(self.Radio_Calibration_Frame)
        self.I2C_ADDR_SI5351_LABEL.configure(
            justify="center",
            relief="flat",
            style="Normal.TLabel",
            text='SI5351 I2C Addr ')
        self.I2C_ADDR_SI5351_LABEL.grid(
            column=1, padx="25 0", pady="15 00", row=7, sticky="w")
        self.I2C_ADDR_SI5351_WIDGET = ttk.Entry(self.Radio_Calibration_Frame)
        self.I2C_ADDR_SI5351 = tk.StringVar()
        self.I2C_ADDR_SI5351_WIDGET.configure(
            justify="center",
            style="Normal.TEntry",
            takefocus=False,
            textvariable=self.I2C_ADDR_SI5351,
            validate="none",
            width=10)
        self.I2C_ADDR_SI5351_WIDGET.grid(
            column=3, pady="15 0", row=7, sticky="w")
        self.Calibration_Screen_Hidden = ttk.Frame(
            self.Radio_Calibration_Frame)
        self.Calibration_Screen_Hidden.configure(height=200, width=200)
        self.CW_FREQUENCY_ADJUSTMENT_WIDGET = ttk.Label(
            self.Calibration_Screen_Hidden)
        self.CW_FREQUENCY_ADJUSTMENT = tk.StringVar()
        self.CW_FREQUENCY_ADJUSTMENT_WIDGET.configure(
            state="disabled", textvariable=self.CW_FREQUENCY_ADJUSTMENT)
        self.CW_FREQUENCY_ADJUSTMENT_WIDGET.pack()
        self.Calibration_Screen_Hidden.grid(column=5, row=7)
        self.FACTORY_SETTING_PROTECTION_WIDGET = ttk.Checkbutton(
            self.Radio_Calibration_Frame)
        self.FACTORY_SETTING_PROTECTION = tk.StringVar()
        self.FACTORY_SETTING_PROTECTION_WIDGET.configure(
            offvalue="NO",
            onvalue="YES",
            style="Checkbox4.TCheckbutton",
            text='Enable update of\nFactory settings?',
            variable=self.FACTORY_SETTING_PROTECTION)
        self.FACTORY_SETTING_PROTECTION_WIDGET.grid(
            column=5, columnspan=4, row=6, rowspan=2)
        self.FACTORY_SETTING_PROTECTION_WIDGET.configure(
            command=self.Factory_Settings_Enable_CB)
        self.Radio_Calibration_Frame.pack(fill="x", side="top")
        self.Radio_Calibration_Frame.grid_anchor("nw")
        self.CW_Calibration_Frame = ttk.Frame(self.frame21)
        self.Calibration_Settings_CW_ADC_Label = ttk.Label(
            self.CW_Calibration_Frame)
        self.Calibration_Settings_CW_ADC_Label.configure(
            justify="left", style="Heading3.TLabel", text='CW ADC')
        self.Calibration_Settings_CW_ADC_Label.grid(
            column=0, pady="20 0", row=1, sticky="ew")
        self.Calibration_Settings_CW_ADC_ADC_Range_Label = ttk.Label(
            self.CW_Calibration_Frame)
        self.Calibration_Settings_CW_ADC_ADC_Range_Label.configure(
            style="Heading4.TLabel", text='ADC Range')
        self.Calibration_Settings_CW_ADC_ADC_Range_Label.grid(
            column=3, columnspan=2, row=5)
        self.Calibration_Settings_CW_ADC_Straight_Key_Label = ttk.Label(
            self.CW_Calibration_Frame)
        self.Calibration_Settings_CW_ADC_Straight_Key_Label.configure(
            style="Heading4.TLabel", text='Straight Key')
        self.Calibration_Settings_CW_ADC_Straight_Key_Label.grid(
            column=1, columnspan=2, row=6, sticky="sw")
        self.Calibration_Settings_CW_ADC_From_Value_Label = ttk.Label(
            self.CW_Calibration_Frame)
        self.Calibration_Settings_CW_ADC_From_Value_Label.configure(
            style="Heading4.TLabel", text='Start', width=7)
        self.Calibration_Settings_CW_ADC_From_Value_Label.grid(
            column=3, padx="18 0", row=6, sticky="s")
        self.Calibration_Settings_CW_ADC_To_Value_Label = ttk.Label(
            self.CW_Calibration_Frame)
        self.Calibration_Settings_CW_ADC_To_Value_Label.configure(
            style="Heading4.TLabel", text='End\t', width=7)
        self.Calibration_Settings_CW_ADC_To_Value_Label.grid(
            column=4, padx="20 0", row=6, sticky="s")
        self.CW_ADC_ST_Lebel = ttk.Label(self.CW_Calibration_Frame)
        self.CW_ADC_ST_Lebel.configure(
            style="Normal.TLabel", text='Key Pressed')
        self.CW_ADC_ST_Lebel.grid(
            column=1,
            padx="0 15",
            pady="0 5",
            row=7,
            sticky="w")
        self.CW_ADC_ST_FROM_WIDGET = ttk.Entry(self.CW_Calibration_Frame)
        self.CW_ADC_ST_FROM = tk.StringVar()
        self.CW_ADC_ST_FROM_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CW_ADC_ST_FROM,
            validate="focus",
            width=5)
        self.CW_ADC_ST_FROM_WIDGET.grid(column=3, pady="0 5", row=7)
        _validatecmd = (
            self.CW_ADC_ST_FROM_WIDGET.register(
                self.validate_CW_ADC_ST_FROM), "%P", "%V")
        self.CW_ADC_ST_FROM_WIDGET.configure(validatecommand=_validatecmd)
        self.CW_ADC_ST_TO_WIDGET = ttk.Entry(self.CW_Calibration_Frame)
        self.CW_ADC_ST_TO = tk.StringVar()
        self.CW_ADC_ST_TO_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CW_ADC_ST_TO,
            validate="focus",
            width=5)
        self.CW_ADC_ST_TO_WIDGET.grid(column=4, pady="0 5", row=7)
        _validatecmd = (
            self.CW_ADC_ST_TO_WIDGET.register(
                self.validate_CW_ADC_ST_TO), "%P", "%V")
        self.CW_ADC_ST_TO_WIDGET.configure(validatecommand=_validatecmd)
        self.Calibration_Settings_CW_ADC_Paddle_Key_Label = ttk.Label(
            self.CW_Calibration_Frame)
        self.Calibration_Settings_CW_ADC_Paddle_Key_Label.configure(
            style="Heading4.TLabel", text='Paddle')
        self.Calibration_Settings_CW_ADC_Paddle_Key_Label.grid(
            column=1, columnspan=2, pady="20 0", row=8, sticky="sw")
        self.CW_ADC_DOT_Lebel = ttk.Label(self.CW_Calibration_Frame)
        self.CW_ADC_DOT_Lebel.configure(
            style="Normal.TLabel", text='Dot Key Pressed')
        self.CW_ADC_DOT_Lebel.grid(column=1, pady="0 5", row=9, sticky="w")
        self.CW_ADC_DOT_FROM_WIDGET = ttk.Entry(self.CW_Calibration_Frame)
        self.CW_ADC_DOT_FROM = tk.StringVar()
        self.CW_ADC_DOT_FROM_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CW_ADC_DOT_FROM,
            validate="focus",
            width=5)
        self.CW_ADC_DOT_FROM_WIDGET.grid(column=3, pady="0 5", row=9)
        _validatecmd = (
            self.CW_ADC_DOT_FROM_WIDGET.register(
                self.validate_CW_ADC_DOT_FROM), "%P", "%V")
        self.CW_ADC_DOT_FROM_WIDGET.configure(validatecommand=_validatecmd)
        self.CW_ADC_DOT_TO_WIDGET = ttk.Entry(self.CW_Calibration_Frame)
        self.CW_ADC_DOT_TO = tk.StringVar()
        self.CW_ADC_DOT_TO_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CW_ADC_DOT_TO,
            validate="focus",
            width=5)
        self.CW_ADC_DOT_TO_WIDGET.grid(column=4, padx="0 5", pady="0 5", row=9)
        _validatecmd = (
            self.CW_ADC_DOT_TO_WIDGET.register(
                self.validate_CW_ADC_DOT_TO), "%P", "%V")
        self.CW_ADC_DOT_TO_WIDGET.configure(validatecommand=_validatecmd)
        self.CW_ADC_DASH_Lebel = ttk.Label(self.CW_Calibration_Frame)
        self.CW_ADC_DASH_Lebel.configure(
            style="Normal.TLabel", text='Dash Key Pressed')
        self.CW_ADC_DASH_Lebel.grid(column=1, pady="0 5", row=10, sticky="w")
        self.CW_ADC_DASH_FROM_WIDGET = ttk.Entry(self.CW_Calibration_Frame)
        self.CW_ADC_DASH_FROM = tk.StringVar()
        self.CW_ADC_DASH_FROM_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CW_ADC_DASH_FROM,
            validate="focus",
            width=5)
        self.CW_ADC_DASH_FROM_WIDGET.grid(column=3, pady="0 5", row=10)
        _validatecmd = (
            self.CW_ADC_DASH_FROM_WIDGET.register(
                self.validate_CW_ADC_DASH_FROM), "%P", "%V")
        self.CW_ADC_DASH_FROM_WIDGET.configure(validatecommand=_validatecmd)
        self.CW_ADC_DASH_TO_WIDGET = ttk.Entry(self.CW_Calibration_Frame)
        self.CW_ADC_DASH_TO = tk.StringVar()
        self.CW_ADC_DASH_TO_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CW_ADC_DASH_TO,
            validate="focus",
            width=5)
        self.CW_ADC_DASH_TO_WIDGET.grid(
            column=4, padx="0 5", pady="0 5", row=10)
        _validatecmd = (
            self.CW_ADC_DASH_TO_WIDGET.register(
                self.validate_CW_ADC_DASH_TO), "%P", "%V")
        self.CW_ADC_DASH_TO_WIDGET.configure(validatecommand=_validatecmd)
        self.CW_ADC_BOTH_Lebel = ttk.Label(self.CW_Calibration_Frame)
        self.CW_ADC_BOTH_Lebel.configure(
            style="Normal.TLabel", text='Both Keys Pressed')
        self.CW_ADC_BOTH_Lebel.grid(
            column=1,
            padx="0 5",
            pady="0 5",
            row=11,
            sticky="w")
        self.CW_ADC_BOTH_FROM_WIDGET = ttk.Entry(self.CW_Calibration_Frame)
        self.CW_ADC_BOTH_FROM = tk.StringVar()
        self.CW_ADC_BOTH_FROM_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CW_ADC_BOTH_FROM,
            validate="focus",
            width=5)
        self.CW_ADC_BOTH_FROM_WIDGET.grid(column=3, pady="0 5", row=11)
        _validatecmd = (
            self.CW_ADC_BOTH_FROM_WIDGET.register(
                self.validate_CW_ADC_BOTH_FROM), "%P", "%V")
        self.CW_ADC_BOTH_FROM_WIDGET.configure(validatecommand=_validatecmd)
        self.CW_ADC_BOTH_TO_WIDGET = ttk.Entry(self.CW_Calibration_Frame)
        self.CW_ADC_BOTH_TO = tk.StringVar()
        self.CW_ADC_BOTH_TO_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.CW_ADC_BOTH_TO,
            validate="focus",
            width=5)
        self.CW_ADC_BOTH_TO_WIDGET.grid(
            column=4, padx="0 5", pady="0 5", row=11)
        _validatecmd = (
            self.CW_ADC_BOTH_TO_WIDGET.register(
                self.validate_CW_ADC_BOTH_TO), "%P", "%V")
        self.CW_ADC_BOTH_TO_WIDGET.configure(validatecommand=_validatecmd)
        self.frame3 = ttk.Frame(self.CW_Calibration_Frame)
        self.frame3.configure(height=200, width=200)
        self.load_Recommended_ADC_CW_Values_WIDGET = ttk.Button(self.frame3)
        self.load_Recommended_ADC_CW_Values_WIDGET.configure(
            style="Button4.TButton", text='Load Recommend ADC Settings')
        self.load_Recommended_ADC_CW_Values_WIDGET.grid(
            column=1, padx=40, row=0, sticky="e")
        self.load_Recommended_ADC_CW_Values_WIDGET.configure(
            command=self.load_Recommended_ADC_CW_Values)
        self.CAL_runADCScanner_WIDGET = ttk.Button(self.frame3)
        self.CAL_runADCScanner_WIDGET.configure(
            style="Button4.TButton", text='ADC Scanner')
        self.CAL_runADCScanner_WIDGET.grid(column=0, row=0)
        self.CAL_runADCScanner_WIDGET.configure(command=self.runADCScanner)
        self.frame3.grid(column=1, columnspan=5, pady=15, row=12, sticky="ew")
        self.CW_Calibration_Frame.pack(fill="x", side="top")
        self.CW_Calibration_Frame.grid_anchor("nw")
        self.S_Meter_Frame = ttk.Frame(self.frame21)
        self.label1 = ttk.Label(self.S_Meter_Frame)
        self.label1.configure(style="Heading3.TLabel", text='S-Meter')
        self.label1.grid(column=0, padx=0, pady="20 0", row=1, sticky="ew")
        self.message7 = tk.Message(self.S_Meter_Frame)
        self.message7.configure(
            borderwidth=2,
            font="TkTextFont",
            justify="left",
            pady=5,
            relief="ridge",
            takefocus=False,
            text='This setting is only for S-Meters where the sensor is directly attached to the main processor. If your uBITX is using a separate processor for the S-Meter (and perhaps SWR), then DO NOT enable this one.',
            width=300)
        self.message7.grid(
            column=1,
            columnspan=2,
            padx="30 0",
            pady="50 0",
            row=1,
            sticky="nw")
        self.S_METER_LEVELS_WIDGET = ttk.Checkbutton(self.S_Meter_Frame)
        self.S_METER_LEVELS = tk.StringVar()
        self.S_METER_LEVELS_WIDGET.configure(
            offvalue="NO",
            onvalue="YES",
            style="Checkbox3.TCheckbutton",
            text='Enable S-Meter',
            variable=self.S_METER_LEVELS)
        self.S_METER_LEVELS_WIDGET.grid(
            column=0, padx=25, pady="15 10", row=2, sticky="w")
        self.S_METER_LEVELS_WIDGET.configure(command=self.SMeter_Input_CB)
        self.frame28 = ttk.Frame(self.S_Meter_Frame)
        self.frame28.configure(height=200, width=200)
        self.SMETER_CONFIG_FRAME = ttk.Frame(self.frame28)
        self.SMETER_CONFIG_FRAME.configure(height=200, width=200)
        self.label29 = ttk.Label(self.SMETER_CONFIG_FRAME)
        self.label29.configure(
            justify="left",
            relief="flat",
            style="Heading4.TLabel",
            text='1')
        self.label29.grid(column=1, padx="8 0", row=2)
        self.S_METER_LEVEL1_WIDGET = ttk.Entry(self.SMETER_CONFIG_FRAME)
        self.S_METER_LEVEL1 = tk.StringVar()
        self.S_METER_LEVEL1_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.S_METER_LEVEL1,
            validate="focus",
            width=5)
        self.S_METER_LEVEL1_WIDGET.grid(
            column=1, padx="10 0", row=3, sticky="w")
        _validatecmd = (
            self.S_METER_LEVEL1_WIDGET.register(
                self.validate_METER_LEVEL1), "%P", "%V")
        self.S_METER_LEVEL1_WIDGET.configure(validatecommand=_validatecmd)
        self.label15 = ttk.Label(self.SMETER_CONFIG_FRAME)
        self.label15.configure(
            justify="right",
            style="Heading4.TLabel",
            takefocus=False,
            text='ADC Value (0-1023)')
        self.label15.grid(column=0, padx="15 0", row=3, sticky="w")
        self.S_METER_LEVEL2_WIDGET = ttk.Entry(self.SMETER_CONFIG_FRAME)
        self.S_METER_LEVEL2 = tk.StringVar()
        self.S_METER_LEVEL2_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.S_METER_LEVEL2,
            validate="focus",
            width=5)
        self.S_METER_LEVEL2_WIDGET.grid(
            column=2, padx="5 0", row=3, sticky="w")
        _validatecmd = (
            self.S_METER_LEVEL2_WIDGET.register(
                self.validate_METER_LEVEL2), "%P", "%V")
        self.S_METER_LEVEL2_WIDGET.configure(validatecommand=_validatecmd)
        self.S_METER_LEVEL3_WIDGET = ttk.Entry(self.SMETER_CONFIG_FRAME)
        self.S_METER_LEVEL3 = tk.StringVar()
        self.S_METER_LEVEL3_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.S_METER_LEVEL3,
            validate="focus",
            width=5)
        self.S_METER_LEVEL3_WIDGET.grid(
            column=3, padx="5 0", row=3, sticky="w")
        _validatecmd = (
            self.S_METER_LEVEL3_WIDGET.register(
                self.validate_METER_LEVEL3), "%P", "%V")
        self.S_METER_LEVEL3_WIDGET.configure(validatecommand=_validatecmd)
        self.S_METER_LEVEL4_WIDGET = ttk.Entry(self.SMETER_CONFIG_FRAME)
        self.S_METER_LEVEL4 = tk.StringVar()
        self.S_METER_LEVEL4_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.S_METER_LEVEL4,
            validate="focus",
            width=5)
        self.S_METER_LEVEL4_WIDGET.grid(
            column=4, padx="5 0", row=3, sticky="w")
        _validatecmd = (
            self.S_METER_LEVEL4_WIDGET.register(
                self.validate_METER_LEVEL4), "%P", "%V")
        self.S_METER_LEVEL4_WIDGET.configure(validatecommand=_validatecmd)
        self.S_METER_LEVEL5_WIDGET = ttk.Entry(self.SMETER_CONFIG_FRAME)
        self.S_METER_LEVEL5 = tk.StringVar()
        self.S_METER_LEVEL5_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.S_METER_LEVEL5,
            validate="focus",
            width=5)
        self.S_METER_LEVEL5_WIDGET.grid(
            column=5, padx="5 0", row=3, sticky="w")
        _validatecmd = (
            self.S_METER_LEVEL5_WIDGET.register(
                self.validate_METER_LEVEL5), "%P", "%V")
        self.S_METER_LEVEL5_WIDGET.configure(validatecommand=_validatecmd)
        self.S_METER_LEVEL6_WIDGET = ttk.Entry(self.SMETER_CONFIG_FRAME)
        self.S_METER_LEVEL6 = tk.StringVar()
        self.S_METER_LEVEL6_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.S_METER_LEVEL6,
            validate="focus",
            width=5)
        self.S_METER_LEVEL6_WIDGET.grid(
            column=6, padx="5 0", row=3, sticky="w")
        _validatecmd = (
            self.S_METER_LEVEL6_WIDGET.register(
                self.validate_METER_LEVEL6), "%P", "%V")
        self.S_METER_LEVEL6_WIDGET.configure(validatecommand=_validatecmd)
        self.S_METER_LEVEL7_WIDGET = ttk.Entry(self.SMETER_CONFIG_FRAME)
        self.S_METER_LEVEL7 = tk.StringVar()
        self.S_METER_LEVEL7_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.S_METER_LEVEL7,
            validate="focus",
            width=5)
        self.S_METER_LEVEL7_WIDGET.grid(
            column=7, padx="5 0", row=3, sticky="w")
        _validatecmd = (
            self.S_METER_LEVEL7_WIDGET.register(
                self.validate_METER_LEVEL7), "%P", "%V")
        self.S_METER_LEVEL7_WIDGET.configure(validatecommand=_validatecmd)
        self.S_METER_LEVEL8_WIDGET = ttk.Entry(self.SMETER_CONFIG_FRAME)
        self.S_METER_LEVEL8 = tk.StringVar()
        self.S_METER_LEVEL8_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.S_METER_LEVEL8,
            validate="focus",
            width=5)
        self.S_METER_LEVEL8_WIDGET.grid(
            column=8, padx="5 0", row=3, sticky="w")
        _validatecmd = (
            self.S_METER_LEVEL8_WIDGET.register(
                self.validate_METER_LEVEL8), "%P", "%V")
        self.S_METER_LEVEL8_WIDGET.configure(validatecommand=_validatecmd)
        self.label45 = ttk.Label(self.SMETER_CONFIG_FRAME)
        self.label45.configure(
            justify="center",
            relief="flat",
            style="Heading3.TLabel",
            text='S-Level')
        self.label45.grid(column=1, columnspan=11, padx="25 20", row=1)
        self.label33 = ttk.Label(self.SMETER_CONFIG_FRAME)
        self.label33.configure(
            justify="left",
            relief="flat",
            style="Heading4.TLabel",
            text='2')
        self.label33.grid(column=2, padx="7 0", row=2)
        self.label35 = ttk.Label(self.SMETER_CONFIG_FRAME)
        self.label35.configure(
            justify="left",
            relief="flat",
            style="Heading4.TLabel",
            text='3')
        self.label35.grid(column=3, padx="7 0", row=2)
        self.label36 = ttk.Label(self.SMETER_CONFIG_FRAME)
        self.label36.configure(
            justify="left",
            relief="flat",
            style="Heading4.TLabel",
            text='4')
        self.label36.grid(column=4, padx="7 0", row=2)
        self.label38 = ttk.Label(self.SMETER_CONFIG_FRAME)
        self.label38.configure(
            justify="left",
            relief="flat",
            style="Heading4.TLabel",
            text='5')
        self.label38.grid(column=5, padx="7 0", row=2)
        self.label39 = ttk.Label(self.SMETER_CONFIG_FRAME)
        self.label39.configure(
            justify="left",
            relief="flat",
            style="Heading4.TLabel",
            text='6')
        self.label39.grid(column=6, padx="7 0", row=2)
        self.label41 = ttk.Label(self.SMETER_CONFIG_FRAME)
        self.label41.configure(
            justify="left",
            relief="flat",
            style="Heading4.TLabel",
            text='7')
        self.label41.grid(column=7, padx="7 0", row=2)
        self.label42 = ttk.Label(self.SMETER_CONFIG_FRAME)
        self.label42.configure(
            justify="left",
            relief="flat",
            style="Heading4.TLabel",
            text='8')
        self.label42.grid(column=8, padx="7 0", row=2)
        self.smeterAssistant_BUTTON_WIDGET = ttk.Button(
            self.SMETER_CONFIG_FRAME)
        self.smeterAssistant_BUTTON_WIDGET.configure(
            style="Button4.TButton", text='S-Meter Assistant')
        self.smeterAssistant_BUTTON_WIDGET.grid(
            column=1, columnspan=11, pady=25, row=4)
        self.smeterAssistant_BUTTON_WIDGET.configure(
            command=self.runSmeterAssistant)
        self.SMETER_CONFIG_FRAME.pack()
        self.frame28.grid(column=0, columnspan=2, row=4)
        self.S_Meter_Frame.pack(fill="x", side="top")
        self.S_Meter_Frame.grid_anchor("nw")
        self.frame21.pack(anchor="w", padx=20, side="top")
        self.Calibration_SF.pack(side="top")
        self.settingsNotebook.add(self.Calibration_SF, text='Calibration')
        self.System_Info_SF = ScrolledFrame(
            self.settingsNotebook, scrolltype="both")
        self.System_Info_SF.configure(usemousewheel=True)
        self.frame26 = ttk.Frame(self.System_Info_SF.innerframe)
        self.frame26.configure(height=200, width=200)
        self.System_Information_Title_Frame = ttk.Frame(self.frame26)
        self.System_Information_Title_Frame.configure(height=200, width=200)
        self.System_Information_Label = ttk.Label(
            self.System_Information_Title_Frame)
        self.System_Information_Label.configure(
            justify="center",
            style="Heading2.TLabel",
            text='System Information')
        self.System_Information_Label.pack(anchor="w", padx=5, pady="15 25")
        self.System_Information_Title_Frame.pack(anchor="w", side="top")
        self.frame27 = ttk.Frame(self.frame26)
        self.frame27.configure(height=200, width=200)
        self.System_Info_Firmware_Version = ttk.Frame(self.frame27)
        self.System_Info_Firmware_Version.configure(width=200)
        self.Firmware_Version_Title = ttk.Frame(
            self.System_Info_Firmware_Version)
        self.Firmware_Version_Title.configure(height=200, width=200)
        self.System_Info_Firmware_Version_Label = ttk.Label(
            self.Firmware_Version_Title)
        self.System_Info_Firmware_Version_Label.configure(
            style="Heading3.TLabel", text='Firmware Version: ')
        self.System_Info_Firmware_Version_Label.pack(expand="true", fill="x")
        self.Firmware_Version_Title.pack(
            anchor="w", expand="true", fill="x", side="top")
        self.Firmware_Version_Content = ttk.Frame(
            self.System_Info_Firmware_Version)
        self.Firmware_Version_Content.configure(height=200, width=200)
        self.KD8CEC_VERSION_WIDGET = ttk.Label(self.Firmware_Version_Content)
        self.KD8CEC_VERSION_WIDGET.configure(
            style="Heading4.TLabel", text='KD8CEC')
        self.KD8CEC_VERSION_WIDGET.grid(column=0, row=0, sticky="e")
        self.EXT_FIRMWARE_VERSION_INFO_WIDGET = ttk.Label(
            self.Firmware_Version_Content)
        self.EXT_FIRMWARE_VERSION_INFO = tk.StringVar()
        self.EXT_FIRMWARE_VERSION_INFO_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_FIRMWARE_VERSION_INFO)
        self.EXT_FIRMWARE_VERSION_INFO_WIDGET.grid(
            column=1, padx=5, row=0, sticky="w")
        self.EXT_RELEASE_NAME_LABEL = ttk.Label(self.Firmware_Version_Content)
        self.EXT_RELEASE_NAME_LABEL.configure(
            style="Heading4.TLabel", text='Release Name:')
        self.EXT_RELEASE_NAME_LABEL.grid(column=0, row=1, sticky="e")
        self.EXT_RELEASE_NAME_WIDGET = ttk.Label(self.Firmware_Version_Content)
        self.EXT_RELEASE_NAME = tk.StringVar()
        self.EXT_RELEASE_NAME_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_RELEASE_NAME)
        self.EXT_RELEASE_NAME_WIDGET.grid(column=1, padx=5, row=1, sticky="w")
        self.label165 = ttk.Label(self.Firmware_Version_Content)
        self.label165.configure(
            state="normal",
            style="Heading4.TLabel",
            text='Build Date:')
        self.label165.grid(column=0, row=2, sticky="e")
        self.EXT_DATE_TIME_STAMP_WIDGET = ttk.Label(
            self.Firmware_Version_Content)
        self.EXT_DATE_TIME_STAMP = tk.StringVar()
        self.EXT_DATE_TIME_STAMP_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_DATE_TIME_STAMP)
        self.EXT_DATE_TIME_STAMP_WIDGET.grid(
            column=1, padx=5, row=2, sticky="w")
        self.label186 = ttk.Label(self.Firmware_Version_Content)
        self.label186.configure(
            state="normal",
            style="Heading4.TLabel",
            text='Functionality Set:')
        self.label186.grid(column=0, row=3, sticky="e")
        self.EXT_FUNCTIONALITY_SET_WIDGET = ttk.Label(
            self.Firmware_Version_Content)
        self.EXT_FUNCTIONALITY_SET = tk.StringVar()
        self.EXT_FUNCTIONALITY_SET_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_FUNCTIONALITY_SET)
        self.EXT_FUNCTIONALITY_SET_WIDGET.grid(
            column=1, padx=5, row=3, sticky="w")
        self.Firmware_Version_Content.pack(
            expand="true", fill="x", padx=75, side="top")
        self.System_Info_Firmware_Version.pack(
            anchor="w", pady="20 0", side="top")
        self.System_Info_Calibration_Settings = ttk.Frame(self.frame27)
        self.System_Info_Calibration_Settings.configure(width=200)
        self.Factory_Data_Title = ttk.Frame(
            self.System_Info_Calibration_Settings)
        self.Factory_Data_Title.configure(height=200, width=200)
        self.System_Info_Factory_Calibration_Label = ttk.Label(
            self.Factory_Data_Title)
        self.System_Info_Factory_Calibration_Label.configure(
            style="Heading3.TLabel", text='Factory Data')
        self.System_Info_Factory_Calibration_Label.pack(anchor="w")
        self.Factory_Data_Title.pack(
            anchor="w", expand="true", fill="x", side="top")
        self.Factory_Data_Content = ttk.Frame(
            self.System_Info_Calibration_Settings)
        self.Factory_Data_Content.configure(height=200, width=200)
        self.System_Info_Factory_Calibration_Master_Label = ttk.Label(
            self.Factory_Data_Content)
        self.System_Info_Factory_Calibration_Master_Label.configure(
            style="Heading4.TLabel", text='Master Calibration:')
        self.System_Info_Factory_Calibration_Master_Label.grid(
            column=0, row=0, sticky="e")
        self.System_Info_MASTER_CAL_WIDGET = ttk.Label(
            self.Factory_Data_Content)
        self.System_Info_MASTER_CAL_WIDGET.configure(
            compound="top",
            style="Normal.TLabel",
            textvariable=self.FACTORY_VALUES_MASTER_CAL)
        self.System_Info_MASTER_CAL_WIDGET.grid(
            column=1, padx=5, row=0, sticky="w")
        self.System_Info_Factory_Calibration_BFO_Label = ttk.Label(
            self.Factory_Data_Content)
        self.System_Info_Factory_Calibration_BFO_Label.configure(
            style="Heading4.TLabel", text='SSB BFO Calibration:')
        self.System_Info_Factory_Calibration_BFO_Label.grid(
            column=0, row=1, sticky="e")
        self.System_Info_USB_CAL_WIDGET = ttk.Label(self.Factory_Data_Content)
        self.System_Info_USB_CAL_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.FACTORY_VALUES_USB_CAL)
        self.System_Info_USB_CAL_WIDGET.grid(
            column=1, padx=5, row=1, sticky="w")
        self.label171 = ttk.Label(self.Factory_Data_Content)
        self.label171.configure(style="Heading4.TLabel", text='CW Sidetone:')
        self.label171.grid(column=0, row=2, sticky="e")
        self.FACTORY_VALUES_CW_SIDETONE_WIDGET = ttk.Label(
            self.Factory_Data_Content)
        self.FACTORY_VALUES_CW_SIDETONE = tk.StringVar()
        self.FACTORY_VALUES_CW_SIDETONE_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.FACTORY_VALUES_CW_SIDETONE)
        self.FACTORY_VALUES_CW_SIDETONE_WIDGET.grid(
            column=1, padx=5, row=2, sticky="w")
        self.label184 = ttk.Label(self.Factory_Data_Content)
        self.label184.configure(style="Heading4.TLabel", text='CW Speed:')
        self.label184.grid(column=0, row=3, sticky="e")
        self.FACTORY_VALUES_CW_SPEED_WIDGET = ttk.Label(
            self.Factory_Data_Content)
        self.FACTORY_VALUES_CW_SPEED = tk.StringVar()
        self.FACTORY_VALUES_CW_SPEED_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.FACTORY_VALUES_CW_SPEED)
        self.FACTORY_VALUES_CW_SPEED_WIDGET.grid(
            column=1, padx=5, row=3, sticky="w")
        self.Factory_Data_Content.pack(
            expand="true", fill="x", padx=50, side="top")
        self.System_Info_Calibration_Settings.pack(
            anchor="w", pady="20 0", side="top")
        self.System_Info_Hardware = ttk.Frame(self.frame27)
        self.System_Info_Hardware.configure(width=200)
        self.Hardware_Title = ttk.Frame(self.System_Info_Hardware)
        self.Hardware_Title.configure(height=200, width=200)
        self.label166 = ttk.Label(self.Hardware_Title)
        self.label166.configure(style="Heading3.TLabel", text='Hardware: ')
        self.label166.pack(anchor="w")
        self.Hardware_Title.pack(
            anchor="w",
            expand="true",
            fill="x",
            side="top")
        self.Hardware_Content = ttk.Frame(self.System_Info_Hardware)
        self.Hardware_Content.configure(height=200, width=200)
        self.label190 = ttk.Label(self.Hardware_Content)
        self.label190.configure(style="Heading4.TLabel", text='uBITX Version:')
        self.label190.grid(column=0, row=0, sticky="e")
        self.EXT_UBITX_BOARD_VERSION_WIDGET = ttk.Label(self.Hardware_Content)
        self.EXT_UBITX_BOARD_VERSION = tk.StringVar()
        self.EXT_UBITX_BOARD_VERSION_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_UBITX_BOARD_VERSION)
        self.EXT_UBITX_BOARD_VERSION_WIDGET.grid(
            column=1, padx=5, row=0, sticky="w")
        self.label192 = ttk.Label(self.Hardware_Content)
        self.label192.configure(
            state="normal",
            style="Heading4.TLabel",
            text='Processor:')
        self.label192.grid(column=0, row=1, sticky="e")
        self.EXT_PROCESSOR_TYPE_WIDGET = ttk.Label(self.Hardware_Content)
        self.EXT_PROCESSOR_TYPE = tk.StringVar()
        self.EXT_PROCESSOR_TYPE_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_PROCESSOR_TYPE)
        self.EXT_PROCESSOR_TYPE_WIDGET.grid(
            column=1, padx=5, row=1, sticky="w")
        self.label194 = ttk.Label(self.Hardware_Content)
        self.label194.configure(
            state="normal",
            style="Heading4.TLabel",
            text='Display:')
        self.label194.grid(column=0, row=2, sticky="e")
        self.EXT_DISPLAY_TYPE_WIDGET = ttk.Label(self.Hardware_Content)
        self.EXT_DISPLAY_TYPE = tk.StringVar()
        self.EXT_DISPLAY_TYPE_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_DISPLAY_TYPE)
        self.EXT_DISPLAY_TYPE_WIDGET.grid(column=1, padx=5, row=2, sticky="w")
        self.label196 = ttk.Label(self.Hardware_Content)
        self.label196.configure(
            state="normal",
            style="Heading4.TLabel",
            text='S-Meter')
        self.label196.grid(column=0, row=3, sticky="e")
        self.EXT_SMETER_SELECTION_WIDGET = ttk.Label(self.Hardware_Content)
        self.EXT_SMETER_SELECTION = tk.StringVar()
        self.EXT_SMETER_SELECTION_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_SMETER_SELECTION)
        self.EXT_SMETER_SELECTION_WIDGET.grid(
            column=1, padx=5, row=3, sticky="w")
        self.Serial_Type_Label = ttk.Label(self.Hardware_Content)
        self.Serial_Type_Label.configure(
            state="normal", style="Heading4.TLabel", text='Serial:')
        self.Serial_Type_Label.grid(column=0, row=4, sticky="e")
        self.EXT_SERIAL_TYPE_WIDGET = ttk.Label(self.Hardware_Content)
        self.EXT_SERIAL_TYPE = tk.StringVar()
        self.EXT_SERIAL_TYPE_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_SERIAL_TYPE)
        self.EXT_SERIAL_TYPE_WIDGET.grid(column=1, padx=5, row=4, sticky="w")
        self.EEPROM_Type_Label = ttk.Label(self.Hardware_Content)
        self.EEPROM_Type_Label.configure(
            state="normal", style="Heading4.TLabel", text='EEPROM:')
        self.EEPROM_Type_Label.grid(column=0, row=5, sticky="e")
        self.EXT_EEPROM_TYPE_WIDGET = ttk.Label(self.Hardware_Content)
        self.EXT_EEPROM_TYPE = tk.StringVar()
        self.EXT_EEPROM_TYPE_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_EEPROM_TYPE)
        self.EXT_EEPROM_TYPE_WIDGET.grid(column=1, padx=5, row=5, sticky="w")
        self.Encoder_Type_Label = ttk.Label(self.Hardware_Content)
        self.Encoder_Type_Label.configure(
            state="normal", style="Heading4.TLabel", text='Encoder:')
        self.Encoder_Type_Label.grid(column=0, row=6, sticky="e")
        self.EXT_ENCODER_TYPE_WIDGET = ttk.Label(self.Hardware_Content)
        self.EXT_ENCODER_TYPE = tk.StringVar()
        self.EXT_ENCODER_TYPE_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_ENCODER_TYPE)
        self.EXT_ENCODER_TYPE_WIDGET.grid(column=1, padx=5, row=6, sticky="w")
        self.Hardware_Content.pack(
            expand="true", fill="x", padx=90, side="top")
        self.System_Info_Hardware.pack(
            anchor="w",
            expand="true",
            fill="x",
            pady="20 0",
            side="top")
        self.System_Info_Pins = ttk.Frame(self.frame27)
        self.System_Info_Pins.configure(width=200)
        self.Pins_Title_Frame = ttk.Frame(self.System_Info_Pins)
        self.Pins_Title_Frame.configure(height=200, width=200)
        self.label185 = ttk.Label(self.Pins_Title_Frame)
        self.label185.configure(
            style="Heading3.TLabel",
            text='Pin Assignments:')
        self.label185.pack(anchor="w")
        self.Pins_Title_Frame.pack(
            anchor="w", expand="true", fill="x", side="top")
        self.Pins_Content_Frame = ttk.Frame(self.System_Info_Pins)
        self.Pins_Content_Frame.configure(height=200, width=200)
        self.frame42 = ttk.Frame(self.Pins_Content_Frame)
        self.frame42.configure(height=200, width=200)
        self.ENC_A_Label = ttk.Label(self.frame42)
        self.ENC_A_Label.configure(style="Heading4.TLabel", text='ENC A:')
        self.ENC_A_Label.grid(column=0, row=0, sticky="e")
        self.EXT_ENC_A_WIDGET = ttk.Label(self.frame42)
        self.EXT_ENC_A = tk.StringVar()
        self.EXT_ENC_A_WIDGET.configure(
            style="Normal.TLabel",
            textvariable=self.EXT_ENC_A)
        self.EXT_ENC_A_WIDGET.grid(column=1, padx="5 0", row=0, sticky="w")
        self.PTT_Label = ttk.Label(self.frame42)
        self.PTT_Label.configure(style="Heading4.TLabel", text='PTT:')
        self.PTT_Label.grid(column=0, row=1, sticky="e")
        self.EXT_PTT_WIDGET = ttk.Label(self.frame42)
        self.EXT_PTT = tk.StringVar()
        self.EXT_PTT_WIDGET.configure(
            style="Normal.TLabel",
            textvariable=self.EXT_PTT)
        self.EXT_PTT_WIDGET.grid(column=1, padx="5 0", row=1, sticky="w")
        self.EXT_LCD_PIN_RS_Label = ttk.Label(self.frame42)
        self.EXT_LCD_PIN_RS_Label.configure(
            style="Heading4.TLabel", text='LCD RS:')
        self.EXT_LCD_PIN_RS_Label.grid(column=0, row=2, sticky="e")
        self.EXT_LCD_PIN_RS_WIDGET = ttk.Label(self.frame42)
        self.EXT_LCD_PIN_RS = tk.StringVar()
        self.EXT_LCD_PIN_RS_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_LCD_PIN_RS)
        self.EXT_LCD_PIN_RS_WIDGET.grid(
            column=1, padx="5 0", row=2, sticky="w")
        self.EXT_LCD_PIN_D5_Label = ttk.Label(self.frame42)
        self.EXT_LCD_PIN_D5_Label.configure(
            style="Heading4.TLabel", text='LCD D5:')
        self.EXT_LCD_PIN_D5_Label.grid(column=0, row=3, sticky="e")
        self.EXT_LCD_PIN_D5_WIDGET = ttk.Label(self.frame42)
        self.EXT_LCD_PIN_D5 = tk.StringVar()
        self.EXT_LCD_PIN_D5_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_LCD_PIN_D5)
        self.EXT_LCD_PIN_D5_WIDGET.grid(
            column=1, padx="5 0", row=3, sticky="w")
        self.EXT_SOFTWARESERIAL_RX_PIN_Label = ttk.Label(self.frame42)
        self.EXT_SOFTWARESERIAL_RX_PIN_Label.configure(
            style="Heading4.TLabel", text='SW Serial RX:')
        self.EXT_SOFTWARESERIAL_RX_PIN_Label.grid(column=0, row=4, sticky="e")
        self.EXT_SOFTWARESERIAL_RX_PIN_WIDGET = ttk.Label(self.frame42)
        self.EXT_SOFTWARESERIAL_RX_PIN = tk.StringVar()
        self.EXT_SOFTWARESERIAL_RX_PIN_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_SOFTWARESERIAL_RX_PIN)
        self.EXT_SOFTWARESERIAL_RX_PIN_WIDGET.grid(
            column=1, padx="5 0", row=4, sticky="w")
        self.frame42.grid(column=0, row=0, sticky="n")
        self.frame44 = ttk.Frame(self.Pins_Content_Frame)
        self.frame44.configure(height=200, width=200)
        self.ENC_B_Label = ttk.Label(self.frame44)
        self.ENC_B_Label.configure(
            justify="left",
            style="Heading4.TLabel",
            text='ENC B:')
        self.ENC_B_Label.grid(column=0, row=0, sticky="e")
        self.EXT_ENC_B_WIDGET = ttk.Label(self.frame44)
        self.EXT_ENC_B = tk.StringVar()
        self.EXT_ENC_B_WIDGET.configure(
            style="Normal.TLabel",
            textvariable=self.EXT_ENC_B)
        self.EXT_ENC_B_WIDGET.grid(column=1, padx="5 0", row=0, sticky="w")
        self.EXT_ANALOG_KEYER_Label = ttk.Label(self.frame44)
        self.EXT_ANALOG_KEYER_Label.configure(
            justify="left", style="Heading4.TLabel", text='CW Keyer:')
        self.EXT_ANALOG_KEYER_Label.grid(column=0, row=1, sticky="e")
        self.EXT_ANALOG_KEYER_WIDGET = ttk.Label(self.frame44)
        self.EXT_ANALOG_KEYER = tk.StringVar()
        self.EXT_ANALOG_KEYER_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_ANALOG_KEYER)
        self.EXT_ANALOG_KEYER_WIDGET.grid(
            column=1, padx="5 0", row=1, sticky="w")
        self.EXT_LCD_PIN_EN_Label = ttk.Label(self.frame44)
        self.EXT_LCD_PIN_EN_Label.configure(
            justify="left", style="Heading4.TLabel", text='LCD EN:')
        self.EXT_LCD_PIN_EN_Label.grid(column=0, row=2, sticky="e")
        self.EXT_LCD_PIN_EN_WIDGET = ttk.Label(self.frame44)
        self.EXT_LCD_PIN_EN = tk.StringVar()
        self.EXT_LCD_PIN_EN_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_LCD_PIN_EN)
        self.EXT_LCD_PIN_EN_WIDGET.grid(
            column=1, padx="5 0", row=2, sticky="w")
        self.EXT_LCD_PIN_D6_Label = ttk.Label(self.frame44)
        self.EXT_LCD_PIN_D6_Label.configure(
            justify="left", style="Heading4.TLabel", text='LCD D6:')
        self.EXT_LCD_PIN_D6_Label.grid(column=0, row=3, sticky="e")
        self.EXT_LCD_PIN_D6_WIDGET = ttk.Label(self.frame44)
        self.EXT_LCD_PIN_D6 = tk.StringVar()
        self.EXT_LCD_PIN_D6_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_LCD_PIN_D6)
        self.EXT_LCD_PIN_D6_WIDGET.grid(
            column=1, padx="5 0", row=3, sticky="w")
        self.EXT_SOFTWARESERIAL_TX_PIN_Label = ttk.Label(self.frame44)
        self.EXT_SOFTWARESERIAL_TX_PIN_Label.configure(
            justify="left", style="Heading4.TLabel", text='SW Serial TX:')
        self.EXT_SOFTWARESERIAL_TX_PIN_Label.grid(column=0, row=4, sticky="e")
        self.EXT_SOFTWARESERIAL_TX_PIN_WIDGET = ttk.Label(self.frame44)
        self.EXT_SOFTWARESERIAL_TX_PIN = tk.StringVar()
        self.EXT_SOFTWARESERIAL_TX_PIN_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_SOFTWARESERIAL_TX_PIN)
        self.EXT_SOFTWARESERIAL_TX_PIN_WIDGET.grid(
            column=1, padx="5 0", row=4, sticky="w")
        self.frame44.grid(column=1, padx="100 0", row=0, sticky="n")
        self.frame52 = ttk.Frame(self.Pins_Content_Frame)
        self.frame52.configure(height=200, width=200)
        self.EXT_FBUTTON_Label = ttk.Label(self.frame52)
        self.EXT_FBUTTON_Label.configure(
            justify="left", style="Heading4.TLabel", text='ENC SW:')
        self.EXT_FBUTTON_Label.grid(column=0, row=0, sticky="e")
        self.EXT_FBUTTON_WIDGET = ttk.Label(self.frame52)
        self.EXT_FBUTTON = tk.StringVar()
        self.EXT_FBUTTON_WIDGET.configure(
            style="Normal.TLabel",
            textvariable=self.EXT_FBUTTON)
        self.EXT_FBUTTON_WIDGET.grid(column=1, padx="5 0", row=0, sticky="w")
        self.EXT_ANALOG_SMETER_Label = ttk.Label(self.frame52)
        self.EXT_ANALOG_SMETER_Label.configure(
            justify="left", style="Heading4.TLabel", text='S-Meter:')
        self.EXT_ANALOG_SMETER_Label.grid(column=0, row=1, sticky="e")
        self.EXT_ANALOG_SMETER_WIDGET = ttk.Label(self.frame52)
        self.EXT_ANALOG_SMETER = tk.StringVar()
        self.EXT_ANALOG_SMETER_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_ANALOG_SMETER)
        self.EXT_ANALOG_SMETER_WIDGET.grid(
            column=1, padx="5 0", row=1, sticky="w")
        self.EXT_LCD_PIN_D4_Label = ttk.Label(self.frame52)
        self.EXT_LCD_PIN_D4_Label.configure(
            justify="left", style="Heading4.TLabel", text='LCD D4:')
        self.EXT_LCD_PIN_D4_Label.grid(column=0, row=2, sticky="e")
        self.EXT_LCD_PIN_D4_WIDGET = ttk.Label(self.frame52)
        self.EXT_LCD_PIN_D4 = tk.StringVar()
        self.EXT_LCD_PIN_D4_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_LCD_PIN_D4)
        self.EXT_LCD_PIN_D4_WIDGET.grid(
            column=1, padx="5 0", row=2, sticky="w")
        self.EXT_LCD_PIN_D7_Label = ttk.Label(self.frame52)
        self.EXT_LCD_PIN_D7_Label.configure(
            justify="left", style="Heading4.TLabel", text='LCD D7:')
        self.EXT_LCD_PIN_D7_Label.grid(column=0, row=3, sticky="e")
        self.EXT_LCD_PIN_D7_WIDGET = ttk.Label(self.frame52)
        self.EXT_LCD_PIN_D7 = tk.StringVar()
        self.EXT_LCD_PIN_D7_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.EXT_LCD_PIN_D7)
        self.EXT_LCD_PIN_D7_WIDGET.grid(
            column=1, padx="5 0", row=3, sticky="w")
        self.frame52.grid(column=2, padx="100 0", row=0, sticky="n")
        self.Pins_Content_Frame.pack(
            expand="true", fill="x", padx=140, side="top")
        self.System_Info_Pins.pack(
            anchor="w",
            expand="true",
            fill="x",
            pady="20 0",
            side="top")
        self.System_Info_VFO_Frame = ttk.Frame(self.frame27)
        self.sytem_Infor_Last_Saved_Freq_Label = ttk.Label(
            self.System_Info_VFO_Frame)
        self.sytem_Infor_Last_Saved_Freq_Label.configure(
            style="Heading3.TLabel", text='Last Used Frequencies')
        self.sytem_Infor_Last_Saved_Freq_Label.grid(
            column=0, columnspan=2, row=3, sticky="ew")
        self.label2 = ttk.Label(self.System_Info_VFO_Frame)
        self.label2.configure(style="Heading4.TLabel", text='Current')
        self.label2.grid(column=2, columnspan=3, padx="0 25", row=4)
        self.System_Info_System_Information_Last_Saved_VFO_Frequency_Label = ttk.Label(
            self.System_Info_VFO_Frame)
        self.System_Info_System_Information_Last_Saved_VFO_Frequency_Label.configure(
            style="Heading4.TLabel", text='Freq(HZ)')
        self.System_Info_System_Information_Last_Saved_VFO_Frequency_Label.grid(
            column=2, padx="0 40", row=5, sticky="e")
        self.System_Info_System_Information_Last_Saved_VFO_Mode_Label = ttk.Label(
            self.System_Info_VFO_Frame)
        self.System_Info_System_Information_Last_Saved_VFO_Mode_Label.configure(
            style="Heading4.TLabel", text='Mode')
        self.System_Info_System_Information_Last_Saved_VFO_Mode_Label.grid(
            column=4, padx="5 30", row=5, sticky="w")
        self.System_Info_System_Information_Last_Saved_VFO_VFO_A_Label = ttk.Label(
            self.System_Info_VFO_Frame)
        self.System_Info_System_Information_Last_Saved_VFO_VFO_A_Label.configure(
            style="Heading4.TLabel", text='VFO A:')
        self.System_Info_System_Information_Last_Saved_VFO_VFO_A_Label.grid(
            column=1, padx="0 40", pady="0 3", row=6, sticky="e")
        self.VFO_A_WIDGET = ttk.Label(self.System_Info_VFO_Frame)
        self.VFO_A = tk.StringVar()
        self.VFO_A_WIDGET.configure(
            style="Normal.TLabel",
            textvariable=self.VFO_A)
        self.VFO_A_WIDGET.grid(
            column=2,
            padx="0 40",
            pady="0 3",
            row=6,
            sticky="e")
        self.VFO_A_MODE_WIDGET = ttk.Label(self.System_Info_VFO_Frame)
        self.VFO_A_MODE = tk.StringVar()
        self.VFO_A_MODE_WIDGET.configure(
            style="Normal.TLabel",
            textvariable=self.VFO_A_MODE)
        self.VFO_A_MODE_WIDGET.grid(
            column=4,
            padx="5 30",
            pady="0 3",
            row=6,
            sticky="w")
        self.System_Info_System_Information_Last_Saved_VFO_VFO_B_Label = ttk.Label(
            self.System_Info_VFO_Frame)
        self.System_Info_System_Information_Last_Saved_VFO_VFO_B_Label.configure(
            style="Heading4.TLabel", text='VFO B:')
        self.System_Info_System_Information_Last_Saved_VFO_VFO_B_Label.grid(
            column=1, padx="0 40", pady="0 3", row=7, sticky="e")
        self.VFO_B_WIDGET = ttk.Label(self.System_Info_VFO_Frame)
        self.VFO_B = tk.StringVar()
        self.VFO_B_WIDGET.configure(
            style="Normal.TLabel",
            textvariable=self.VFO_B)
        self.VFO_B_WIDGET.grid(
            column=2,
            padx="0 40",
            pady="0 3",
            row=7,
            sticky="e")
        self.VFO_B_MODE_WIDGET = ttk.Label(self.System_Info_VFO_Frame)
        self.VFO_B_MODE = tk.StringVar()
        self.VFO_B_MODE_WIDGET.configure(
            style="Normal.TLabel",
            textvariable=self.VFO_B_MODE)
        self.VFO_B_MODE_WIDGET.grid(
            column=4,
            padx="5 30",
            pady="0 3",
            row=7,
            sticky="w")
        self.HAM_BAND_FREQS1_Label = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS1_Label.configure(
            style="Heading4.TLabel", text='Band 1:')
        self.HAM_BAND_FREQS1_Label.grid(
            column=1, padx="0 40", pady="15 3", row=8, sticky="e")
        self.HAM_BAND_FREQS1_WIDGET = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS1 = tk.StringVar()
        self.HAM_BAND_FREQS1_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS1)
        self.HAM_BAND_FREQS1_WIDGET.grid(
            column=2, padx="0 40", pady="15 3", row=8, sticky="e")
        self.HAM_BAND_FREQS1_MODE_WIDGET = ttk.Label(
            self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS1_MODE = tk.StringVar()
        self.HAM_BAND_FREQS1_MODE_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS1_MODE)
        self.HAM_BAND_FREQS1_MODE_WIDGET.grid(
            column=4, padx="5 30", pady="15 3", row=8, sticky="w")
        self.HAM_BAND_FREQS2_Label = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS2_Label.configure(
            style="Heading4.TLabel", text='Band 2:')
        self.HAM_BAND_FREQS2_Label.grid(
            column=1, padx="0 40", pady="0 3", row=9, sticky="e")
        self.HAM_BAND_FREQ2_WIDGET = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS2 = tk.StringVar()
        self.HAM_BAND_FREQ2_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS2)
        self.HAM_BAND_FREQ2_WIDGET.grid(
            column=2, padx="0 40", row=9, sticky="e")
        self.HAM_BAND_FREQS2_MODE_WIDGET = ttk.Label(
            self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS2_MODE = tk.StringVar()
        self.HAM_BAND_FREQS2_MODE_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS2_MODE)
        self.HAM_BAND_FREQS2_MODE_WIDGET.grid(
            column=4, padx="5 30", row=9, sticky="w")
        self.HAM_BAND_FREQS3_Label = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS3_Label.configure(
            style="Heading4.TLabel", text='Band 3:')
        self.HAM_BAND_FREQS3_Label.grid(
            column=1, padx="0 40", pady="0 3", row=10, sticky="e")
        self.HAM_BAND_FREQS3_WIDGET = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS3 = tk.StringVar()
        self.HAM_BAND_FREQS3_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS3)
        self.HAM_BAND_FREQS3_WIDGET.grid(
            column=2, padx="0 40", row=10, sticky="e")
        self.HAM_BAND_FREQS3_MODE_WIDGET = ttk.Label(
            self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS3_MODE = tk.StringVar()
        self.HAM_BAND_FREQS3_MODE_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS3_MODE)
        self.HAM_BAND_FREQS3_MODE_WIDGET.grid(
            column=4, padx="5 30", row=10, sticky="w")
        self.HAM_BAND_FREQS4_Label = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS4_Label.configure(
            style="Heading4.TLabel", text='Band 4:')
        self.HAM_BAND_FREQS4_Label.grid(
            column=1, padx="0 40", pady="0 3", row=11, sticky="e")
        self.HAM_BAND_FREQS4_WIDGET = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS4 = tk.StringVar()
        self.HAM_BAND_FREQS4_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS4)
        self.HAM_BAND_FREQS4_WIDGET.grid(
            column=2, padx="0 40", row=11, sticky="e")
        self.HAM_BAND_FREQS4_MODE_WIDGET = ttk.Label(
            self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS4_MODE = tk.StringVar()
        self.HAM_BAND_FREQS4_MODE_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS4_MODE)
        self.HAM_BAND_FREQS4_MODE_WIDGET.grid(
            column=4, padx="5 30", row=11, sticky="w")
        self.HAM_BAND_FREQS5_Label = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS5_Label.configure(
            style="Heading4.TLabel", text='Band 5:')
        self.HAM_BAND_FREQS5_Label.grid(
            column=1, padx="0 40", pady="0 3", row=12, sticky="e")
        self.HAM_BAND_FREQS5_WIDGET = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS5 = tk.StringVar()
        self.HAM_BAND_FREQS5_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS5)
        self.HAM_BAND_FREQS5_WIDGET.grid(
            column=2, padx="0 40", row=12, sticky="e")
        self.HAM_BAND_FREQS5_MODE_WIDGET = ttk.Label(
            self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS5_MODE = tk.StringVar()
        self.HAM_BAND_FREQS5_MODE_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS5_MODE)
        self.HAM_BAND_FREQS5_MODE_WIDGET.grid(
            column=4, padx="5 30", row=12, sticky="w")
        self.HAM_BAND_FREQS6_Label = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS6_Label.configure(
            style="Heading4.TLabel", text='Band 6:')
        self.HAM_BAND_FREQS6_Label.grid(
            column=1, padx="0 40", pady="0 3", row=13, sticky="e")
        self.HAM_BAND_FREQS6_WIDGET = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS6 = tk.StringVar()
        self.HAM_BAND_FREQS6_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS6)
        self.HAM_BAND_FREQS6_WIDGET.grid(
            column=2, padx="0 40", row=13, sticky="e")
        self.HAM_BAND_FREQS6_MODE_WIDGET = ttk.Label(
            self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS6_MODE = tk.StringVar()
        self.HAM_BAND_FREQS6_MODE_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS6_MODE)
        self.HAM_BAND_FREQS6_MODE_WIDGET.grid(
            column=4, padx="5 30", row=13, sticky="w")
        self.HAM_BAND_FREQS7_Label = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS7_Label.configure(
            style="Heading4.TLabel", text='Band 7:')
        self.HAM_BAND_FREQS7_Label.grid(
            column=1, padx="0 40", pady="0 3", row=14, sticky="e")
        self.HAM_BAND_FREQS7_WIDGET = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS7 = tk.StringVar()
        self.HAM_BAND_FREQS7_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS7)
        self.HAM_BAND_FREQS7_WIDGET.grid(
            column=2, padx="0 40", row=14, sticky="e")
        self.HAM_BAND_FREQS7_MODE_WIDGET = ttk.Label(
            self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS7_MODE = tk.StringVar()
        self.HAM_BAND_FREQS7_MODE_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS7_MODE)
        self.HAM_BAND_FREQS7_MODE_WIDGET.grid(
            column=4, padx="5 30", row=14, sticky="w")
        self.HAM_BAND_FREQS8_Label = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS8_Label.configure(
            style="Heading4.TLabel", text='Band 8:')
        self.HAM_BAND_FREQS8_Label.grid(
            column=1, padx="0 40", pady="0 3", row=15, sticky="e")
        self.HAM_BAND_FREQS8_WIDGET = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS8 = tk.StringVar()
        self.HAM_BAND_FREQS8_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS8)
        self.HAM_BAND_FREQS8_WIDGET.grid(
            column=2, padx="0 40", row=15, sticky="e")
        self.HAM_BAND_FREQS8_MODE_WIDGET = ttk.Label(
            self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS8_MODE = tk.StringVar()
        self.HAM_BAND_FREQS8_MODE_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS8_MODE)
        self.HAM_BAND_FREQS8_MODE_WIDGET.grid(
            column=4, padx="5 30", row=15, sticky="w")
        self.HAM_BAND_FREQS9_Label = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS9_Label.configure(
            style="Heading4.TLabel", text='Band 9:')
        self.HAM_BAND_FREQS9_Label.grid(
            column=1, padx="0 40", pady="0 3", row=16, sticky="e")
        self.HAM_BAND_FREQS9_WIDGET = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS9 = tk.StringVar()
        self.HAM_BAND_FREQS9_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS9)
        self.HAM_BAND_FREQS9_WIDGET.grid(
            column=2, padx="0 40", row=16, sticky="e")
        self.HAM_BAND_FREQS9_MODE_WIDGET = ttk.Label(
            self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS9_MODE = tk.StringVar()
        self.HAM_BAND_FREQS9_MODE_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS9_MODE)
        self.HAM_BAND_FREQS9_MODE_WIDGET.grid(
            column=4, padx="5 30", row=16, sticky="w")
        self.HAM_BAND_FREQS10_Label = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS10_Label.configure(
            style="Heading4.TLabel", text='Band 10:')
        self.HAM_BAND_FREQS10_Label.grid(
            column=1, padx="0 40", pady="0 3", row=17, sticky="e")
        self.HAM_BAND_FREQS10_WIDGET = ttk.Label(self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS10 = tk.StringVar()
        self.HAM_BAND_FREQS10_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS10)
        self.HAM_BAND_FREQS10_WIDGET.grid(
            column=2, padx="0 40", row=17, sticky="e")
        self.HAM_BAND_FREQS10_MODE_WIDGET = ttk.Label(
            self.System_Info_VFO_Frame)
        self.HAM_BAND_FREQS10_MODE = tk.StringVar()
        self.HAM_BAND_FREQS10_MODE_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.HAM_BAND_FREQS10_MODE)
        self.HAM_BAND_FREQS10_MODE_WIDGET.grid(
            column=4, padx="5 30", row=17, sticky="w")
        self.System_Info_VFO_Frame.pack(anchor="w", pady="20 0", side="top")
        self.System_Info_VFO_Frame.grid_anchor("nw")
        self.frame27.pack(anchor="w", padx=20, side="top")
        self.frame26.pack(anchor="w", padx=5, pady=5, side="top")
        self.SYSTEM_INFO_HIDDEN_Frame = ttk.Frame(
            self.System_Info_SF.innerframe)
        self.SYSTEM_INFO_HIDDEN_Frame.configure(height=200, width=200)
        self.FIRMWARE_ID_ADDR1_WIDGET = ttk.Label(
            self.SYSTEM_INFO_HIDDEN_Frame)
        self.FIRMWARE_ID_ADDR1 = tk.StringVar()
        self.FIRMWARE_ID_ADDR1_WIDGET.configure(
            textvariable=self.FIRMWARE_ID_ADDR1)
        self.FIRMWARE_ID_ADDR1_WIDGET.pack(side="top")
        self.FIRMWARE_ID_ADDR2_WIDGET = ttk.Label(
            self.SYSTEM_INFO_HIDDEN_Frame)
        self.FIRMWARE_ID_ADDR2 = tk.StringVar()
        self.FIRMWARE_ID_ADDR2_WIDGET.configure(
            relief="flat", textvariable=self.FIRMWARE_ID_ADDR2)
        self.FIRMWARE_ID_ADDR2_WIDGET.pack(side="top")
        self.FIRMWARE_ID_ADDR3_WIDGET = ttk.Label(
            self.SYSTEM_INFO_HIDDEN_Frame)
        self.FIRMWARE_ID_ADDR3 = tk.StringVar()
        self.FIRMWARE_ID_ADDR3_WIDGET.configure(
            textvariable=self.FIRMWARE_ID_ADDR3)
        self.FIRMWARE_ID_ADDR3_WIDGET.pack(side="top")
        self.FACTORY_VALUES_VFO_A_WIDGET = ttk.Label(
            self.SYSTEM_INFO_HIDDEN_Frame)
        self.FACTORY_VALUES_VFO_A = tk.StringVar()
        self.FACTORY_VALUES_VFO_A_WIDGET.configure(
            textvariable=self.FACTORY_VALUES_VFO_A)
        self.FACTORY_VALUES_VFO_A_WIDGET.pack(side="top")
        self.FACTORY_VALUES_VFO_B_WIDGET = ttk.Label(
            self.SYSTEM_INFO_HIDDEN_Frame)
        self.FACTORY_VALUES_VFO_B = tk.StringVar()
        self.FACTORY_VALUES_VFO_B_WIDGET.configure(
            textvariable=self.FACTORY_VALUES_VFO_B)
        self.FACTORY_VALUES_VFO_B_WIDGET.pack(side="top")
        self.SYSTEM_INFO_HIDDEN_Frame.pack(side="top")
        self.System_Info_SF.pack(expand="true", fill="both", side="top")
        self.settingsNotebook.add(self.System_Info_SF, text='System Info')
        self.settingsNotebook.pack(
            anchor="w",
            expand="true",
            fill="both",
            padx=5,
            pady="15 25",
            side="top")
        self.configure(height=600, padding=5, relief="groove", width=600)
        self.pack(expand="true", fill="both", side="top")

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

    def validate_USER_CALLSIGN(self, p_entry_value, v_condition):
        pass

    def Tuning_Steps_Set_Common(self):
        pass

    def validate_TUNING_STEP1(self, p_entry_value, v_condition):
        pass

    def validate_TUNING_STEP2(self, p_entry_value, v_condition):
        pass

    def validate_TUNING_STEP3(self, p_entry_value, v_condition):
        pass

    def validate_TUNING_STEP4(self, p_entry_value, v_condition):
        pass

    def validate_TUNING_STEP5(self, p_entry_value, v_condition):
        pass

    def validate_CW_SIDETONE(self, p_entry_value, v_condition):
        pass

    def validate_CW_SPEED_WPM(self, p_entry_value, v_condition):
        pass

    def validate_CW_START_MS(self, p_entry_value, v_condition):
        pass

    def validate_CW_DELAY_MS(self, p_entry_value, v_condition):
        pass

    def toggle_IF1_Calibration_Frame(self):
        pass

    def validate_IF_SHIFTVALUE(self, p_entry_value, v_condition):
        pass

    def validate_QSO_CALLSIGN(self, p_entry_value, v_condition):
        pass

    def validate_CW_Message_Change(
            self, p_entry_value, v_condition, w_entry_name):
        pass

    def CW_Auto_Msg_Cleanup_CB(self):
        pass

    def validate_HAM_BAND_COUNT(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE1_START(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE1_END(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE2_START(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE2_END(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE3_START(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE3_END(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE4_START(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE4_END(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE5_START(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE5_END(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE6_START(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE6_END(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE7_START(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE7_END(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE8_START(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE8_END(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE9_START(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE9_END(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE10_START(self, p_entry_value, v_condition):
        pass

    def validate_HAM_BAND_RANGE10_END(self, p_entry_value, v_condition):
        pass

    def autoInputRegion1(self):
        pass

    def autoInputRegion2(self):
        pass

    def autoInputRegion3(self):
        pass

    def validate_CHANNEL_FREQ1_NAME(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ1(self, p_entry_value, v_condition):
        pass

    def clearErrorMsgPersistFlag(self):
        pass

    def validate_CHANNEL_FREQ2_NAME(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ2(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ3_NAME(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ3(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ4_NAME(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ4(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ5_NAME(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ5(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ6_NAME(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ6(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ7_NAME(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ7(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ8_NAME(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ8(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ9_NAME(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ9(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ10_NAME(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ10(self, p_entry_value, v_condition):
        pass

    def toggleExtendedChannels(self):
        pass

    def validate_CHANNEL_FREQ11(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ12(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ13(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ14(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ15(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ16(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ17(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ18(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ19(self, p_entry_value, v_condition):
        pass

    def validate_CHANNEL_FREQ20(self, p_entry_value, v_condition):
        pass

    def validate_WSPR_MESSAGE1_NAME(self, p_entry_value, v_condition):
        pass

    def runWSPRMsg1Gen_CB(self):
        pass

    def validate_WSPR_MESSAGE2_NAME(self, p_entry_value, v_condition):
        pass

    def runWSPRMsg2Gen_CB(self):
        pass

    def validate_WSPR_MESSAGE3_NAME(self, p_entry_value, v_condition):
        pass

    def runWSPRMsg3Gen_CB(self):
        pass

    def validate_WSPR_MESSAGE4_NAME(self, p_entry_value, v_condition):
        pass

    def runWSPRMsg4Gen_CB(self):
        pass

    def runWSPR_Band1_Select_Button_CB(self):
        pass

    def runWSPR_Band2_Select_Button_CB(self):
        pass

    def runWSPR_Band3_Select_Button_CB(self):
        pass

    def validate_I2C_LCD_MASTER(self, p_entry_value, v_condition):
        pass

    def runI2CScanner(self):
        pass

    def validate_I2C_LCD_SECOND(self, p_entry_value, v_condition):
        pass

    def validate_SDR_FREQUENCY(self, p_entry_value, v_condition):
        pass

    def validate_EXTENDED_KEY1_START(self, p_entry_value, v_condition):
        pass

    def validate_EXTENDED_KEY1_END(self, p_entry_value, v_condition):
        pass

    def validate_EXTENDED_KEY2_START(self, p_entry_value, v_condition):
        pass

    def validate_EXTENDED_KEY2_END(self, p_entry_value, v_condition):
        pass

    def validate_EXTENDED_KEY3_START(self, p_entry_value, v_condition):
        pass

    def validate_EXTENDED_KEY3_END(self, p_entry_value, v_condition):
        pass

    def validate_EXTENDED_KEY4_START(self, p_entry_value, v_condition):
        pass

    def validate_EXTENDED_KEY4_END(self, p_entry_value, v_condition):
        pass

    def runADCScanner(self):
        pass

    def validate_EXTENDED_KEY5_START(self, p_entry_value, v_condition):
        pass

    def validate_EXTENDED_KEY5_END(self, p_entry_value, v_condition):
        pass

    def validate_EXTENDED_KEY6_START(self, p_entry_value, v_condition):
        pass

    def validate_EXTENDED_KEY6_END(self, p_entry_value, v_condition):
        pass

    def CUST_LPF_SELECTION_CB(self, option):
        pass

    def validate_CUST_LPF_FILTER1_ENDFREQ(self, p_entry_value, v_condition):
        pass

    def CUST_LPF_FILTER1_CONTROL_CB(self):
        pass

    def validate_CUST_LPF_FILTER2_ENDFREQ(self, p_entry_value, v_condition):
        pass

    def CUST_LPF_FILTER2_CONTROL_CB(self):
        pass

    def validate_CUST_LPF_FILTER3_ENDFREQ(self, p_entry_value, v_condition):
        pass

    def CUST_LPF_FILTER3_CONTROL_CB(self):
        pass

    def validate_CUST_LPF_FILTER4_ENDFREQ(self, p_entry_value, v_condition):
        pass

    def CUST_LPF_FILTER4_CONTROL_CB(self):
        pass

    def validate_CUST_LPF_FILTER5_ENDFREQ(self, p_entry_value, v_condition):
        pass

    def CUST_LPF_FILTER5_CONTROL_CB(self):
        pass

    def validate_CUST_LPF_FILTER6_ENDFREQ(self, p_entry_value, v_condition):
        pass

    def CUST_LPF_FILTER6_CONTROL_CB(self):
        pass

    def validate_CUST_LPF_FILTER7_ENDFREQ(self, p_entry_value, v_condition):
        pass

    def CUST_LPF_FILTER7_CONTROL_CB(self):
        pass

    def validate_IF1_CAL(self, p_entry_value, v_condition):
        pass

    def validate_MASTER_CAL(self, p_entry_value, v_condition):
        pass

    def Reset_Master_Cal_To_Factory(self):
        pass

    def Copy_Master_Cal_Over_Factory_Value(self):
        pass

    def validate_USB_CAL(self, p_entry_value, v_condition):
        pass

    def Reset_SSB_BFO_To_Factory(self):
        pass

    def Copy_SSB_BFO_Over_Factory_Value(self):
        pass

    def validate_CW_CAL(self, p_entry_value, v_condition):
        pass

    def Factory_Settings_Enable_CB(self):
        pass

    def validate_CW_ADC_ST_FROM(self, p_entry_value, v_condition):
        pass

    def validate_CW_ADC_ST_TO(self, p_entry_value, v_condition):
        pass

    def validate_CW_ADC_DOT_FROM(self, p_entry_value, v_condition):
        pass

    def validate_CW_ADC_DOT_TO(self, p_entry_value, v_condition):
        pass

    def validate_CW_ADC_DASH_FROM(self, p_entry_value, v_condition):
        pass

    def validate_CW_ADC_DASH_TO(self, p_entry_value, v_condition):
        pass

    def validate_CW_ADC_BOTH_FROM(self, p_entry_value, v_condition):
        pass

    def validate_CW_ADC_BOTH_TO(self, p_entry_value, v_condition):
        pass

    def load_Recommended_ADC_CW_Values(self):
        pass

    def SMeter_Input_CB(self):
        pass

    def validate_METER_LEVEL1(self, p_entry_value, v_condition):
        pass

    def validate_METER_LEVEL2(self, p_entry_value, v_condition):
        pass

    def validate_METER_LEVEL3(self, p_entry_value, v_condition):
        pass

    def validate_METER_LEVEL4(self, p_entry_value, v_condition):
        pass

    def validate_METER_LEVEL5(self, p_entry_value, v_condition):
        pass

    def validate_METER_LEVEL6(self, p_entry_value, v_condition):
        pass

    def validate_METER_LEVEL7(self, p_entry_value, v_condition):
        pass

    def validate_METER_LEVEL8(self, p_entry_value, v_condition):
        pass

    def runSmeterAssistant(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = SettingsnotebookWidget(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
