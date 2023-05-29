import requests
import json

API_KEY = 'afc06520f3bb0129a20259ad06ecc33c'

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.HTTPError as http_error:
        print(f'Error fetching weather for city {city}. Check city name.')
        print(f'HTTP error occurred: {http_error}')
    except requests.exceptions.RequestException as request_exception:
        print(f'Error fetching weather for city {city}. Check city name.')
        print(f'Request exception occurred: {request_exception}')
    except json.JSONDecodeError as json_error:
        print(f'JSON decoding error occurred: {json_error}')
    except Exception as error:
        print(f'An error occurred: {error}')

    return None

def display_weather(weather_data):
    if weather_data is not None:
        city_name = weather_data.get('name')
        weather = weather_data.get('weather')
        main_weather = weather[0]['main'] if weather else None
        description = weather[0]['description'] if weather else None
        main = weather_data.get('main')
        temperature = main['temp'] if main else None
        humidity = main['humidity'] if main else None

        print(f'********** {city_name} **********')
        print(f'Weather: {main_weather} - {description}' if main_weather else 'Weather data not available')
        print(f'Temperature: {temperature}°C' if temperature else 'Temperature data not available')
        print(f'Humidity: {humidity}%' if humidity else 'Humidity data not available')
        print('**************************')

def get_city():
    city = input('Enter city name OR type QUIT to exit: ')
    if city.lower() == 'quit':
        exit()
    else:
        weather_data = get_weather(city)
        display_weather(weather_data)
        main()

def main():
    get_city()

if __name__ == '__main__':
    main()
