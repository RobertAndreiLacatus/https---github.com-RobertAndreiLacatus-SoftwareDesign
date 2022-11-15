import sys

print(sys.executable)

import tkinter as tk


from functools import partial

from tkinter import *

from tkinter import messagebox

from PIL import Image, ImageTk


class QRcode():

    def openQR(self):

        QRcode=tk.Toplevel()
        QRcode.geometry('300x300')
        QRcode.title('This is your QR code')
        QRcode.configure(bg='#C97E48')


        QRphoto=Image.open('C:\Robert Andrei\Facultate\FEUP\Software Design\Source code\source.png')
        QRphotoResiz=QRphoto.resize((300,300))
        QRrende=ImageTk.PhotoImage(QRphotoResiz)
        QRLabel=Label(QRcode,image=QRrende,bg='#C97E48')
        QRLabel.place(relx=0.5,rely=0.5,anchor=CENTER)
        

   
        mainloop()