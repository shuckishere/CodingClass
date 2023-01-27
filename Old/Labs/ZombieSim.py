import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create the player turtle
player = turtle.Turtle()
player.color("white")
player.shape("turtle")

# Set the player's speed
player.speed(0)

# Create the zombie turtle
zombie = turtle.Turtle()
zombie.color("green")
zombie.shape("turtle")

# Set the zombie's speed
zombie.speed(0)

# Initialize variables
player_health = 100
zombie_health = 100

# Main game loop
while True:
    # Move the player
    player.forward(10)
    player_health -= 1

    # Move the zombie
    zombie.forward(5)
    zombie_health -= 1

    # Check if the player has been bitten
    if player.distance(zombie) < 20:
        player_health -= 10

    # Check if the zombie has been killed
    if player.distance(zombie) < 10:
        zombie_health = 0

    # Check if the game is over
    if player_health <= 0 or zombie_health <= 0:
        break

# Print game over message
if player_health <= 0:
    print("The zombie has bitten you! You lose.")
else:
    print("You have killed the zombie! You win.")

# Close the window
screen.exitonclick()
