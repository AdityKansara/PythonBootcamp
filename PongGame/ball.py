from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.moveSpeed = 0.1
        
    def moveBall(self):
        x = self.xcor()
        y = self.ycor()
        newX = x + self.x_move
        newY = y + self.y_move
        self.goto(newX, newY)
    
    def bouncefromy(self):
        self.y_move *= (-1)
    
    def bouncefromx(self):
        self.x_move *= (-1)
        self.moveSpeed *= 0.9
    
    def resetPosition(self):
        self.goto(0,0)
        self.bouncefromx()
        self.moveSpeed = 0.1