#Write a python program that takes courses marks as input and then calculates average of all the
#courses. After calculating the average, calculate the percentage of a student using total marks. Assume
#the total of all the courses marks is 500 or take the total marks from the user as input. 
# Prompt the user to input marks for 5 subjects
print("Enter Marks Obtained in 5 Subjects: ")
Subject_1 = int(input())
Subject_2 = int(input())
Subject_3 = int(input())
Subject_4 = int(input())
Subject_5 = int(input())
#Calculate the sum of marks
Sum = Subject_1 + Subject_2 + Subject_3 + Subject_4 + Subject_5
#Calculate the average of marks
Average = Sum/5
#Calculate the percentage based on a total of 500 marks
Percentage = (Sum/500)*100
#Display the average and percentage
print(end="Average Mark = ")
print(Average)
print(end="Percentage Mark = ")
print(Percentage)