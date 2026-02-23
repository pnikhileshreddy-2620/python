import random
from random import  randint
from tkinter import *
import pandas as pd



BG="#B1DDC6"


df =pd.read_csv('french_words.csv')
to_words= df.to_dict(orient='records')

def random_word():
    current_card=random.choice(to_words)
    print(current_card['French'])
    # df= pd.read_csv('french_words.csv')
    # new_dict=df['French'].to_dict()
    # len_of_dict = len(new_dict)
    # random_key = random.randint(0,len_of_dict)
    # print(new_dict[random_key])
    canvas.itemconfig(you,text='French',font=("Airel",40,"bold"))
    canvas.itemconfig(my,text=current_card['French'],font=("Airel",40,"bold"))




window =Tk()
# window.minsize(500,500)
window.title('Flash Card')
window.config(padx=50,pady=50,background=BG)



canvas =Canvas(width=800,height=526)
card_front =PhotoImage(file='image/card_front.png')
canvas.create_image(400,263,image=card_front)
canvas.config(background=BG,highlightthickness=0)
you=canvas.create_text(400,150,text="Title",font=("Airel",40,"italic"))
my=canvas.create_text(400,263,text='WORD',font=("Airel",40,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

cross_image =PhotoImage(file='image/wrong.png')
unknown =Button(image=cross_image,highlightthickness=0,command=random_word)
unknown.grid(row=1,column=0)

check_mark =PhotoImage(file='image/right.png')
known =Button(image=check_mark,highlightthickness=0,command=random_word)
known.grid(row=1,column=1)











window.mainloop()