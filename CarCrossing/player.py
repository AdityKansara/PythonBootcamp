from turtle import Turtle

START_POS = (0, -280)
MOVE_SPEED = 10
FINISHLINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.gotoStart()

    def moveup(self):
        self.forward(MOVE_SPEED)
    
    def gotoStart(self):
        self.goto(START_POS)
    
    def isAtFinishLine(self):
        if self.ycor() >= 300:
            self.gotoStart()
            return True
        else:
            return False
    

