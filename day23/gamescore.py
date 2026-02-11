from turtle import Turtle

from python.day23.car import Car


class GameScore(Turtle):

    def __init__(self):
        super().__init__()
        self.score =0
        self.hideturtle()
        self.penup()
        self.color('red')
        self.goto(-240,240)

    def update_score(self):
        self.clear()
        self.score +=1
        self.write(f" LEVEL {self.score} ", align="center",font=('Arial',16,"bold"))

    def increase_score(self):
        self.score+=1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=('Arial',16,"bold"))


