from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Weather
from .serializers import WeatherSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['POST', 'GET'])
def esp(request):
    if request.method == 'POST':
        serializer = WeatherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return render(request, 'esp.html')
    if request.method == 'GET':
        weather_list = Weather.objects.all()
        serializer = WeatherSerializer(weather_list, many=True)
        temperature = weather_list.last().temperature
        humidity = weather_list.last().humidity
        #return JsonResponse({'weather_list': serializer.data})
        return render(request, 'esp.html', {'temperature': temperature, 'humidity': humidity, 'weather_list': weather_list})
    

    
