Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city_name = input("Enter a city name: ")

if city_name in Australia:
    print(city_name, "is in Australia")
elif city_name in UAE:
    print(city_name, "is in UAE")
elif city_name in India:
    print(city_name, "is in India")
else:
    print("City not found in the given lists")

