import random
from turtle import Turtle,Screen,colormode
import colorgram
my_colors=[]
colors=colorgram.extract('photo.jpg',10)

for color in colors:
    r=color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color=(r,g,b)
    my_colors.append(new_color)

screen = Screen()
t=Turtle()
t.penup()
colormode(255)
t.shape("turtle")

for h in range(5):
    for i in range(5):
        t.dot(20,random.choice(my_colors))
        t.forward(100)



    t.back(500)
    t.left(90)
    t.forward(100)
    t.right(90)
screen.exitonclick()