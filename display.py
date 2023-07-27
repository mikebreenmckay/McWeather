from datetime import datetime


def get_day_and_time(datetime_str):
    #Function to get day of week and time of day (morning, afternoon, evening)
    date_time = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    day_of_week = date_time.strftime("%A")
    hour = date_time.hour
    time_of_day = "Morning" if 5 <= hour < 12 else "Afternoon" if 12 <= hour < 18 else "Evening"
    return day_of_week, time_of_day


def convert_to_fahrenheit(celsius_temp):
    return (celsius_temp * 9/5) + 32

def display_weather(weather_data):
    if weather_data is None:
        print("Error fetching weather data. Please try again later.")
        return

    # Parse the weather data to extract relevant information
    city_name = weather_data["name"]
    main_weather = weather_data["weather"][0]["main"]
    description = weather_data["weather"][0]["description"]
    temperature = convert_to_fahrenheit(weather_data["main"]["temp"])
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]

    # Display the weather information to the user
    print(f"Weather forecast for {city_name}:")
    print(f"Condition: {main_weather} - {description}")
    print(f"Temperature: {temperature:.1f}°F")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")


def display_forecast(forecast_data):
    if forecast_data is None:
        print("Error fetching forecast data. Please try again later.")
        return

    # Parse the forecast data to extract relevant information
    city_name = forecast_data["city"]["name"]
    forecast_list = forecast_data["list"]

    # Display the future weather forecast for the next 5 days
    print(f"Weather forecast for {city_name} - Next 5 days:")
    for forecast in forecast_list:
        date_time = forecast["dt_txt"]
        main_weather = forecast["weather"][0]["main"]
        description = forecast["weather"][0]["description"]
        temperature = convert_to_fahrenheit(forecast["main"]["temp"])
        humidity = forecast["main"]["humidity"]
        wind_speed = forecast["wind"]["speed"]

        # Get day of the week and time of day
        day_of_week, time_of_day = get_day_and_time(date_time)

        print(f"\n{day_of_week} - {time_of_day}")
        print(f"Condition: {main_weather} - {description}")
        print(f"Temperature: {temperature:.1f}°F")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")



# Test the function
if __name__ == "__main__":
    # Assume you already have the weather_data dictionary
    weather_data = {
        "name": "New York",
        "weather": [{"main": "Clouds", "description": "scattered clouds"}],
        "main": {"temp": 25.5, "humidity": 70},
        "wind": {"speed": 3.5},
    }
    display_weather(weather_data)
    forecast_data = {
        "city": {"name": "New York"},
        "list": [
            {
                "dt_txt": "2023-07-26 09:00:00",
                "weather": [{"main": "Rain", "description": "light rain"}],
                "main": {"temp": 22.5, "humidity": 80},
                "wind": {"speed": 4.5},
            },
            # Additional forecast entries for other days and times
        ]
    }
    display_forecast(forecast_data)