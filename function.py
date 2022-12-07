import sys
print(sys.executable)

from tkinter import ttk

import tkinter as tk

from tkinter import *

from functools import partial

from PIL import ImageTk, Image

from eva2 import *


from phyEvaluation import *

from onlys import *

class Methods():
    def closeWindow(self):
                #newvar=createlogin.tkLogin
                #btn=Button(MainPageClass,command=newvar.withdraw)
                #btn.pack()
                pass
    def openSub(self):
                newpage2=MainSub()
                newpage2.subpage()
    def openPhy(self):
                newpage3=Phy()
                newpage3.evaluation()
    def openNut(self):
                newpage4=Nutrition()
                newpage4.plan()

