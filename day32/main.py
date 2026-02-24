import smtplib

my_email='pnikhileshreddy2620@gmail.com'
password='lvirnfkantlpyrle'

with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs='nikhilesh.redddi@gmail.com',msg="subject:Testing\n\n This testing purpose")
    connection.close()