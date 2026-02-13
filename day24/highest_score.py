from turtle import Turtle




class HighestScore:
    def __init__(self):
        self.high_score =0
        self.load_high_score()
    def load_high_score(self):
        try:
            with open("highest_score.txt") as f :
                self.high_score=int(f.read())
        except:
            with open("highest_score.txt","w") as f:
                f.write("0")
                self.high_score=0
    def update_high_score(self,score):
        if score>self.high_score:
            self.high_score=score
            with open("highest_score.txt","w") as f:
                f.write(str(self.high_score))












