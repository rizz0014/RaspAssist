from Classes import astroPi as s
import requests
from sense_hat import SenseHat
sense = SenseHat()


def readings():
    # using the OOP concept
    temp = s.Temperature("Temp", str(round(sense.get_temperature(), 1)))
    pressure = s.Pressure("Pressure", str(round(sense.get_pressure(), 1)))
    humidity = s.Humidity("Humidity", str(round(sense.get_humidity(), 1)))

    url = "https://dweet.io/dweet/for/rizz0014sense?" + "Temp=" + str(temp.data) + "&" + "Pressure=" + str(pressure.data) + "&" + "Humidity=" + str(humidity.data)

    r = requests.post(url)

    print("\nReading data...")
    print("\n-Temp: " + str(temp.data) + " C")
    print("-Pressure: " + str(pressure.data) + " Pa")
    print("-Humidity: " + str(humidity.data) + " %")
    print("\nReadings recorded")
