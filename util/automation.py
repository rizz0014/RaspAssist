from time import sleep
import schedule
import sys
from util import animation
from util import sensor
from util import senseDisplay as display

from sense_hat import SenseHat
sense = SenseHat()

sense.clear()

def mascot():
    schedule.every(3).minutes.do(animation.snake)
    schedule.every().hour.do(animation.snakeNotify)
    schedule.every(60).seconds.do(sensor.readings)
    schedule.every(5).minutes.do(display.update_screen)
    schedule.every(15).minutes.do(animation.taco)

def showData(event):
    if event.action == 'pressed':
        display.update_screen

def lunchTime():
    schedule.every().day.at('11:30').do(animation.kirby)
    schedule.every().day.at('12:30').do(animation.kirby)
    schedule.every().day.at('12:30').do(animation.snakeQuestion)
    schedule.every().day.at('13:30').do(animation.kirby)
    schedule.every().day.at('13:30').do(animation.snakeQuestion)


def nightTime():
    schedule.every().day.at('15:55').do(animation.taco)
    schedule.every().day.at('16:00').do(animation.taco)
    schedule.every().day.at('16:05').do(animation.taco)
    schedule.every().day.at('16:10').do(animation.taco)
    schedule.every().day.at('16:15').do(animation.taco)
    schedule.every().day.at('16:20').do(animation.taco)
    schedule.every().day.at('20:00').do(animation.pikachu)
    schedule.every().day.at('21:00').do(animation.pikachu)
    schedule.every().day.at('22:00').do(animation.pikachu)
    schedule.every().day.at('23:00').do(animation.pikachu)
    schedule.every().day.at('23:00').do(animation.snakeNotify)
    schedule.every().day.at('00:00').do(animation.snakeNotify)


def goodbye():
    '''NOT IN USE - To quit program before Office power supply routine goes off'''
    # schedule.every().day.at('00:50').do(sys.exit(0))


# automation exec

mascot()
lunchTime()
nightTime()
# showData()

sense.stick.direction_any = showData

while True:
    schedule.run_pending()
    sleep(1)
    pass # This keeps the program running to receive joystick events