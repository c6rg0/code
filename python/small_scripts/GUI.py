"""
import tkinter 
from tkinter import *
from tkinter import messagebox
t = tkinter.Tk()

t.geometry("1980x1080")
t.state('zoomed')

def draw():
   global B1
   B1 = Button(t, text = "Draw a card", command = card)
   B1.place(x=950,y=500)

def card():
   global B2, B3
   B2 = Button(t, text = "You drawn a card!")
   B2.place(x=940,y=500)
   B3 = Button(t, text = "Reset", command = reset)
   B3.place(x=970,y=530)  
   
def reset():
   B1.destroy()
   B2.destroy()
   B2.destroy()
   draw()

B1 = ""
B2 = ""
B3 = ""

draw()

t.mainloop()
"""


from tkinter import * 
from tkinter.ttk import * 
from time import strftime

# creating tkinter window
root = Tk()
root.title('Text editor')
root.geometry("1280x720")

# Creating Menubar
menubar = Menu(root)

# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
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

# display Menu
root.config(menu = menubar)
mainloop()