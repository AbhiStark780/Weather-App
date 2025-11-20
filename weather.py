# [Requests] library is used for API calling 
import requests
# Getting the secret API Key without directly embedding it the main file
from config import apiKey
# Module to handle Date and Time 
from datetime import datetime

# List of Yes Options 
YES_OPTIONS = ["y","yes"]

# Time for which i am looking the forecast data
FORECAST_TIME = "12:00:00"

# Emoji for showing the weather visuals
weather_emoji = {
    'Clear':'☀️', 
    'Rain':'🌧️', 
    'Clouds':'☁️',
    'Thunderstorm': '⛈️',
    'Snow':'❄️'
    }

# Create the get_weather function to handle the api call
def get_weather(city, API_key):
    """
        Fetches the weather data from OpenWeather API

        Args:
            city (string): The city to look up
            api_key (string): Your Personal API KEY
        
        Returns:
            dict: weather data if successfull, otherwise None
    """
    # Create the url variable (using the city and api_key parameters)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"
    # Get the response
    response = requests.get(url)
    # If the status code is 200, return the response.json().
    # If it fails (else), return None
    if response.status_code == 200:
        return response.json()
    else:   
        return None

def get_forecast(city, API_key):
    """
        Fetches the weather forecast data from OpenWeather API

        Args:
            city (string): The city to look up
            api_key (string): Your Personal API Key

        Return:
            dict: forecast weather data if successfull, otherwise None
    """
    # created the url variable that stores the api end-point
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}&units=metric"
    # get the response
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None
    
# function for displaying the forecast data
def display_forecast(forecast_data):
    """
        Display the 5 Days weather forecast

        Args: 
            forecast_data (dict): Extract data from this dictionary

        Return:
            Nothing to return, just display the forecast data upon calling
    """
    # itereate through each forecast data
    print("-" * 40)
    print("5 Day Weather Forecast")
    print("-" * 40)
    daily_forecast = forecast_data['list']
    for forecast in daily_forecast:
        if FORECAST_TIME in forecast['dt_txt']:
            date = datetime.strptime(forecast['dt_txt'][:10], "%Y-%m-%d") # Here we are creating a date object, slicing the dt_txt as we need only the date and not the time 
            temperature = forecast['main']['temp']
            visual_temp = str(temperature) + "\u00b0C"
            description = forecast['weather'][0]['description']
            print(f"{date.strftime('%a, %d %b'):<15}",end="") # strftime helps in formating the date object just as we need i.e Fri, 21 Nov
            print(f"{weather_emoji.get(forecast['weather'][0]['main'], '⚪'):<5}   {visual_temp:<10} - {description:<15}")



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

            # Get the Forecast Data
            forecast_data = get_forecast(city_name, apiKey)
            # Display the Forecast Data
            display_forecast(forecast_data)
        else:
            print("City Not Found.")

        # Prompt the user to check for another city
        user_answer = input("Check another city ? (Y/N): ")

        if user_answer.lower() in YES_OPTIONS:
            continue
        else:
            break

main()



