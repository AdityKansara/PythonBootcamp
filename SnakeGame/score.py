from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 18, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.displayScore()

    def updateScore(self):
        self.clear()
        self.score += 1

    def displayScore(self):
        self.write(
            f"Game Roshi - The SNAKE\tScore: {self.score}", align=ALIGN, font=FONT
        )

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"HAHAHA, Chal Nikkal!!!!", align=ALIGN, font=FONT)
