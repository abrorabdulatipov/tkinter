from tkinter import Label, Tk

root = Tk()
label1 = Label(root, text='Option1', width=20, height=10, bg='green')
label2 = Label(root, text='Option2', width=20, height=10, bg='red')

label2.pack()
label1.pack()
root.mainloop()


