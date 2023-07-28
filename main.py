# main.py

# Step 1: Import necessary modules
from api import get_weather_data, get_weather_forecast  # Functions to fetch weather data and forecast from the API
from display import display_weather, display_forecast  # Functions to display weather information and forecast
from config import API_KEY
from settings import DEFAULT_LOCATION, DEFAULT_UNIT

api_key = API_KEY


def update_settings_file(default_location, default_unit):
    # Function to update the settings in settings.py file
    with open("settings.py", "w") as file:
        file.write(f"DEFAULT_LOCATION = '{default_location}'\n")
        file.write(f"DEFAULT_UNIT = '{default_unit}'\n")


def get_user_settings(settings_update=False):
    # Function to get user settings for default location and temperature units.
    default_location = input(f"Enter the default location [{DEFAULT_LOCATION}]: ")
    default_location = default_location.strip() if default_location.strip() else DEFAULT_LOCATION

    default_unit = input(f"(Fahrenheit or Celsius) Enter the preferred temperature unit [{DEFAULT_UNIT}]: ")
    default_unit = default_unit.strip().capitalize() if default_unit.strip() else DEFAULT_UNIT

    if settings_update:
        update_settings_file(default_location, default_unit)

    return default_location, default_unit


def get_user_location():
    # Function to get user input for the location
    while True:
        user_input = input("Enter the location for weather forecast (city name or zip code): ")
        # Perform input validation here, e.g., check if the input is not empty.
        if user_input:
            return user_input
        else:
            print("Invalid input. Please try again.")


def display_menu(current_location, current_unit):
    # Display the main menu options
    print("\n===== Weather Forecast Application =====")
    print(f"Current Location: {current_location}")
    print(f"Current Units: {current_unit}")
    print("1. View Current Weather")
    print("2. View Extended Weather Forecast")
    print("3. Edit Settings")
    print("4. Exit")


def main():
    current_location, current_unit = DEFAULT_LOCATION, DEFAULT_UNIT
    unit = "metric" if current_unit == "Celsius" else "imperial"

    while True:
        display_menu(current_location, current_unit)

        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == "1":
            weather_data = get_weather_data(api_key, current_location)
            display_weather(weather_data, unit)
        elif choice == "2":
            forecast_data = get_weather_forecast(api_key, current_location)
            display_forecast(forecast_data, unit)
        elif choice == "3":
            current_location, current_unit = get_user_settings(True)
            unit = "metric" if current_unit == "Celsius" else "imperial"
        elif choice == "4":
            print("Exiting the Weather Forecast Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1, 2, or 3).")


if __name__ == "__main__":
    main()
