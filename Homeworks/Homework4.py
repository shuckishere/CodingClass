import math

myList = [23, 55, 123, 2, 1, 99, 21, 59, 293, 11, 55, 100]


# Assignment: uncomment the prints at the bottom, and make them work properly

# Remember the tools you have: 
#   For loops - https://www.geeksforgeeks.org/iterate-over-a-list-in-python/
#   Variables - https://www.w3schools.com/python/python_variables.asp
#   Accessing lists - https://www.w3schools.com/python/gloss_python_access_list_items.asp


# All of these involve looping through a list 
# Most of these involve a variable that gets added to with each loop

# Ex: 
# num = 0
# for item in theList:
#     num = item + num
# return num


# Get the first item in the list
def getFirst(myList):
    return False;

# Get the last item in the list
def getLast(myList):
    return False;

# Get the biggest number in the list
def getGreatest(myList):
    bigNum = 0
    for item in myList:
        if item > bigNum:
            bigNum = item
    return bigNum

# Get the smallest number in the list
def getSmallest(myList):
    return False

# Get all the numbers added up
def getAddedUp(myList):
    return False

# Get all the numbers multipled up
def getMultiplied(myList):
    return False

print("\n\n\n\n")
print(myList)
#print( getFirst(myList) )
#print( getLast(myList) )
print("Biggest Num: " + str(getGreatest(myList)))
#print( getSmallest(myList) )
#print( getAddedUp(myList) )
#print( getMultiplied(myList) )
print("\n\n")

