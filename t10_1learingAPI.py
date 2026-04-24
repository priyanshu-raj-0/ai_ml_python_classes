# using weather api and fetching data using requests library to fetch data form weather API

import requests

# We need coordinates to get weather data

# latitude = 48.85 # Paris latitude
# longitude = 2.35 # Paris longitude

latitude = 25.45 # Bakhtiyarpur latitude
longitude = 85.53 # Bakhtiyarpur longitude


# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"


# Make the request
response = requests.get(url)
data = response.json()

print(data)
type(data)
print(data["current"])
print(data["current"]["time"])
print(data["current"]["temperature_2m"])

print(">-<" * 100)

print(data.keys())
print(data.values())
print(data.items())





# writing function that takes latitude and longitude as an input and display the temperature

def check_weather(latitude, longitude):

    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
    data = response.json()

    return data["current"]["temperature_2m"]


bkp_temp = check_weather(latitude=25.45, longitude=85.53)
paris_temp = check_weather(latitude=48.85, longitude=2.35)
london_temp = check_weather(latitude=51.50, longitude=-0.12)
tokyo_temp = check_weather(latitude=35.68, longitude=139.69)

print(f"Bakhtiyar pur : {bkp_temp} degree c")
print(f"Paris : {paris_temp} degree c")
print(f"London : {london_temp} degree c")
print(f"Tokyo : {tokyo_temp} degree c")






