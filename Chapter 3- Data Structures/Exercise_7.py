# List of locations
locations = ['Alps', ' Rockies', 'Patagonia', 'Yukon', 'Fiji']

# Print the original order of locations
print("Original order:")
print(locations)

# Print the locations in alphabetical order without modifying the original list
print("\nAlphabetical:")
print(sorted(locations))

# Confirm that the original order is unchanged
print("\nOriginal order:")
print(locations)

# Print the locations in reverse alphabetical order without modifying the original list
print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

# Confirm that the original order is unchanged
print("\nOriginal order:")
print(locations)

# Reverse the order of locations in the original list
print("\nReversed:")
locations.reverse()
print(locations)

# Reverse the order again to restore the original order
print("\nOriginal order:")
locations.reverse()
print(locations)

# Sort the locations in alphabetical order in the original list
print("\nAlphabetical:")
locations.sort()
print(locations)

# Sort the locations in reverse alphabetical order in the original list
print("\nReverse alphabetical:")
locations.sort(reverse=True)
print(locations)
