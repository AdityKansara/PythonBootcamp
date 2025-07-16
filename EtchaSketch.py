from turtle import Screen, Turtle
import turtle

tom = Turtle()
tom.shape("arrow")
tom.speed("fast")
s = Screen()


def fwd():
    tom.forward(10)


def bwd():
    tom.backward(10)


def lft():
    tom.left(10)
    tom.forward(10)


def rgt():
    tom.right(10)
    tom.forward(10)

def clear():
    tom.home()
    tom.clear()
    

s.listen()
s.onkey(key="w", fun=fwd)
s.onkey(key="s", fun=bwd)
s.onkey(key="d", fun=rgt)
s.onkey(key="a", fun=lft)
s.onkey(key="c", fun=clear)

s.exitonclick()
