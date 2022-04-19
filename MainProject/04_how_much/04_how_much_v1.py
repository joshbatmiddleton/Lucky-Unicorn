# File for Version 1.2.

# This file creates the amount of money needed for the game.
# For example, the user might enter $5, and that would be valid.

user_balance = int(input("How much do you want to play with? It must be an integer between 1 and 10: "))

# Keep asking until a valid input (1 - 10) is entered.
while not 1 <= user_balance <= 10:
    print("Try again. Please enter a whole number between 1 and 10")
    # Ask for the input:
    user_balance = int(input("How much do you want to play with? "))

print(f"You're playing with S{user_balance}")
