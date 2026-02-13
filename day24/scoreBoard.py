from turtle import Turtle
class ScoreBroad(Turtle):
    def __init__(self,high_obj):
        super().__init__()
        self.score=0
        self.high =high_obj
        self.penup()
        self.hideturtle()
        self.color('red')
        self.goto(0, 270)



    def update_score(self):
        self.clear()
        self.write(f'score :{self.score} and high score is {self.high.high_score}', align="center", font=('Arial', 8, 'normal'))

    def increase_score(self):
        self.score+=1
        self.update_score()
    def reset(self):
        self.high.update_high_score(self.score)
        self.score=0
        self.update_score()










