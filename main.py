from turtle import *

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.fd(10)


def move_back():
    turtle.bk(10)


def turn_right():
    turtle.rt(10)


def turn_left():
    turtle.lt(10)


def clear_screen():
    turtle.reset()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_back, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(clear_screen, "c")
screen.exitonclick()
