from tkinter import *
from tkinter.constants import END
oyna = Tk()
oyna.title("Kalkulator")
oyna.geometry("400x440")
oyna.configure(bg="#00001a")
oyna.resizable(False, False)


# Raqamlarni entryga chiqarish funksiyalari--------------
def nolr():
    ekran.insert(END, '0')


def birr():
    ekran.insert(END, '1')


def ikkir():
    ekran.insert(END, '2')


def uchr():
    ekran.insert(END, '3')


def tortr():
    ekran.insert(END, '4')


def beshr():
    ekran.insert(END, '5')


def oltir():
    ekran.insert(END, '6')


def yettir():
    ekran.insert(END, '7')


def sakkizr():
    ekran.insert(END, '8')


def toqqizr():
    ekran.insert(END, 9)


# Raqamlar yakuni------------------------------

def tozalash():
    ekran.delete(0, END)


def birdel():
    try:
        ekr = ekran.get()
        ekran.delete(0, END)
        ekran.insert(0, ekr[:-1])
    except:
        pass



def bolinmab():
    try:
        if ekran.get()[-1] !='/' and ekran.get()[-1] !='*' and ekran.get()[-1] != '-' and ekran.get()[-1] !='+':
            ekran.insert(END, '/')
    except:
        pass

def kopaytirb():
    try:
        if ekran.get()[-1] != '/' and ekran.get()[-1] != '*' and ekran.get()[-1] != '-' and ekran.get()[-1] != '+':
            ekran.insert(END, '*')
    except:
        pass

def minusb():
    try:
        if ekran.get()[-1] != '/' and ekran.get()[-1] != '*' and ekran.get()[-1] != '-' and ekran.get()[-1] != '+':
            ekran.insert(END, '-')
    except:
        pass

def plusb():
    try:
        if ekran.get()[-1] != '/' and ekran.get()[-1] != '*' and ekran.get()[-1] != '-' and ekran.get()[-1] != '+':
            ekran.insert(END, '+')
    except:
        pass

def nuqtab():
    if ekran.get() == "":
        ekran.insert(END,'0.')
    else:
        ekran.insert(END,'.')

def plminb():
    try:
        if ekran.get()[0] != "-":
            ekran.insert(0,'-')
        else:
            ekran.delete(0,1)
    except:
        pass

def ekr():
    ekran.delete(0,END)
    ekran.configure(fg='black')
    teng.configure(bg='orange',state=NORMAL)

def tengb():
    try:
        misol = ekran.get()
        ekran.delete(0,END)

        n=eval(misol)
        n1=str(n)
        if n1.endswith('.0'):
            n1 = int(n)

            ekran.insert(END,n1)
        else:
            ekran.insert(END,n)
    except:
        ekran.delete(0,END)
        ekran.configure(fg='red')
        ekran.insert(END, 'ERROR')
        teng.configure(state=DISABLED,  bg='silver')
        ekran.after(1500, ekr)







ekran = Entry(oyna, bd=5, font=("Arial 25"), width=20, justify=RIGHT)
ekran.place(x=13, y=10)

ce = Button(oyna, text="CE", font=("Arial", 20), bg="peru", fg="white", width=4, command=tozalash)
ce.place(x=10, y=90)

c = Button(oyna, text="C", font=("Arial", 20), bg="peru", fg="white", width=4, command=tozalash)
c.place(x=112, y=90)

tozala = Button(oyna, text="<×", font=("Arial", 20), bg="peru", fg="white", width=4, command=birdel)
tozala.place(x=214, y=90)

bolinma = Button(oyna, text="/", font=("Arial", 20), bg="orange", fg="white", width=4, command=bolinmab)
bolinma.place(x=316, y=90)

yetti = Button(oyna, text="7", font=('Arial', 20), bg='white', fg='black', width=4, command=yettir)
yetti.place(x=10, y=160)

sakkiz = Button(oyna, text="8", font=('Arial', 20), bg='white', fg='black', width=4, command=sakkizr)
sakkiz.place(x=112, y=160)

toqqiz = Button(oyna, text="9", font=('Arial', 20), bg='white', fg='black', width=4, command=toqqizr)
toqqiz.place(x=214, y=160)

kopaytir = Button(oyna, text="*", font=('Arial', 20), bg='orange', fg='white', width=4, command=kopaytirb)
kopaytir.place(x=316, y=160)

tort = Button(oyna, text="4", font=('Arial', 20), bg='white', fg='black', width=4, command=tortr)
tort.place(x=10, y=230)

besh = Button(oyna, text="5", font=('Arial', 20), bg='white', fg='black', width=4, command=beshr)
besh.place(x=112, y=230)

olti = Button(oyna, text="6", font=('Arial', 20), bg='white', fg='black', width=4, command=oltir)
olti.place(x=214, y=230)

minus = Button(oyna, text="-", font=('Arial', 20), bg='orange', fg='white', width=4, command=minusb)
minus.place(x=316, y=230)

bir = Button(oyna, text="1", font=('Arial', 20), bg='white', fg='black', width=4, command=birr)
bir.place(x=10, y=300)

ikki = Button(oyna, text="2", font=('Arial', 20), bg='white', fg='black', width=4, command=ikkir)
ikki.place(x=112, y=300)

uch = Button(oyna, text="3", font=('Arial', 20), bg='white', fg='black', width=4, command=uchr)
uch.place(x=214, y=300)

plus = Button(oyna, text="+", font=('Arial', 20), bg='orange', fg='white', width=4, command=plusb)
plus.place(x=316, y=300)

plmin = Button(oyna, text="±", font=('Arial', 20), bg='peru', fg='white', width=4, command=plminb)
plmin.place(x=10, y=370)

nol = Button(oyna, text="0", font=('Arial', 20), bg='white', fg='black', width=4, command=nolr)
nol.place(x=112, y=370)

nuqta = Button(oyna, text=".", font=('Arial', 20), bg='white', fg='black', width=4, command=nuqtab)
nuqta.place(x=214, y=370)

teng = Button(oyna, text="=", font=('Arial', 20), bg='orange', fg='white', width=4, command=tengb)
teng.place(x=316, y=370)

oyna.mainloop()