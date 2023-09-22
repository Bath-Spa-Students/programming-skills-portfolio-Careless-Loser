# The user will enter the radius which will convert it to a float
#Input is for typing the radius
radius = float(input("Enter the radius of the circle: "))
# Calculate the area of the circle using the formula: π * r^2
pi = 3.14 # Approximation of pi
area = pi * (radius ** 2)
# Displaying the calculated area with two decimal places
print(f"The area of the circle with radius {radius} is {area:.2f}")
