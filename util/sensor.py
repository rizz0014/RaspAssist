from Classes import astroPi as s
import requests, os
from sense_hat import SenseHat
from datetime import datetime
from util import config

sense = SenseHat()

def readings():

    global senseTemperature
    global cpu_temp
    global sensePressure
    global senseHumidity

    # to adjust the CPU temperature / ambient temperature
    cpu_temp = 0
    cpu_temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
    cpu_temp = cpu_temp[:-3]
    cpu_temp = cpu_temp[5:]

    dt = datetime.now()
    senseTemperature = sense.get_temperature()
    sensePressure = sense.get_pressure() + 16  # calibration
    senseHumidity = sense.get_humidity() + 22  # calibration

    if cpu_temp == "42.9":
        senseTemperature = senseTemperature - 14.5
    elif cpu_temp == "44.0":
        senseTemperature = senseTemperature - 14.8
    elif cpu_temp == "44.5":
        senseTemperature = senseTemperature - 15.2
    elif cpu_temp == "45.1":
        senseTemperature = senseTemperature - 15.5
    elif cpu_temp == "46.7":
        senseTemperature = senseTemperature - 15.6
    elif cpu_temp == "47.2":
        senseTemperature = senseTemperature - 15.7
    elif cpu_temp == "47.8":
        senseTemperature = senseTemperature - 15.8
    elif cpu_temp == "48.3":
        senseTemperature = senseTemperature - 15.85
    elif cpu_temp == "48.9":
        senseTemperature = senseTemperature - 15.9
    else:
        senseTemperature = senseTemperature - 16

    # passing the sensor values to the global variables at the config module
    config.temp_value = senseTemperature
    config.pressure_value = sensePressure
    config.humidity_value = senseHumidity
    config.timestamp = dt

    # using the OOP concept
    temp = s.Temperature("Temp", str(round(senseTemperature, 1)))
    pressure = s.Pressure("Pressure", str(round(sensePressure, 1)))
    humidity = s.Humidity("Humidity", str(round(senseHumidity, 1)))

    url = "https://dweet.io/dweet/for/rizz0014sense?" + "Time=" + str(dt) + "&" + "Temp=" + str(temp.data) + "&" + "Pressure=" + str(pressure.data) + "&" + "Humidity=" + str(humidity.data)

    r = requests.post(url)

    print("\nReading data...")
    print("\n-Temp: " + str(temp.data) + " C")
    print("-Pressure: " + str(pressure.data) + " Pa")
    print("-Humidity: " + str(humidity.data) + " %")
    print("\nReadings recorded")

    sense.clear()