import random
num = 0

# basic for loop
for i in range(3):
    print ("cheese")

# using index of for loop
for i in range(3):
    print(i)


# using for loop to go through list 
TheList = ["cake", "hees", "soup"]
for obj in TheList:
    print(obj)


# using loop with iterator  
TheList = ["cake", "hees", "soup"]
for obj in TheList:
    num = num + 1
    print(obj, num)

while num > 0:
    print("wrong")
    num = num - 1


    

