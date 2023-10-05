import smtplib
import random
import math
import os

n = "0123456789"
otp = ""
for i in range(6):
    otp+= n[math.floor(random.random()*10)]
OT = otp + " is your One-Time-Password for verification"
message = OT

email = smtplib.SMTP(host='smtp.gmail.com', port=587)  # To call the gmail account client
email.starttls()
email.login(user="email", password="password")  # To login into your account successfully
key = input("Enter your email address : ")
email.sendmail(from_addr= "faryalimran7@gmail.com", to_addrs=key, msg=message)   # Sending the OTP email
x = input("Enter your OTP: ")
if x == otp:
    print("Your account has been successfully verified.")
else:
    print("Please check your OTP once again.")
