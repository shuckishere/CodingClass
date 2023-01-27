import random


def startUp(randNum):
    num = 0
    while num != randNum:
        print("choose a number 1 - 10")
        num = input()
        if num == randNum:
            print("you got it!")
        else:
            print("wrong try again")



# startup called 1st time - num == 5
#   While 5 != 10
    # startup called 2nd time - num == 10
    # AYYY you got it



def turnToString(number):    
    stringNumber = str(number)
    return stringNumber


r = random.randint(0, 10)
r = str(r)
startUp(r)

print(r)

