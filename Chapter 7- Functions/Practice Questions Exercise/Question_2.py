#Write a Python function that calculates the factorial of a given positive integer using
#recursion.
def factorial(n):
    # Base case: If n is 0 or 1, the factorial is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: Calculate the factorial by multiplying n with the factorial of (n-1)
        return n * factorial(n - 1)
# Example usage:
number = 5  # Replace with the desired positive integer
result = factorial(number)
print(f"The factorial of {number} is {result}")
