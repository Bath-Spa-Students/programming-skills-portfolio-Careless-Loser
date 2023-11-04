#You have given a Python list. Write a program to find value 20 in the list, and if it is present,
#replace it with 200. Only update the first occurrence of an item.
#Work with the given list:
#Given list
#list1 = [5, 10, 15, 20, 25, 50, 20]
list1 = [5, 10, 15, 20, 25, 50, 20]
#Iterate through the list using enumerate to get both index and value
for index, value in enumerate(list1):
    #Check if the current value is equal to 20
    if value == 20:
        #If a match is found, replace the value with 200
        list1[index] = 200
#Print the modified list
print(list1)


