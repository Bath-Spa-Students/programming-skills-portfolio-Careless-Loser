#Define a string with leading and trailing whitespace
Name = "\tAda Lovelace\n"
#Displayong the original string
print("Unaltered:")
print(Name)
#Removing leading whitespace tab using lstrip
print("\nUsing lstrip():")
print(Name.lstrip())
#Removing traling whitespace newline using rstip
print("\nUsing rstrip():")
print(Name.rstrip())
#Removing both leading and trailing whitespace using strip
print("\nUsing strip():")
print(Name.strip())