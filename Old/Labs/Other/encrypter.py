# get input (message) from user
# go through every letter in message, and codify it
# Print that out



# Your goal: Create a program that asks the user if they want to encrypt or decrypt

# If the user wants to encrypt: 






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





print(uncrip)
print("\n")
print (uncripSTR)