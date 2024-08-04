import random
from turtle import Turtle,Screen
screen = Screen()
t=Turtle()

t.shape("turtle")
x=[t.forward(random.randint(1,100))]

color_choices=["red","orange","black","green","blue"]
y=0

for i in range(3,12):
    t.color(random.choice(color_choices))
    for l in range(i):
        t.forward(100)
        t.right(360/i)
    y=y+1


t.color(random.choice(color_choices))
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

t.color(random.choice(color_choices))