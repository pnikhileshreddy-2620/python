import  datetime as dt
import  calendar
import random
import smtplib
from random import choice

my_email='YOU@gmail.com'
password=''
dt =dt.datetime
day_number = dt.now().weekday()
day_name =calendar.day_name[day_number]
try:
    with open('quotes.txt','r') as f:
        l =[i.strip() for i in f]
except FileNotFoundError:
    print(FileNotFoundError)
else:
    print("File Found")

mss=f"SUBJECT:QUOTES \n\n{random.choice(l)}"
if day_name=='Wednesday':
    """Below code is used to connected host server"""
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        """Starttls used to connected data secure"""
        connection.starttls()
        """Connecting the servers with email, password"""
        connection.login(user=my_email,password=password)
        """sendmail to user"""
        connection.sendmail(from_addr=my_email, to_addrs='YOU@gmail.com',
                            msg=mss)
        """Connection closed"""
        connection.close()
        print("Email sent successfully")
else:
    print("Sorry Today is not Tuesday")
