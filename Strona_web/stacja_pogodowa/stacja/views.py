from django.shortcuts import render
from django.http import HttpResponse
from .apipogodowe import get_data 

# Create your views here.

def home(request):
    flag = 0 # OK
    
    api_city = request.GET.get('api_city')
    if api_city == None or api_city == '':
        city = ''
        country = ''
        temperature = ''
        sensed_temperature = ''
        max_temperature = ''
        min_temperature = ''
        weather_description = ''
        humidity = ''
        pressure = ''
        wind_speed_km_h = ''
        wind_speed_m_s = ''
        flag = 1 # Nie podano miasta
    else:
        try:
            temperature, sensed_temperature, max_temperature, min_temperature, weather_description, humidity, pressure, wind_speed_km_h, wind_speed_m_s, city, country = get_data(api_city)
        except:
            city = ''
            country = ''
            temperature = ''
            sensed_temperature = ''
            max_temperature = ''
            min_temperature = ''
            weather_description = ''
            humidity = ''
            pressure = ''
            wind_speed_km_h = ''
            wind_speed_m_s = ''
            flag = 2 # Podano złe miasto

    
    dictionary_home = {'title': 'Stacja pogodowa', 'api_city': api_city, 'temperature': temperature, 'sensed_temperature': sensed_temperature, 'max_temperature': max_temperature,
                        'min_temperature': min_temperature, 'weather_description': weather_description, 'humidity': humidity, 'pressure': pressure, 'wind_speed_km_h': wind_speed_km_h,
                        'wind_speed_m_s': wind_speed_m_s, 'city': city, 'country': country, 'flag': flag}
    return render(request, 'home.html', dictionary_home)

def about(request):
    return render(request, 'about.html')
