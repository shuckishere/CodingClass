from turtle import Turtle, Screen

sreen = Screen()
sreen.bgcolor('lightblue')

snake = Turtle()
snake.color('red')
snake.penup()

speed = 5

def travel():
    snake.forward(speed)
    sreen.ontimer(travel, 10)

sreen.onkey(lambda: snake.setheading(90), 'Up')
sreen.onkey(lambda: snake.setheading(180), 'Left')
sreen.onkey(lambda: snake.setheading(0), 'Right')
sreen.onkey(lambda: snake.setheading(270), 'Down')

sreen.listen()

travel()

sreen.mainloop()