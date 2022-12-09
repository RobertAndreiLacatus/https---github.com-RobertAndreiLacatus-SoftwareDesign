from eva2 import Nutrition

from onlys import MainSub
from phyEvaluation import Phy


from tkinter import *



def closeWindow():
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

 
class Hamburger():
 #create hamburger menu
    def __init__(self):
        self.window=None
    def toggle_win(self,root):
            self.window=root
            f1=Frame(self.window,width=300,height=500,bg='#262626')
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
