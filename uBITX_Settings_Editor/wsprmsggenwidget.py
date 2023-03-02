#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class WsprmsggenWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(WsprmsggenWidget, self).__init__(master, **kw)
        self.WSPR_MSG_GEN_Frame = ttk.Frame(self)
        self.WSPR_MSG_GEN_Frame.configure(height=200, width=800)
        self.frame2 = ttk.Frame(self.WSPR_MSG_GEN_Frame)
        self.frame2.configure(height=200, width=50)
        self.frame1 = ttk.Frame(self.frame2)
        self.frame1.configure(height=200, width=200)
        self.label1 = ttk.Label(self.frame1)
        self.label1.configure(style="Heading4.TLabel", text='Callsign')
        self.label1.grid(column=0, padx="0 5", row=0)
        self.entry1 = ttk.Entry(self.frame1)
        self.callsign = tk.StringVar()
        self.entry1.configure(
            style="Normal.TEntry",
            textvariable=self.callsign,
            width=11)
        self.entry1.grid(column=1, padx="0 10", row=0)
        self.label2 = ttk.Label(self.frame1)
        self.label2.configure(style="Heading4.TLabel", text='Grid')
        self.label2.grid(column=2, padx="0 5", row=0)
        self.entry2 = ttk.Entry(self.frame1)
        self.gridSq = tk.StringVar()
        self.entry2.configure(
            style="Normal.TEntry",
            textvariable=self.gridSq,
            width=4)
        self.entry2.grid(column=3, padx="0 10", row=0)
        self.label3 = ttk.Label(self.frame1)
        self.label3.configure(style="Heading4.TLabel", text='dbm')
        self.label3.grid(column=4, padx="0 5", row=0)
        self.entry3 = ttk.Entry(self.frame1)
        self.dbm = tk.StringVar(value='10')
        self.entry3.configure(
            style="Normal.TEntry",
            textvariable=self.dbm,
            width=3)
        _text_ = '10'
        self.entry3.delete("0", "end")
        self.entry3.insert("0", _text_)
        self.entry3.grid(column=5, row=0)
        self.frame1.grid(column=0, pady="5 10", row=0)
        self.frame3 = ttk.Frame(self.frame2)
        self.frame3.configure(height=200, width=200)
        self.button1 = ttk.Button(self.frame3)
        self.button1.configure(
            style="Normal.TButton",
            text='Generate WSPR Message')
        self.button1.grid(column=0, padx="0 10", row=0)
        self.button1.configure(command=self.WSPR_Msg_Gen_Button)
        self.button2 = ttk.Button(self.frame3)
        self.button2.configure(style="Normal.TButton", text='Cancel')
        self.button2.grid(column=1, row=0)
        self.button2.configure(command=self.WSPR_Msg_Gen_Cancel_Button)
        self.frame3.grid(column=0, pady="0 5", row=1)
        self.frame2.pack(padx=10, side="top")
        self.WSPR_MSG_GEN_Frame.pack(
            anchor="center",
            expand="true",
            fill="both",
            side="top")
        self.WSPR_MSG_GEN_Frame.columnconfigure(0, weight=2)
        self.WSPR_MSG_GEN_Frame.columnconfigure(1, weight=2)
        self.configure(height=200, width=600)
        self.resizable(True, True)
        self.title("Create WSPR Tone Code")

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

    def WSPR_Msg_Gen_Button(self):
        pass

    def WSPR_Msg_Gen_Cancel_Button(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = WsprmsggenWidget(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
