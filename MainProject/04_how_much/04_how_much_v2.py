# File for Version 1.2.

# This file creates the amount of money needed for the game.
# For example, the user might enter $5, and that would be valid.
# This version alters the code a bit by using a try/accept loop to get the user out of the crashing error.

error = "Please enter a whole number between 1 and 10\n"
valid = False

while not valid:
    try:
            user_balance = int(input("How much do you want to play with? "))
