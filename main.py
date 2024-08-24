from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def counterclockwise():
    turtle.left(10)


def clockwise():
    turtle.right(10)


def clear():
    turtle.clear()
    turtle.teleport(0, 0)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counterclockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)


screen.exitonclick()
