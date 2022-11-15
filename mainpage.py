import sys

print(sys.executable)

import tkinter as tk


from functools import partial

from tkinter import *

from tkinter import messagebox

from PIL import Image, ImageTk

from QRcodepage import QRcode



class MainPage():
    def pageMain(self):
        MainPageClass=tk.Toplevel()
        MainPageClass.geometry('500x500')
        MainPageClass.title('MainPage')

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


        Logo=Image.open('C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\Logo2.png')
        LogoResiz=Logo.resize((100,100))
        LogoRend=ImageTk.PhotoImage(LogoResiz)
        LogoLabel=Label(MainPageClass,image=LogoRend)
        LogoLabel.place(relx=0,rely=0)
      

        

        
        photoHamburger=PhotoImage(file=r"C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\hamburger.png")
        photoHamburgerResize=photoHamburger.subsample(7,7)

        Hamburgerbtn=tk.Button(MainPageClass,image=photoHamburgerResize,text='Login',bd='0')
        Hamburgerbtn.place(relx=0.9,rely=0.1,anchor=CENTER)

        #This is the end of our code for the Canva area
        TitleLabel=tk.Label(MainPageClass,text='Welcome to your digital gym friend',bg="#C97E48",font='Helvetica 14 bold')
        TitleLabel.place(relx=0.18,rely=0.3)

        QRbutton=tk.Button(MainPageClass,text='QR Code',bd='4',command=code)
        QRbutton.place(relx=0.45,rely=0.38)

        
        mainloop()

