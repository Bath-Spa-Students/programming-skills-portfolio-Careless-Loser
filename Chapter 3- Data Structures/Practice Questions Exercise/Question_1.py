#Given a Python list, write a program to remove all occurrences of item 20.
#Given list: list = [5, 20, 15, 20, 25, 50, 20]
# Given list
List = [5, 20, 15, 20, 25, 50, 20]
# Item to remove
Item_Remove = 20
# Create a new list by iterating through the elements of list
# and only include elements that are not equal to the item we want to remove
List = [x for x in List if x != Item_Remove]
# Print the updated list without occurrences of item 20
print(List)
