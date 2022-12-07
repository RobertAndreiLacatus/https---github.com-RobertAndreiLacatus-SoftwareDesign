import sys

print(sys.executable)

import tkinter  as tk

from tkinter import ttk

from functools import partial

from tkinter import *

from tkinter import messagebox

from PIL import Image, ImageTk


from phyEvaluation import Phy

from  eva2 import Nutrition

class MainSub():
    def __init__(self):
        pass
    def subpage(self):
        
        subscriptionpage=tk.Tk()
        subscriptionpage.geometry('500x500')
        subscriptionpage.title('GMY Subscription')
        subscriptionpage.resizable(0,0)

        subscriptionpage.configure(bg='#C97E48')

        
        def toggle_win():
            f1=Frame(subscriptionpage,width=300,height=500,bg='#262626')
            f1.place(x=300,y=0)

            #create the rest of the buttons
            def bttn(x,y,text,bcolor,fcolor,cmd):
                def on_entera(e):
                    myButton1['background']=bcolor #ffcc66
                    myButton1['foreground']='#ab6038' #000d33
                def on_leavea(e):
                    myButton1['background']=fcolor
                    myButton1['foreground']='#262626'
                
                myButton1=Button(f1,text=text,width=24,height=2,fg='#262626'
                ,border=0,bg=fcolor,activeforeground='#262626'
                ,activebackground=bcolor,command=cmd)

                myButton1.bind("<Enter>",on_entera)
                myButton1.bind("<Leave>",on_leavea)

                myButton1.place(x=x,y=y)
            def closeWindow(self):
                #newvar=createlogin.tkLogin
                #btn=Button(MainPageClass,command=newvar.withdraw)
                #btn.pack()
                pass
            def openSub():
                newpage2=MainSub()
                newpage2.subpage()
            def openPhy():
                newpage3=Phy()
                newpage3.evaluation()
            def openNut():
                newpage4=Nutrition()
                newpage4.plan()

            bttn(13,140,'HOME','#0f9d9a','#14c4c0',None)
            bttn(13,200,'SUBSCRIPTION','#0fd9da','#14c4c0',openSub)
            bttn(13,260,'NUTRITIONAL PLAN','#0fd9da','#14c4c0',openNut)
            bttn(13,320,'PHYSICAL EVALUATION','#0fd9da','#14c4c0',openPhy)
            bttn(13,380,'LOG OUT','#0fd9da','#14c4c0',closeWindow)
           

            def dele():
                f1.destroy()

            #global img2
            #img2=ImageTk.PhotoImage(Image.open('x.png'))
            


            
            Button(f1,text='X',command=dele).place(x=5,y=10)

        #Creating header using Canva function



        
        
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

        Hamburgerbtn=tk.Button(subscriptionpage,image=photoHamburgerResize,command=toggle_win,text='Login',bd='0')
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
        
