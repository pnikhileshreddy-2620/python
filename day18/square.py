from turtle import Turtle,Screen

square = Turtle()
screen = Screen()

# One of doing
square.forward(100)
square.right(90)
square.forward(100)
square.right(90)
square.forward(100)
square.right(90)
square.forward(100)

print()

# One way of doing
for i in range(4):
    square.forward(100)
    square.right(90)
    

screen.exitonclick()