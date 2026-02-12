import random
import time
import turtle
from turtle import Turtle,Screen


from python.day23.car import Car
from python.day23.game_object import GAME
from python.day23.gamescore import GameScore

screen_game =Screen()
screen_game.screensize(600,600)
screen_game.tracer(9)
screen_game.listen()

Level =0

colors = [
    "black",  "red", "green", "blue",
    "yellow", "orange", "purple", "pink", "brown",
     "gold"
]
game =GAME()
gamescore =GameScore()
game.goto(0,-290,)

screen_game.onkey(game.up,"Up")
# screen_game.onkey(game.down,"Down")
cars=[]
position_car=[-249,200,150,100,50,0,-50,-100,-150,-200,-249]
for i in range(0,len(position_car)-1):
    car =Car(random.choice(colors), x=300,y=position_car[i])
    cars.append(car)
is_game_on =True
is_paused= False

def move_up():
    global is_paused
    if is_paused:
        is_paused=False
        game.up()
while is_game_on:
    time.sleep(0.05)
    screen_game.update()
    for car in cars:
        car.speed_car()
        if car.distance(game)<20:
            print('Game Over')
            is_game_on=False
    if game.ycor()>250:
        game.goto(0,-290)
        gamescore.increase_score()
        for car in cars:
            car.speed_car()
        is_paused=True




screen_game.exitonclick()