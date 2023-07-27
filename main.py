# main.py

# Step 1: Import necessary modules
import requests  # For making API requests (Step 3)
from api import get_weather_data  # Function to fetch weather data from the API
from display import display_weather  # Function to display weather information
from config import API_KEY

api_key = API_KEY


def get_user_location():
    # Function to get user input for the location
    while True:
        user_input = input("Enter the location for weather forecast (city name or zip code): ")
        # Perform input validation here, e.g., check if the input is not empty.
        if user_input:
            return user_input
        else:
            print("Invalid input. Please try again.")


def main():
    # Step 1: Get the API key (you've already done this)

    # Step 2: Get user input for the location
    location = get_user_location()
    print(f"Fetching weather data for {location}...")

    # Step 3: Fetch weather data using the API
    weather_data = get_weather_data(api_key, location)

    # Step 4: Parse and display weather information
    display_weather(weather_data)


if __name__ == "__main__":
    main()
