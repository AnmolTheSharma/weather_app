from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# OpenWeatherMap API configuration
API_KEY = '2a333c869432e924f4981fa9047abad0'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Route to display weather form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle weather data request
@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}  # Metric units for Celsius
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data['cod'] == 200:
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return render_template('weather.html', weather=weather)
    else:
        return render_template('error.html', message=data['message'])

if __name__ == '__main__':
    app.run(debug=True)
