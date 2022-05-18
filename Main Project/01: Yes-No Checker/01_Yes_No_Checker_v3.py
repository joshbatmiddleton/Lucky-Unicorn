
show_instructions = ""
while show_instructions != "x":

    # Ask the user if they have played before:

    show_instructions = input("Have you played Lucky Unicorn Assesment before? ").lower()

    # If they say yes, output "Program continues"

    if show_instructions == "yes" or show_instructions == "Yes" or show_instructions == "Y" or show_instructions == "y":
        print("Program Continues")

    # If they say no, output "display instructions"
    elif show_instructions == "no" or show_instructions == "No" or show_instructions == "N" or show_instructions == "n":
        print("Display Instructions")

    # Otherwise, show error message
    else:
        print("Please answer 'yes' or 'no'.")

    print(f"You entered '{show_instructions}'")
