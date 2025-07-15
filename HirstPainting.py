# HirstPainting

from turtle import Screen, Turtle
import turtle
import colorgram
import random

turtle.colormode(255)
img = "beginnerPackage//image.jpeg"
colorPallete = colorgram.extract(img, 50)


def fetchColours():
    clr = random.choice(colorPallete)
    return clr.rgb


tom = Turtle()
tom.shape("circle")
tom.width(15)
tom.speed("fast")

tom.penup()
tom.setheading(225)
tom.forward(250)
tom.setheading(0)

for _ in range(10):
    for _ in range(10):
        tom.pendown()
        tom.dot(20, fetchColours())
        tom.penup()
        tom.forward(50)
        tom.penup()

    tom.setheading(90)
    tom.forward(50)
    tom.setheading(180)
    tom.forward(500)
    tom.setheading(0)

s = Screen()
s.exitonclick()
