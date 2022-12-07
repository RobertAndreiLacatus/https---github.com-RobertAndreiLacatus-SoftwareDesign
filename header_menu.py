import sys

print(sys.executable)

import tkinter

import tkinter as tk

from tkinter import ttk

from functools import partial

from tkinter import *

from tkinter import messagebox

from PIL import Image, ImageTk



from hamburber import Toggle

class Header():
        def __init__(self,root):
                self.header=root
        def createHeader(self):
    
        
        #Creating header using Canva function
                w,h=(550,100)

                canvas=tk.Canvas(self.header,height=h,width=w)
                canvas.pack()
        
                #bg=ImageTk.PhotoImage(file="headerbackground.png")
                #bg_1=tk.Label(self.header,image=bg)
                #bg_1.place()

                #bg=Image.open('headerbackground.png')
                #bgResize=bg.resize((75,75))
                bg=tk.PhotoImage(file="C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\headerbackground.png")
                bg_1=tk.Label(self.header,image=bg)
                bg_1.place()


                Logo=Image.open('C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\Logo2.png')
                LogoResiz=Logo.resize((100,100))
                LogoRend=ImageTk.PhotoImage(LogoResiz)
                LogoLabel=Label(self.header,image=LogoRend)
                LogoLabel.place(relx=0,rely=0)

                Ham=Image.open('C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\hamburger.png')
                HamResiz=Ham.resize((65,65))
                HamRend=ImageTk.PhotoImage(HamResiz)
       # HamLabel=Label(root,image=HamRend)
       # HamLabel.place(relx=0.9,rely=0.1)


    
        #photoHamburger=PhotoImage(file=r"C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\hamburger.png")
        #photoHamburgerResize=photoHamburger.subsample(7,7)

                Hamburgerbtn=tk.Button(self.header,image=HamRend,bd='0',command=Toggle.toggle_win(self.header))
                Hamburgerbtn.place(relx=0.85,rely=0.05)
        
                mainloop() #Creating header using Canva function