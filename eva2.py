import sys
print(sys.executable)

import tkinter  as tk

from tkinter import ttk

from functools import partial

from tkinter import *

from tkinter import messagebox

from PIL import Image, ImageTk


from tkinter import messagebox
import hamburger

class Nutrition():
    
    def __init__(self):
        pass
    def plan(self):
       

        nut=tk.Toplevel()
        nut.geometry('500x500')
        nut.title('Nutritional Plan')
        nut.resizable(0,0)
        nut.configure(bg="#C97E48")

        #Creating header using Canva function

        def hamb():
            new=hamburger.Hamburger()
            new.toggle_win(nut)

        w,h=(550,100)

        canvas=tk.Canvas(nut,height=h,width=w)
        canvas.pack()

        
        bg1=PhotoImage(file="headerbackground.png")
        bg_12=ttk.Label(nut,image=bg1)
        bg_12.place()


        Logo1=Image.open('C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\Logo2.png')
        LogoResiz1=Logo1.resize((100,100))
        LogoRend1=ImageTk.PhotoImage(LogoResiz1)
        LogoLabel1=Label(nut,image=LogoRend1)
        LogoLabel1.place(relx=0,rely=0)
    

 
        photoHamburger=PhotoImage(file=r"C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\hamburger.png")
        photoHamburgerResize=photoHamburger.subsample(7,7)

        Hamburgerbtn=tk.Button(nut,image=photoHamburgerResize,command=hamb,text='Login',bd='0')
        Hamburgerbtn.place(relx=0.9,rely=0.1,anchor=CENTER)

        TitleLabel=tk.Label(nut,text='Nutritional Plan',bg="#C97E48",font='Helvetica 12 bold',fg='white')
        TitleLabel.place(relx=0.4,rely=0.3)

        TitleLabel=tk.Label(nut,text='Please enter the date',bg="#C97E48",font='Helvetica 12 bold',fg='white')
        TitleLabel.place(relx=0.35,rely=0.4)

        def deletevar():
                wieghtEntry.delete(0,END)
                heighteEntry.delete(0,END)
                ageeEntry.delete(0,END)
                gendereEntry.delete(0,END)
                typeweighteEntry.delete(0,END)

        def reqfunction():
            if  (wieghtEntry.get()=="") or ( heighteEntry.get()=="") or (ageeEntry.get()=="") or(gendereEntry.get()=="") or (typeweighteEntry.get()==""):
                messagebox.showerror('Error','Please fill the all empty spaces')
            else:
                deletevar()
                messagebox.showinfo('Information','Your request has been sent to your trainer')
        WeightLabel=tk.Label(nut,text='Weight',bg="#C97E48",font=('Times New Roman',12,'italic'),fg='white')
        WeightLabel.place(relx=0.1,rely=0.5)

        wieghte=StringVar()
        wieghtEntry=Entry(nut,textvariable=wieghte)
        wieghtEntry.place(relx=0.4,rely=0.5)
        
        heightLabel=tk.Label(nut,text='Height',bg="#C97E48",font=('Times New Roman',12,'italic'),fg='white')
        heightLabel.place(relx=0.1,rely=0.55)

        heighte=StringVar()
        heighteEntry=Entry(nut,textvariable=heighte)
        heighteEntry.place(relx=0.4,rely=0.55)

        ageLabel=tk.Label(nut,text='Age',bg="#C97E48",font=('Times New Roman',12,'italic'),fg='white')
        ageLabel.place(relx=0.1,rely=0.6)

        agee=StringVar()
        ageeEntry=Entry(nut,textvariable=agee)
        ageeEntry.place(relx=0.4,rely=0.6)

        genderLabel=tk.Label(nut,text='Gender',bg="#C97E48",font=('Times New Roman',12,'italic'),fg='white')
        genderLabel.place(relx=0.1,rely=0.65)

        gendere=StringVar()
        gendereEntry=Entry(nut,textvariable=gendere)
        gendereEntry.place(relx=0.4,rely=0.65)

        typeweight=tk.Label(nut,text='Type weight you want',bg="#C97E48",font=('Times New Roman',12,'italic'),fg='white')
        typeweight.place(relx=0.1,rely=0.7)

        typeweighte=StringVar()
        typeweighteEntry=Entry(nut, textvariable=typeweighte)
        typeweighteEntry.place(relx=0.4,rely=0.7)

        
        photoRequest=PhotoImage(file=r"C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\request.png")
        photoRequestResize=photoRequest.subsample(3,3)

        Requestbtn=tk.Button(nut,image=photoRequestResize,command=reqfunction,text='Login',bd='0',bg='#C97E48')
        Requestbtn.place(relx=0.525,rely=0.85,anchor=CENTER)


        
        nut.mainloop()

