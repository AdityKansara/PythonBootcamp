# Spinograph

from turtle import Screen, Turtle
import turtle
import random

turtle.colormode(255)


def random_colours():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle_color = (r, g, b)
    return turtle_color


tom = Turtle()
tom.shape("arrow")
tom.speed("fastest")
angle = 360
while angle > 0:
    tom.color(random_colours())
    tom.setheading(angle)
    tom.circle(100)
    angle -= 5

s = Screen()
s.exitonclick()
