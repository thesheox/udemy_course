from turtle import Turtle,Screen
screen = Screen()
timmy=Turtle()

timmy.shape("turtle")
timmy.color('red','yellow')
timmy.begin_fill()
while True:
    timmy.forward(200)
    timmy.left(170)
    if abs(timmy.pos())<1:
        break
timmy.end_fill()
screen.exitonclick()
