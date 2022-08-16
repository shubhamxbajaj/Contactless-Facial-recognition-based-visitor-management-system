#Importing all the modules 
import tkinter as tk
from tkinter import *
from tkinter import ttk
import show_attendance
import takeImage
import trainImage
import automaticAttedance
from PIL import ImageTk, Image
import pyttsx3
import mysql.connector


#MySQL server credentials
mydb = mysql.connector.connect(
  host="localhost",
  user="XXXXX",
  password="XXXXX",
  database="XXXXX"
)

mycursor = mydb.cursor()

text1="I accept to reset database as Admin"

#Text to speech function
def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


#Main reset_database function
def reset_database():

        def checkinput():
            userinput=tx.get()
            if userinput!=text1:
                e="Please enter the line exactly same"
                text_to_speech(e)
            else:
                mycursor.execute("delete from full_data;")
                mydb.commit()
                mycursor.execute("select * from full_data")
                result2=mycursor.fetchall()
                print(result2)
                if(result2==[]):
                    s="Successfully reseted the database"
                    text_to_speech(s)
                else:
                    s="Not able to reset the database"
                    text_to_speech(s)
                
            
        
         #Tkinter GUI Intialization 
        subject = Tk()
        subject.title("Database Reset Page")
        subject.geometry("580x320")
        subject.resizable(0, 0)
        subject.configure(background="black")
        titl = tk.Label(subject, bg="black", relief=RIDGE, bd=10, font=("arial", 30))
        titl.pack(fill=X)

        #Title label
        titl = tk.Label(
            subject,
            text="Database Reset Page",
            bg="black",
            fg="green",
            font=("arial", 25),
        )
        titl.place(x=170, y=10)

        #Admin Declaration
        user_declaration_label = tk.Label(
            subject,
            text="Please type the same line to continue--->",
            width=30,
            height=2,
            bg="black",
            fg="red",
            relief=RIDGE,
            font=("times new roman", 12),
        )
        user_declaration_label.place(x=20, y=70)
        #Admin input
        user_declaration_txt = tk.Label(
            subject,
            text=text1,
            width=30,
            height=2,
            bg="black",
            fg="red",
            relief=RIDGE,
            font=("times new roman", 12),
        )
        user_declaration_txt.place(x=290, y=70)

        #Submit request
        tx = tk.Entry(
            subject,
            width=20,
            bd=5,
            bg="black",
            fg="red",
            relief=RIDGE,
            font=("times", 30, "bold"),
        )
        tx.place(x=100, y=120)

        attf = tk.Button(
            subject,
            text="Sumbit Request",
            command=checkinput,
            bd=7,
            font=("times new roman", 15),
            bg="black",
            fg="red",
            height=2,
            width=15,
            relief=RIDGE,
        )
        attf.place(x=210, y=190)
        subject.mainloop()






