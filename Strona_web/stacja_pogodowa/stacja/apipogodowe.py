import requests

api_link = "https://api.openweathermap.org/data/2.5/weather?q="
api_key = "&appid=ce4356a69daed361db04060e154043f9"
api_units = "&units=metric"
api_lang = "&lang=pl"


def get_data(api_city):
    try:
        URL = api_link + api_city + api_key + api_units + api_lang
        response_dict = requests.get(URL).json()
        temperature = round(response_dict['main']['temp'])
        sensed_temperature = round(response_dict['main']['feels_like'])
        max_temperature = round(response_dict['main']['temp_max'])
        min_temperature = round(response_dict['main']['temp_min'])
        weather_description = response_dict['weather'][0]['description']
        humidity = response_dict['main']['humidity']
        pressure = response_dict['main']['pressure']
        wind_speed_km_h = round(response_dict['wind']['speed'] * 3.6, 1)
        wind_speed_m_s = response_dict['wind']['speed']
        city = response_dict['name'] 
        country = response_dict['sys']['country']
    
    except KeyError:
        print("Error, nie ma takiego miasta")

    return temperature, sensed_temperature, max_temperature, min_temperature, weather_description, humidity, pressure, wind_speed_km_h, wind_speed_m_s, city, country

