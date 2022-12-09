import sys

print(sys.executable)

import tkinter  as tk

from tkinter import ttk

from functools import partial

from tkinter import *

from tkinter import messagebox

from PIL import Image, ImageTk


import hamburger
class MainSub():
    def __init__(self):
        pass
    def subpage(self):
        
        subscriptionpage=tk.Toplevel()
        subscriptionpage.geometry('500x500')
        subscriptionpage.title('GMY Subscription')
        subscriptionpage.resizable(0,0)

        subscriptionpage.configure(bg='#C97E48')

        #Creating header using Canva function

        def hamb():
            new=hamburger.Hamburger()
            new.toggle_win(subscriptionpage)
        

        
        
        w,h=(550,100)

        canvas=tk.Canvas(subscriptionpage,height=h,width=w)
        canvas.pack()
        bg=tk.PhotoImage(file="headerbackground.png")
        bg_1=tk.Label(subscriptionpage,image=bg)
        bg_1.place()


        Logo=Image.open('C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\Logo2.png')
        LogoResiz=Logo.resize((100,100))
        LogoRend=ImageTk.PhotoImage(LogoResiz)
        LogoLabel=Label(subscriptionpage,image=LogoRend)
        LogoLabel.place(relx=0,rely=0)



        

        
        photoHamburger=PhotoImage(file=r"C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\hamburger.png")
        photoHamburgerResize=photoHamburger.subsample(7,7)

        Hamburgerbtn=tk.Button(subscriptionpage,image=photoHamburgerResize,command=hamb,text='Login',bd='0')
        Hamburgerbtn.place(relx=0.9,rely=0.1,anchor=CENTER)

        TitleLabel=tk.Label(subscriptionpage,text='Your subscriptions',bg="#C97E48",font='Helvetica 14 bold')
        TitleLabel.place(relx=0.3,rely=0.3)

        
        def demoColorChange1():
             btnPremium.configure(bg='yellow')
             btnPremium2.configure(bg='white')
             textLabel=Label(subscriptionpage, text= "You bought the Premium subscription!   ",bg="#C97E48" ,font= ('Helvetica 10 bold')).place(relx=0.25,rely=0.8)
             
        def demoColorChange2():
             btnPremium2.configure(bg='yellow')
             btnPremium.configure(bg='white')
             textLabel=Label(subscriptionpage, text= "You bought the Regular subscription!  ",bg="#C97E48" ,font= ('Helvetica 10 bold')).place(relx=0.25,rely=0.8)

        btnPremium= Button(subscriptionpage,text='Premium subscription',command=demoColorChange1,height=2,width=40)
        btnPremium.place(relx=0.2,rely=0.4)

        
        btnPremium2=Button(subscriptionpage,text='Regular subscription',command=demoColorChange2,height=2,width=40)
        btnPremium2.place(relx=0.2,rely=0.6)

        subscriptionpage.mainloop()
        
