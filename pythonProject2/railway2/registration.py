from tkinter import *
import mysql.connector as c
from tkinter import messagebox
from tkinter import *

def registrationpage():
    def insert():
        inname=ename.get()
        inpassword =epass.get()
        inemail=eemail.get()
        inAdhaarno=edate.get()


        con=c.connect(host="localhost",user="root",passwd="Bankim@12345",db="railway1")
        if(con):
            cursor=con.cursor(prepared=True)
            pre_qry="insert into reg values(%s,%s,%s,%s)"
            cursor.execute(pre_qry)
            con.commit()
            if cursor.rowcount!=0:
                messagebox.showinfo("insert info","Registration sucessful")
            else:
                messagebox.showinfo("error","fail to register")

    root = Tk()
    root["bg"] = "brown"
    root.title("railway registration")
    root.geometry("655x455")
    lb1 = Label(root, text="user name", bg="lightgreen")
    lb2 = Label(root, text="user password", bg="lightgreen")
    lb4 = Label(root, text="Email", bg="lightgreen")
    lb5 = Label(root, text="Addar number", bg="lightgreen")
    ename = Entry(root, font="Elephant 15", width=30, bg="lightgreen")
    epass = Entry(root, show="*", font="Elephant 15", width=30, bg="lightgreen")
    eemail = Entry(root, font="Elephant 15", width=30, bg="lightgreen")
    edate = Entry(root, font="Elephant 15", width=30, bg="lightgreen")
    loginbtn = Button(root, text="Registration", command=insert, font="Elephant 15", width=20, bg="lightgreen")
    lb1.grid(row=1, column=1, padx=10, pady=20)
    ename.grid(row=1, column=2, padx=20, pady=20)
    lb2.grid(row=2, column=1, padx=10, pady=20)
    epass.grid(row=2, column=2, padx=20, pady=20)
    lb4.grid(row=4, column=1, padx=10, pady=20)
    eemail.grid(row=4, column=2, padx=20, pady=20)
    lb5.grid(row=5, column=1, padx=10, pady=20)
    edate.grid(row=5, column=2, padx=20, pady=20)
    loginbtn.grid(row=6, column=1, padx=20, pady=20)
    root.mainloop()
