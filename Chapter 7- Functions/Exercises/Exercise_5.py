# Define a function named describe_city with a default country of 'Chile'.
def describe_city(city, country='Chile'):
    """Describe a city and its country."""
    # Create a message that combines the city and country.
    msg = f"{city.title()} is in {country.title()}."
    # Print the message.
    print(msg)
# Call the function with different city and country combinations.
describe_city('Barcelona', 'Spain')  # Describing Barcelona in Spain.
describe_city('Reykjavik', 'Iceland')  # Describing Reykjavik in Iceland.
describe_city('Cape Town', 'South Africa')  # Describing Cape Town in South Africa.
