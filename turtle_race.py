from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(500, 400)

user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    turtles.append(new_turtle)

x_axis = -230
y_axis = -100

for turtle in turtles:
    turtle.penup()
    turtle.goto(x=x_axis, y=y_axis)
    y_axis += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
