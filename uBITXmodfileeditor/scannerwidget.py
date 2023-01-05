#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.scrollbarhelper import ScrollbarHelper


class ScannerWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(ScannerWidget, self).__init__(master, **kw)
        self.scanner_frame = ttk.Frame(self)
        self.scanner_frame.configure(height=200, width=800)
        self.com_portManager_frame = ttk.Frame(self.scanner_frame)
        self.com_portManager_frame.configure(height=50, width=550)
        self.com_portManager_frame.grid(
            column=0, columnspan=3, row=0, sticky="ew")
        frame2 = ttk.Frame(self.scanner_frame)
        frame2.configure(height=200, width=50)
        self.scanner_Go_Button_Widget = ttk.Button(frame2)
        self.scanner_Go_Button_Widget.configure(
            state="normal", style="Button4.TButton", text='Start')
        self.scanner_Go_Button_Widget.pack(pady=30)
        self.scanner_Go_Button_Widget.configure(command=self.scannerStart)
        self.scanner_Done_Button_Widget = ttk.Button(frame2)
        self.scanner_Done_Button_Widget.configure(text='Done')
        self.scanner_Done_Button_Widget.pack()
        self.scanner_Done_Button_Widget.configure(command=self.scannerDone)
        frame2.grid(column=2, ipadx=15, row=1, sticky="new")
        scrollbarhelper1 = ScrollbarHelper(
            self.scanner_frame, scrolltype="vertical")
        scrollbarhelper1.configure(usemousewheel=False)
        self.scannerLog_Text = tk.Text(scrollbarhelper1.container)
        self.scannerLog_Text.configure(
            height=10, state="disabled", width=50, wrap="none")
        self.scannerLog_Text.pack(side="top")
        scrollbarhelper1.add_child(self.scannerLog_Text)
        scrollbarhelper1.grid(padx=10, pady=15, row=1)
        self.scanner_frame.pack(
            anchor="center",
            expand="true",
            fill="both",
            side="top")
        self.scanner_frame.columnconfigure(0, weight=2)
        self.scanner_frame.columnconfigure(1, weight=2)
        self.configure(height=200, width=600)
        self.resizable(True, True)
        self.title("I2C Scanner")

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

    def scannerStart(self):
        pass

    def scannerDone(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = ScannerWidget(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
