# Pong Game

import time
from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from score import Score

SCREENX = 800
SCREENY = 600
HALFX = SCREENX / 2
HALFY = SCREENY / 2
START_POS = [(HALFX - 20, 0), (-HALFX + 20, 0)]  # -380 to 380


def drawLine():
    centerLine = Turtle()
    centerLine.hideturtle()
    centerLine.penup()
    centerLine.color("white")
    centerLine.goto(0, HALFY)
    centerLine.setheading(270)
    centerLine.pendown()
    centerLine.goto(0, -HALFY)

def drawRectangle():
    centerLine = Turtle()
    centerLine.hideturtle()
    centerLine.penup()
    centerLine.color("white")
    centerLine.goto(HALFX,HALFY)
    centerLine.pendown()
    centerLine.goto(HALFX,-HALFY)
    centerLine.goto(-HALFX,-HALFY)
    centerLine.goto(-HALFX,HALFY)
    centerLine.goto(HALFX,HALFY)


s = Screen()
s.bgcolor("black")
s.setup(SCREENX, SCREENY)
s.title("The Ping Pong Game")
s.tracer(0)

paddle1 = Paddle(START_POS[0])
paddle2 = Paddle(START_POS[1])
score = Score()
ball = Ball()

s.listen()
s.onkeypress(paddle1.go_up, "Up")
s.onkeypress(paddle1.go_down, "Down")

s.onkeypress(paddle2.go_up, "w")
s.onkeypress(paddle2.go_down, "s")

drawLine()
drawRectangle()
gameOn = True

while gameOn:
    time.sleep(ball.moveSpeed)
    s.update()
    ball.moveBall()
    if not (-HALFY + 20 < ball.ycor() < HALFY - 20):
        ball.bouncefromy()

    # ===Detect Collision with Paddle
    if ((ball.xcor() > HALFX - 50) and (ball.distance(paddle1) < 50)) or (
        (ball.xcor() < -HALFX + 50) and (ball.distance(paddle2) < 50)
    ):
        ball.bouncefromx()

    # ===Detect a miss
    if ball.xcor() > HALFX - 10:
        ball.resetPosition()
        score.p2score += 1

    if ball.xcor() < -HALFX + 10:
        ball.resetPosition()
        score.p1score += 1

    score.displayScore()


s.exitonclick()
