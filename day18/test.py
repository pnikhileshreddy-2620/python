import  random
from turtle import  *

all = Turtle()
scr = Screen()

col  = [
    "black", "white", "red", "green", "blue",
    "yellow", "orange", "purple", "pink", "brown",
    "cyan", "magenta", "gray", "gold", "violet"
]


def shap(num):
    angle = 360 / num
    for _ in range(num):
       all.forward(100)
       all.right(angle)


if __name__=='__main__':
    for i in range(3,11):
        all.color(random.choice(col))
        shap(i)
