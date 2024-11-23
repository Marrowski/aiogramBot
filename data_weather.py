import requests
import json

city_name = input('Введіть місто:').strip().title()
API_KEY = 'a6fb4d9c8a6d29df78711ba6ee93a935'
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}')
json_resp = response.json()
print(json_resp)

def weather_info():
    print('Інформація про вибране місто')
    print('------------------------------')
    print(f'Країна: {json_resp['sys']['country']}\n'
          f'Місто: {json_resp['name']}\n'
          f'Погода:{json_resp['weather'][0]['main']}\n'
          f'Температура:{json_resp['main']['temp'] - 272}\n'
          f'Швидкість вітру:{json_resp['wind']['speed']}')

weather_info()
