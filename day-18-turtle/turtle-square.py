from turtle import Turtle,Screen
screen = Screen()
t=Turtle()

t.shape("turtle")

# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)

for i in range(15):
    t.forward(20)
    t.penup()
    t.forward(20)
    t.pendown()
