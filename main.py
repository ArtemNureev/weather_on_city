import requests
import json

city = 'Казань'

url = ('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347')

weather_data = requests.get(url).json()
weather_data_structure = json.dumps(weather_data, indent=2)

temperature = round(weather_data['main']['temp'])

print('Сейчас в городе', city, str(temperature), 'градусов')

temperature_feels = round(weather_data['main']['feels_like'])
print('Ощущается как', str(temperature_feels), 'градусов')

wind_speed = round(weather_data['wind']['speed'])
print("Скорость ветра", str(wind_speed), "м/с")