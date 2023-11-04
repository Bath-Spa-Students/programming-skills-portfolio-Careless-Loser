#Write a Python program that defines a function to check whether a given number is prime.
# Define a function to check if a number is prime
def is_prime(number):
    # Prime numbers are greater than 1
    if number <= 1:
        return False
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # It's not prime if it's divisible by any number in this range
    return True  # If no factors were found, it's a prime number
# Input: Enter the number to check for primality
number = int(input("Enter a number: "))
# Call the is_prime function to check if the number is prime
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
