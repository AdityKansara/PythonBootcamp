from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 28, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.p1score = 0
        self.p2score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.displayScore()

    def displayScore(self):
        self.clear()
        self.write(f"Score\n{self.p2score}    {self.p1score}", align=ALIGN, font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"HAHAHA, Chal Nikkal!!!!", align=ALIGN, font=FONT)
