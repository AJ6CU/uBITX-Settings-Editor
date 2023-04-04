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
fontList = {'Heading1': ('Times New Roman',24, 'bold', 'italic' ),
            'Heading2': ('Arial',18, 'bold' ),
            'Heading3': ('Arial',12, 'bold' ),
            'Heading4': ('Arial',10, 'bold' ),
            'Normal': ('Default', 10),
            'Emphasis': ('Default',12, 'bold'),
            'Symbol1': ('Symbol',18, 'bold'),
            'Symbol3': ('Symbol',12, 'bold')}

style.configure('Heading1.TLabel',font=fontList['Heading1'], background='blue', foreground='white')
style.configure('Heading2.TLabel',font=fontList['Heading2'])
style.configure('Heading3.TLabel',font=fontList['Heading3'])
style.configure('Heading4.TLabel',font=fontList['Heading4'])
style.configure('Normal.TLabel',font=fontList['Normal'])
style.configure('Symbol1.TLabel',font=fontList['Symbol1'])
style.configure('Button3.TButton',font=fontList['Heading3'])
style.configure('Button4.TButton',font=fontList['Heading4'])
style.configure('Button3Blue.TButton',font=fontList['Heading3'], foreground='blue')
style.configure('Normal.TButton',font=fontList['Normal'])
style.configure('Symbol1.TButton',font=fontList['Symbol1'])
style.configure('Symbol3.TButton',font=fontList['Symbol3'])
style.configure('ButtonEmphasis.TButton',font=fontList['Emphasis'])
style.configure('RadioButton3.TRadiobutton',font=fontList['Heading3'])
style.configure('RadioButton4.TRadiobutton',font=fontList['Heading4'])
style.configure('RadioButtonNormal.TRadiobutton',font=fontList['Normal'])
style.configure('RadioButtonEmphasis.TRadiobutton',font=fontList['Emphasis'])
style.configure('Checkbox3.TCheckbutton',font=fontList['Heading3'])
style.configure('Checkbox4.TCheckbutton',font=fontList['Heading4'])
style.configure('CheckboxNormal.TCheckbutton',font=fontList['Normal'])
style.configure('CheckboxNormalNoBorder.TCheckbutton',font=fontList['Normal'],highlightthickness=0, borderwidth=0, bd=0)
style.configure('CheckboxEmphasis.TCheckbutton',font=fontList['Emphasis'])
style.configure('ComboBox3.TCombobox',font=fontList['Heading3'])
style.configure('ComboBox4.TCombobox',font=fontList['Heading4'])
style.configure('ComboBox4White.TCombobox',font=fontList['Heading4'],foreground='white')
style.configure('Normal.TEntry',font=fontList['Normal'])
style.configure('NoBorder.TEntry',font=fontList['Normal'], highlightthickness=0, borderwidth=0, bd=0)
style.configure('Title.TFrame', background='blue', foreground='white')
style.configure('Heading2.TLabelframe.Label',font=fontList['Heading3'])
style.configure('Heading2.TLabelframe')
style.configure('Normal.TText', font=fontList['Heading3'])

style.configure('Highlight.TFrame', background='blue', bd=4 )
style.configure('Normal.TFrame', background='gray', bd=4)

style.configure('Fixed.TNotebook')
style.configure('Fixed.TNotebook.Tab',padding=[5,2])






