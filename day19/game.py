from  turtle import *



game = Turtle()
scree = Screen()

def move_forward():
    game.forward(10)
# def move_left():
#     game.left(10)
def move_up():
    game.left(90)
def move_down():
    game.right(90)
# def move_right():
#     game.right(10)
def move_back():
    game.backward(10)

def clear():
    game.clear()
scree.listen()
scree.onkey(key='W',fun=move_forward)
# scree.onkey(key='l',fun=move_left)
# scree.onkey(key='D',fun=move_right)
scree.onkey(key='A',fun=move_up)
scree.onkey(key='D',fun=move_down)
scree.onkey(key='S',fun=move_back)
scree.onkey(key='c',fun=clear)




scree.exitonclick()
