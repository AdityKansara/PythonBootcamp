# SnakeGame

from turtle import Screen
from score import Score
from food import Food
from snake import Snake
import time

s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Roshi The Snake")
s.tracer(0)

snaky = Snake()
foody = Food()
score = Score()

s.listen()
s.onkey(snaky.up, "Up")
s.onkey(snaky.down, "Down")
s.onkey(snaky.left, "Left")
s.onkey(snaky.right, "Right")

gameOn = True
while gameOn:
    s.update()
    snaky.move()
    x, y = snaky.snakeHead.xcor(), snaky.snakeHead.ycor()

    # ===== Put Food == Update Score == Extend Snake
    if snaky.snakeHead.distance(foody) < 15:
        score.updateScore()
        score.displayScore()
        snaky.extendSnake()
        foody.refresh()

    # ===== Hit the wall
    if not (-290 <= x <= 290 and -290 <= y <= 270):
        score.reset()
        snaky.reset()

    # =====Hit the tail
    for bodyPart in snaky.snakeBody[1:]:
        if bodyPart.distance(snaky.snakeHead) < 10:
            score.reset()
            snaky.reset()

s.exitonclick()
