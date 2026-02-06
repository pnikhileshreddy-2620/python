# import  turtle
from turtle import Turtle,Screen

# HERE timmy is object and Turtle is class
timmy=Turtle()
print(timmy)

# To access the attributes

my_screen = Screen()
# Here my_screen is object
print(my_screen.canvheight)
my_screen.screensize(canvwidth=100,canvheight=100)
for i in range(1,100):
    timmy.forward(100)
    timmy.right(90)
    timmy.color('red')
    timmy.forward(100)
    timmy.right(90)
    timmy.color('green')
    timmy.forward(100)
    timmy.right(90)
    timmy.color('blue')
    timmy.forward(100)
    timmy.home()
print(my_screen.canvheight)
# my_screen object call the attributes using . here canvheight() is attributes of the Screen class
my_screen.exitonclick()
# exitonclick() function.
# my_screen.screensize(canvwidth=100,canvheight=100) object calling the method in Screen class. To call the method, we need to use . dot operator