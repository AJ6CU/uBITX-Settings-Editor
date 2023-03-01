#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class WsprfreqselectWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(WsprfreqselectWidget, self).__init__(master, **kw)
        self.WSPR_MSG_GEN_Frame = ttk.Frame(self)
        self.WSPR_MSG_GEN_Frame.configure(height=200, width=800)
        self.frame2 = ttk.Frame(self.WSPR_MSG_GEN_Frame)
        self.frame2.configure(height=200, width=50)
        self.frame1 = ttk.Frame(self.frame2)
        self.frame1.configure(height=200, width=200)
        self.label1 = ttk.Label(self.frame1)
        self.label1.configure(style="Heading3.TLabel", text='Band')
        self.label1.grid(column=0, padx="0 10", row=0)
        self.frame7 = ttk.Frame(self.frame1)
        self.frame7.configure(height=200, width=200)
        self.WSPR_BAND_SELECTION_WIDGET = ttk.Combobox(self.frame7)
        self.WSPR_BAND_SELECTION = tk.StringVar()
        self.WSPR_BAND_SELECTION_WIDGET.configure(
            style="ComboBox3.TCombobox",
            takefocus=False,
            textvariable=self.WSPR_BAND_SELECTION,
            values='600m 160m 80m 60m 40m 30m 20m 17m 15m 12m 10m 6m 4m 2m',
            width=8)
        self.WSPR_BAND_SELECTION_WIDGET.pack(padx="0 10", side="top")
        self.WSPR_BAND_SELECTION_WIDGET.bind(
            "<<ComboboxSelected>>", self.WSPR_BAND_SELECTED_CB, add="+")
        self.frame7.grid(column=1, row=0)
        self.WSPR_BAND_DESCRIPTION_WIDGET = ttk.Label(self.frame1)
        self.WSPR_BAND_DESCRIPTION = tk.StringVar()
        self.WSPR_BAND_DESCRIPTION_WIDGET.configure(
            style="Heading3.TLabel", textvariable=self.WSPR_BAND_DESCRIPTION, width=55)
        self.WSPR_BAND_DESCRIPTION_WIDGET.grid(column=2, row=0)
        self.frame1.pack(pady=10, side="top")
        self.frame4 = ttk.Frame(self.frame2)
        self.frame4.configure(height=200, width=200)
        self.WSPR_SLIDER_MOVED_WIDGET = ttk.Scale(self.frame4)
        self.WSPR_SLIDER = tk.StringVar(value='100')
        self.WSPR_SLIDER_MOVED_WIDGET.configure(
            from_=0,
            length=100,
            orient="horizontal",
            state="normal",
            to=200,
            value=100,
            variable=self.WSPR_SLIDER)
        self.WSPR_SLIDER_MOVED_WIDGET.pack(expand="true", fill="x", side="top")
        self.WSPR_SLIDER_MOVED_WIDGET.configure(
            command=self.WSPR_SLIDER_MOVED_CB)
        self.frame4.pack(expand="true", fill="x", pady="0 10", side="top")
        self.frame5 = ttk.Frame(self.frame2)
        self.frame5.configure(height=40, width=100)
        self.label3 = ttk.Label(self.frame5)
        self.label3.configure(style="Heading3.TLabel", text='TX Freq:')
        self.label3.place(anchor="n", relx=0.35, rely=0.0, x=0, y=0)
        self.frame6 = ttk.Frame(self.frame5)
        self.frame6.configure(height=200, width=200)
        self.WSPR_CURRENT_FREQUENCY_WIDGET = ttk.Label(self.frame6)
        self.WSPR_CURRENT_FREQUENCY = tk.StringVar(value='14,097,100 Hz')
        self.WSPR_CURRENT_FREQUENCY_WIDGET.configure(
            style="Heading3.TLabel",
            text='14,097,100 Hz',
            textvariable=self.WSPR_CURRENT_FREQUENCY)
        self.WSPR_CURRENT_FREQUENCY_WIDGET.pack(anchor="center", side="top")
        self.frame6.place(anchor="n", relx=0.5, x=0, y=0)
        self.WSPR_CURRENT_BANDWIDTH_WIDGET = ttk.Label(self.frame5)
        self.WSPR_CURRENT_BANDWIDTH = tk.StringVar(value='1.500')
        self.WSPR_CURRENT_BANDWIDTH_WIDGET.configure(
            style="Heading3.TLabel",
            text='1.500',
            textvariable=self.WSPR_CURRENT_BANDWIDTH)
        self.WSPR_CURRENT_BANDWIDTH_WIDGET.place(
            anchor="n", relx=.91, x=0, y=0)
        self.label2 = ttk.Label(self.frame5)
        self.label2.configure(style="Heading3.TLabel", text='Hz')
        self.label2.place(anchor="n", relx=.97, x=0, y=0)
        self.frame5.pack(
            anchor="center",
            expand="false",
            fill="x",
            pady="0 10",
            side="top")
        self.frame3 = ttk.Frame(self.frame2)
        self.frame3.configure(height=200, width=200)
        self.WSPR_BAND_OK_CB_Button = ttk.Button(self.frame3)
        self.WSPR_BAND_OK_CB_Button.configure(
            style="Normal.TButton", text='OK')
        self.WSPR_BAND_OK_CB_Button.grid(column=0, padx="0 10", row=0)
        self.WSPR_BAND_OK_CB_Button.configure(
            command=self.WSPR_BAND_OK_Button_CB)
        self.button2 = ttk.Button(self.frame3)
        self.button2.configure(style="Normal.TButton", text='Cancel')
        self.button2.grid(column=1, row=0)
        self.button2.configure(command=self.WSPR_BAND_CANCEL_Button_CB)
        self.frame3.pack(pady="0 10", side="top")
        self.frame2.pack(padx=10, side="top")
        self.WSPR_MSG_GEN_Frame.pack(
            anchor="center",
            expand="true",
            fill="both",
            side="top")
        self.configure(height=200, width=600)
        self.resizable(True, True)
        self.title("Select WSPR Band and Tone Frequency")

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

    def WSPR_BAND_SELECTED_CB(self, event=None):
        pass

    def WSPR_SLIDER_MOVED_CB(self, scale_value):
        pass

    def WSPR_BAND_OK_Button_CB(self):
        pass

    def WSPR_BAND_CANCEL_Button_CB(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = WsprfreqselectWidget(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
