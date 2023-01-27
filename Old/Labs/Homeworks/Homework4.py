import math

myList1 = [23, 55, 123, 2, 1, 99, 21, 59, 293, 11, 55, 100]

myList2 = [55, 123, 2, 11, 55, 100]

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
    return myList[0]

# Get the last item in the list
def getLast(myList):
    return myList[-1]

# Get the biggest number in the list
def getGreatest(myList):
    booty = 0
    for thing in myList:    
        #print(thing)  
        if(thing > booty):
            #print("Biggest so far: " + str(thing))
            booty = thing
    return booty

# Get the smallest number in the list
def getSmallest(myList):
    puck = 999999999999 * 99999999999 * 2
    for thing in myList:
        print(thing)
        if (thing < puck):
            print("the smallest so far: " + str(thing))
            puck = thing 
    return puck

# Get all the numbers added up
def getAddedUp(myList):
    booty = 0
    numItems = len(myList) # This is number of things in the list - length of list is: len(list)
    for x in range(numItems): # x is the index in the foor loop, so 0, then 1, then 2, then 3
        booty = myList[x] + booty # This adds up each thing in the fo
    return booty

# Get all the numbers multipled up
def getMultiplied(myList):
    butts = 1
    numofstuff = len(myList)
    for x in range(numofstuff):
        print("x is = " + str(x) + " mylist at x is " + str(myList[x]))
        butts = myList[x] * butts
    return butts

    return butts



print("\n\nLIST 1\n")

#print( getFirst(myList1) )
#print( getLast(myList1) )
#print( getGreatest(myList1) )
#smallestBoi = getSmallest(myList1)
#print( smallestBoi )
#print( getAddedUp(myList1) )
print( getMultiplied(myList1) )


print("\n\nLIST 2\n")
#print( getFirst(myList2) )
#print( getLast(myList2) )
#print( getGreatest(myList2) )
#print( getSmallest(myList2) )
#print( getAddedUp(myList2) )
#print( getMultiplied(myList2) )
