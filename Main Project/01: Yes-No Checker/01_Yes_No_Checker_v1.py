# Ask the user if they have played before:

show_instructions = input("Have you played Lucky Unicorn Assesment before? ")

# If they say yes, output "Program continues"

if show_instructions == "yes":
    print("Program Continues")

# If they say no, output "display instructions"
elif show_instructions == "no":
    print("Display Instructions")

# Otherwise, show error message
else:
    print("Please answer 'yes' or 'no'.")
