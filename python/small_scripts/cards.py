import random

import tkinter 
from tkinter import *
from tkinter import messagebox
t = tkinter.Tk()

t.geometry("1980x1080")
t.state('zoomed')

def diverge():
    if temp == 0:
        temp = 1
        display_first()

    if temp == 1:
        display()

def cards():

    global type
    global suit

    #Suits 
    suits = ("Spades","Hearts","Clubs","Diamonds")
    suit = random.choice(suits)

    #Types of cards
    num = random.randint(0,13)

    if num < 2:
        type = "Ace"
    
    elif 2 <= num <= 9:
        type = num

    elif num == 10:
        type = "Jack"

    elif num == 11:
        type = "Queen"

    elif num == 12:
        type = "King"

    elif num == 13:
        type = "Joker"

    global Button1
    Button1 = Button(t, text = "Draw a card", command = diverge)
    Button1.place(x=950,y=500)

def display_first():
   global Button2, label 
   Button1.destroy()
   Button2 = Button(t, text = "Draw another card", command = cards)
   Button2.place(x=940,y=500)
   label = Label(t, text = ("Your card is a",type,"of",suit))
   label.place(x=922,y=530)

def display():
   Button1.destroy()
   Button2 = Button(t, text = "Draw another card", command = cards)
   Button2.place(x=940,y=500)
   label = Label(t, text = ("Your card is a",type,"of",suit))
   label.place(x=922,y=530)  

#main program
cards()

t.mainloop()
