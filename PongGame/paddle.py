import time
from turtle import Turtle

DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(1, 5)
        self.penup()
        self.setheading(DOWN)
        self.goto(position)

    def go_up(self):
        newY = self.ycor() + 30
        self.goto(self.xcor(), newY)

    def go_down(self):
        newY = self.ycor() - 30
        self.goto(self.xcor(), newY)
