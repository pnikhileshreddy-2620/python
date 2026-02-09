import turtle
import random
from test import  col as bb
sc = turtle.Screen()
walk = turtle.Turtle()
walk.pensize(10)

# col  = [
#     "black", "white", "red", "green", "blue",
#     "yellow", "orange", "purple", "pink", "brown",
#     "cyan", "magenta", "gray", "gold", "violet"
# ]

for _ in range(10000):
    move = random.choice(["f", "b", "l", "r"])
    if move == "f":
        walk.color(random.choice(bb))
        walk.forward(20)

    elif move == "b":

        walk.color(random.choice(bb))
        walk.backward(20)
    elif move == "l":
        walk.color(random.choice(bb))
        walk.left(90)
    elif move == "r":
        walk.color(random.choice(bb))
        walk.right(90)

sc.exitonclick()
