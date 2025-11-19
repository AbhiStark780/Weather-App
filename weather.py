# [Requests] library is used for API calling 
import requests
# Getting the secret API Key without directly embedding it the main file
from config import apiKey

# List of Yes Options 
YES_OPTIONS = ["y","yes"]

# Emoji for showing the weather visuals
weather_emoji = {
    'Clear':'☀️', 
    'Rain':'🌧️', 
    'Clouds':'☁️',
    'Thunderstorm': '⛈️',
    'Snow':'❄️'
    }

# Create the get_weather function to handle the api call
def get_weather(city, api_key):
    """
        Fetches the weather data from OpenWeather API

        Args:
            city (string): The city to look up
            api_key (string): Your Personal API KEY
        
        Returns:
            dict: weather data if successfull, otherwise None
    """
    # Create the url variable (using the city and api_key parameters)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    # Get the response
    response = requests.get(url)
    # If the status code is 200, return the response.json().
    # If it fails (else), return None
    if response.status_code == 200:
        return response.json()
    else:   
        return None

def main():
    while True:
        # Take the user input
        city_name = input("Enter a city name: ")

        # Get the weather data for the city
        weather_data = get_weather(city_name, apiKey)

        if weather_data != None:
            # Display the Header
            print("-" * 40)
            print(f"Weather Report for {city_name}")
            print("-" * 40)
            # Display the weather description
            print(weather_emoji.get(weather_data['weather'][0]['main'], "⚪"), end="   ")
            print(weather_data['weather'][0]['description'])
            # Display the Temperaure (in celsius)
            print("🌡️", end = "   ")
            print(f"Temperature: {weather_data['main']['temp']}\u00b0C")
            # Display The Humidity(%)
            print("💧", end = "   ")
            print(f"Humidity: {weather_data['main']['humidity']}%")
            # Display the Wind Speed(m/s)
            print("💨", end = "   ")
            print(f"Wind: {weather_data['wind']['speed']}m/s")
            print("-" * 40)
        else:
            print("City Not Found.")

        user_answer = input("Check another city ? (Y/N): ")

        if user_answer.lower() in YES_OPTIONS:
            continue
        else:
            break

main()



