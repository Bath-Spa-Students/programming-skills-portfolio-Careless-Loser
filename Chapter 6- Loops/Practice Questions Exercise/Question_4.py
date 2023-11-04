#Write a Python program that uses the break statement to exit a for loop when a specific
#condition is met.
# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use a for loop to iterate through the numbers
for number in numbers:
    print(number)
    if number == 5:
        break  # Exit the loop when the condition is met
