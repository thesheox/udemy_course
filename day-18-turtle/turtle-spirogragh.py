import random

from turtle import Turtle,Screen,colormode
screen = Screen()
t=Turtle()
colormode(255)

color_choices=["red","orange","black","green","blue"]
directions=[0,90,180,270]
t.shape("turtle")
t.speed("fastest")
# t.pensize(15)

def random_color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
def draw(gap):
    for i in range(int(360/gap)):
        t.color(random_color())
        t.circle(2)
        t.forward(2)
        #t.setheading(t.heading()+gap)

draw(2)
screen.exitonclick()