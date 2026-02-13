import time

from turtle import Screen


from python.day21.Food import Food
from python.day20.snake import Snake
from python.day24.scoreBoard import ScoreBroad
from python.day24.highest_score import HighestScore

food =Food()
snake =Snake()
High =HighestScore()
SB = ScoreBroad(High)


SB.goto(-5,280)





current_score=0

highest=[]


screen =Screen()
screen.setup(600,600)
screen.bgcolor('black')
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
        SB.increase_score()



    if snake.head.xcor()> 280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on =False
        SB.reset()



    for segment in snake.seg[1:]:
        if snake.head.distance(segment)<10:
            game_is_on =False
            SB.reset()

            snake.game_over()







screen.exitonclick()







