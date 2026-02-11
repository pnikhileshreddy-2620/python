import random
from turtle import Turtle

from jedi.debug import speed


class Car(Turtle):



    def __init__(self,color,x,y):
        super().__init__()

        self.shape('square')
        self.penup()
        self.color(color)
        self.goto(x,y)
        self.shapesize(1,2)
        self.setheading(180)
        self.move_distance = random.randint(3,6)

    def speed_car(self):
        self.forward(self.move_distance)
        if self.xcor()<-300:
            self.goto(300,self.ycor())

    def  increase_speed(self):
        self.move_distance+=1



