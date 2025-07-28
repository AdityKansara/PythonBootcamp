import time
from turtle import Screen, Turtle
from score import Score
from cars import Cars
from player import Player

SCREENX = 800
SCREENY = 600
HALFX = SCREENX / 2
HALFY = SCREENY / 2


def drawRectangle():
    boxLine = Turtle()
    boxLine.hideturtle()
    boxLine.penup()
    boxLine.color("black")
    boxLine.goto(HALFX, HALFY)
    boxLine.pendown()
    boxLine.goto(HALFX, -HALFY)
    boxLine.goto(-HALFX, -HALFY)
    boxLine.goto(-HALFX, HALFY)
    boxLine.goto(HALFX, HALFY)


s = Screen()
s.setup(SCREENX, SCREENY)
s.title("Car Crossing")
s.tracer(0)
s.listen()

drawRectangle()
car = Cars()
score = Score()
player = Player()

s.onkeypress(player.moveup, "Up")
gameOn = True

while gameOn:
    car.create_cars()
    car.moveCar()
    car.destroy()
    time.sleep(0.1)
    score.displayScore()
    s.update()
    allCars = car.all_cars
    for c in allCars:
        if c.distance(player) <= 20:
            gameOn = False
            score.gameOver()

    if player.isAtFinishLine():
        car.speedUp()
        score.updateScore()


s.exitonclick()
