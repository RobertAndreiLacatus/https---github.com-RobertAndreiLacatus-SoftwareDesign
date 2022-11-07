import tkinter

from tkinter import *

from functools import partial

from PIL import ImageTk, Image


class RegisterPage:
    
        
    def page(self):

   

        Register=Tk()
        Register.geometry('500x500')
        Register.title('Register')

        Register.configure(bg='#C97E48')
        titleReg=Label(Register,text='Create your account')
        titleReg.place(relx=0.5,rely=0.2,anchor=CENTER)

        usernameRegLabel=Label(Register,text='Username')
        usernameRegLabel.place(relx=0.3,rely=0.5,anchor=CENTER)
        usernameRe=StringVar()
        usernameReEntry=Entry(Register,textvariable=usernameRe)
        usernameReEntry.place(relx=0.5,rely=0.5,anchor=CENTER)

        #Labels and entry for passwords

        passwordReLabel=Label(Register,text='Password')
        passwordReLabel.place(relx=0.3,rely=0.6,anchor=CENTER)
        passwordRe=StringVar()
        passwordReEntry=Entry(Register,textvariable=passwordRe)
        passwordReEntry.place(relx=0.5,rely=0.6,anchor=CENTER)

        emailReLabel=Label(Register,text='Email')
        emailReLabel.place(relx=0.3,rely=0.7)
        emailRe=StringVar()
        emailReEntry=Entry(Register,textvariable=emailRe)
        emailReEntry.place(relx=0.5,rely=0.715, anchor=CENTER)


        ageReLabel=Label(Register,text='Age')
        ageReLabel.place(relx=0.3,rely=0.8,anchor=CENTER)
        ageRe=StringVar()
        ageReEntry=Entry(Register,textvariable=ageRe)
        ageReEntry.place(relx=0.5,rely=0.8,anchor=CENTER)


        phoneReLabel=Label(Register,text='Phone Number')
        phoneReLabel.place(relx=0.27,rely=0.9,anchor=CENTER)
        phoneRe=StringVar()
        phoneReEntry=Entry(Register,textvariable=phoneRe)
        phoneReEntry.place(relx=0.37,rely=0.9)

        #Labels and entry for passwords




