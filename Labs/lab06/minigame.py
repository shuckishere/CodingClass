
# Your Goal: Create a background, create boundries, 




# ======= Imports =============
from os import curdir
from turtle import *
import turtle
from tkinter import PhotoImage
from turtle import Turtle, Screen, Shape
import threading
import math


# ======= Contants =============
screen = turtle.Screen()
rick = turtle.Turtle()
boundry = 250
moving = False
speed = 15
stride = 4
travelInterval = 3

# ======= FUNCTIONS ===========


def arrow():
    arrow = turtle.Turtle("arrow")
    arrow.penup()
    arrow.speed('fastest')
    arrow.goto(0,250)
    arrow.speed(1)
    arrow.goto(0,-250)
    arrow.hideturtle()  

def changeDirection(angle):
    global moving
    moving = False
    rick.setheading(angle)
    moving = True



def travel():
    global rick
    pos = rick.pos()
    loc = int(pos[0])
    if(moving != False):
        if(loc < boundry and loc > -boundry):
            rick.forward(stride)
        else:
            if(rick.heading() == 0):
                changeDirection(180)
            elif(rick.heading() == 180):
                changeDirection(0)
            rick.forward(stride*2)
    screen.ontimer(travel, travelInterval)



# ========== Setup ============
gif = PhotoImage(file="Labs/lab06/capybera.gif").zoom(1,1)
turtle.addshape("Capybera", Shape("image", gif))
rick.shape("Capybera")
rick.penup()
rick.speed(speed)


screen.onkey(lambda: changeDirection(180), 'Left')
screen.onkey(lambda: changeDirection(0), "Right")
screen.listen()


# ========= Main Code ==========


#for i in range(5):
 #   thread = threading.Thread(target=arrow)
 #   thread.start()


rick.forward(50)

travel()


screen.mainloop()