# app.py

from flask import Flask, render_template, request
from api import get_weather_data, get_weather_forecast
from display import display_weather, display_forecast
from settings import DEFAULT_LOCATION, DEFAULT_UNIT

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        unit = request.form['unit']
    else:
        location = DEFAULT_LOCATION
        unit = DEFAULT_UNIT

    weather_data = get_weather_data(api_key, location)
    forecast_data = get_weather_forecast(api_key, location)

    if unit == 'Celsius':
        unit_key = 'metric'
    else:
        unit_key = 'imperial'

    return render_template('index.html', weather_data=weather_data, forecast_data=forecast_data, unit=unit_key)

if __name__ == '__main__':
    app.run(debug=True)
