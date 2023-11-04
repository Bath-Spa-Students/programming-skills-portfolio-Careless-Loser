#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 
#each pet
# Make an empty list to store the pets in.
Pets = []
# Make individual pets, and store each one in the list.
Pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
Pets.append(Pet)

Pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
Pets.append(Pet)

Pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
Pets.append(Pet)

# Display information about each pet.
for Pet in Pets:
    print(f"\nHere's what I know about {Pet['name'].title()}:")
    for key, value in Pet.items():
        print(f"\t{key}: {value}")