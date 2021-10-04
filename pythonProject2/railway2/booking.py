from tkinter import *
import mysql.connector
from tkinter import messagebox
con = mysql.connector.connect(host="localhost",user ="root",passwd ="Bankim@12345",db="railway1")
if con:
    print("connection done")
else:
    print("connection failed")

def getvals():
    def login():
        pass

    root = Tk()
    root.title("Welcome to indian railway login page")
    root["bg"] = "black"
    root.geometry("655x333")

    user = Label(root, text="username", bg="yellow")

    password = Label(root, text="password", bg="yellow")

    user.grid(row=4, column=6,padx=20,pady=20)
    password.grid(row=5, column=6,padx=20,pady=20)
    uservalue = StringVar()
    passvalue = StringVar()
    userentry = Entry(root, textvariable=uservalue, bg="Dark red")
    passentry = Entry(root, textvariable=passvalue, bg="Dark red")
    userentry.grid(row=4, column=8)
    passentry.grid(row=5, column=8)
    Button( root,text="submit", bg="red", command=login).grid(row=10, column=8)
    root.mainloop()

