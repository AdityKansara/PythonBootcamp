# Random draw turtle
from turtle import Screen, Turtle
import turtle
import random

directions = [0, 90, 180, 270]
turtle.colormode(255)


def random_colours():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle_color = (r, g, b)
    return turtle_color


tom = Turtle()
tom.shape("arrow")
tom.width(15)
tom.speed("fast")

for _ in range(100):
    tom.setheading(random.choice(directions))
    tom.color(random_colours())
    tom.forward(30)

s = Screen()
s.exitonclick()
