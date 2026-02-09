from turtle import *

dash =Turtle()
screen =Screen()
# screen.screensize(10000,100)


for i in range(0,20):
    dash.forward(10)
    dash.penup()
    dash.forward(10)
    dash.pendown()


screen.exitonclick()