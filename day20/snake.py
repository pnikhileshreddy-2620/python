import time
from turtle import Turtle,Screen
from turtledemo.clock import setup



STARTING_POSITION= [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE=20
UP,DOWN,LEFT,RIGHT=90,270,180,0




class Snake:
     def __init__(self):
         self.seg = []
         self.create_snake()
         self.head=self.seg[0]

     def create_snake(self):
         for i in STARTING_POSITION:
             new_segment = Turtle("square")
             new_segment.penup()
             new_segment.color('white')
             new_segment.goto(i)
             self.seg.append(new_segment)

     def move(self):
         for seg_num in range(len(self.seg) - 1, 0, -1):
             new_x = self.seg[seg_num - 1].xcor()
             new_y = self.seg[seg_num - 1].ycor()
             self.seg[seg_num].goto(new_x, new_y)
         self.head.forward(MOVING_DISTANCE)

     def Up(self):
         if self.head.heading()!=DOWN:
            self.head.setheading(UP)
     def Down(self):
         if self.head.heading()!=UP:
            self.head.setheading(DOWN)
     def Left(self):
         if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
     def Right(self):
         if self.head.heading() != LEFT:
            self.head.setheading(0)


