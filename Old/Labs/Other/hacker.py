# ===== IMPORTS ======
import turtle


# ====== Contants ======
screen = turtle.Screen()
screen.bgcolor('green')

# ======= Functions ========

def writePasswordInitial(password):
    passTurtle = turtle.Turtle()
    passTurtle.hideturtle()
    passTurtle.penup()
    passTurtle.speed(999999999999999999)
    passTurtle.goto(0,250)
    style = ('Courier', 25, 'italic')
    passTurtle.write(str("Your Password: " + password), font=style, align="center")


def setupGuessTurtle():
    global guessTurtle
    guessTurtle = turtle.Turtle()
    guessTurtle.hideturtle()
    guessTurtle.speed(999999999999999999)
    guessTurtle.penup()
    guessTurtle.goto(0,150)
    

def writeGuess(guess):
    global guessTurtle
    global password

    print(guess)
    guessTurtle.clear()
    style = ('Courier', 30, 'italic')
    guessTurtle.write(str(guess), font=style, align="center")


def hackPassword(showUpdates):
    global password
    passwordGuess = ""
    attempts = 0

    letterlist = ["a", "b", "c", 'd', 'e', 'f', 'g']
    
    for letter in letterlist:
        passwordGuess = letter
        if password == passwordGuess:
            
            break
        attempts = attempts + 1
        print(passwordGuess)









        if(showUpdates == True):
            writeGuess(passwordGuess)
    writeGuess(passwordGuess)
    print("Hacked your password in " + str(attempts) + " attempts")



# ======= Main ============
password = turtle.textinput("Hacker Maker", "Enter your password")

writePasswordInitial(password)
setupGuessTurtle()

hackPassword(False)



print("\n\n\n")



screen.mainloop()






