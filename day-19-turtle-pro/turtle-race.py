import random
import turtle
from turtle import Turtle,Screen,colormode
screen = Screen()

screen.setup(500,400)
user_bet=screen.textinput("make your bet","which color win the game?")
colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]
for i in range(0,6):
    t=Turtle("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-230,y_positions[i])
    all_turtles.append(t)

if user_bet:
    is_race_on=True
win_color=""
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            win_color=turtle.pencolor()

            if win_color==user_bet:
                print("won")
            else:
                print(f"lost / {win_color} won")
        rand_dis=random.randint(0,10)
        turtle.forward(rand_dis)

screen.exitonclick()