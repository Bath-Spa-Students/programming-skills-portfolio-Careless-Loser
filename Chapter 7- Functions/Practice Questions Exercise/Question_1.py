#Write a Python function that takes two numbers as arguments and returns their sum.
# Define a function called add_numbers that takes two arguments: num1 and num2
def add_numbers(num1, num2):
    # Calculate the sum of num1 and num2 and store it in the result variable
    result = num1 + num2
    # Return the result as the function's output
    return result
# Example usage:
number1 = 5  # Assign a value to the first number
number2 = 7  # Assign a value to the second number
# Call the add_numbers function with number1 and number2 as arguments
sum_result = add_numbers(number1, number2)
# Print the result, displaying the sum of the two numbers
print("The sum of", number1, "and", number2, "is", sum_result)
