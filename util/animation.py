from util import pixelArt as pixel
from sense_hat import SenseHat

import time

sense = SenseHat()

def pikachu():
    pikachu = pixel.pikachu()
    sense.set_pixels(pikachu)
    time.sleep(5)
    sense.clear()

def kirby():
    kirby = pixel.kirby()
    sense.set_pixels(kirby)
    time.sleep(5)
    sense.clear()

def snake():
    snakeAnimated = [pixel.snake, pixel.snake2]
    count = 0

    while count < 10:
        sense.set_pixels(snakeAnimated[count % len(snakeAnimated)]())
        time.sleep(1)
        count += 1

    sense.clear()

def snakeNotify():
    snake = pixel.snakeExclam()
    sense.set_pixels(snake)
    time.sleep(2)
    sense.clear()

def snakeQuestion():
    snake = pixel.snakeQuestion()
    sense.set_pixels(snake)
    time.sleep(2)
    sense.clear()