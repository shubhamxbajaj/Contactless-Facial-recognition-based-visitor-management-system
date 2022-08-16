#Importing modules 
import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.ttk as tkk
import tkinter.font as font
import mysql.connector
import tkinter
import pyttsx3


#MySQL credentials
mydb = mysql.connector.connect(
  host="localhost",
  user="XXXXX",
  password="XXXXX",
  database="XXXXX"
)
mycursor = mydb.cursor(buffered=True)

#Defining all the paths 
haarcasecade_path = "C:\\Users\\XXXXXXXX\XXXXXXXX\\XXXXXXXX\\XXXXXXXX\\haarcascade_frontalface_default.xml"
trainingimagelabel ="C:\\Users\\XXXXXXXX\XXXXXXXX\\XXXXXXXX\\XXXXXXXX\\TrainingImageLabel\\Trainner.yml"
trainimage_path = "C:\\Users\\XXXXXXXX\XXXXXXXX\\XXXXXXXX\\XXXXXXXX\\TrainingImage"
studentdetail_path ="C:\\Users\\XXXXXXXX\XXXXXXXX\\XXXXXXXX\\XXXXXXXX\\StudentDetails\\studentdetails.csv"
attendance_path= "C:\\Users\\XXXXXXXX\XXXXXXXX\\XXXXXXXX\\XXXXXXXX\\\\Attendance"



#Function for checking only valid phone number are taken as input
def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit() :
            return False
    return True


#Main host choose function
def hostChoose(text_to_speech):
    def FillAttendance():
        NameofUser = nametxt.get()
        now = time.time()
        future = now + 20
        print(now)
        print(future)
        if NameofUser == "":
            t = "Please enter your name"
            text_to_speech(t)
        else:
            try:
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                try:
                    recognizer.read(trainingimagelabel)
                except:
                    e = "Model not found,please train model"
                    Notifica.configure(
                        text=e,
                        bg="black",
                        fg="red",
                        width=33,
                        font=("times", 15, "bold"),
                    )
                    Notifica.place(x=20, y=250)
                    text_to_speech(e)
                facecasCade = cv2.CascadeClassifier(haarcasecade_path)
                df = pd.read_csv(studentdetail_path)
                cam = cv2.VideoCapture(0)
                font = cv2.FONT_HERSHEY_SIMPLEX
                col_names = ["Phone number", "name of user"]
                attendance = pd.DataFrame(columns=col_names)
                while True:
                    ___, im = cam.read()
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    faces = facecasCade.detectMultiScale(gray, 1.2, 5)
                    for (x, y, w, h) in faces:
                        global Id

                        Id, conf = recognizer.predict(gray[y : y + h, x : x + w])
                        if conf < 70:
                            #print(conf)
                            global Subject
                            global aa
                            global date
                            global timeStamp
                            Subject =  nametxt.get()
                            ts = time.time()
                            date = datetime.datetime.fromtimestamp(ts).strftime(
                                "%Y-%m-%d"
                            )
                            timeStamp = datetime.datetime.fromtimestamp(ts).strftime(
                                "%H:%M:%S"
                            )
                            aa = df.loc[df["Phone number"] == Id]["name of user"].values
                            print(aa)
                            global tt
                            tt = str(Id) + "-" + aa
                            # En='1604501160'+str(Id)
                            attendance.loc[len(attendance)] = [
                                Id,
                                aa,
                            ]
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 4)
                            cv2.putText(
                                im, str(tt), (x + h, y), font, 1, (255, 255, 0,), 4
                            )
                        else:
                            Id = "Unknown"
                            tt = str(Id)
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                            cv2.putText(
                                im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4
                            )
                    if time.time() > future:
                        break

                    attendance = attendance.drop_duplicates(
                        ["Phone number"], keep="first"
                    )
                    cv2.imshow("", im)
                    key = cv2.waitKey(30) & 0xFF
                    if key == 27:
                        break

                ts = time.time()
                print(aa)
                attendance[date] = 1
                date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
                Hour, Minute, Second = timeStamp.split(":")
                # fileName = "Attendance/" + Subject + ".csv"
                path = os.path.join(attendance_path, Subject)
                fileName = (
                    f"{path}/"
                    + Subject
                    + "_"
                    + date
                    + "_"
                    + Hour
                    + "-"
                    + Minute
                    + "-"
                    + Second
                    + ".csv"
                )
                attendance = attendance.drop_duplicates(["Phone number"], keep="first")
                print(attendance)
                attendance.to_csv(fileName, index=False)

                m = "User successfullly exited " + Subject
                Notifica.configure(
                    text=m,
                    bg="black",
                    fg="red",
                    width=33,
                    relief=RIDGE,
                    bd=5,
                    font=("times", 15, "bold"),
                )
                text_to_speech(m)

                Notifica.place(x=20, y=250)

                cam.release()
                cv2.destroyAllWindows()

                import csv
                import tkinter

                root = tkinter.Tk()
                root.title("Check Out screen")
                root.configure(background="black")
                cs = os.path.join(path, fileName)
                print(cs)
                with open(cs, newline="") as file:
                    reader = csv.reader(file)
                    r = 0

                    for col in reader:
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
                print(attendance)
            except Exception as E:
                f = "No Face found for check out"
                print(E)
                text_to_speech(f)
                cv2.destroyAllWindows()

    #Tkinter GUI Intialization 
    subject = Tk()
    subject.title("Check out screen")
    subject.geometry("580x320")
    subject.resizable(0, 0)
    subject.configure(background="black")
    titl = tk.Label(subject, bg="black", relief=RIDGE, bd=10, font=("arial", 30))
    titl.pack(fill=X)
    titl = tk.Label(
        subject,
        text="Check out screen",
        bg="black",
        fg="green",
        font=("arial", 25),
    )
    titl.place(x=160, y=12)
    Notifica = tk.Label(
        subject,
        text="Visitor successfully checked out",
        bg="red",
        fg="black",
        width=33,
        height=2,
        font=("times", 15, "bold"),
    )


    #Name label
    namelabel = tk.Label(
        subject,
        text="Enter your Name",
        width=20,
        height=2,
        bg="black",
        fg="red",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 15),
    )
    namelabel.place(x=20, y=75)

    #Name txt
    nametxt= tk.Entry(
        subject,
        width=15,
        bd=5,
        bg="black",
        fg="red",
        relief=RIDGE,
        font=("times", 30, "bold"),
    )
    nametxt.place(x=260, y=75)

    #Phone label
    phonelabel = tk.Label(
        subject,
        text="Enter your Phone Number",
        width=20,
        height=2,
        bg="black",
        fg="red",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 15),
    )
    phonelabel.place(x=20, y=150)
    #Phone txt
    phonetxt = tk.Entry(
        subject,
        width=15,
        bd=5,
        bg="black",
        validate="key",
        fg="red",
        relief=RIDGE,
        font=("times", 30, "bold"),
    )
    phonetxt.place(x=260, y=150)
    phonetxt["validatecommand"] = (phonetxt.register(testVal),"%P","%d")

    fill_a = tk.Button(
        subject,
        text="Submit Request",
        command=FillAttendance,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="red",
        height=2,
        width=12,
        relief=RIDGE,
    )
    fill_a.place(x=220, y=220)
    subject.mainloop()
