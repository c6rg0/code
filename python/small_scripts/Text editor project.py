# Text editor project

# Plan:
# Creating a user interface (inculding a menu bar),
# Reading files, and formatting it in the edittor,
# Writing data into a temp file/variable,
# Displaying the data in an optimized way (underscore/line etc),
# Writing the temp file/variable to a desired; file name, file format, path/location,

from tkinter import * 
import tkinter as tk
from tkinter.ttk import * 
from time import strftime
from tkinter import filedialog as fd

# creating tkinter window
root = Tk()
root.title('Text editor')
root.geometry("1280x720")

def text_routine():
# Create text widget and specify size.
    global T_var
    T_var = Text(root, height = 1200, width = 720)
    T_var.pack()
"""
def selectfile():
    """

# Creating Menubar
menubar = Menu(root)

# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_separator()
file.add_command(label ='New File', command = None)
file.add_command(label ='Open', command = selectfile())
file.add_command(label ='Save', command = None)
file.add_command(label ='Exit', command = root.destroy)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)

# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='', command = None)
help_.add_command(label ='', command = None)
help_.add_separator()
help_.add_command(label ='', command = None)

text_routine()
T = T_var.get("1.0",END)

"""
# Insert The Fact.
T.insert(tk.END, Fact)
"""

# display Menu
root.config(menu = menubar)
mainloop()