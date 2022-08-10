from tkinter import *
from tkinter.messagebox import *

top = Tk()
top.geometry('200x200')

def hello():      showerror(title="abror", message="Hello World")


B1 = Button(top, text="Salom ", command=hello)
B1.pack()
top.mainloop()