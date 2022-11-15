import sys
print(sys.executable)

from tkinter import ttk

import tkinter as tk

from tkinter import *

from functools import partial

from PIL import ImageTk, Image

from Registerpage import RegisterPage

from mainpage import MainPage


from tkinter import messagebox




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

LoginIcon=Image.open('C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\SettingIcon.png')
LoginResize=LoginIcon.resize((100,100))
LoginRend=ImageTk.PhotoImage(LoginResize)
LoginLabel=Label(bg='#C97E48',image=LoginRend)
LoginLabel.place(relx=0.1,rely=0.1)
LoginLabel.pack()

tkLogin.configure(bg='#C97E48')



#title=Label(tkLogin,text='Login')
#title.place(relx=0.5,rely=0.2,anchor=CENTER)

#Labels and entry for usernames

usernameLabel=Label(tkLogin,text='Username',bg='#C97E48')
usernameLabel.place(relx=0.3,rely=0.5,anchor=CENTER)
username=StringVar()
usernameEntry=Entry(tkLogin,textvariable=username)
usernameEntry.place(relx=0.5,rely=0.5,anchor=CENTER)

#Labels and entry for passwords




#This method  is used to create a new window after we press the Login button
def openNewWindow():
    newPage=MainPage()
    newPage.pageMain()
    

passwordLabel=Label(tkLogin,text='Password',bg='#C97E48')
passwordLabel.place(relx=0.3,rely=0.6,anchor=CENTER)
password=StringVar()
passwordEntry=Entry(tkLogin,textvariable=password,show='*')
passwordEntry.place(relx=0.5,rely=0.6,anchor=CENTER)


def loginVariables():
    if (usernameEntry.get()=="" and passwordEntry.get()==""):
        messagebox.showerror("Login error","Please, introduce your credentials.")
    else:
        openNewWindow()
        


   

#This method will help us opening the register page which was created by the Registerpage class (Registerpage.py)
def ForRegister():
    
    pageR=RegisterPage()
    pageR.page()
   
#Create the Login button

#login_btn_image=Image.open('C:/Robert Andrei/Facultate/FEUP/Software Design/Source code/LoginB.png')
#login_btn_resize=login_btn_image.resize((100,100))
#login_btn_rend=ImageTk.PhotoImage(login_btn_resize)
#loginLabel=Label(bg='#C97E48',image=login_btn_rend)
#loginLabel.pack()


photoLogin=PhotoImage(file=r"C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\LoginB.png")
photoImageLogin=photoLogin.subsample(5,5)


photoRegister=PhotoImage(file=r"C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\Registernow.png")
photoRegisterImage=photoRegister.subsample(6,6)


Loginbtn=tk.Button(tkLogin,image=photoImageLogin,text='Login',bd='0',command=loginVariables,bg="#C97E48",anchor=CENTER)
Loginbtn.place(relx=0.5,rely=0.7,anchor=CENTER) #side- the place where we want to place the LoginBtn and pady= distance from the margin to the button


Registerbtn=tk.Button(tkLogin,text='Register',image=photoRegisterImage,bd='0',command=ForRegister,bg="#C97E48",anchor=CENTER)
Registerbtn.place(relx=0.5,rely=0.85,anchor=CENTER)






tkLogin.mainloop()



