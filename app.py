# app.py

from flask import Flask, render_template, request
from api import get_weather_data, get_weather_forecast
from display import process_forecast
from settings import DEFAULT_LOCATION, DEFAULT_UNIT
from config import API_KEY
from datetime import datetime

api_key = API_KEY

app = Flask(__name__)


# Custom Jinja2 filter for date formatting
@app.template_filter('datetimeformat')
def datetimeformat(value, format='%Y-%m-%d'):
    return datetime.strptime(value, '%Y-%m-%d %H:%M:%S').strftime(format)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        unit = request.form['unit']
    else:
        location = DEFAULT_LOCATION
        unit = DEFAULT_UNIT

    if unit == 'Celsius':
        unit_key = 'metric'
    else:
        unit_key = 'imperial'

    # Get the weather
    weather_data = get_weather_data(api_key, location, unit_key)
    forecast_data = get_weather_forecast(api_key, location, unit_key)

    # Get current local time
    current_time = datetime.now().time()

    # Determine if it's daytime or nighttime
    sunrise_time = datetime.fromtimestamp(weather_data['sys']['sunrise']).time()
    sunset_time = datetime.fromtimestamp(weather_data['sys']['sunset']).time()
    is_daytime = sunrise_time <= current_time <= sunset_time

    forecast_dict = process_forecast(forecast_data, unit_key)

    return render_template('index.html', weather_data=weather_data,
                           forecast_dict=forecast_dict, unit=unit_key, is_daytime=is_daytime,
                           sunrise_time=sunrise_time, sunset_time=sunset_time)


if __name__ == '__main__':
    app.run(debug=True)
