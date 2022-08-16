#Importing modules
import pandas as pd
from glob import glob
import os
import tkinter
import csv
import tkinter as tk
from tkinter import *
import mysql.connector



#MySQL server credentials
mydb = mysql.connector.connect(
  host="localhost",
  user="XXXXX",
  password="XXXXX",
  database="XXXXX"
)

mycursor = mydb.cursor(buffered=True)


#Realtime visitors function
def realtime_visitors(text_to_speech):
    def check_host_visitors():
        Hostname = HostTxt.get()
        if HostTxt=="":
            t='Please enter a host name or else please choose view all visitors '
            text_to_speech(t)
        
        mycursor.execute(f"SELECT * FROM full_data WHERE host_name='{Hostname}';")

        myresult = mycursor.fetchall()


        if myresult==[]:
            t="Please enter a valid host name"
            text_to_speech(t)
        else:
            root = tkinter.Tk()
            root.title("Admin Page ")
            root.configure(background="black")
            r = 0
            for col in myresult:
                c = 0
                for row in col:
                    
                    label = tkinter.Label(
                        root,
                        width=10,
                        height=1,
                        fg="red",
                        font=("times", 15, " bold "),
                        bg="black",
                        text=row,
                        relief=tkinter.RIDGE,
                    )
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
            root.mainloop()


    #Tkinter GUI Intialization 
    subject = Tk()
    subject.title("Real time visitor viewing page")
    subject.geometry("580x320")
    subject.resizable(0, 0)
    subject.configure(background="black")
    titl = tk.Label(subject, bg="black", relief=RIDGE, bd=10, font=("arial", 30))
    titl.pack(fill=X)

    #Title label
    titl = tk.Label(
        subject,
        text="Real time visitor viewing page",
        bg="black",
        fg="green",
        font=("arial", 25),
    )
    titl.place(x=100, y=12)

    #HostLabel
    HostLabel = tk.Label(
        subject,
        text="Enter Host Name",
        width=15,
        height=2,
        bg="black",
        fg="red",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 15),
    )
    HostLabel.place(x=30, y=100)

    #HostTxt
    HostTxt = tk.Entry(
        subject,
        width=15,
        bd=5,
        bg="black",
        fg="red",
        relief=RIDGE,
        font=("times", 30, "bold"),
    )
    HostTxt.place(x=230, y=100)

    #Viewresult
    ViewResult = tk.Button(
        subject,
        text="View results",
        command=check_host_visitors,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="red",
        height=2,
        width=12,
        relief=RIDGE,
    )
    ViewResult.place(x=110, y=170)


    #View all visitors function
    def Viewallvisitors():
        mycursor.execute("SELECT * FROM full_data;")

        myresult2 = mycursor.fetchall()

        root2 = tkinter.Tk()
        root2.title("Admin Page ")
        root2.configure(background="black")
        r = 0
        for col in myresult2:
            c = 0
            for row in col:
                    
                label = tkinter.Label(
                    root2,
                    width=10,
                    height=1,
                    fg="red",
                    font=("times", 15, " bold "),
                    bg="black",
                    text=row,
                    relief=tkinter.RIDGE,
                )
                label.grid(row=r, column=c)
                c += 1
            r += 1
        root2.mainloop()


    #View all visitors button
    vav = tk.Button(
        subject,
        text="View all visitors",
        command=Viewallvisitors,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="red",
        height=2,
        width=15,
        relief=RIDGE,
    )
    vav.place(x=290, y=170)
    subject.mainloop()

