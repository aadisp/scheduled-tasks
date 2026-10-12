import datetime
import pandas
import random
import smtplib
import os
current=datetime.datetime.now()
data=pandas.read_csv("birthdays.csv")
month=data["month"].to_list()
date=data["day"].to_list()
names=data["name"].to_list()
body="Subject: Birthday wishes\n\n"
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
def sendletter(n):
    global body
    letter=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter,"r")as file:
        cont=file.read()
        body+=cont.replace("[NAME]",n)
    with smtplib.SMTP("smtp.gmail.com",587)as connec:
        connec.starttls()
        connec.login(user=MY_EMAIL,password=MY_PASSWORD)
        connec.sendmail(from_addr=MY_EMAIL,to_addrs="aadisp16@yahoo.com",msg=body)
for m in month:
    if current.month==m:
        for d in date:
            if current.day==d:
                nm=names[date.index(d)]
                sendletter(nm)
                break
        break
