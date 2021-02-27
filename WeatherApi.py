import requests

city = input("Enter the name of the city: ")
api_address = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=[YOUR API KEY]'

json_data = requests.get(api_address).json()
weather_main = json_data['weather'][0]['main']
weather_desc = json_data['weather'][0]['description']
temp_max = int(json_data['main']['temp_max']) - 273
temp_min = int(json_data['main']['temp_min']) - 273
humidity = int(json_data['main']['humidity'])


print(f"=+ Weather stats of {city.upper()} += ")
print(f"Status: {weather_main}")
print(f"Temperature: \n- Max: {temp_max} °C \n- Min: {temp_min} °C")
print(f"Humidity: {humidity} %")    