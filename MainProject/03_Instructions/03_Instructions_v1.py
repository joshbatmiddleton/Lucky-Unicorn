# Took the code from 02_Yes_No_Function and made it the base for the instructions.


# functions go here:
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

# function to display instructions


def instructions():
    print("**** How To Play ****")
    print()
    print("The rules will go here")
    print()
    print("Program Continues")
    print()


# Main Routine goes here.
played_before = yes_no("Have you played Lucky Unicorn Before? ")
print(f"You entered '{played_before}'")
print()

if played_before == "No":
    instructions()
else:
    print("Program Continues")
