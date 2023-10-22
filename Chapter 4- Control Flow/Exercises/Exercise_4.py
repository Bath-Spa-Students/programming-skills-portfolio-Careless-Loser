# Define the variable Age and set it to 18.
Age = 18
# Check the value of Age against different age ranges.
# If Age is less than 2, print "You're a baby!"
if Age < 2:
    print("You're a baby!")
# If Age is not less than 2, but is less than 4, print "You're a toddler!"
elif Age < 4:
    print("You're a toddler!")
# If Age is not in the above two ranges, but is less than 13, print "You're a kid!"
elif Age < 13:
    print("You're a kid!")
# If Age is not in the previous ranges, but is less than 20, print "You're a teenager!"
elif Age < 20:
    print("You're a teenager!")
# If Age is not in the above ranges, but is less than 65, print "You're an adult!"
elif Age < 65:
    print("You're an adult!")
# If none of the previous conditions are met, print "You're an elder!"
else:
    print("You're an elder!")
