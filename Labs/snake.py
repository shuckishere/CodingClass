 ##===== Imports ===========

import math
import turtle
import time
import random


 ##===== CONSTANTS ===========

amount = 0
Boundry = 250
speed = 5
travelInterval = 15
activeGame = True
startTime = time.time()
moving = True
foodlist = [turtle]

scoreTurtle = turtle.Turtle()

 ##===== Functions ===========

def inBounds():
    position = snake.pos()
    if position[0] > Boundry or position[0] < -Boundry or position[1] > Boundry or  position[1] < -Boundry:
        endGame()
        return False
    else:
        return True

 
def travel():
    isItGood = inBounds()
    if isItGood != False:
        closeToFood = checkCloseFood()
        if(moving):
            snake.forward(speed)
        else:
            snake.speed(0)
        screen.ontimer(travel, travelInterval)

   
def drawBoundry():
    wall = turtle.Turtle()
    wall.penup()
    wall.speed(1000000)
    wall.fillcolor("light green")
    wall.begin_fill()
    wall.goto(Boundry, Boundry)
    wall.pendown()
    wall.goto(-Boundry, Boundry)
    wall.goto(-Boundry, -Boundry)
    wall.goto(Boundry, -Boundry)
    wall.goto(Boundry, Boundry)
    wall.end_fill()
    wall.hideturtle()


def checkCloseFood():
    global foodList
    mypos = snake.pos()
    for food in foodlist:
        if math.dist(mypos, food.pos()) < 10:
            food.color('white')
            return True
    return False


   
def DisplayScore():
    global scoreTurtle
    scoreTurtle.hideturtle()
    scoreTurtle.speed(999999999999999999)
    scoreTurtle.penup()
    scoreTurtle.goto(250,250)
    scoreTurtle.begin_fill()
    scoreTurtle.pendown()
    scoreTurtle.goto(500, 250)
    scoreTurtle.goto(500, 350)
    scoreTurtle.goto(200, 350)
    scoreTurtle.goto(200, 250)
    scoreTurtle.end_fill()
    scoreTurtle.penup()
    scoreTurtle.goto(250, 260)
    scoreTurtle.color("green")
    style = ('Courier', 30, 'italic')
    scoreTurtle.write(str(amount), font=style, align="center")
    screen.ontimer(IncreaseScore, 1000)

   
def IncreaseScore():
    if activeGame != False:
        global amount
        global scoreTurtle
        amount = amount + 1
        screen.ontimer(IncreaseScore, 1000)
        style = ('Courier', 30, 'italic')
        scoreTurtle.clear()
        scoreTurtle.write(str(amount), font=style, align="center")
        


def endGame():
    print("EndGame")
    global activeGame
    activeGame = False
    print("--- %s seconds ---" % (time.time() - startTime))
    penBoi = turtle.Turtle()
    penBoi.hideturtle()
    penBoi.speed(999999999999999999999999999999999999)
    penBoi.penup()
    penBoi.goto(0,200)
    penBoi.color('red')
    style = ('Courier', 30, 'italic')
    penBoi.write('AHHH YOU SUCK', font=style, align="center")
    snake.hideturtle()

 
def changeDirection(angle):
    global snake
    global moving
    moving = False
    snake.setheading(angle)
    moving = True

def spawnfood():
    foodcords = Getfoodpos()
    apple = turtle.Turtle()
    apple.hideturtle()
    apple.penup()
    apple.goto(foodcords)
    apple.showturtle()
    global foodlist
    foodlist.append(apple)
    return False

def Getfoodpos():
    rand1 = random.randrange(1, Boundry)
    rand2 = random.randrange(1, Boundry)
    foodCoords = (rand1, rand2)
    return foodCoords
    

 ##===== SETUP ===========


screen = turtle.Screen()
screen.bgcolor('black')

snake = turtle.Turtle()
snake.color('red')
snake.penup()


screen.onkey(lambda: changeDirection(90), 'Up')
screen.onkey(lambda: changeDirection(180), 'Left')
screen.onkey(lambda: changeDirection(0), "Right")
screen.onkey(lambda: changeDirection(270), 'Down')
screen.listen()



 ##===== MAIN CODE ===========


DisplayScore()
drawBoundry()
travel()
spawnfood()
screen.mainloop()