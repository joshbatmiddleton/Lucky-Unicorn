
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


# Main Routine goes here.
show_instructions = yes_no("Have you played Lucky Unicorn Assesment Before? ")
print(f"You entered '{show_instructions}'")
print()
having_fun = yes_no("Are you having fun? ")
print(f"You entered '{having_fun}'")
