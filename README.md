# Contactless-facial-recognition-based-visitor-management-system
About This is a contactless visitor management system project and it uses Python, OpenCV, MySQL and many other technologies for functioning.



## Summary of project:

This project is a cheap alternative for the expensive visitor management systems which are widely avaiable in the market. This project also have an admin only accessible page and that can be used to reset the database manually(after verification of Admin). Admin page can also be used to monitor all the visitors in real time. We can also view visitors for a particular host as well. 

## Functioning of the project:



![main menu](https://user-images.githubusercontent.com/47914856/184867039-0e2dbc5c-9279-493e-8391-1d74b95fe29c.PNG)





### New User Registeration

1) Visitor is greeted with the main menu of the VMS. The main menu have "New user registeration" and "Check out" buttons available. New user registeration is a form which take 7 inputs(Name of the user, Email of the visitor, phone number of the visitor, purpose of visit, host name, host email and address where visitor wants to go).

2) If all the details on the form are filled correctly, a face model of the visitor will be created and will be trained using the Haar Cascade facial detection algorithm.

3)  After creation of facial model, all the details of the user will be inserted in the MySQL server(this server can either be on a local machine or on cloud). All the details will also be inserted in a csv file. 



![new_user_registeration](https://user-images.githubusercontent.com/47914856/184867060-b3fd1a12-e003-4dea-8352-3e1e0c8fc03f.PNG)







### Check out of visitor

1) While exiting visitor will be given the same menu screen. Check out screen will have 2 inputs(Name of the visitor, phone number of the visitor). If the visitor given inputs match the details, facial recognition will start to check if visitor is authentic, here comparision of the 2 models will be done(Model 1: which is created while registering a visitor, Model 2: which is created when visitor details are checked on the check out screen).

2) If visitor is authenicated using facial recognition then user will be given the permission to exit. 

3) Exit time, date and status of visitor will be automatically updated on the MySQL server. Hence making the whole VMS contactless.




![check_out_screen](https://user-images.githubusercontent.com/47914856/184708211-ad11648b-c484-41ef-a8e2-2c9c718ed62d.PNG)


### Admin page of VMS


We also have an admin page for VMS. Admin page 2 buttons "Check real time visitors" and "Reset database" 

![admin_page](https://user-images.githubusercontent.com/47914856/184867597-d64cec78-3232-4fb1-bbda-8b9f82107973.PNG)




* Check real time visitors: 
This feature can be used to view all the visitors in real time(which have not exited). Here we can also choose a particular host for which we want to see the visitors. All the details of user will be displayed on this page. 

![real_time_users](https://user-images.githubusercontent.com/47914856/184714080-c599d9f9-efd8-42fa-ae4a-aacb770e421a.PNG)



* Reset database: This feature can be used by the admin to reset the database. The database will be only reseted after successful verification of the admin. 

![database_reset](https://user-images.githubusercontent.com/47914856/184713518-394cc4ed-748b-4ce6-8ce1-689453de43a2.PNG)




### How to run this project locally on your devices:
1) Run requirements.py file to install all the necessary modules to run this project
2) Set the following variables location correctly(haarcasecade_path,trainingimagelabel_path,trainimage_path,studentdetails_path)
3) Set MySQL credentials and check connection of server and VMS
4) Try running and fix any issues if they arise, add issues if you are not able to fix it


### Note: The following modules are required to be installed to run this project-->
1) Python 3.6+
2) Tkinter(Available in python)
3) PIL (pip install Pillow)
4) Pandas(pip install pandas)
5) Numpy(pip install numpy)
6) Opencv(pip install opencv-python)

Please note that:  This project will require require high processing power for computation of visitor captured image. I used 20gb ram and 4Gb of graphics card personally to run this project. Using low quality images and noisy image can reduce accuracy of facial recongition hencequality of images matter.

### Features that can be added in this project in future:

* We can add automatic email sender feature through which host is notified with a visitor to meet him/her.
* Facial recognition can also be used to verify admin of the VMS.
* A web application which can be hosted on the local network, this web application can have the "Main menu" of the VMS. Hence removing the dependancy of a physical device at entry.
* For added security we can add a fingerprint sensor in this project

I am open for collaborations, so hit me up if anyone is interested in adding a new feature.





