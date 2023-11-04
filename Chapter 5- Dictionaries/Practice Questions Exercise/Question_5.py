#Write a Python program to merge two dictionaries into one
# Create two sample dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
# Merge dict2 into dict1 using the update() method
dict1.update(dict2)
# The result is stored in dict1
print(dict1)
# Create two sample dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
# Merge the dictionaries using a dictionary comprehension
merged_dict = {**dict1, **dict2}
print(merged_dict)