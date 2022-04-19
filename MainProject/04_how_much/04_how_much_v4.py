# File for Version 1.2.

# This file creates the amount of money needed for the game.
# For example, the user might enter $5, and that would be valid.
# This version alters the code a bit by making the code more efficient.

# Main Routine
error = "That wasn't a valid input\n"
user_balance = 0

# Keep asking until a valid input (1-10) is entered.
while not 1 <= user_balance <= 10:
    try:
        user_balance = int(input("Please enter a whole number between 1 and 10"
                                 "\nHow much wold you like to play with? $"))
        print()

    except ValueError:
        print(error)

print(f"You are playing with {user_balance}")
