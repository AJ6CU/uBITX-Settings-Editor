#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.pathchooserinput import PathChooserInput


class SourceselectorWidget(ttk.Labelframe):
    def __init__(self, master=None, **kw):
        super(SourceselectorWidget, self).__init__(master, **kw)
        self.SourceSelector = ttk.Frame(self)
        self.SourceSelector.configure(height=200, width=200)
        radiobutton1 = ttk.Radiobutton(self.SourceSelector)
        self.sourceSelectorRadioButton = tk.StringVar(value='uBITX')
        radiobutton1.configure(
            state="normal",
            style="RadioButton4.TRadiobutton",
            text='uBITX',
            value="uBITX",
            variable=self.sourceSelectorRadioButton)
        radiobutton1.pack(anchor="w", side="top")
        radiobutton1.configure(command=self.sourceSelected)
        radiobutton2 = ttk.Radiobutton(self.SourceSelector)
        radiobutton2.configure(
            state="normal",
            style="RadioButton4.TRadiobutton",
            text='Saved File',
            value="SavedFIle",
            variable=self.sourceSelectorRadioButton)
        radiobutton2.pack(anchor="w", side="left")
        radiobutton2.configure(command=self.sourceSelected)
        self.SourceSelector.grid(column=0, padx=20, row=0)
        separator1 = ttk.Separator(self)
        separator1.configure(orient="vertical")
        separator1.grid(column=1, padx=5, row=0, sticky="ns")
        self.sourceBlock = ttk.Frame(self)
        self.sourceBlock.configure(height=200, padding="10 0", width=400)
        self.selectComPortFrame = ttk.Frame(self.sourceBlock)
        self.selectComPortFrame.configure(height=200, width=200)
        self.comPortListRefresh = ttk.Button(self.selectComPortFrame)
        self.comPortListRefresh.configure(
            style="Normal.TButton", text='Refresh Port List')
        self.comPortListRefresh.grid(column=0, padx="0 15", row=0, sticky="w")
        self.comPortListRefresh.configure(command=self.updateComPorts)
        self.availableComPorts = tk.StringVar(value='Select Serial Port')
        __values = ['Select Serial Port']
        self.comPortsOptionMenu = ttk.OptionMenu(
            self.selectComPortFrame,
            self.availableComPorts,
            "Select Serial Port",
            *__values,
            command=self.comPortSelected)
        self.comPortsOptionMenu.grid(column=1, padx="0 180", row=0, sticky="w")
        self.selectComPortFrame.pack(anchor="w", expand="false", side="top")
        self.selectSaveFileFrame = ttk.Frame(self.sourceBlock)
        self.selectSaveFileFrame.configure(height=200, width=200)
        label2 = ttk.Label(self.selectSaveFileFrame)
        label2.configure(style="Normal.TLabel", text='Select Saved File')
        label2.grid(column=0, padx="0 20", row=0, sticky="w")
        self.savedFilePathChooserWidget = PathChooserInput(
            self.selectSaveFileFrame)
        self.savedFilePathChooser = tk.StringVar()
        self.savedFilePathChooserWidget.configure(
            initialdir="~",
            mustexist="false",
            textvariable=self.savedFilePathChooser,
            title="Select Previously Saved Settings File",
            type="file")
        self.savedFilePathChooserWidget.grid(
            column=1, ipadx=70, padx="0 5", row=0)
        self.savedFilePathChooserWidget.bind(
            "<<PathChooserPathChanged>>", self.on_path_changed, add="")
        self.selectSaveFileFrame.pack(anchor="w", expand="false", side="top")
        self.sourceBlock.grid(column=2, padx="0 70", row=0)
        self.readButtonFrame = ttk.Frame(self)
        self.readButtonFrame.configure(height=200, width=200)
        self.goButtonWidget = ttk.Button(self.readButtonFrame)
        self.goButton = tk.StringVar(value='READ')
        self.goButtonWidget.configure(
            state="disabled",
            style="Button4.TButton",
            text='READ',
            textvariable=self.goButton)
        self.goButtonWidget.pack(anchor="n", side="left")
        self.readButtonFrame.grid(column=3, row=0, sticky="e")
        self.configure(
            height=300,
            style="Heading2.TLabelframe",
            text='Select Source',
            width=200)
        self.grid(column=0, row=1, sticky="ew")

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

    def sourceSelected(self):
        pass

    def updateComPorts(self):
        pass

    def comPortSelected(self, option):
        pass

    def on_path_changed(self, event=None):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = SourceselectorWidget(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
