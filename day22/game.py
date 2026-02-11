import time
import turtle
from turtle import Turtle,Screen

from python.day22.Ball import Ball
from python.day22.paddle import Paddle
from python.day22.scorebroad import ScoreBroad

game = Turtle()
screen = Screen()

screen.tracer(0)
screen.title('pong game')
screen.setup(800,600)
game.hideturtle()
game.goto(0,300)
game.goto(0,-300)


ball = Ball()
score_r =ScoreBroad(200,270,'hp')
score_l =ScoreBroad(-200,270,'dell')

paddle = Paddle(380,0)
paddle2 =Paddle(-380,0)





screen.listen()
screen.onkey(paddle.UP,"a")
screen.onkey(paddle.DOWN,"s")
screen.onkey(paddle2.UP,"Up")
screen.onkey(paddle2.DOWN,"Down")





is_game=True
while is_game:
    time.sleep(0.05)
    screen.update()
    ball.refresh()


    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    # if ball.distance(paddle)<50  and ball.xcor()>320 or  ball.distance(paddle2)<50 and ball.xcor()<-320:
    #     if ball.distance(paddle)<50  and ball.xcor()>320:
    #         score_r.increase_score()
    #         ball.bounce_x()
    #     elif ball.distance(paddle2)<50 and ball.xcor()<-320:
    #         score_l.increase_score()
    #         ball.bounce_x()

    if ball.distance(paddle)< 50 and ball.xcor()>350:
        ball.bounce_x()
    if ball.distance(paddle2)<50 and ball.xcor()<-350:
        ball.bounce_x()
    if ball.xcor()>400:
        score_l.increase_score()
        ball.reset_position()

    if ball.xcor()<-400:
        score_r.increase_score()
        ball.reset_position()







    #
    # if ball.distance(paddle)<50 and ball.xcor() >380:
    #         ball.setx(320)
    #         ball.bounce_x()
    #
    # if ball.distance(paddle2) < 50 and ball.xcor() <-330:
    #         ball.setx(-320)
    #         ball.bounce_x()


        # if ball.xcor()>280 or ball.xcor()<-280 or ball.ycor()>380 or ball.ycor()<-380:
    if ball.xcor() > 400 or ball.xcor() < -400:
        ball.goto(0, 0)
        ball.bounce_x()

    if score_r.score == 5:
        score_r.gameover(f"{score_r.name} win the game")
        is_game=False
    elif score_l.score == 5:
        score_l.gameover(f"{score_l.name} win the game")
        is_game = False






screen.exitonclick()