from turtle import Turtle
class ScoreBroad(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high =0
        self.penup()
        self.hideturtle()
        self.color('red')
        self.goto(0, 270)
        self.write(f'score :{self.score} and high score is {self.high}',align="center",font=('Arial', 8, 'normal'))

    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f'score :{self.score} and high score is {self.high}', align="center", font=('Arial', 8, 'normal'))
    def game_over(self):
        if self.score>self.high:
            self.high=self.score
        self.score=0
        self.clear()










