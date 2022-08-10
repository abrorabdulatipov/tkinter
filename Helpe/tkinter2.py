# from tkinter import Tk, Button
#
# root = Tk()
# root.geometry('300x400')
# root.config(bg='green')
#
#
# def f():
#     root.config(bg='red')
#
#
# btn = Button(root, text='Next Color', command=f)
# btn.pack()
# root.mainloop()



from tkinter import Tk, Button

root = Tk()

count=0

def f():
    global count
    count +=1
    if count==34:
        count=0
    print(count)
    btn.config(text= count)

btn = Button(root, text='Join', command=f)
btn.pack()
root.mainloop()
