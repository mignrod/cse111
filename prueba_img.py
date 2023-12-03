from tkinter import *
import sys
from datetime import *
import time
import random
import os       
import threading
import sched
from sched import *
import pickle
hora1=15
hora2=21
hora3=16
fichero = open("Imagen.txt", "w")
obj=-1
pickle.dump(obj, fichero)
fichero.close()
fichero=open("Imagen.txt","r")
obj=pickle.load(fichero)
class SplashScreen(Frame):
     def __init__(self, master=None, useFactor=True):
            Frame.__init__(self, master)
            self.master.geometry("1366x768+0+0")
            self.master.config(bg="black")
            self.master.overrideredirect(True)
            self.lift()
def p():
     root = Tk()
     sp = SplashScreen(root)
     sp.config(bg="black")
     fichero.close()
     Img1=PhotoImage(file="Libre.gif")
     Img2=PhotoImage(file="Soy.gif")
     Img3=PhotoImage(file="universe.gif")
     Img4=PhotoImage(file="BBN.gif")
     Img5=PhotoImage(file="tr.gif")
     Img6=PhotoImage(file="final.gif")
     Img7=PhotoImage(file="alc.gif")
     Img8=PhotoImage(file="cer.gif")
     Img9=PhotoImage(file="at.gif")
     Img10=PhotoImage(file="bos.gif")
     Img11=PhotoImage(file="se.gif")
     #Img=PhotoImage(file=".gif")
     Imagenes=[Img1,Img2,Img3,Img4,Img5,Img7,Img8,Img9,Img10,Img11]
     Imgf=obj
     Imagenf=Imagenes[Imgf]
     #logo=Label(root,image=Img6).place(x=00,y=00)
     lbl=Label(root,image=Imagenf).place(x=00,y=00)
     #lbl2=Label(root,image=Img10).place(x=00,y=00)
     root.after(20000,root.destroy)
     root.mainloop()
def t():
     root = Tk()
     sp = SplashScreen(root)
     sp.config(bg="black")
     Img6=PhotoImage(file="final.gif")
     logo=Label(root,image=Img6).place(x=00,y=00)
     root.after(2000,root.destroy)
     root.mainloop()
p=threading.Thread(target=p)
t=threading.Thread(target=t)
if (hora3 == datetime.now().hour) or ((datetime.now().hour == hora2) or(datetime.now().hour == hora1)):
     p.start()
     t.start()