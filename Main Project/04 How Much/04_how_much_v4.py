# File for Version 1.2.

# This file creates the amount of money needed for the game, and turns it into a function.

def num_check(question, low, high):
    error = "That was not a valid input\n" \
        "Please enter a number between {} and {}\n".format(low, high)

    while True:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


user_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${user_balance}")
