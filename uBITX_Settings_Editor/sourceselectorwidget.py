#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.pathchooserinput import PathChooserInput


class SourceselectorWidget(ttk.Labelframe):
    def __init__(self, master=None, **kw):
        super(SourceselectorWidget, self).__init__(master, **kw)
        self.SourceSelector = ttk.Frame(self)
        self.SourceSelector.configure(height=200, width=200)
        self.uBITX_sourceSelector_WIDGET = ttk.Radiobutton(self.SourceSelector)
        self.sourceSelectorRadioButton = tk.StringVar(value='uBITX')
        self.uBITX_sourceSelector_WIDGET.configure(
            state="normal",
            style="RadioButton4.TRadiobutton",
            text='uBITX',
            value="uBITX",
            variable=self.sourceSelectorRadioButton)
        self.uBITX_sourceSelector_WIDGET.pack(anchor="w", side="top")
        self.uBITX_sourceSelector_WIDGET.configure(command=self.sourceSelected)
        self.File_sourceSelector_WIDGET = ttk.Radiobutton(self.SourceSelector)
        self.File_sourceSelector_WIDGET.configure(
            state="normal",
            style="RadioButton4.TRadiobutton",
            text='Saved File',
            value="SavedFIle",
            variable=self.sourceSelectorRadioButton)
        self.File_sourceSelector_WIDGET.pack(anchor="w", side="left")
        self.File_sourceSelector_WIDGET.configure(command=self.sourceSelected)
        self.SourceSelector.grid(column=0, padx=20, row=0)
        self.separator1 = ttk.Separator(self)
        self.separator1.configure(orient="vertical")
        self.separator1.grid(column=1, padx=5, row=0, sticky="ns")
        self.sourceBlock = ttk.Frame(self)
        self.sourceBlock.configure(height=75, padding="10 0", width=550)
        self.selectComPort_Frame = ttk.Frame(self.sourceBlock)
        self.selectComPort_Frame.configure(height=200, width=200)
        self.com_portManager_frame = ttk.Frame(self.selectComPort_Frame)
        self.com_portManager_frame.configure(height=50, width=400)
        self.com_portManager_frame.grid(column=0, row=0)
        self.actionButton = ttk.Button(self.selectComPort_Frame)
        self.actionButton_Text = tk.StringVar(value='button1')
        self.actionButton.configure(
            state="normal",
            style="ButtonEmphasis.TButton",
            text='button1',
            textvariable=self.actionButton_Text)
        self.actionButton.grid(column=1, padx="10 25", row=0)
        self.actionButton.configure(command=self.processComPort)
        self.selectComPort_Frame.pack(side="left")
        self.selectSaveFileFrame = ttk.Frame(self.sourceBlock)
        self.selectSaveFileFrame.configure(height=50, width=400)
        self.label2 = ttk.Label(self.selectSaveFileFrame)
        self.label2.configure(style="Normal.TLabel", text='Select Saved File')
        self.label2.grid(column=0, padx="0 20", row=0, sticky="w")
        self.savedFilePathChooserWidget = PathChooserInput(
            self.selectSaveFileFrame)
        self.savedFilePathChooser = tk.StringVar()
        self.savedFilePathChooserWidget.configure(
            initialdir="~",
            mustexist=True,
            textvariable=self.savedFilePathChooser,
            type="file")
        self.savedFilePathChooserWidget.grid(
            column=1, ipadx=70, padx="0 5", row=0)
        self.savedFilePathChooserWidget.bind(
            "<<PathChooserPathChanged>>", self.on_path_changed, add="")
        self.selectSaveFileFrame.pack(side="left")
        self.sourceBlock.grid(column=2, row=0)
        self.sourceBlock.pack_propagate(0)
        self.optionalInfo_Frame = ttk.Frame(self)
        self.optionalInfo_Frame.configure(height=200, width=200)
        self.resetButton_Frame = ttk.Frame(self.optionalInfo_Frame)
        self.resetButton_Frame.configure(height=50)
        self.reset_uBITX_Button_WIDGET = ttk.Button(self.resetButton_Frame)
        self.resetButton = tk.StringVar(value='Reboot uBITX')
        self.reset_uBITX_Button_WIDGET.configure(
            state="disabled",
            style="Button4.TButton",
            takefocus=True,
            text='Reboot uBITX',
            textvariable=self.resetButton)
        self.reset_uBITX_Button_WIDGET.pack()
        self.reset_uBITX_Button_WIDGET.configure(command=self.reset_ubitx)
        self.resetButton_Frame.grid(column=0, row=0, sticky="w")
        self.PORTECT_FACTORY_Frame = ttk.Frame(self.optionalInfo_Frame)
        self.PROTECT_FACTORY_WIDGET = ttk.Checkbutton(
            self.PORTECT_FACTORY_Frame)
        self.PROTECT_FACTORY = tk.StringVar()
        self.PROTECT_FACTORY_WIDGET.configure(
            offvalue="NO",
            onvalue="YES",
            state="normal",
            style="CheckboxNormal.TCheckbutton",
            text='Protect Factory Calibration',
            variable=self.PROTECT_FACTORY)
        self.PROTECT_FACTORY_WIDGET.pack(anchor="w", side="top")
        self.PROTECT_FACTORY_WIDGET.configure(
            command=self.protect_factory_cal_cb)
        self.PORTECT_FACTORY_Frame.grid(
            column=1, columnspan=2, padx="15 0", row=0, sticky="w")
        self.optionalInfo_Frame.grid(column=3, row=0)
        self.configure(
            height=300,
            style="Heading2.TLabelframe",
            text='Select Source',
            width=200)
        self.grid(column=0, row=1, sticky="ew")
        self.grid_anchor("w")

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

    def sourceSelected(self):
        pass

    def processComPort(self):
        pass

    def on_path_changed(self, event=None):
        pass

    def reset_ubitx(self):
        pass

    def protect_factory_cal_cb(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = SourceselectorWidget(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
