import smtplib

my_email='YOU@gmail.com'
password=''

with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs='YOU@gmail.com',msg="subject:Testing\n\n This testing purpose")
    connection.close()