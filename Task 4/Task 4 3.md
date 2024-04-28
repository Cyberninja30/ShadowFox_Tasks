Task 4.3

# Define a dictionary mapping cities to their respective countries
city_country_map = {"Mumbai": "India","Chennai": "India","Sydney": "Australia","Dubai": "UAE"}

# Get input from the user
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

# Get the countries of both cities
country1 = city_country_map.get(city1)
country2 = city_country_map.get(city2)

# Check if both cities belong to the same country
if country1 and country2 and country1 == country2:
    print("Both cities are in", country1)
else:
    print("They don't belong to the same country")

