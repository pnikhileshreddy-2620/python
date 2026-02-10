from turtle import Turtle
class ScoreBroad(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.color('red')
        self.goto(0, 270)
        self.write(f'score :{self.score}',align="center",font=('Arial', 8, 'normal'))

    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f'score :{self.score}', align="center", font=('Arial', 8, 'normal'))

    def game_over(self):
        self.home()
        self.write(f' GAME OVER',align="center", font=('Arial', 8, 'normal'))




