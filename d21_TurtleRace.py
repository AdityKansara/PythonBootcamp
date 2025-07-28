# Turtle Race

from turtle import Screen, Turtle
import turtle
from Resources.data import turtle_colors
import random

turtle_list = []
y = 100
race = False

finishline = Turtle()
finishline.shape("arrow")
finishline.color("black")
finishline.width(15)
finishline.speed("fast")
finishline.penup()
finishline.goto(220, 150)
finishline.pendown()
finishline.setheading(270)
finishline.forward(240)

for i in range(0, 6):
    tom = Turtle()
    tom.shape("turtle")
    tom.color(turtle_colors[i])
    tom.speed("fast")
    tom.penup()
    tom.goto(-235, y)
    y -= 30
    turtle_list.append(tom)

s = Screen()
s.setup(500, 500)
userBet = s.textinput(
    "===Turtle Race===",
    "What do you think, which turtle will Win?\n red, yellow, blue, black, cyan, blue4",
)

if userBet != "":
    race = True

while race:
    for miniTurtle in turtle_list:
        distance = random.randint(0, 10)
        miniTurtle.forward(distance)

        if miniTurtle.xcor() >= 220:
            race = False
            winner = miniTurtle.pencolor()

            if userBet == winner:
                print(f"You win! Winner is {winner}")
            else:
                print(f"You lose! Winner is {winner}")
            break
s.exitonclick()
