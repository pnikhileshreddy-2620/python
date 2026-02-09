from turtle import *
import random
sc = Screen()
sc.setup(height=900,width=700)
user_bet =sc.textinput(title='make you bet',prompt='which turtle will win the race? enter color')
colo =[ "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "black",
    "white",
    "gray",
    "cyan",
    "magenta",
    "lime",
    "navy"]
y_position=[200,175,150,125,100,0,-100,-125,-150,-175,-200]
all =[]

race= False
for i in range(0,11):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(colo[i])
    tim.goto(-250,y_position[i])
    all.append(tim)

if user_bet:
    race=True
OU=""
while race:

    for t in all:
        if t.xcor() > 300:
            OU = t.pencolor()
            race=False
            break
        random_distance=random.randint(0,10)
        t.forward(random_distance)

if user_bet.lower()==OU.lower():
    print("you win")
else:
    print(f"You loose color  {OU} turtle win the game..")





sc.exitonclick()