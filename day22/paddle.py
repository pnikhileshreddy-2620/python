from turtle import  Turtle

class Paddle(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(5,1)
        self.goto(x,y)
        self.color('red')

    def UP(self):
        new_y =self.ycor()+20
        self.goto(self.xcor(),new_y)
        pass
    def DOWN(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



