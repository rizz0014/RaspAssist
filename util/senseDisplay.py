from util import pixelArt as pixel
from sense_hat import SenseHat
from util import sensor
from Classes import astroPi as s
from util import config

import time

sense = SenseHat()
sense.low_light = True

green = (0, 160, 77)
red = (255, 30, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
caution = (255, 30, 0)

global snakeColour


def show_t(color):
    snakeT = pixel.snakeTemp(color)
    sense.set_pixels(snakeT)
    time.sleep(2)
    sense.clear()


def show_h(color):
    snakeH = pixel.snakeHumidity(color)
    sense.set_pixels(snakeH)
    time.sleep(2)
    sense.clear()


def show_p():
    snakeP = pixel.snakePressure()
    sense.set_pixels(snakeP)
    time.sleep(2)
    sense.clear()


def update_screen():

    senseTemperature = config.temp_value
    senseHumidity = config.humidity_value
    sensePressure = config.pressure_value

    if senseTemperature == 0 or None or senseHumidity == 0 or None:
        sense.set_pixels(pixel.snakeQuestion())
        time.sleep(2)
        sense.clear()
    elif senseTemperature > 27 or senseHumidity < 30:
        sense.set_pixels(pixel.snakeExclam())
        time.sleep(2)
        sense.clear()   

    # to set how many times to display the temp data
    num = 3

    for _ in range(num):
        # temp
        tempString = str(round(senseTemperature, 1)) + " C"
        snakeColour = "h" if senseTemperature > 27 else "l" if senseTemperature < 21 else "g"
        show_t(snakeColour)
        sense.show_message(tempString, text_colour=caution, scroll_speed=0.05) if senseTemperature > 27 else sense.show_message(tempString, text_colour=blue, scroll_speed=0.05) if senseTemperature < 21 else sense.show_message(tempString, text_colour=green, scroll_speed=0.05)
    
        # humidity
        humidityString = str(round(senseHumidity, 1)) + " %"
        snakeColour = "l" if senseHumidity < 30  else "h" if senseHumidity > 50 else "g"
        show_h(snakeColour)       
        sense.show_message(humidityString, text_colour=caution, scroll_speed=0.05) if senseHumidity < 30 else sense.show_message(humidityString, text_colour=blue, scroll_speed=0.05) if senseHumidity > 50 else sense.show_message(humidityString, text_colour=green, scroll_speed=0.05)
    
        # pressure
        pressureString = str(round(sensePressure, 1)) + " Pa"
        show_p()    
        sense.show_message(pressureString, text_colour=green, scroll_speed=0.05)