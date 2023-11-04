# Define a list of sandwich orders.
Sandwich_Orders = ['club', 'tuna', 'ham and cheese', 'pastrami']
# Create an empty list to store finished sandwiches.
Finished_Sandwiches = []
# Process each sandwich order.
while Sandwich_Orders:
    Current_Sandwich = Sandwich_Orders.pop()  # Get the last order.
    print(f"I'm working on your {Current_Sandwich} sandwich.")
    Finished_Sandwiches.append(Current_Sandwich)  # Add to finished sandwiches.
print("\nSandwiches ready for pickup:")
# Display the list of finished sandwiches.
for Sandwich in Finished_Sandwiches:
    print(f"I made a {Sandwich} sandwich.")
