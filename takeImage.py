#Importing all the modules 
import csv
import os, cv2
import numpy as np
import pandas as pd
import datetime
import time
import mysql.connector
status="Inside"

#MySQL server credentials
mydb = mysql.connector.connect(
  host="localhost",
  user="XXXX",
  password="XXXXX",
  database="XXXXX"
)

mycursor = mydb.cursor()


# Main function
def Submitform(l1,l2,l3,l4,l5,l6,l7,l8,haarcasecade_path, trainimage_path, message, err_screen,text_to_speech):
    if (l1 == "") and (l2=="") and (l3 == "") and (l4=="") and (l5 == "") and (l6=="") and (l7==""):
        t='Please Enter all your details to continue.'
        text_to_speech(t)
    elif l1=='':
        t='Please Enter the your Name.'
        text_to_speech(t)
    elif l2 == "":
        t='Please Enter the your Phone Number.'
        text_to_speech(t)
    elif l3 == "":
        t='Please Enter your Email ID.'
        text_to_speech(t)
    elif l4 == "":
        t='Please Enter the your Purpose of visit.'
        text_to_speech(t)
    elif l5 == "":
        t='Please Enter the host name you wish to meet.'
        text_to_speech(t)
    elif l6 == "":
        t='Please Enter the host email address.'
        text_to_speech(t)
    elif l7 == "":
        t='Please Enter the address of host you wish you meet.'
        text_to_speech(t)
    
    else:
        try:
            cam = cv2.VideoCapture(0)
            detector = cv2.CascadeClassifier(haarcasecade_path)
            Name = l1
            PhoneNumber = l2
            EmailId = l3
            PurposeofVisit=l4
            HostName=l5
            HostEmail=l6
            Address=l7
            timecurr=l8
            sampleNum = 0
            directory = PhoneNumber + "_" + Name
            path = os.path.join(trainimage_path, directory)
            os.mkdir(path)
            while True:
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    sampleNum = sampleNum + 1
                    cv2.imwrite(
                        f"{path}\ "
                        + Name
                        + "_"
                        + PhoneNumber
                        + "_"
                        + str(sampleNum)
                        + ".jpg",
                        gray[y : y + h, x : x + w],
                    )
                    cv2.imshow("Frame", img)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
                elif sampleNum > 50:
                    break
            cam.release()
            cv2.destroyAllWindows()
            row = [Name,EmailId,PhoneNumber,PurposeofVisit,HostName,HostEmail,Address]
            sql = "INSERT INTO full_data (first_name,email,phone,purpose,host_name,host_email,address,currtime,curr_status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(Name,EmailId, PhoneNumber,PurposeofVisit,HostName,HostEmail,Address,timecurr,status)
            mycursor.execute(sql,val)
            print(mycursor.rowcount, "record inserted in sql database.")

            mydb.commit()

            with open(
                "C:\\Users\\XXXXXXXX\XXXXXXXX\\XXXXXXXX\\XXXXXXXX\\StudentDetails\\studentdetails.csv",
                "a+",
            ) as csvFile:
                writer = csv.writer(csvFile, delimiter=",")
                writer.writerow(row)
                csvFile.close()
            res = "Images Saved for ER No:" + PhoneNumber + " Name:" + Name
            print(mycursor.rowcount, "record inserted in csv file.")

            message.configure(text=res)
            text_to_speech(res)

        except FileExistsError as F:
            F = "Student Data already exists"
            text_to_speech(F)
