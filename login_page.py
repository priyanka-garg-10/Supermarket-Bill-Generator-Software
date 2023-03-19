from tkinter import *
from tkinter import messagebox

def ok():
    uname=e1.get()
    password=e2.get()

    if(uname == '' and password == ''):
        messagebox.showinfo('','Blank not allowed')

    elif(uname == 'admin' and password == 'np'):
        messagebox.showinfo('',"Login success")
        root.destroy()

    else :
        messagebox.showinfo('',"Incorrect username or password")


root=Tk()
root.title('Login') 
root.geometry('300x200')
global e1
global e2
global e3
global e4
Label(root, text='Username').place(x=10,y=10)
Label(root, text='Password').place(x=10,y=40)

e1 = Entry(root)
e1.place(x=140,y=10)

e2 = Entry(root)
e2.place(x=140,y=40)
e2.config(show='*')

Button(root, text='Login' , command=ok,height =3,width=13).place(x=10,y=100)

root.mainloop() 

