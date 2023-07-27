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