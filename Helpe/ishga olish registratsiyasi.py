from tkinter import *
from tkinter.messagebox import *
from datetime import date

hozirgiyil = date.today().year
root = Tk()
root.title("rigistratsiya")
window_width = 800
window_height = 400
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(width=False, height=False)

root.configure(bg='#00001a')
Label(root, text='ISHGA OLISH:', font=('Sans serif', 32, 'bold'), justify=CENTER).pack()

ism = Label(root, text="Ism:", font=("Arial", 17), bg='#00001a', fg='white').place(x=10, y=90)
ism_e = Entry(root, font=("Arial", 17), width=17)
ism_e.place(x=150, y=90)

familiya = Label(root, text="Familiya:", font=("Arial", 17), bg='#00001a', fg='white').place(x=420, y=90)
familiya_e = Entry(root, font=("Arial", 17), width=17)
familiya_e.place(x=540, y=90)

tyil = Label(root, text="Tugilgan yil:", font=("Arial", 17), bg='#00001a', fg='white').place(x=10, y=150)
tyil_e = Entry(root, font=("Arial", 17), width=17)
tyil_e.place(x=150, y=150)

manzil = Label(root, text="Manzil:", font=("Arial", 17), bg='#00001a', fg='white').place(x=420, y=150)
manzil_e = Entry(root, font=("Arial", 17), width=17)
manzil_e.place(x=540, y=150)

fayln = Label(root, text="Fayl nomi:", font=("Arial", 17), bg='#00001a', fg='white').place(x=10, y=210)
fayln_e = Entry(root, font=('Arial',17),width=18)
fayln_e.place(x=150,y=210)

def hello():
 askquestion(title="text",
 message="text saqlandi")
B1 =Button(text = "OK",
 command = hello)
B1. pack()

def saqla():
    i=ism_e.get()
    x=familiya_e.get()
    t=tyil_e.get()
    m = manzil_e.get()
    f = fayln_e.get()
    with open(f,'a') as f:
       f.write(f'_________________________________________\n'
               f'ism:{i}\nFamilya:{x}\nyil:{t}\nmanzil:{m}')
       f.close()


ok_b = Button(root, text="Saqlash", font=("Times New Roman", 17), justify=CENTER, padx=123,command=saqla).place(x=433, y=200)



root.mainloop()