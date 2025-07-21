from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 18, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highestScore = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.displayScore()

    def updateScore(self):
        self.clear()
        self.score += 1

    def displayScore(self):
        self.clear()
        self.write(
            f"The SNAKE\tScore: {self.score} High Score: {self.highestScore}", align=ALIGN, font=FONT
        )
    
    def reset(self):
        if self.score > self.highestScore:
            self.highestScore = self.score
        
        self.score = 0
        self.displayScore()
