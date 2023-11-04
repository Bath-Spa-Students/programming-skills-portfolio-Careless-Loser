#Write a python program with nested decision structures that perform the following: If amount_1
#is greater than 10 and amount_2 is less than 100, display the greater of amount_1 and amount_2
# Replace these values with your actual values for amount_1 and amount_2
amount_1 = 15
amount_2 = 80
# Check if amount_1 is greater than 10 and amount_2 is less than 100
if amount_1 > 10:
    if amount_2 < 100:
        # Display the greater of amount_1 and amount_2
        if amount_1 > amount_2:
            print("The greater value is:", amount_1)
        else:
            print("The greater value is:", amount_2)
    else:
        print("amount_2 is not less than 100")
else:
    print("amount_1 is not greater than 10")
