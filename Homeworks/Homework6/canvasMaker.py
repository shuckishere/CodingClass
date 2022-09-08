
# Your Goal: Create a canvas 
# - Homework 6: part 1
# - Make a function that builds a tree
# - Make a function that builds a bush
# - Make a function that builds a skyscraper (bigger than tree)
# - Make a function that builds a animal of some kind




# ======= Imports =============
from turtle import *
import turtle


# ======= Contants =============
screen = turtle.Screen()
rick = turtle.Turtle()
pizelSize = 5


# ======= FUNCTIONS ===========


def square():
    for i in range(4):
        rick.forward(pizelSize)
        rick.right(90)

def pixel(color):
    rick.begin_fill()
    square()
    rick.color(color)
    rick.end_fill()
    rick.color("black")
    rick.forward(pizelSize)

def move(direction):
    if(direction == "left"):
        pos = rick.pos()
        rick.goto(pos[0] - pizelSize, pos[1])
    elif(direction == "right"):
        pos = rick.pos()
        rick.goto(pos[0] + pizelSize, pos[1])
    elif(direction == "down"):
        pos = rick.pos()
        rick.goto(pos[0], pos[1] - pizelSize)
    elif(direction == "up"):
        pos = rick.pos()
        rick.goto(pos[0] - pizelSize, pos[1] + pizelSize)

def paint(color, number):
    for i in range(number):
        pixel(color)

# ========== Setup ============

screen.bgcolor("white")
rick.speed(10000000)
rick.pensize(.1)
rick.hideturtle()
turtle.tracer(0,0)


# ========= Main Code ==========


rick.goto(0,0)
pixel("green")
for i in range(50):
    move("down")
    paint("green", 50)
    for i in range(50):
        move('left')

# move("left")
# move("left")
# pixel("red")
# move("up")
# pixel("blue")
# move("left")
# pixel("yellow")

# rick.penup()
# move("left")
# rick.pendown()

turtle.update()
screen.mainloop()