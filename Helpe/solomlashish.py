from tkinter import *
root = Tk()
var = StringVar()
label = Label( root, bg="yellow", fg="red", font="Algerian", textvariable=var, relief=RAISED )
var.set("Assalom-u alaykum! ")
label.pack()
root.mainloop()