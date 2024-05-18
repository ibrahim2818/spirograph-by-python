import turtle
from turtle import Turtle, Screen
import random


tim=Turtle()
#tim.shape('turtle')
turtle.colormode(255) 
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colors=(r,g,b)
    return colors
tim.speed(0)
def draw_circle(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading= tim.heading()
        tim.setheading(current_heading+size_of_gap)

draw_circle(5)

Screen=turtle.Screen()
Screen.exitonclick()