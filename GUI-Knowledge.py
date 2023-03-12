from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

gui = Tk()
gui.title('Program Data Record')
gui.geometry('500x400')

b1 = Button(gui,text='button')
#b1.place(x=20,y=200)
b1.pack()

fb1 = Frame(gui)
fb1.place(x=100,y=300)
b2 = ttk.Button(fb1,text='button with theme')
b2.pack(ipadx=20, ipady=20)

###############################
def Button2():
    text = 'Money = 300 baht'
    messagebox.showinfo('account',text)
    #messagebox.showerror('error', text)
    #messagebox.showwarning('warning', text)
    
fb2 = Frame(gui)
fb2.place(x=200,y=200)
b3 =ttk.Button(fb2, text='How much money', command=Button2)
b3.pack(ipadx=20, ipady=20)
b3.pack(ipadx=20, ipady=20, padx=10, pady=10)
##################################

l1 = Label(gui, text='Record km', font=('Angsana New',30), fg='green')
l1.place(x=30,y=20)


gui.mainloop()
