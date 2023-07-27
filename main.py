# main.py

# Step 1: Import necessary modules
import requests  # For making API requests (Step 3)
from api import get_weather_data, get_weather_forecast  # Functions to fetch weather data and forecast from the API
from display import display_weather, display_forecast  # Functions to display weather information and forecast
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


def display_menu():
    # Display the main menu options
    print("\n===== Weather Forecast Application =====")
    print("1. View Weather Forecast")
    print("2. View Extended Weather Forecast")
    print("3. Enter New Location")
    print("4. Exit")


def main():
    # Step 1: Get the API key (you've already done this)

    while True:
        display_menu()

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            location = get_user_location()
            weather_data = get_weather_data(api_key, location)
            display_weather(weather_data)
        elif choice == "2":
            location = get_user_location()
            forecast_data = get_weather_forecast(api_key, location)
            display_forecast(forecast_data)
        elif choice == "4":
            print("Exiting the Weather Forecast Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1, 2, or 3).")


if __name__ == "__main__":
    main()
