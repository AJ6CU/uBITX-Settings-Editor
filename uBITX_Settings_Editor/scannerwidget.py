#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class ScannerWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(ScannerWidget, self).__init__(master, **kw)
        self.scanner_frame = ttk.Frame(self)
        self.scanner_frame.configure(height=200, width=600)
        self.com_portManager_frame = ttk.Frame(self.scanner_frame)
        self.com_portManager_frame.configure(height=50, width=550)
        self.com_portManager_frame.grid(
            column=0, columnspan=3, row=0, sticky="ew")
        self.frame2 = ttk.Frame(self.scanner_frame)
        self.frame2.configure(height=200)
        self.scanner_Start_Button_Widget = ttk.Button(self.frame2)
        self.scanner_Start_Button_Widget.configure(
            state="normal", style="Button4.TButton", text='Start')
        self.scanner_Start_Button_Widget.pack(pady="15 25")
        self.scanner_Start_Button_Widget.configure(command=self.scannerStart)
        self.scanner_Stop_Button_Widget = ttk.Button(self.frame2)
        self.scanner_Stop_Button_Widget.configure(
            state="disabled", style="Button4.TButton", text='Stop')
        self.scanner_Stop_Button_Widget.pack(pady="0 25")
        self.scanner_Stop_Button_Widget.configure(command=self.scannerStop)
        self.scanner_Quit_Button_Widget = ttk.Button(self.frame2)
        self.scanner_Quit_Button_Widget.configure(
            style="Button4.TButton", text='Quit')
        self.scanner_Quit_Button_Widget.pack()
        self.scanner_Quit_Button_Widget.configure(command=self.scannerQuit)
        self.frame2.grid(column=1, padx=25, pady="20 0", row=1, sticky="new")
        self.frame3 = ttk.Frame(self.scanner_frame)
        self.frame3.configure(width=55)
        self.scannerLog_Text = tk.Text(self.frame3)
        self.scannerLog_Text.configure(
            borderwidth=0,
            height=10,
            state="disabled",
            width=45,
            wrap="none")
        self.scannerLog_Text.pack(
            expand="true",
            fill="both",
            padx="20 0",
            side="left")
        self.scrollbar1 = ttk.Scrollbar(self.frame3)
        self.scrollbar1.configure(orient="vertical")
        self.scrollbar1.pack(expand="true", fill="y", side="top")
        self.frame3.grid(column=0, pady="20 20", row=1)
        self.scanner_frame.pack(
            anchor="center",
            expand="true",
            fill="both",
            side="top")
        self.scanner_frame.columnconfigure(0, weight=2)
        self.scanner_frame.columnconfigure(1, weight=2)
        self.configure(height=200, width=600)
        self.resizable(True, True)

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

    def scannerStart(self):
        pass

    def scannerStop(self):
        pass

    def scannerQuit(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = ScannerWidget(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
