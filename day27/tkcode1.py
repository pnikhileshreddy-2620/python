import tkinter as tk

from tkinter import *

window = tk.Tk()

my_label =tk.Label(text='I am Label',font=("Arial",10,'bold'))
my_label.pack()
# my_label['text']='new text'
# my_label.config(text=e.get)

def click_me():
    my_label.config(text=e.get())

window.title("TKINTER")
window.minsize(1000,500)





button = tk.Button(window,text='click me',command=click_me)
button.pack()


# entry
def input_user():
    print(e.get())




e =Entry(window,width=10)
e.insert(END,string="Enter something")
e.pack()
butt = tk.Label(window,text="Enter name")
butt.pack()

text =Text(height=5,width=30)
text.focus()
text.insert(END,"Enter something here")
text.pack()


""""
class :
LABEL,ENTRY,BUTTON,PACK,
TEXT,SPINBOX,CHECKBOX,RADIOBUTTON,

get() methods
"""











window.mainloop()