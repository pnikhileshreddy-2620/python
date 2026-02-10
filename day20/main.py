import time
from turtle import Turtle,Screen
from snake import Snake


screen=Screen()
screen.setup(600,600)
screen.title("Snake game")
screen.tracer()
screen.bgcolor('black')

snake =Snake()
screen.listen()
screen.onkey(snake.Up,"Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Left,"Left")
screen.onkey(snake.Right,"Right")


game_is_on =True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()