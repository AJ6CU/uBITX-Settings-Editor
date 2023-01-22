#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.scrolledframe import ScrolledFrame


class SettingsnotebookWidget(ttk.Frame):
    def __init__(self, master=None, **kw):
        super(SettingsnotebookWidget, self).__init__(master, **kw)
        self.settingsNotebook = ttk.Notebook(self)
        self.settingsNotebook.configure(height=800, width=800)
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
            pady="10 0",
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
            anchor="w", expand="true", fill="x", pady="20 0", side="top")
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
        self.label26 = ttk.Label(self.frame6)
        self.label26.grid(row=2)
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
            values='10 20 50 100 1000',
            width=5)
        self.TUNING_STEP_INDEX_VALUE_WIDGET.grid(column=1, row=0)
        self.TUNING_STEP_INDEX_WIDGET = ttk.Label(self.frame1)
        self.TUNING_STEP_INDEX = tk.StringVar()
        self.TUNING_STEP_INDEX_WIDGET.configure(
            textvariable=self.TUNING_STEP_INDEX)
        self.TUNING_STEP_INDEX_WIDGET.grid(column=0, row=1)
        self.frame1.pack(anchor="w", side="top")
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
            pady="10 0",
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
        __values = ['STRAIGHT', 'IAMBICA', 'IAMICAB']
        self.CW_KEY_TYPE_WIDGET = tk.OptionMenu(
            self.General_CW_Settings_Frame,
            self.CW_KEY_TYPE,
            *__values,
            command=None)
        self.CW_KEY_TYPE_WIDGET.grid(column=1, pady="0 10", row=0)
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
        self.General_CW_Settings_Frame.pack(padx="50 0", side="top")
        self.frame5 = ttk.Frame(self.General_CW_Frame)
        self.frame5.configure(height=200, width=200)
        self.separator3 = ttk.Separator(self.frame5)
        self.separator3.configure(orient="horizontal")
        self.separator3.pack(
            anchor="center",
            expand="true",
            fill="x",
            pady="10 0",
            side="top")
        self.frame5.pack(anchor="w", expand="true", fill="x", side="top")
        self.General_CW_Frame.pack(anchor="w", side="top")
        self.Operator_Channel_Frame = ttk.Frame(self.General_Frame)
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
            style="Normal.TEntry",
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
        self.checkbutton2 = ttk.Checkbutton(self.show_extended_channels_frame)
        self.toggleExtendedChannelsCheckBox = tk.StringVar()
        self.checkbutton2.configure(
            offvalue=0,
            onvalue=1,
            style="Checkbox4.TCheckbutton",
            text='Show Extended Channels',
            variable=self.toggleExtendedChannelsCheckBox)
        self.checkbutton2.pack(anchor="w", pady="10 0")
        self.checkbutton2.configure(command=self.toggleExtendedChannels)
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
        self.label3.pack(anchor="w", padx=5, pady="15 25")
        self.CW_Autokeyer_Titlle_Frame.pack(
            anchor="center", fill="x", side="top")
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
        self.CW_Autokeyer_Callsigns_Frame.pack(
            anchor="w", padx="50 0", side="top")
        self.CW_Autokeyer_Callsign_Frame.pack(anchor="w", padx=20, side="top")
        self.Autokeyer_Frame.pack(
            anchor="center",
            expand="true",
            fill="both",
            padx=5,
            pady=5,
            side="top")
        self.Autokeyer_SF.pack(side="top")
        self.settingsNotebook.add(self.Autokeyer_SF, text='CW Autokeyer')
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
        self.region1 = ttk.Button(self.frame58)
        self.region1.configure(style="Button4.TButton", text='Region 1')
        self.region1.grid(column=1, padx=5, row=1)
        self.region1.configure(command=self.autoInputRegion1)
        self.label136 = ttk.Label(self.frame58)
        self.label136.configure(
            style="Heading3.TLabel",
            text='Auto Input Bands For:')
        self.label136.grid(column=0, ipadx=5, padx=5, row=1)
        self.region2 = ttk.Button(self.frame58)
        self.region2.configure(style="Button4.TButton", text='Region 2')
        self.region2.grid(column=2, padx=5, row=1)
        self.region2.configure(command=self.autoInputRegion2)
        self.region3 = ttk.Button(self.frame58)
        self.region3.configure(style="Button4.TButton", text='Region 3')
        self.region3.grid(column=3, padx=5, row=1)
        self.region3.configure(command=self.autoInputRegion3)
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
        self.HW_ADJ_SF = ScrolledFrame(
            self.settingsNotebook, scrolltype="both")
        self.HW_ADJ_SF.configure(usemousewheel=True)
        self.HW_ADJ_Frame = ttk.Frame(self.HW_ADJ_SF.innerframe)
        self.frame17 = ttk.Frame(self.HW_ADJ_Frame)
        self.frame17.configure(height=200, width=200)
        self.label5 = ttk.Label(self.frame17)
        self.label5.configure(
            justify="center",
            style="Heading2.TLabel",
            text='Hardware Advanced Settings')
        self.label5.pack(padx=5, pady="15 25")
        self.frame17.pack(
            anchor="w",
            expand="false",
            padx=5,
            pady="15 25",
            side="top")
        self.frame18 = ttk.Frame(self.HW_ADJ_Frame)
        self.frame18.configure(height=200, width=200)
        self.frame18.pack(anchor="w", padx=20, side="top")
        self.HW_ADJ_Frame.pack(
            anchor="w",
            expand="true",
            fill="both",
            padx=5,
            pady=5,
            side="top")
        self.HW_ADJ_SF.pack(expand="true", fill="both", side="top")
        self.settingsNotebook.add(self.HW_ADJ_SF, text='HW ADV')
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
            column=5, row=3, sticky="n")
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
        self.img_redarrowpointingleft59x36 = tk.PhotoImage(
            file="./images/red-arrow-pointing-left59x36.png")
        self.MASTER_CAL_COPY_BUTTON.configure(
            image=self.img_redarrowpointingleft59x36,
            style="Normal.TButton",
            width=10)
        self.MASTER_CAL_COPY_BUTTON.grid(
            column=4, padx="0 5", pady=2, row=4, sticky="w")
        self.MASTER_CAL_COPY_BUTTON.configure(
            command=self.Reset_Master_Cal_To_Factory)
        self.button2 = ttk.Button(self.Radio_Calibration_Frame)
        self.img_redarrowpointingright59x36 = tk.PhotoImage(
            file="./images/red-arrow-pointing-right59x36.png")
        self.button2.configure(
            image=self.img_redarrowpointingright59x36,
            style="Normal.TButton",
            width=10)
        self.button2.grid(column=5, padx="0 5", pady=2, row=4, sticky="w")
        self.button2.configure(command=self.Copy_Master_Cal_Over_Factory_Value)
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
        self.USB_CAL_COPY_BUTTON.configure(
            image=self.img_redarrowpointingleft59x36,
            style="Normal.TButton",
            width=10)
        self.USB_CAL_COPY_BUTTON.grid(column=4, pady=2, row=5, sticky="w")
        self.USB_CAL_COPY_BUTTON.configure(
            command=self.Reset_SSB_BFO_To_Factory)
        self.button5 = ttk.Button(self.Radio_Calibration_Frame)
        self.button5.configure(
            image=self.img_redarrowpointingright59x36,
            style="Normal.TButton",
            width=10)
        self.button5.grid(column=5, padx="0 5", pady=2, row=5, sticky="w")
        self.button5.configure(command=self.Copy_SSB_BFO_Over_Factory_Value)
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
        self.button4 = ttk.Button(self.frame3)
        self.button4.configure(
            style="Button4.TButton",
            text='Load Recommend ADC Settings')
        self.button4.grid(column=1, padx=40, row=0, sticky="e")
        self.button4.configure(command=self.load_Recommended_ADC_CW_Values)
        self.button1 = ttk.Button(self.frame3)
        self.button1.configure(style="Button4.TButton", text='ADC Scanner')
        self.button1.grid(column=0, row=0)
        self.button1.configure(command=self.runADCScanner)
        self.frame3.grid(column=1, columnspan=5, pady=15, row=12, sticky="ew")
        self.CW_Calibration_Frame.pack(fill="x", side="top")
        self.CW_Calibration_Frame.grid_anchor("nw")
        self.S_Meter_Frame = ttk.Frame(self.frame21)
        self.label1 = ttk.Label(self.S_Meter_Frame)
        self.label1.configure(style="Heading3.TLabel", text='S-Meter')
        self.label1.grid(column=0, padx=0, pady="20 0", row=1, sticky="ew")
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
        self.frame9 = ttk.Frame(self.S_Meter_Frame)
        self.frame9.configure(height=200, width=200)
        self.label29 = ttk.Label(self.frame9)
        self.label29.configure(
            justify="left",
            relief="flat",
            style="Heading4.TLabel",
            text='1')
        self.label29.grid(column=1, padx="8 0", row=2)
        self.S_METER_LEVEL1_WIDGET = ttk.Entry(self.frame9)
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
                self.validate__METER_LEVEL1), "%P", "%V")
        self.S_METER_LEVEL1_WIDGET.configure(validatecommand=_validatecmd)
        self.label15 = ttk.Label(self.frame9)
        self.label15.configure(
            justify="right",
            style="Heading4.TLabel",
            takefocus=False,
            text='ADC Value (0-1023)')
        self.label15.grid(column=0, padx="15 0", row=3, sticky="w")
        self.S_METER_LEVEL2_WIDGET = ttk.Entry(self.frame9)
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
                self.validate__METER_LEVEL2), "%P", "%V")
        self.S_METER_LEVEL2_WIDGET.configure(validatecommand=_validatecmd)
        self.S_METER_LEVEL4_WIDGET = ttk.Entry(self.frame9)
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
                self.validate__METER_LEVEL4), "%P", "%V")
        self.S_METER_LEVEL4_WIDGET.configure(validatecommand=_validatecmd)
        self.S_METER_LEVEL3_WIDGET = ttk.Entry(self.frame9)
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
                self.validate__METER_LEVEL3), "%P", "%V")
        self.S_METER_LEVEL3_WIDGET.configure(validatecommand=_validatecmd)
        self.S_METER_LEVEL5_WIDGET = ttk.Entry(self.frame9)
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
                self.validate__METER_LEVEL5), "%P", "%V")
        self.S_METER_LEVEL5_WIDGET.configure(validatecommand=_validatecmd)
        self.S_METER_LEVEL6_WIDGET = ttk.Entry(self.frame9)
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
                self.validate__METER_LEVEL6), "%P", "%V")
        self.S_METER_LEVEL6_WIDGET.configure(validatecommand=_validatecmd)
        self.S_METER_LEVEL7_WIDGET = ttk.Entry(self.frame9)
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
                self.validate__METER_LEVEL7), "%P", "%V")
        self.S_METER_LEVEL7_WIDGET.configure(validatecommand=_validatecmd)
        self.S_METER_LEVEL8_WIDGET = ttk.Entry(self.frame9)
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
                self.validate__METER_LEVEL8), "%P", "%V")
        self.S_METER_LEVEL8_WIDGET.configure(validatecommand=_validatecmd)
        self.label33 = ttk.Label(self.frame9)
        self.label33.configure(
            justify="left",
            relief="flat",
            style="Heading4.TLabel",
            text='2')
        self.label33.grid(column=2, padx="7 0", row=2)
        self.label35 = ttk.Label(self.frame9)
        self.label35.configure(
            justify="left",
            relief="flat",
            style="Heading4.TLabel",
            text='3')
        self.label35.grid(column=3, padx="7 0", row=2)
        self.label36 = ttk.Label(self.frame9)
        self.label36.configure(
            justify="left",
            relief="flat",
            style="Heading4.TLabel",
            text='4')
        self.label36.grid(column=4, padx="7 0", row=2)
        self.label38 = ttk.Label(self.frame9)
        self.label38.configure(
            justify="left",
            relief="flat",
            style="Heading4.TLabel",
            text='5')
        self.label38.grid(column=5, padx="7 0", row=2)
        self.label39 = ttk.Label(self.frame9)
        self.label39.configure(
            justify="left",
            relief="flat",
            style="Heading4.TLabel",
            text='6')
        self.label39.grid(column=6, padx="7 0", row=2)
        self.label41 = ttk.Label(self.frame9)
        self.label41.configure(
            justify="left",
            relief="flat",
            style="Heading4.TLabel",
            text='7')
        self.label41.grid(column=7, padx="7 0", row=2)
        self.label42 = ttk.Label(self.frame9)
        self.label42.configure(
            justify="left",
            relief="flat",
            style="Heading4.TLabel",
            text='8')
        self.label42.grid(column=8, padx="7 0", row=2)
        self.label45 = ttk.Label(self.frame9)
        self.label45.configure(
            justify="center",
            relief="flat",
            style="Heading3.TLabel",
            text='S-Level')
        self.label45.grid(column=1, columnspan=11, padx="25 20", row=1)
        self.smeterAssistant_BUTTON_WIDGET = ttk.Button(self.frame9)
        self.smeterAssistant_BUTTON_WIDGET.configure(
            style="Button4.TButton", text='S-Meter Assistant')
        self.smeterAssistant_BUTTON_WIDGET.grid(
            column=1, columnspan=11, pady=25, row=4)
        self.smeterAssistant_BUTTON_WIDGET.configure(
            command=self.runSmeterAssistant)
        self.frame9.grid(column=0, columnspan=5, row=3, sticky="ew")
        self.S_Meter_Frame.pack(fill="x", side="top")
        self.S_Meter_Frame.grid_anchor("nw")
        self.frame21.pack(anchor="w", padx=20, side="top")
        self.Calibration_SF.pack(side="top")
        self.settingsNotebook.add(self.Calibration_SF, text='Calibration')
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
        self.frame23 = ttk.Frame(self.frame22)
        self.frame23.configure(height=200, width=200)
        self.frame23.pack(expand="true", fill="both", padx=20, side="top")
        self.frame22.pack(anchor="w", padx=5, pady=5, side="top")
        self.WSPR_SF.pack(side="top")
        self.settingsNotebook.add(self.WSPR_SF, text='WSPR')
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
        self.message1.configure(justify="left", relief="raised", text="NONE:\tNo offset is provided to the data send to the \n\tSDR\n\nFIXED:\tThe SDR offset frequency is added to the\n\tfrequency on the display and sent to the SDR\n\nMHZ:\tThe single MHZ digit of the radio's frequency is\n\tadded. For example, if the radio was at\n\t14.032.000, and the offset was at 30.000.000,\n\tthe resulting frequency would be 43.032.000.\n\nKHZ:\tSimilar to MHZ_OFFSET, but using the KHZ\n\tnumber. So with a 30.000.000 offset and and \n\ta 14.032.000 radio setting, the SDR will see \n\ta 30.032.000 frequency.", width=300)
        self.message1.grid(column=3, columnspan=2, row=5, sticky="ne")
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
            style="Normal.TEntry",
            textvariable=self.SDR_FREQUENCY,
            validate="focus",
            width=10)
        self.SDR_FREQUENCY_WIDGET.grid(
            column=3, pady="20 0", row=6, sticky="w")
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
        self.label8.pack(anchor="w", padx=5, pady="15 25", side="top")
        self.LCD_Frame.pack(anchor="w", side="top")
        self.frame25 = ttk.Frame(self.frame24)
        self.frame25.configure(height=200, width=200)
        self.frame2 = ttk.Frame(self.frame25)
        self.label22 = ttk.Label(self.frame2)
        self.label22.configure(
            relief="flat",
            style="Heading3.TLabel",
            text='LCD Addresses')
        self.label22.grid(
            column=0,
            columnspan=2,
            padx=5,
            pady="20 0",
            row=2,
            sticky="ew")
        self.label28 = ttk.Label(self.frame2)
        self.label28.configure(style="Normal.TLabel", text='Master I2C LCD')
        self.label28.grid(column=1, padx="75 5", row=4, sticky="w")
        self.I2C_LCD_MASTER_WIDGET = ttk.Entry(self.frame2)
        self.I2C_LCD_MASTER = tk.StringVar()
        self.I2C_LCD_MASTER_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.I2C_LCD_MASTER,
            validate="focusin",
            width=10)
        self.I2C_LCD_MASTER_WIDGET.grid(
            column=3, padx="0 5", row=4, sticky="w")
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
        self.button3 = ttk.Button(self.frame2)
        self.button3.configure(style="Button4.TButton", text='I2C Scanner')
        self.button3.grid(column=4, padx=25, row=5, sticky="e")
        self.button3.configure(command=self.runI2CScanner)
        self.frame2.pack(anchor="w", side="top")
        self.frame2.grid_anchor("nw")
        self.frame11 = ttk.Frame(self.frame25)
        self.label9 = ttk.Label(self.frame11)
        self.label9.configure(
            relief="flat",
            style="Heading3.TLabel",
            text='LCD User Interface Customization')
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
        self.frame24.pack(anchor="w", padx=5, pady=5, side="top")
        self.LCD_SF.pack(side="top")
        self.settingsNotebook.add(self.LCD_SF, text='LCD Displays')
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
        self.System_Info_Firmware_Version_Label = ttk.Label(
            self.System_Info_Firmware_Version)
        self.System_Info_Firmware_Version_Label.configure(
            style="Heading3.TLabel", text='Firmware Version: ')
        self.System_Info_Firmware_Version_Label.grid(column=0, row=0)
        self.KD8CEC = ttk.Label(self.System_Info_Firmware_Version)
        self.KD8CEC.configure(style="Normal.TLabel", text='KD8CEC  ')
        self.KD8CEC.grid(column=1, row=0, sticky="ew")
        self.VERSION_ADDRESS_WIDGET = ttk.Label(
            self.System_Info_Firmware_Version)
        self.VERSION_ADDRESS = tk.StringVar()
        self.VERSION_ADDRESS_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.VERSION_ADDRESS)
        self.VERSION_ADDRESS_WIDGET.grid(column=2, row=0, sticky="w")
        self.System_Info_Firmware_Version.pack(
            anchor="w", pady="20 0", side="top")
        self.System_Info_Calibration_Settings = ttk.Frame(self.frame27)
        self.System_Info_Calibration_Settings.configure(width=200)
        self.System_Info_Factory_Calibration_Label = ttk.Label(
            self.System_Info_Calibration_Settings)
        self.System_Info_Factory_Calibration_Label.configure(
            style="Heading3.TLabel", text='Factory Calibration Data')
        self.System_Info_Factory_Calibration_Label.grid(
            column=0, columnspan=3, row=0, sticky="w")
        self.System_Info_Factory_Calibration_Master_Label = ttk.Label(
            self.System_Info_Calibration_Settings)
        self.System_Info_Factory_Calibration_Master_Label.configure(
            style="Heading4.TLabel", text='Master:')
        self.System_Info_Factory_Calibration_Master_Label.grid(
            column=1, padx="75 50", row=2, sticky="e")
        self.System_Info_MASTER_CAL_WIDGET = ttk.Label(
            self.System_Info_Calibration_Settings)
        self.System_Info_MASTER_CAL_WIDGET.configure(
            compound="top",
            style="Normal.TLabel",
            textvariable=self.FACTORY_VALUES_MASTER_CAL)
        self.System_Info_MASTER_CAL_WIDGET.grid(column=2, row=2, sticky="e")
        self.System_Info_Factory_Calibration_BFO_Label = ttk.Label(
            self.System_Info_Calibration_Settings)
        self.System_Info_Factory_Calibration_BFO_Label.configure(
            style="Heading4.TLabel", text='SSB BFO:')
        self.System_Info_Factory_Calibration_BFO_Label.grid(
            column=1, padx="75 50", pady="0 3", row=3, sticky="e")
        self.System_Info_USB_CAL_WIDGET = ttk.Label(
            self.System_Info_Calibration_Settings)
        self.System_Info_USB_CAL_WIDGET.configure(
            style="Normal.TLabel", textvariable=self.FACTORY_VALUES_USB_CAL)
        self.System_Info_USB_CAL_WIDGET.grid(column=2, row=3, sticky="e")
        self.System_Info_Calibration_Settings.pack(
            anchor="w", pady="20 0", side="top")
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
            'CheckboxEmphasis.TCheckbutton',
            font=fontList['Emphasis'])
        style.configure('ComboBox3.TCombobox', font=fontList['Heading3'])
        style.configure('ComboBox4.TCombobox', font=fontList['Heading4'])
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

    def validate_QSO_CALLSIGN(self, p_entry_value, v_condition):
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

    def runADCScanner(self):
        pass

    def validate__METER_LEVEL1(self, p_entry_value, v_condition):
        pass

    def validate__METER_LEVEL2(self, p_entry_value, v_condition):
        pass

    def validate__METER_LEVEL4(self, p_entry_value, v_condition):
        pass

    def validate__METER_LEVEL3(self, p_entry_value, v_condition):
        pass

    def validate__METER_LEVEL5(self, p_entry_value, v_condition):
        pass

    def validate__METER_LEVEL6(self, p_entry_value, v_condition):
        pass

    def validate__METER_LEVEL7(self, p_entry_value, v_condition):
        pass

    def validate__METER_LEVEL8(self, p_entry_value, v_condition):
        pass

    def runSmeterAssistant(self):
        pass

    def runI2CScanner(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = SettingsnotebookWidget(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
