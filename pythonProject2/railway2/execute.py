from railway2.registration import *
from railway2.login import *
from railway2.booking import *
from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk

con = mysql.connector.connect(host="localhost",user ="root",passwd ="Bankim@12345",database="railway1")
if con.is_connected ():
    print("connection done")
else:
    print("connection failed")
root=Tk()
root.title("Railway reservation system")
root["bg"] = "Lavender"
root.geometry("655x345")
f1 = Frame(root ,borderwidth=6,relief=SUNKEN).pack()
Label(root,text="welcome to railway",font="comicsansms 13 bold").pack()
mn=Menu(root)
homemenu=Menu(mn,tearoff=0)
homemenu.add_command(label="home")
mn.add_cascade(label="home",menu=homemenu,font="20")
loginmenu=Menu(mn,tearoff=0)
loginmenu.add_command(label="login",command=getvals)
mn.add_cascade(label="login",menu=loginmenu,font="20")
ticketbooking=Menu(mn,tearoff=0)
ticketbooking.add_command(label="ticket",command=ticketbooking)
mn.add_cascade(label="ticket",menu=ticketbooking,font="25")
registermenu=Menu(mn,tearoff=0)
registermenu.add_command(label="registration",command= registrationpage)
mn.add_cascade(label="register",menu=registermenu,font="30")
exitmenu=Menu(mn,tearoff=0)
exitmenu.add_command(label="exit")
mn.add_cascade(label="exit",menu="exitmenu")

root.config(menu=mn)
root.minsize(655,300)
root.maxsize(1000,1100)
#photo = PhotoImage(file="trian_PNG101351.png")
image = Image.open("train.jpg")
photo = ImageTk.PhotoImage(image)
ticket_Label = Label(image=photo)
ticket_Label.pack(side=TOP)
title_label = Label(text="Indian railway ia oldest railway .it gives employment lagest people in world "
                         "copyright 2021,centre for railway information designed and hosted by Bankim",bg="purple",fg="red",padx=5,pady=10,font="comicsansms 9 bold",borderwidth=3,relief=SUNKEN )

title_label.pack(side=BOTTOM, fill=Y,padx=20,pady=35)


root.mainloop()
