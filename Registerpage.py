
import sys
print(sys.executable)
import tkinter as tk

from tkinter import *

from functools import partial

from PIL import ImageTk, Image

from tkinter import messagebox



class RegisterPage:
    

    
    def page(self):

   

        Register=tk.Toplevel()
        Register.geometry('500x500')
        Register.title('Register')


        Register.configure(bg='#C97E48')

        LogoRegister=PhotoImage(file=r"C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\RegisterLogo.png")
        LogoRegisterImage=LogoRegister.subsample(4,4)

        
        titleReg=Label(Register,text='Create your account',image=LogoRegisterImage,bg='#C97E48')
        titleReg.place(relx=0.5,rely=0.2,anchor=CENTER)

        usernameRegLabel=Label(Register,text='Username',bg='#C97E48')
        usernameRegLabel.place(relx=0.3,rely=0.35,anchor=CENTER)
        usernameRe=StringVar()
        usernameReEntry=Entry(Register,textvariable=usernameRe)
        usernameReEntry.place(relx=0.5,rely=0.35,anchor=CENTER)

        #Labels and entry for passwords

        passwordReLabel=Label(Register,text='Password',bg='#C97E48')
        passwordReLabel.place(relx=0.3,rely=0.45,anchor=CENTER)
        passwordRe=StringVar()
        passwordReEntry=Entry(Register,textvariable=passwordRe)
        passwordReEntry.place(relx=0.5,rely=0.45,anchor=CENTER)

        emailReLabel=Label(Register,text='Email',bg='#C97E48')
        emailReLabel.place(relx=0.3,rely=0.55)
        emailRe=StringVar()
        emailReEntry=Entry(Register,textvariable=emailRe)
        emailReEntry.place(relx=0.5,rely=0.56, anchor=CENTER)


        ageReLabel=Label(Register,text='Age',bg='#C97E48')
        ageReLabel.place(relx=0.3,rely=0.65,anchor=CENTER)
        ageRe=StringVar()
        ageReEntry=Entry(Register,textvariable=ageRe)
        ageReEntry.place(relx=0.5,rely=0.65,anchor=CENTER)


        phoneReLabel=Label(Register,text='Phone Number',bg='#C97E48')
        phoneReLabel.place(relx=0.27,rely=0.75,anchor=CENTER)
        phoneRe=StringVar()
        phoneReEntry=Entry(Register,textvariable=phoneRe)
        phoneReEntry.place(relx=0.37,rely=0.75)

        #Labels and entry for EnterButton

        

        #RegisterImage=Image.open('C:/Robert Andrei/Facultate/FEUP/Software Design/Source code/buttonenr.png')
        #RegisterResize=RegisterImage.resize((100,100))
        #RegisterRend=ImageTk.PhotoImage(RegisterResize)
        #RegisterLabel=Label(bg='#C97E48',image=RegisterRend)
        #RegisterLabel.pack()

        

        def approvement():
            if (usernameReEntry.get()=="") or (ageReEntry.get()=="") or (phoneReEntry.get()=="") or (passwordReEntry.get()=="") or (emailReEntry.get()==""):
                messagebox.showerror('Error','Please fill the all empty spaces')
            else:
                NextPage=tk.Toplevel()
                NextPage.geometry('500x500')
                NextPage.title('NextPage')

                



        ButtonRegister=PhotoImage(file=r"C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\anotherregister.png")
        ButtonRegisterImage=ButtonRegister.subsample(5,5)

      

        Enterbtn=tk.Button(Register,text='Enter',image=ButtonRegisterImage,bd='0',background='#C97E48',command=approvement)
        Enterbtn.pack()
        Enterbtn.place(relx=0.5,rely=0.9,anchor=CENTER)
       
        mainloop()



