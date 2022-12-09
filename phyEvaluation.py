import sys


print(sys.executable)

import tkinter  as tk

from tkinter import ttk

from functools import partial

from tkinter import *

from PIL import Image, ImageTk

import hamburger


class Phy():
    def __init__(self):
        pass
    def evaluation(self):
        
        eva=tk.Toplevel()
        eva.geometry('500x500')
        eva.title('Physical Evaluation')
        eva.resizable(0,0)
        eva.configure(bg='#C97E48')

        def hamb():
            new=hamburger.Hamburger()
            new.toggle_win(eva)

        #Creating header using Canva function



        
        
        w,h=(550,100)

        canvas=tk.Canvas(eva,height=h,width=w)
        canvas.pack()

        
        bg1=PhotoImage(file="headerbackground.png")
        bg_12=ttk.Label(eva,image=bg1)
        bg_12.place()


        Logo1=Image.open('C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\Logo2.png')
        LogoResiz1=Logo1.resize((100,100))
        LogoRend1=ImageTk.PhotoImage(LogoResiz1)
        LogoLabel1=Label(eva,image=LogoRend1)
        LogoLabel1.place(relx=0,rely=0)
    

 
        photoHamburger=PhotoImage(file=r"C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\hamburger.png")
        photoHamburgerResize=photoHamburger.subsample(7,7)

        Hamburgerbtn=tk.Button(eva,image=photoHamburgerResize,command=hamb,text='Login',bd='0')
        Hamburgerbtn.place(relx=0.9,rely=0.1,anchor=CENTER)

        TitleLabel=tk.Label(eva,text='Your physical evaluation',bg="#C97E48",font='Helvetica 14 bold')
        TitleLabel.place(relx=0.27,rely=0.3)

        photoContact=PhotoImage(file=r"C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\ContactTrainerButton.png")
        photoContactResize=photoContact.subsample(7,7)

        def popwin():
            top=Toplevel()
            top.geometry('200x200')
            top.configure(bg='#C97E48')
            Label(top,text='Text your message',background='#C97E48').place(relx=0.3,rely=0)
            def deletevar():
                entry.delete(0,END)
            entryRe=StringVar()
            entry=Entry(top,width=25,textvariable=entryRe)
            entry.place(relx=0.15,rely=0.1)

            ButtonRegister=PhotoImage(file=r"C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\anotherregister.png")
            ButtonRegisterImage=ButtonRegister.subsample(3,3)

            SendButton=tk.Button(top,text='Insert',bd='3',command=deletevar)
            SendButton.place(relx=0.4,rely=0.3)

        ContactButton=tk.Button(eva,image=photoContact,bd='0',bg='#C97E48',command=popwin)
        ContactButton.place(relx=0.23,rely=0.4)

        LabelName=tk.Label(eva,text='Name of your Trainer',bg='#C97E48',font=('Times New Roman',12,'italic'))
        LabelName.place(relx=0.05,rely=0.55)

        LabelReName=StringVar()
        LabenReNameEntry=Entry(eva,width=35,textvariable=LabelReName)
        LabenReNameEntry.place(relx=0.5,rely=0.55)

        LabelName2=tk.Label(eva,text='Physical Evaluation',bg='#C97E48',font=('Times New Roman',12,'italic'))
        LabelName2.place(relx=0.05,rely=0.7)

        #frame=Frame(eva,height=130,width=210)
        #frame.pack(expand=True,fill=BOTH).place(relx=0.5,rely=0.7)
        c=Canvas(eva,bg='white',height=130,width=210)
        c.place(relx=0.5,rely=0.7)
        #vbar=Scrollbar(frame,orient=VERTICAL)
        #vbar.pack(side=RIGHT,fill=Y)
        #vbar.config(command=c.yview)
        #c.config(width=210,height=130)
        #c.config(yscrollcommand=vbar.set)

        eva.mainloop()
