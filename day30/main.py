import string
import random
from tkinter import  *
from tkinter import messagebox
import json
from tkinter.messagebox import showinfo

import pyperclip


def show_pop():
    messagebox.showwarning(title="Missing data please check",message="Information Missing")


def password_file(website,email,password):
    if len(website)==0 or len(email)==0 or len(str(password))==0:
        show_pop()
    else:
        messagebox.showinfo(title="Details",message=f"Website :{website} \n Email/Username : {email} \n Password :{password}")
        try:



            website_data = {
                website: {
                    "email": email,
                    "password": password,
                }
            }

            try:
                # Step 1: Read existing data
                with open('password.json', 'r') as f:
                    data = json.load(f)

            except FileNotFoundError:
                # File does not exist → create new dictionary
                data = {}

            except json.JSONDecodeError:
                # File exists but empty → treat as empty dictionary
                data = {}

            # Step 2: Update data
            data.update(website_data)

            # Step 3: Write back to file
            with open('password.json', 'w') as f:
                json.dump(data, f, indent=4)



                website_input.delete(0,END)
                password_display.delete(0,END)


        except FileNotFoundError:
            print(FileNotFoundError)




def search():
    masterdata =website_input.get()
    try :
        with open("password.json",'r') as s:
            data =json.load(s)
            if masterdata in data:
                messagebox.showinfo(title="Information",message=f"Website {masterdata} \n Email {data[masterdata]['email']} \n Password {[data[masterdata]['password']]}")
            else:
                messagebox.showinfo(title="Information",
                                    message="No information available")
    except FileNotFoundError:
        print(FileNotFoundError)






def password_generate():
    combine =string.punctuation+string.ascii_letters+string.digits
    randon_password = [random.choice(combine) for _ in range(10)]
    random.shuffle(randon_password)
    randon_password= ''.join(randon_password)
    password_display.insert(0,randon_password)
    pyperclip.copy(randon_password)
def search_operation():
    pass

window =Tk()
window.title('PASSWORD MANAGER')

# window.minsize(10,10)
window.config(padx=20,pady=20)


canvas =Canvas(height=200,width=200,bg='white',highlightthickness=0)
photoimage = PhotoImage(file='C:/Users/pongredd/OneDrive - Capgemini/Desktop/Python/python/day29/logo.png')
canvas.create_image(100,100,image=photoimage)
canvas.grid(row=2,column=6)


# Below used to take the website data as input.

label_website=Label(text="Website",background='white',width=10,height=1)
label_website.grid(row=4,column=4)
website_input = Entry(window,width=35,borderwidth=2)
website_input.focus()
website_input.grid(row=4,column=6)

search =Button(text="Search",background='green',width=5,height=1,command=search)
search.grid(row=4,column=8)

# Below entry used to take input from the user [email/username]. Default we set email.
email_label=Label(text="Email",background='white',width=10,height=1)
email_label.grid(row=6,column=4)
email_input =Entry(window,width=35,borderwidth=2)
email_input.insert(0,'my@gmail.com')
email_input.grid(row=6,column=6)

# Below code will generate the password and save the data inside the file.
password_generator= Label(text='Password',background='white',highlightthickness=0,width=10,height=1)
password_generator.grid(row=7,column=4)
password_display= Entry(window,width=21,borderwidth=2,background='white')

password_display.grid(row=7,column=6)

# This button used call the password() and return to above to display
button = Button(text="Generate Password",highlightthickness=0,background='green',width=14,borderwidth=2,command=password_generate)
button.grid(row=7,column=8,columnspan=10)


# This Button used to save data inside the file.
Add_to_file= Button(text="Add",background='blue',width=35,height=1,command=lambda:password_file(website_input.get(),email_input.get(),password_display.get()))
Add_to_file.grid(row=9,column=6)






















window.mainloop()