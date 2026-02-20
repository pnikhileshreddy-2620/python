import string
import random
from tkinter import  *
from tkinter import messagebox

import pyperclip


def show_pop():
    messagebox.showwarning(title="Missing data please check",message="Information Missing")


def password_file(website,email,password):
    if len(website)==0 or len(email)==0 or len(str(password))==0:
        show_pop()
    else:
        try:
            with open('password.txt','a') as f:
                f.write(f'{website} |{email} |{password} \n')
                website_input.delete(0,END)
                password_display.delete(0,END)


        except FileNotFoundError:
            print(FileNotFoundError)

def password_generate():
    combine =string.punctuation+string.ascii_letters+string.digits
    randon_password = [random.choice(combine) for _ in range(10)]
    random.shuffle(randon_password)
    randon_password= ''.join(randon_password)
    password_display.insert(0,randon_password)
    pyperclip.copy(randon_password)


window =Tk()
window.title('PASSWORD MANAGER')

# window.minsize(10,10)
window.config(padx=20,pady=20)


canvas =Canvas(height=200,width=200,bg='white',highlightthickness=0)
photoimage = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=photoimage)
canvas.grid(row=2,column=6)


label_website=Label(text="Website",background='white',width=10,height=1)
label_website.grid(row=4,column=4)
website_input = Entry(window,width=35,borderwidth=2)
website_input.focus()
website_input.grid(row=4,column=6)


email_label=Label(text="Email",background='white',width=10,height=1)
email_label.grid(row=6,column=4)
email_input =Entry(window,width=35,borderwidth=2)
email_input.insert(0,'my@gmail.com')
email_input.grid(row=6,column=6)

password_generator= Label(text='Password',background='white',highlightthickness=0,width=10,height=1)
password_generator.grid(row=7,column=4)
password_display= Entry(window,width=21,borderwidth=2,background='white')
password_display.grid(row=7,column=6)

button = Button(text="Generate Password",highlightthickness=0,width=14,borderwidth=2,command=password_generate)
button.grid(row=7,column=8,columnspan=10)

Add_to_file= Button(text="Add",background='blue',width=35,height=1,command=lambda:password_file(website_input.get(),email_input.get(),password_display.get()))
Add_to_file.grid(row=9,column=6)






















window.mainloop()