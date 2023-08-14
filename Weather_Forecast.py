import requests

def get_weather_data(city, api_key):
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(base_url)
    weather_data = response.json()
    return weather_data

def display_weather(weather_data):
    if weather_data['cod'] == 200:
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description']

        print(f'Temperature: {temp}°C')
        print(f'Humidity: {humidity}%')
        print(f'Wind Speed: {wind_speed} m/s')
        print(f'Description: {description}')
    else:
        print('City not found.')

def main():
    api_key = '********************************'
    city = input('Enter city name (e.g., Hyderabad, IN): ')
    weather_data = get_weather_data(city, api_key)
    display_weather(weather_data)

if __name__ == '__main__':
    main()
