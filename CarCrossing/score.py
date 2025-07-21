from turtle import Turtle

ALIGN = "left"
FONT = ("Courier", 18, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.displayScore()

    def updateScore(self):
        self.clear()
        self.score += 1

    def displayScore(self):
        self.write(f"Level: {self.score}", align=ALIGN, font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=FONT)
