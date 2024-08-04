import random
import turtle
from turtle import Turtle,Screen,colormode
screen = Screen()
t=Turtle()

def move_forwards():
    t.forward(10)

def move_backwards():
    t.back(10)

def move_right():
    t.right(10)

def move_left():
    t.left(10)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkeypress(move_forwards,"w")
screen.onkeypress(move_right,"a")
screen.onkeypress(move_backwards,"s")
screen.onkeypress(move_right,"d")
screen.onkey(clear,"c")
screen.exitonclick()