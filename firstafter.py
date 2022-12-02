import sys

print(sys.executable)

import tkinter as tk

from tkinter import ttk

from functools import partial

from tkinter import *

from tkinter import messagebox

from PIL import Image, ImageTk

from QRcodepage import QRcode





class ThePage():
    
    def pageMain(self):
        MainPageClass=tk.Toplevel()
        MainPageClass.geometry('500x500')
        MainPageClass.title('MainPage')
        MainPageClass.resizable(0,0)
        MainPageClass.configure(bg='#C97E48')

        #Create a main frame
        #main_frame=Frame(MainPageClass)
        #main_frame.pack(fill=BOTH,expand=1)
        #Create canvas
        #my_canvas=Canvas(main_frame)
        #my_canvas.pack(side=LEFT,fill=BOTH, expand=1)


        #Add a ScrollBar to the Canvas
        #my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL)
        #my_scrollbar.pack(side=RIGHT,fill=Y)


        #Configure the canvas
        #main_frame.configure(yscrollcommand=my_scrollbar.set)
        #my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scollregion=my_canvas.bbox("all")))

        #Create another frame inside the canvas
        #second_frame=Frame(my_canvas)
        #Add that new frame to a window in the Canvas
        #my_canvas.create_window((0,0),window=second_frame,anchor="nw")

        #create hamburger menu
        def toggle_win():
            f1=Frame(MainPageClass,width=300,height=500,bg='#262626')
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

            def closeWindow():
                #newvar=createlogin.tkLogin
                #btn=Button(MainPageClass,command=newvar.withdraw)
                #btn.pack()
                pass
          


            bttn(13,140,'HOME','#0f9d9a','#14c4c0',None)
            bttn(13,200,'SUBSCRIPTION','#0fd9da','#14c4c0',None)
            bttn(13,260,'NUTRITIONAL PLAN','#0fd9da','#14c4c0',None)
            bttn(13,320,'PHYSICAL EVALUATION','#0fd9da','#14c4c0',None)
            bttn(13,380,'LOG OUT','#0fd9da','#14c4c0',closeWindow)
           

            def dele():
                f1.destroy()

            #global img2
            #img2=ImageTk.PhotoImage(Image.open('x.png'))
            


            
            Button(f1,text='X',command=dele).place(x=5,y=10)

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

        Hamburgerbtn=tk.Button(MainPageClass,image=photoHamburgerResize,command=toggle_win,text='Login',bd='0')
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

