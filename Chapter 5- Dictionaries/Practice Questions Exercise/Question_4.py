#Write a Python program to iterate through both the keys and values of a dictionary and print
#them 
# Create a sample dictionary
my_dict = {
    "Name": "Ifrah",
    "Age": 18,
    "Born": 2004,
    "Birth Place": "Dubai"
}
# Iterate through both keys and values and print them
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")