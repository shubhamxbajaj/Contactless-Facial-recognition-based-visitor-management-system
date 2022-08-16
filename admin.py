#Importing modules 
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pyttsx3
import mysql.connector




import ResetDatabase
import takeImage
import check_realtime_visitors

def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


window = Tk()
window.title("Admin Page of VMS")
window.geometry("1280x720")
dialog_title = "QUIT"
dialog_text = "Are you sure want to close?"
window.configure(background="black")


def del_sc1():
    sc1.destroy()


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
        text="Enrollment & Name required!!!",
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


logo = Image.open("icons/logo.jpeg")
logo = logo.resize((150,50), Image.Resampling.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
titl.pack(fill=X)
l1 = tk.Label(window, image=logo1, bg="black",)
l1.place(x=200, y=10)

titl = tk.Label(
    window, text="ContactLess Vistor Management System!!", bg="black", fg="green", font=("arial", 27),
)
titl.place(x=375, y=12)

a = tk.Label(
    window,
    text="Smart Face Recognition Based\nVistor Management System",
    bg="black",
    fg="red",
    bd=10,
    font=("arial", 35),
)
a.pack()


ai = Image.open("icons/visitor_check.png")
ai = ai.resize((220,150), Image.Resampling.LANCZOS)
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=400, y=355)


def checkrealtimevisitors():
    check_realtime_visitors.realtime_visitors(text_to_speech)


def resetdatabase():
    ResetDatabase.reset_database()
    



r = tk.Button(
    window,
    text="Check Real time visitors",
    command=checkrealtimevisitors,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="red",
    height=2,
    width=17,
)
r.place(x=400, y=520)



ai = Image.open("icons/reset_database.png")
ai = ai.resize((220,150), Image.Resampling.LANCZOS)
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=700, y=355)


r = tk.Button(
    window,
    text="Reset Database",
    command=resetdatabase,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="red",
    height=2,
    width=17,
)
r.place(x=700, y=520)

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
r.place(x=550, y=640)


window.mainloop()


