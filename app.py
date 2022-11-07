import sys
print(sys.executable)

import tkinter

from tkinter import *

from functools import partial

from PIL import ImageTk, Image

from Registerpage import RegisterPage



#Define our interface

tkLogin=Tk()
tkLogin.geometry('500x500')
tkLogin.title('GMY Login Page')
#set the background
#imageBackground=Image.open('C:/Robert Andrei/Facultate/FEUP/Software Design/Source code/background.png')
#Backgrooundresize=imageBackground.resize((700,700)) #The resize is made before ImageTk
#bg=ImageTk.PhotoImage(Backgrooundresize)


#labelBack=Label(tkLogin,image=bg)
#labelBack.place(x=0,y=0)

#Add the Logo


Logo=Image.open('C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\Logo2.png')
LogoResiz=Logo.resize((100,100))
LogoRend=ImageTk.PhotoImage(LogoResiz)
LogoLabel=Label(bg='#C97E48',image=LogoRend)

LogoLabel.pack()

tkLogin.configure(bg='#C97E48')


title=Label(tkLogin,text='Login')
title.place(relx=0.5,rely=0.2,anchor=CENTER)

#Labels and entry for usernames

usernameLabel=Label(tkLogin,text='Username')
usernameLabel.place(relx=0.3,rely=0.5,anchor=CENTER)
username=StringVar()
usernameEntry=Entry(tkLogin,textvariable=username)
usernameEntry.place(relx=0.5,rely=0.5,anchor=CENTER)

#Labels and entry for passwords

passwordLabel=Label(tkLogin,text='Password')
passwordLabel.place(relx=0.3,rely=0.6,anchor=CENTER)
password=StringVar()
passwordEntry=Entry(tkLogin,textvariable=password)
passwordEntry.place(relx=0.5,rely=0.6,anchor=CENTER)


#This method  is used to create a new window after we press the Login button
def openNewWindow():
    newWindow=Toplevel(tkLogin)
    newWindow.title('New Window')

    newWindow.geometry('500x500')
    newWindow.configure(bg='#C97E48')

    Label(newWindow,text='This is a new window').pack()

   

#This method will help us opening the register page which was created by the Registerpage class (Registerpage.py)
def ForRegister():
    
    pageR=RegisterPage()
    pageR.page()
   
#Create the Login button

Loginbtn=Button(tkLogin,text='Login',bd='5',command=openNewWindow)
Loginbtn.place(relx=0.45,rely=0.8)

Registerbtn=Button(tkLogin,text='Register',bd='5',command=ForRegister)
Registerbtn.place(relx=0.44,rely=0.9)

tkLogin.mainloop()



