import machine
import dht
from time import sleep
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import urequests
import network
import ujson
import socket

# stworzenie zmiennych dla czujnika i wyswietlacza LCD oraz przypisanie odpowiednich parametrow
sensor = dht.DHT11(Pin(14))
I2C_ADDR = 0x3f
totalRows = 2
totalColumns = 16

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

# stworzenie znaku specjalnego dla wyswietlacza LCD - znak stopni
temperature_sign = bytearray([
    0x04,
    0x0A,
    0x04,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00
])
lcd.custom_char(0, temperature_sign)

# zmienne wykorzystane przy polaczeniu z siecia
ssid = 'ssid Twojej sieci'
key = 'haslo Twojej sieci'

# funkcje
def connect_to_wifi(ssid, key):
    global wlan
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # might already be connected somehow.
    if wlan.isconnected() == False:
        wlan.connect(ssid, key)

    # Wait for connection.
    while wlan.isconnected() == False:
        pass

    print('connected!')
    
def measure():
    try:
        sensor.measure()
        temp = sensor.temperature()
        humidity = sensor.humidity()
        print(f"Temperatura: {temp} {chr(176)}C")
        print(f"Wilgotność: {humidity}%")
        return temp, humidity
    except:
        print('Nie wykonano pomiaru')

def send_measurements(temperature, humidity):
    try:
        data = {'temperature': temperature, 'humidity': humidity}
        data = ujson.dumps(data) # zmiana formatu z dict na JSON
        req = urequests.post(url, data=data, headers = {'content-type': 'application/json'})
        #print(req.text)
    except:
        print('Nie udało się wysłać danych')



    
connect_to_wifi(ssid, key)      
url = "url strony na ktora wysyłasz POSTA" #w przypadku localhosta wzor wyglada nastepujaco: http://IPv4 Address:8000/dalsza czesc linku/

while True:
    sleep(1)
    temperature, humidity = measure()
    lcd.clear()
    lcd.putstr("Temp: %d" %temperature + chr(0) + "C\n")
    lcd.putstr("Humidity: %d%%" %humidity)
    sleep(0.1)
    send_measurements(temperature, humidity)
    sleep(58.9)
    




   
   

