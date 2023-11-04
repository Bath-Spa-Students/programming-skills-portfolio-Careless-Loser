# Set the initial prompt for topping selection.
Pizza = "\nWhat topping would you like on your pizza?"
Pizza += "\nEnter 'quit' when you are finished: "
# Create a loop that continues until the user decides to quit.
while True:
    # Prompt the user for a topping choice.
    Topping = input(Pizza)
    # Check if the user wants to quit.
    if Topping != 'quit':
        # Display the selected topping.
        print(f"  I'll add {Topping} to your pizza.")
    else:
        # Exit the loop when the user enters 'quit'.
        break