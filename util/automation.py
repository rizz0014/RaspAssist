from time import sleep
import schedule
import sys
from util import animation
from util import sensor
from util import senseDisplay as display

from sense_hat import SenseHat
sense = SenseHat()


def mascot():
    schedule.every(3).minutes.do(animation.snake)
    schedule.every().hour.do(animation.snakeNotify)
    schedule.every(60).seconds.do(sensor.readings)
    schedule.every(5).minutes.do(display.update_screen)

def showData():
    display.update_screen


def lunchTime():
    schedule.every().day.at('11:30').do(animation.kirby)
    schedule.every().day.at('12:30').do(animation.kirby)
    schedule.every().day.at('12:30').do(animation.snakeQuestion)
    schedule.every().day.at('13:30').do(animation.kirby)
    schedule.every().day.at('13:30').do(animation.snakeQuestion)


def nightTime():
    schedule.every().day.at('20:00').do(animation.pikachu)
    schedule.every().day.at('21:00').do(animation.pikachu)
    schedule.every().day.at('22:00').do(animation.pikachu)
    schedule.every().day.at('23:00').do(animation.pikachu)
    schedule.every().day.at('23:00').do(animation.snakeNotify)
    schedule.every().day.at('00:00').do(animation.snakeNotify)


def goodbye():
    '''To quit program before Office power supply routine goes off'''
    # schedule.every().day.at('00:50').do(sys.exit(0))


# automation exec

mascot()
lunchTime()
nightTime()
sense.stick.direction_any = showData

while True:
    schedule.run_pending()
    sleep(1)
