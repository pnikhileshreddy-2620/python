import time
import turtle
from turtle import Turtle,Screen
from python.day21.ScoreBroad import ScoreBroad
from python.day21.Food import Food
from snake import Snake


screen=Screen()
turtle.hideturtle()
screen.setup(600,600)
screen.title("Snake game")

screen.tracer()
screen.bgcolor('black')

snake =Snake()
food =Food()
scorecard= ScoreBroad()





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


    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend_snake()
        scorecard.increase_score()


    if snake.head.xcor()> 280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on =False
        scorecard.game_over()


    for segment in snake.seg[1:]:
        if snake.head.distance(segment)<10:
            game_is_on =False
            scorecard.game_over()






screen.exitonclick()
