from  turtle import Turtle,Screen
import  random

extract_color=[(252, 245, 248), (233, 240, 249), (172, 74, 42), (22, 27, 59), (241, 234, 79), (209, 144, 108), (61, 87, 143), (129, 159, 203), (142, 24, 42), (51, 33, 23), (35, 46, 130), (209, 80, 119), (64, 22, 32), (221, 81, 55), (149, 56, 75), (148, 29, 19), (86, 112, 207), (200, 130, 159), (25, 44, 34), (129, 181, 141), (164, 183, 231), (75, 107, 63), (175, 132, 56), (68, 76, 32), (240, 164, 153), (243, 225, 4), (42, 78, 58), (227, 169, 185), (158, 202, 220), (112, 168, 82), (166, 205, 181), (79, 148, 157), (45, 77, 81)]

e_t =Turtle()
s_t =Screen()
s_t.colormode(255)
s_t.bgcolor('white')
s_t.screensize(10000,10000)
# e_t.hideturtle()
e_t.penup()
e_t.speed('fastest')
e_t.setheading(225)
e_t.forward(250)
e_t.setheading(0)

num_of_dots =101
for  i in range(1,num_of_dots):
    e_t.dot(20,random.choice(extract_color))
    e_t.forward(50)
    if i%10==0:
        e_t.setheading(90)
        e_t.forward(50)
        e_t.setheading(180)
        e_t.forward(500)
        e_t.setheading(0)



s_t.exitonclick()