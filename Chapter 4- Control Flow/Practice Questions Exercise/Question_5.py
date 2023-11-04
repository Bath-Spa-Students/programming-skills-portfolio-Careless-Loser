#Write a Python program that uses the elif statement to determine the season based on the
#month provided as input.
# Input: month as an integer (1 for January, 2 for February, etc.)
month = int(input("Enter the month (1-12): "))
# Determine the season based on the month
if 3 <= month <= 5:
    season = "Spring"
elif 6 <= month <= 8:
    season = "Summer"
elif 9 <= month <= 11:
    season = "Autumn"
else:
    season = "Winter"
# Display the determined season
print(f"The season for month {month} is {season}")
