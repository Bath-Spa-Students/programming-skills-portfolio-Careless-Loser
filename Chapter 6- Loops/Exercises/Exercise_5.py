# List of sandwich orders, including some pastrami sandwiches
sandwich_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'turkey', 'roast beef', 'pastrami']
# List to store finished sandwiches
finished_sandwiches = []
# Inform customers that pastrami sandwiches are unavailable
print("I'm sorry, we're all out of pastrami today.")
# Remove all instances of 'pastrami' from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
# Print a separator for clarity
print("\n")
# Prepare the remaining sandwiches
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()  # Get the last sandwich order
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)  # Add it to the finished_sandwiches list
# Print a separator for clarity
print("\n")
# Display the finished sandwiches
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")
