#Price of one USB
USB_Price = 6
#total budget
Budget = 50
#Calculating the number of USB she can buy
#Using divison operation
Number_USB = Budget // USB_Price
#Using the remainder
Remaining_Money = Budget % USB_Price
#Printing the results
print(f"She can buy {Number_USB} USB sticks and she will have ${Remaining_Money} left.")

