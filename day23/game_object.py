from turtle import Turtle


class GAME(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
    def up(self):
        self.forward(10)
    # def down(self):
    #     self.back(10)