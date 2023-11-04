#Write a Python program that uses a while loop to find the largest number among a series of
#user-input values until they enter '0' to exit the loop.
largest = None  # Initialize a variable to store the largest number
while True:
    user_input = input("Enter a number (or '0' to exit): ")
    if user_input == '0':
        break  # Exit the loop if '0' is entered
    try:
        number = float(user_input)  # Convert user input to a float
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue  # Continue to the next iteration
    if largest is None or number > largest:
        largest = number  # Update the largest number
if largest is not None:
    print(f"The largest number entered is: {largest}")
else:
    print("No valid numbers entered.")

