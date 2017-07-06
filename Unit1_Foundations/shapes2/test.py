from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,600)
sides = input("enter a number")
angle = 360/sides
pencolor("red")
pendown()
for i in range(sides):
    forward(100)
    left(angle)
penup()
exitonclick()
