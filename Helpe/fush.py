"""12.04.2022
 YIL SESHANBA KINI"""
from time import strftime
from tkinter import *
from tkinter.ttk import *

import datetime as dt
root = Tk()
root.title('SEVGI HATI')
def time():
    soat =strftime('acer')

    label.config(text=soat)
    label.after(1000,time)


label =Label(root,font=('ds-digtal',100),foreground='red',background='pink')
label.pack(anchor='center')
time()
mainloop()

