from tkinter import *
from tkinter.messagebox import *

top = Tk()
Lb1 = Listbox(top, font="italic")
Lb1.insert(1, "Python")
Lb1.insert(2, "Java")
Lb1.insert(3, "C++")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JavaScript")
Lb1.insert(6, "HTML")
Lb1.pack()

top.mainloop()