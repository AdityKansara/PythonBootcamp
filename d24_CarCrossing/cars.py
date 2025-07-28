from turtle import Turtle
import random

turtle_colors = ["red", "blue", "yellow", "black", "cyan", "blue4", "SeaGreen"]
LEFT = 180
MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RIGHT_EDGE = 400
LEFT_EDGE = -400


class Cars:
    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        if random.randint(1, 6) == 1:
            car = Turtle()
            car.color(random.choice(turtle_colors))
            car.shape("square")
            car.shapesize(1, 2)
            car.penup()
            car.setheading(LEFT)
            car.goto(RIGHT_EDGE, random.randint(-230, 230))
            self.all_cars.append(car)
            self.speed = MOVE_DISTANCE

    def moveCar(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def speedUp(self):
        self.speed += MOVE_INCREMENT

    def destroy(self):
        for car in self.all_cars:
            if car.xcor() <= LEFT_EDGE:
                car.hideturtle()
