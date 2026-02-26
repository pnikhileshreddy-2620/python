import requests
from tkinter import *


"""
Aim :- Every time click on screen. Quote change in the screen.

Modules used in program is Tkinter for GUI, requests for connected the code with external software or system.



"""


window =Tk()
window.title('Quotes API')
# window.minsize(600,500)
window.config(padx=50,pady=50)


def get_quote():
    """This is used to get data from kanye website. connected through api"""
    url ='https://api.kanye.rest'
    quotes =requests.get(url)
    quotes.raise_for_status()

    get=quotes.json()['quote']
    new =get
    canvas.itemconfig(quote_text,text=new)




canvas =Canvas(width=300,height=414)
background=PhotoImage(file='background.png')
canvas.create_image(150,207,imag=background)
quote_text=canvas.create_text(150,207,text='Kanye Quote Goes Here',width=250,font=('Airel',20,"bold"))
canvas.grid(row=0,column=0)

kanye_img=PhotoImage(file='kanye.png')
kanye_button =Button(image=kanye_img,highlightthickness=0,command=get_quote)
kanye_button.grid(row=1,column=0)

mainloop()