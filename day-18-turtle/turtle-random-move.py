import random
from turtle import Turtle,Screen,colormode
screen = Screen()
t=Turtle()
colormode(255)

color_choices=["red","orange","black","green","blue"]
directions=[0,90,180,270]
t.shape("turtle")
t.speed("fastest")
t.pensize(15)

for i in range(200):
    t.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    t.forward(30)
    t.setheading(random.choice(directions))
