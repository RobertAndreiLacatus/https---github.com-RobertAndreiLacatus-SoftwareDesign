import sys

print(sys.executable)

import tkinter as tk

from tkinter import ttk

from functools import partial

from tkinter import *

from tkinter import messagebox

from PIL import Image, ImageTk

from QRcodepage import QRcode

from hamburger import *



class ThePage():
    
    def pageMain(self):
        MainPageClass=tk.Toplevel()
        MainPageClass.geometry('500x500')
        MainPageClass.title('MainPage')
        MainPageClass.resizable(0,0)
        MainPageClass.configure(bg='#C97E48')

       

      
        
        #Creating header using Canva function
        

        def code():
            code=QRcode()
            code.openQR()
        
        w,h=(550,100)

        canvas=tk.Canvas(MainPageClass,height=h,width=w)
        canvas.pack()
        bg=tk.PhotoImage(file="headerbackground.png")
        bg_1=tk.Label(MainPageClass,image=bg)
        bg_1.place()

        Logo=PhotoImage(file=r"C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\Logo2.png")
        LogoResize=Logo.subsample(15,15)

        LogoLabel=Label(MainPageClass,image=LogoResize)
        LogoLabel.place(relx=0,rely=0)

        def hamburger():
         new=Hamburger()
         new.toggle_win(MainPageClass)
        

        
        photoHamburger=PhotoImage(file=r"C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\hamburger.png")
        photoHamburgerResize=photoHamburger.subsample(7,7)

        Hamburgerbtn=tk.Button(MainPageClass,image=photoHamburgerResize,command=hamburger,text='Login',bd='0')
        Hamburgerbtn.place(relx=0.9,rely=0.1,anchor=CENTER)
      
        #This is the end of our code for the Canva area
        TitleLabel=tk.Label(MainPageClass,text='Welcome to your digital gym friend',bg="#C97E48",font='Helvetica 14 bold')
        TitleLabel.place(relx=0.18,rely=0.3)

        QRbutton=tk.Button(MainPageClass,text='QR Code',bd='4',command=code)
        QRbutton.place(relx=0.45,rely=0.38)

        photoYogaclass=PhotoImage(file=r"C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\yoga.PNG")
        photoYogaResize=photoYogaclass.subsample(2,2)

        YogaLabel=tk.Label(MainPageClass,image=photoYogaResize,border=0)
        YogaLabel.place(relx=0.1,rely=0.5)
        
        YogaText=tk.Label(MainPageClass,text='Yoga Class',border=0,bg='#C97E48', foreground='white',font=('Arial',14))
        YogaText.place(relx=0.13,rely=0.7)

        photoJoin=PhotoImage(file=r'C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\JoinButton.PNG')
        photoJoinResize=photoJoin.subsample(1,1)

        JoinButton=tk.Button(MainPageClass,image=photoJoinResize,command=None,bd='0',bg="#C97E48")
        JoinButton.place(relx=0.5,rely=0.5)

        photoJogging=PhotoImage(file=r'C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\Jogging.PNG')
        photoJoggingResize=photoJogging.subsample(2,2)

        JoggingLabel=tk.Label(MainPageClass,image=photoJoggingResize,border=0)
        JoggingLabel.place(relx=0.1,rely=0.8)

        JoggingText=tk.Label(MainPageClass,text='Jogging Class',border=0,bg='#C97E48', foreground='white',font=('Arial',14))
        JoggingText.place(relx=0.13,rely=1.1)


    

    

        mainloop()
