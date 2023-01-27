
#Pre-steps: Go over strings in python and how to manipulate

# ==== Lessons =====


# string.split(" ") - it splits on whatever is in quotations 
# "hello how are you" -> ["hello", "how", "are", "you"]


# list1.extend(list2) - it adds list2 on the back of list1
# list1 = ["hello", "how", "are", "you"]
# list2 = ["whaaaat"]
# list1.extend(list2) -> ["hello", "how", "are", "you", "whaaaat"]

# === IMPORTS ========
from http.client import REQUEST_URI_TOO_LONG
from unittest.mock import sentinel


# ======= CONTSANTS =========


# ======== FUNCTIONS =========

def readFile():
    # the open keyword opens a file in read-only mode by default
    f = open("Labs/Lab05/story.txt")
    # read all the lines in the file and return them in a list
    inputWords = []
    lines = f.readlines()
    for line in lines: 
        words = line.split(" ")
        inputWords.extend(words)
    f.close()
    return inputWords

def writeFile(words):
    f = open("Labs/Lab05/output.txt", "w")
    f.write(words)
    f.close()


def wordcount(allwords):
    numwords = 0
    for words in allwords:
        numwords = numwords + 1
    return numwords

def numoftimes(wordsch, allwords):
    numwords = 0
    for words in allwords:
        if words == wordsch:
            numwords = numwords + 1
    return numwords
    



# ========== MAIN ===========

wordsinstory = readFile()
numberofwords = wordcount(wordsinstory)
print("\n" + str(numberofwords) + " is the number of words")

print("\n" + "what word would you like to find")
wordsch = input()
wordamount = numoftimes(wordsch, wordsinstory)
print(" the word (" + wordsch + ") is used..." + "\n" + str(wordamount) + " Times!")


writeFile(" the word (" + wordsch + ") is used..." + "\n" + str(wordamount) + " Times!")
    


#Step 1
# Open story file and get words



# Step 2: 

#   Create a word detector (ex: How many times is "" found in story)
# 

# Step 3: 
# Print stuff to output file


# Step 3: 
#   Build app functionality to make it work

# Step 4: 
#   Detect most common words


# Step 5: 
# Build word replacer


#Step 6: 
# Homeworks!



