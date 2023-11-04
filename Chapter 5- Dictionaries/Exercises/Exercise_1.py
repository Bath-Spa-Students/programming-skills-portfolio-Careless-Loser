#Use a dictionary to store information about a person you know.Store their first name, last name, age, and the city in which they live. You
#should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
# Define a list of dictionaries, each representing a person
People = [
    {
        'First_Name': 'Zara',
        'Last_Name': 'Imtiaz',
        'Age': 43,
        'Place': 'sitka',
    },
    {
        'First_Name': 'Amina',
        'Last_Name': 'Imtiaz',
        'Age': 30,
        'Place': 'new york',
    },

]
# Create a function to print information about a person
def print_person_info(person):
    print(f"First Name: {person['First_Name']}")
    print(f"Last Name: {person['Last_Name']}")
    print(f"Age: {person['Age']}")
    print(f"City: {person['Place']}")
    print()
# Loop through the list of people and print their information
for person in People:
    print("Person Information:")
    print_person_info(person)
