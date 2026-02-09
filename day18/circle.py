from turtle import Turtle,Screen
import random as rn
import turtle as t

cir =Turtle()
sc = Screen()
r =50
t.colormode(255)
def rand_color():
    r = rn.randint(0,255)
    g = rn.randint(0,255)
    b = rn.randint(0,255)
    return (r, g, b)

cir.speed(50)
def draw(angle):
    for _ in range(int(360/angle)):
        cir.circle(r)
        cir.setheading(cir.heading() + angle)
        cir.color(rand_color())
draw(5)


sc.exitonclick()