#Write a Python program that defines a function to calculate the area of a circle, and then
#calls that function with a given radius.
import math  # Import the math module for pi
# Define a function to calculate the area of a circle
def calculate_circle_area(radius):
    # Use the formula for the area of a circle: π * r^2
    area = math.pi * (radius ** 2)
    return area
# Input: Enter the radius of the circle
radius = float(input("Enter the radius of the circle: "))
# Call the calculate_circle_area function to calculate the area
area = calculate_circle_area(radius)
# Display the calculated area
print(f"The area of the circle with radius {radius} is {area:.2f}")
