import time
from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakeBody = []
        self.createSnake()
        self.snakeHead = self.snakeBody[0]

    def addBody(self, position):
        snaky = Turtle("square")
        snaky.color("white")
        snaky.penup()
        snaky.goto(position)
        self.snakeBody.append(snaky)

    def createSnake(self):
        for pos in START_POS:
            self.addBody(pos)

    def extendSnake(self):
        self.addBody(self.snakeBody[-1].position())

    def move(self):
        for i in range(len(self.snakeBody) - 1, 0, -1):
            new_x = self.snakeBody[i - 1].xcor()
            new_y = self.snakeBody[i - 1].ycor()
            self.snakeBody[i].goto(new_x, new_y)
        self.snakeHead.forward(MOVE_DISTANCE)
        time.sleep(0.1)

    def up(self):
        if self.snakeHead.heading() != DOWN:
            self.snakeHead.setheading(UP)

    def down(self):
        if self.snakeHead.heading() != UP:
            self.snakeHead.setheading(DOWN)

    def left(self):
        if self.snakeHead.heading() != RIGHT:
            self.snakeHead.setheading(LEFT)

    def right(self):
        if self.snakeHead.heading() != LEFT:
            self.snakeHead.setheading(RIGHT)
