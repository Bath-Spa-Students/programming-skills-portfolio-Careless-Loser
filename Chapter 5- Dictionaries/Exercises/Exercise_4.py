#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
#* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
#* Use a loop to print the name of each river included in the dictionary.
#* Use a loop to print the name of each country included in the dictionary.
Rivers = {
    'nile': 'Egypt',
    'Volga River ': 'Russia',
    'fraser': 'Canada',
    'Thames River': 'United Kingdom (specifically, England)',
    'yangtze': 'china',
    }

for River, country in Rivers.items():
    print(f"The {River.title()} flows through {country.title()}.")

print("\nThe following are rivers:")
for River in Rivers.keys():
    print(f"- {River.title()}")

print("\nThe following are countries:")
for country in Rivers.values():
    print(f"- {country.title()}")