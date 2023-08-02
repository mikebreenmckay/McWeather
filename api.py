# api.py

import requests
from config import API_KEY


def get_weather_data(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Create the parameters for the API request
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric",  # You can change this to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for unsuccessful requests
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def get_weather_forecast(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"

    # Create the parameters for the API request
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric",  # You can change this to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for unsuccessful requests
        forecast_data = response.json()
        return forecast_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


# Test the function
if __name__ == "__main__":
    # Replace YOUR_API_KEY with your actual API key
    api_key = API_KEY
    location = "27705"  # Replace with the location you want to fetch the weather for
    weather_data = get_weather_data(api_key, location)
    forecast_data = get_weather_forecast(api_key, location)
    if weather_data:
        print(weather_data)
        print(forecast_data)
