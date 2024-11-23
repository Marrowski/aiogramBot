import requests


city_name = 'Mykolayiv'
API_KEY = 'a6fb4d9c8a6d29df78711ba6ee93a935'
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={46.966080}&lon={32.003246}&appid={API_KEY}')
print(response.text)