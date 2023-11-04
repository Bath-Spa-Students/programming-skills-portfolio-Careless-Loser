#Assume the lists numbers_1 has 100 elements and numbers_2 is an empty list. Write code that
#copies the values in numbers to numbers_2
# Create numbers1 with elements from 1 to 100
numbers1 = list(range(1, 101))
# Create an empty list numbers2
numbers2 = []
# Copy the values from numbers1 to numbers2
# This creates a copy of the list
numbers2 = numbers1[:]
# Print the copied list, which contains elements from 1 to 100
print(numbers2)