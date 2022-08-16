#Importing modules 
from cmath import exp
from ssl import Options
import tkinter as tk
from tkinter import *
import os, cv2
from tkinter import ttk
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3
import mysql.connector
from mysql.connector import Error
import re

#Importing all modules from other files
import takeImage
import check_realtime_visitors
import check_out

#Defining all the paths 
haarcasecade_path = "C:\\Users\\XXXXXXXX\XXXXXXXX\\XXXXXXXX\\XXXXXXXX\\haarcascade_frontalface_default.xml"
trainingimagelabel ="C:\\Users\\XXXXXXXX\XXXXXXXX\\XXXXXXXX\\XXXXXXXX\\TrainingImageLabel\\Trainner.yml"
trainimage_path = "C:\\Users\\XXXXXXXX\XXXXXXXX\\XXXXXXXX\\XXXXXXXX\\TrainingImage"
studentdetail_path ="C:\\Users\\XXXXXXXX\XXXXXXXX\\XXXXXXXX\\XXXXXXXX\\StudentDetails\\studentdetails.csv"


#Text to speech function 
def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

#MySQL credentials
pw = "XXXX"
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = create_server_connection("localhost", "root", pw)



#Tkinter GUI Intialization 
window = Tk()
window.title("Main Menu of VMS")
window.geometry("1220x720")
dialog_title = "quit"
dialog_text = "Are you sure want to quit?"
window.configure(background="black")


# To exit the screen
def del_sc1():
    sc1.destroy()


# Error message function for name and phone number
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="black")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Phone number & Name required!",
        fg="red",
        bg="black",
        font=("times", 20, " bold "),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="red",
        bg="black",
        width=9,
        height=1,
        activebackground="Red",
        font=("times", 20, " bold "),
    ).place(x=110, y=50)
#Function for checking only valid phone number are taken as input
def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True


#GUI for Main Menu
logo = Image.open("icons/logo.jpeg")
logo = logo.resize((150,50), Image.Resampling.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
titl.pack(fill=X)
l1 = tk.Label(window, image=logo1, bg="black",)
l1.place(x=170, y=10)

titl = tk.Label(
    window, text="ContactLess Vistor Management System!!", bg="black", fg="red", font=("arial", 27),
)
titl.place(x=330, y=12)

a = tk.Label(
    window,
    text="Smart Face Recognition Based\nVistor Management System",
    bg="black",
    fg="red",
    bd=10,
    font=("arial", 35),
)
a.pack()

ri = Image.open("icons/register.png")
ri = ri.resize((220,150), Image.Resampling.LANCZOS)
r = ImageTk.PhotoImage(ri)

label1 = Label(window, image=r)
label1.image = r
label1.place(x=300, y=355)

#New user registeration function
def NewUserRegisteration():
    ImageUI = Tk()
    ImageUI.title("Main Menu")
    ImageUI.geometry("600x700")
    ImageUI.configure(background="black")
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
    titl.pack(fill=X)
    # image and title
    titl = tk.Label(
        ImageUI, text="New Vistor Registeration", bg="black", fg="green", font=("arial", 30),
    )
    titl.place(x=120, y=12)


    # Heading 
    a = tk.Label(
        ImageUI,
        text="Enter the details",
        bg="black",
        fg="red",
        bd=10,
        font=("arial", 24),
    )
    a.place(x=180, y=75)


    # Name
    NameLabel = tk.Label(
        ImageUI,
        text="Enter Your Name",
        width=20,
        height=2,
        bg="black",
        fg="red",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    NameLabel.place(x=50, y=130)
    NameTxt = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="black",
        fg="red",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    NameTxt.place(x=250, y=130)
    NameTxt["validatecommand"] = (NameTxt.register(testVal), "%P", "%d")

    # Email
    EmailLabel = tk.Label(
        ImageUI,
        text="Enter your Email",
        width=20,
        height=2,
        bg="black",
        fg="red",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    EmailLabel.place(x=50, y=180)
    EmailTxt = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="black",
        fg="red",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    EmailTxt.place(x=250, y=180)

    #Phone
    PhoneLabel = tk.Label(
        ImageUI,
        text="Enter Your Phone Number",
        width=20,
        height=2,
        bg="black",
        fg="red",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    PhoneLabel.place(x=50, y=230)
    PhoneTxt = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        validate="key",
        bg="black",
        fg="red",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    PhoneTxt.place(x=250, y=230)
    PhoneTxt["validatecommand"] = (PhoneTxt.register(testVal),"%P","%d")



    #Host Name
    PurposeofVisitLabel = tk.Label(
        ImageUI,
        text="Enter purpose of visit",
        width=20,
        height=2,
        bg="black",
        fg="red",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    PurposeofVisitLabel.place(x=50, y=280)
    PurposeofVisitTxt = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="black",
        fg="red",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    PurposeofVisitTxt.place(x=250, y=280)

    
    #HOST EMAIL
    HostNameLabel = tk.Label(
        ImageUI,
        text="Enter Host Name",
        width=20,
        height=2,
        bg="black",
        fg="red",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    HostNameLabel.place(x=50, y=330)
    HostNameTxt = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="black",
        fg="red",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    HostNameTxt.place(x=250, y=330)

    #Host Phone
    HostEmailLabel = tk.Label(
        ImageUI,
        text="Enter Host Email",
        width=20,
        height=2,
        bg="black",
        fg="red",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    HostEmailLabel.place(x=50, y=380)
    HostEmailTxt = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="black",
        fg="red",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    HostEmailTxt.place(x=250, y=380)




    #Address
    AddressLabel = tk.Label(
        ImageUI,
        text="Enter Address",
        width=20,
        height=2,
        bg="black",
        fg="red",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    AddressLabel.place(x=50, y=430)
    AddressTxt = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="black",
        fg="red",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    AddressTxt.place(x=250, y=430)



    #Notification
    NotificationLabel = tk.Label(
        ImageUI,
        text="Notification",

        width=20,
        height=2,
        bg="black",
        fg="red",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    NotificationLabel.place(x=50, y=480)

    NotificationTxt = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=5,
        bg="black",
        fg="red",
        relief=RIDGE,
        font=("times", 12, "bold"),
    )
    NotificationTxt.place(x=250, y=480)

    #Take image function
    def submit_request():
        l1 = NameTxt.get()
        l2 = PhoneTxt.get()
        l3= EmailTxt.get()
        l4=PurposeofVisitTxt.get()
        l5=HostNameTxt.get()
        l6=HostEmailTxt.get()
        l7=AddressTxt.get()
        l8 =time.strftime('%Y-%m-%d %H:%M:%S')
        takeImage.Submitform(
            l1,
            l2,
            l3,
            l4,
            l5,
            l6,
            l7,
            l8,
            haarcasecade_path,
            trainimage_path,
            NotificationTxt,
            err_screen,
            text_to_speech,
        )
        NameTxt.delete(0, "end")
        PhoneTxt.delete(0, "end")
        EmailTxt.delete(0,"end")
        PurposeofVisitTxt.delete(0,"end")
        HostNameTxt.delete(0,"end")
        HostEmailTxt.delete(0,"end")
        AddressTxt.delete(0,"end")


    # Submit Button 
    takeImg = tk.Button(
        ImageUI,
        text="Submit Request",
        command=submit_request,
        bd=10,
        font=("times new roman", 18),
        bg="black",
        fg="red",
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=200, y=550)



#New user registeration button
r = tk.Button(
    window,
    text="New Visitor Registeration",
    command=NewUserRegisteration,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="red",
    height=2,
    width=17,
)
r.place(x=300, y=520)


def check_out():
    check_out.subjectChoose(text_to_speech)

#Checkout Button

check_out_image = Image.open("icons/check_out.png")
check_out_image = check_out_image.resize((220,150), Image.Resampling.LANCZOS)
r = ImageTk.PhotoImage(check_out_image)

label1 = Label(window, image=r)
label1.image = r
label1.place(x=600, y=355)


r = tk.Button(
    window,
    text="Check OUT",
    command=check_out,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="red",
    height=2,
    width=17,
)
r.place(x=600, y=520)

def view_attendance():
    show_attendance.hostchoose(text_to_speech)


#Exit button
r = tk.Button(
    window,
    text="EXIT",
    bd=10,
    command=quit,
    font=("times new roman", 16),
    bg="black",
    fg="red",
    height=2,
    width=17,
)
r.place(x=450, y=660)

window.mainloop()
