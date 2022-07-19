
# Your Goal: 

# Ask the user if they want to encrypt or decrypt a message

# Step 1: 
# 1. Ask the user if they want to encrypt or decrypt
# 2. Ask them for input, save it, and either encrypt it or decrypt it in a message that you print (loop through and encrypt / decrypt)


# Step 2: 
# 1. Ask the user if they want to read from the file, or type it in the chat (ask for option 1 or 2)
# 2. If they want to type in chat, it shouldn't do anything new. 
# 3. If they want to read file, call readfile function and paste the words in the output file
# 4. It should still ask if they want to encrypt or decrypt 
# 5. If the user doesn't want to use the files, let them just do it with the chat like above


# Ex: A list of words like ['hello', 'I', 'Am', 'Gavin'] is returned from def readFile
# wordsInFile = readFile() <- that lets you read file
#print(wordsInFile)


# ======= Contants =============


# ======= FUNCTIONS ===========
from os import getcwd


def readFile():
    # the open keyword opens a file in read-only mode by default
    f = open("Homeworks/input.txt")
    # read all the lines in the file and return them in a list
    inputWords = []
    lines = f.readlines()
    for line in lines: 
        words = line.split(" ")
        inputWords.extend(words)
    f.close()
    return inputWords


def writeFile(words):
    f = open("Homeworks/output.txt", "w")
    f.write(words)
    f.close()


def encryptWords(words):
    return


def decryptWords(words):
    return



# ========= Main Code ==========


# Take this code below and put it in funtions above (encrypt and decrypt )

print("\n\nType your message")
message = input()


encrypt = []

#encrypt.append() - add to list 

for letter in message:
    codelett = ord(letter)
    encrypt.append(codelett)


print(encrypt)

goodList = []
goodStr = ""


for numbs in encrypt:
    codereturn = chr(numbs)
    uncripSTR = uncripSTR + codereturn
    #uncrip.append(codereturn)


