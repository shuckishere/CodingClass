import turtle

screen = turtle.Screen()
screen.bgcolor('black')
#screen.screensize(3500, 350)


snake = turtle.Turtle()
snake.color('red')
snake.penup()

Boundry = 250
bigBondry = 500

speed = 3




def inBounds():
    position = snake.pos()
    #print(position[0])
    if position[0] > Boundry or position[0] < -Boundry or position[1] > Boundry or  position[1] < -Boundry: 
        snake.hideturtle()
        endGame()
        return False
    else:
        return True

def travel():
    isItGood = inBounds()
    if isItGood == False:
        return False
    else:
        snake.forward(speed)
        screen.ontimer(travel, 10)
    


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

def endGame():
    penBoi = turtle.Turtle()
    penBoi.hideturtle()
    penBoi.speed(999999999999999999999999999999999999)
    penBoi.penup()
    penBoi.goto(0,200)
    penBoi.color('red')
    style = ('Courier', 30, 'italic')
    penBoi.write('GAME OVER', font=style, align="center")
    


screen.onkey(lambda: snake.setheading(90), 'Up')
screen.onkey(lambda: snake.setheading(180), 'Left')
screen.onkey(lambda: snake.setheading(0), "Right")
screen.onkey(lambda: snake.setheading(270), 'Down')

screen.listen()


drawBoundry()
travel()

screen.mainloop()