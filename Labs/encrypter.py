from ctypes import alignment
import tkinter as tk

window = tk.Tk()


frame1 = tk.Frame(
    background ="blue",
    master=window
    )

frame2 = tk.Frame(
    background ="green",
    master=window
    )

label1 = tk.Button(
    master=frame1,
    text="Encrypt",
    foreground="black",  # Set the text color to white
)

label2 = tk.Button(
    master=frame2,
    text="Decrypt",
    foreground="black",  # Set the text color to white
)


encryptInput = tk.Entry(    
    master=frame1
)
decryptInput = tk.Entry(    
    master=frame2
)


label1.pack()
encryptInput.pack()
label2.pack()
decryptInput.pack()



frame1.pack()
frame2.pack()
window.mainloop()

# get input (message) from user
# go through every letter in message, and codify it
# Print that out



print("\n\nType your message")
message = input()


encrypt = []

#encrypt.append() - add to list 

for letter in message:
    codelett = ord(letter)
    encrypt.append(codelett)




print(encrypt)

uncrip = []
uncripSTR = ""

for numbs in encrypt:
    codereturn = chr(numbs)
    uncripSTR = uncripSTR + codereturn
    #uncrip.append(codereturn)


print(uncrip)
print("\n")
print (uncripSTR)



# CLASSES 




# Warrior 
# hitpoints - int
# strength - int 
# invetory = []

# warrior.pickup(item)
    # myself.invetory.Append(item)
# Warrior.fight()
    #take hitpoints from other warrior
#warrior.takeDamage()
    # hitpoints - 5
# warrior.fight(): 
# Warrior 
    # 