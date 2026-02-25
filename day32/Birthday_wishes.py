import random
from datetime import date
import pandas as pd
import smtplib

today=date.today()
my_email='YOU@gmail.com'
password=''
name =None
month =None
day=None
letter_temp =['letter_1.txt','letter_2.txt','letter_3.txt,','letter_4.txt','letter_5.txt']
select_format=random.choice(letter_temp)
print(select_format)
try:
    df =pd.read_csv('birthdays.csv')
    for index,row in df.iterrows():
        # print(row.size)
        name =row['name']
        day= row['day']
        month= row['month']
        email=row['email']
        print(name,day,month)
        with open(f'letter_templates\{select_format}', 'r') as read_file:
                read_file_output = read_file.read()
                letter=read_file_output.replace("[NAME]",name)
                sub ="Subject:Birthday Wishes\n\n"
                print(today.month,today.day)
                print(day==today.day)
                if month==today.month and day==today.day:
                    with smtplib.SMTP("smtp.gmail.com",587) as connection:
                        connection.starttls()
                        connection.login(user=my_email,password=password)
                        connection.sendmail(from_addr=my_email, to_addrs=email,
                                msg=sub+letter)



except FileNotFoundError:
    print("birthdays.csv not found.")
else:
    print("File Found")



