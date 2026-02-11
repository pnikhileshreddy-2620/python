from turtle import Turtle


class ScoreBroad(Turtle):
    def __init__(self,x,y,name):
        super().__init__()
        self.score = 0
        self.name =name
        self.penup()
        self.hideturtle()
        self.color('red')
        self.goto(x,y)
        self.write(f' {self.name} score :{self.score}', align="center", font=('Arial', 8, 'normal'))
    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f'score :{self.score}', align="center", font=('Arial', 8, 'normal'))
    def gameover(self,message):
        self.goto(0,0)
        self.write(message,align="center",font=("Courier",30,"normal"))


