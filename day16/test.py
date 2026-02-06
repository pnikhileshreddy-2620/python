import turtle
from turtle import Turtle
obj =Turtle()
for steps in range(100):
    for c in ('blue', 'red', 'green'):
        obj.color(c)
        obj.forward(steps)
        obj.right(30)