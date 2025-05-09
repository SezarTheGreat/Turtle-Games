from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which Turtle will win the race? Enter the color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [-70,-40,-10,20,50,80]
all_turtles = []

for turtle_index in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winner!")
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()