def yes_no(question_text):
    while True:

        # Ask the user if they have played before:
        answer = input(question_text).lower()

        # If they say yes, output "Program continues"
        if answer == "yes" or answer == "Yes" or answer == "Y" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output "display instructions"
        elif answer == "no" or answer == "No" or answer == "N" or answer == "n":
            answer = "No"
            return answer

        # Otherwise, show error message
        else:
            print("Please answer 'yes' or 'no'.")


def instructions():
    print("**** How To Play ****")
    print()
    print("The rules will go here")
    print()

# Number checking function


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

# Main Routine goes here.


played_before = yes_no("Have you played Lucky Unicorn Before? ")

if played_before == "No":
    instructions()


# Ask the user how much they want to play with:

user_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${user_balance}")
