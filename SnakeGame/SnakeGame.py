# SnakeGame

from turtle import Screen
from snake import Snake
import time

s = Screen()
s.setup(500, 500)
s.bgcolor("black")
s.title("Roshi The Snake")
s.tracer(0)

snaky = Snake()

s.listen()
s.onkey(snaky.up, "Up")
s.onkey(snaky.down, "Down")
s.onkey(snaky.left, "Left")
s.onkey(snaky.right, "Right")

gameOn = True

while gameOn:
    s.update()
    snaky.move()

# =====Place random food

# =====Hit the Food

# =====Hit the wall

# =====Hit the tail

# =====Maintain Score

# =====Increase the tail size

s.exitonclick()
