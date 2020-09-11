from sense_hat import SenseHat
from util import pixelArt as pixel
import time

sense = SenseHat()
sense.low_light = True

def pikachu():
    pikachu = pixel.pikachu()
    sense.set_pixels(pikachu)
    time.sleep(5)
    sense.clear()

def snake():
    snake = pixel.snake()
    sense.set_pixels(snake)
    time.sleep(5)
    sense.clear()