# smtplib -> this library is used for accesing simple mail tranfer protocall

import smtplib
print("process started...")

 # Set the host name and port no:

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
print("server started...")

# Enter senders email id and password for login purpose

server.login("nikhil.s.wani@gmail.com", "put your password")
print("login succesfully....")

# Enter sender email id receivers email id
# you can write your subject name as "Subject: <subject>"
# discription as "\n\n <discription>"

server.sendmail("nikhil.s.wani@gmail.com","sureshlimkar@gmail.com","Subject: 2nd Practical demo Nikhil Wani \n\n Welcome to email world \nFrom nikhil Wani!!!")
print("mail sent....")

#quit the server

server.quit()
