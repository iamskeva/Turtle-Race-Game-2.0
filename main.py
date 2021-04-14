from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make yor bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_game_on = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!. The {winning_color} turtle is the winner")
            else:
                print(f"You've lost!. The {winning_color} turtle is the winner")




        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)



# def reset():
#     tim.reset()
#
# def forwards():
#     tim.forward(10)
#
# def backwards():
#     tim.backward(10)
#
# def clockwise():
#     tim.right(10)
#
# def counter_clockwise():
#     tim.left(10)
#
#
# screen.listen()
# screen.onkey(fun=forwards, key="w")
# screen.onkey(fun=reset, key="c")
# screen.onkey(fun=backwards, key="s")
# screen.onkey(fun=counter_clockwise, key="a")
# screen.onkey(fun=counter_clockwise, key="d")


screen.exitonclick()