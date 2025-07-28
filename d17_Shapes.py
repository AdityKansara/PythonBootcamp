# Shapes
from turtle import Screen, Turtle
import random
from Resources.data import turtle_colors

shree = Turtle()
shree.shape("turtle")
shree.turtlesize(2, 2, 2)

i = 3
angle = 360

while i <= 10:
    angle = 360 / i
    clr = random.choice(turtle_colors)
    shree.color(clr)
    for x in range(i):
        shree.forward(100)
        shree.right(angle)
    i += 1

screen = Screen(300, 300)
screen.exitonclick()
