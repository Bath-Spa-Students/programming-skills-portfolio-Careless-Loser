# Set the initial prompt for age input.
Age = "How old are you?"
Age += "\nEnter 'quit' when you are finished. "
# Create a loop that continues until the user decides to quit.
while True:
    # Prompt the user for their age.
    age = input(Age)
    # Check if the user wants to quit.
    if age == 'quit':
        break
    age = int(age)
    # Convert the user's input to an integer.
    # Determine ticket price based on age and display the result.
    if age < 3:
        print("  You get in free!")
    elif age < 18:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")