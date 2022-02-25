####################################################################################
# Author:                           TODO: Change this to your name
# Username:                         TODO: Change this to your username
#
# Assignment: E1 - Coding Portion
# Purpose: Evaluate your ability to write code in Python
# Value: 25 points total
#
# Instructions:
#   Complete ALL of the tasks indicated below. Read carefully!
#   Even if you do not complete all tasks, submit what you complete before the class period ends.
#   Anything pushed after the class end time will not be considered while grading.
#   You may use the Python documentation, your own code, any code we've given you as part of this class,
#       and the online book. No other resources, especially no Googling!
#   You must do this alone without a partner and without help from your classmates.
#
# Overview:
#   This program draws a lovely array of winter-colored snowflakes.
#
####################################################################################
#
# TODO A successful student will have completed the following tasks:
#   Task 1: Refactor the code to use a main() function. (6 pts)
#   Task 2: Ask the user to input a number between 1 and 4.  (3 pts)
#   Task 3: Call the draw_winter function, indicating how many snowflakes to draw using the user's input from Task 2. (4 pts)
#   Task 4: Fix the draw_winter() function by converting it to use a loop and iterate the right number of times. (8 pts)
#   Task 5: Add docstrings and comments where appropriate, modify this header, and clean up any unused code. (4 pts)
#   Bonus: Include a new function that writes "It's February!" to the turtle screen.
#          modify main() to use this new function correctly IF the user picked four. (+3 pts)

####################################################################################
# Submission Instructions:
# Use git to commit and push your changes to the GitHub repository.
# Make sure your push is complete before the end of class!
####################################################################################

import turtle

def colors(col):
    """
    Returns a color. DO NOT MODIFY!!!
    :param col: color number
    :return: String representing a color
    """
    if col == 0:
        return "turquoise"
    elif col == 1:
        return "lightblue"
    elif col == 2:
        return "lightgray"
    elif col == 3:
        return "violet"

def draw_flake(t, mycolor='blue'):
    """
    This function draws one Snowflake on the screen.  DO NOT MODIFY!!!
    :return: None
    """

    t.seth(0)
    t.color(mycolor)
    t.fillcolor(mycolor)

    points = 8
    old_heading = t.heading()
    for i in range(points):
        t.begin_fill()
        for j in range(2):
            t.forward(40)
            t.left(45)
            t.fd(40)
            t.left(135)
        t.end_fill()

        t.seth(old_heading + int(360 / points))
        old_heading = t.heading()

def move(t):
    """
    Moves a turtle object 75 pixels to the right and 75 pixels down.  DO NOT MODIFY!!!
    :param t: a Turtle
    :return: None
    """
    t.penup()
    t.setpos(t.xcor() + 75, t.ycor() - 75)
    t.pendown()

def draw_winter(t, numflakes):
    """

    :param t:
    :param numflakes:
    :return:
    """
    # TODO Complete the docstring for this function. Follow the format of the other docstrings in this file.

    # TODO   This code is inefficient and inflexible. Rewrite the code below to use a loop
    #        the right number of times, based on the input parameters.

    # Draws four snowflakes
    draw_flake(t, mycolor=colors(0 % 4))
    move(t)
    draw_flake(t, mycolor=colors(1 % 4))
    move(t)
    draw_flake(t, mycolor=colors(2 % 4))
    move(t)
    draw_flake(t, mycolor=colors(3 % 4))
    move(t)

# The program starts running here
# TODO  Refactor this program to use a main() function. The highest level of the program should include
#       import statements, function definitions, and a call to main() ONLY
w = turtle.Screen()
t = turtle.Turtle()

t.speed(15)
t.penup()
t.setpos(-125, 150)
t.pendown()


# TODO   Ask the user to input a number between 1 and 4.

# TODO   Call the draw_winter function, indicating how many snowflakes to draw using the user's input (instead of four)

draw_winter(t, 4)

w.exitonclick()
