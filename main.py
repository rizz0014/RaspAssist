from time import sleep
import schedule
from util import animation
from util import sensor
from sense_hat import SenseHat
sense = SenseHat()
sense.low_light = True

# starting point of the code


def main():
    print("Testing the code structure")

    # Schedule Time
    schedule.every(5).minutes.do(animation.snake)
    schedule.every().hour.do(animation.snakeNotify)
    schedule.every(30).seconds.do(sensor.readings)

    # Lunch time
    schedule.every().day.at('11:30').do(animation.kirby)
    schedule.every().day.at('12:30').do(animation.kirby)
    schedule.every().day.at('12:30').do(animation.snakeQuestion)
    schedule.every().day.at('13:30').do(animation.kirby)
    schedule.every().day.at('13:30').do(animation.snakeQuestion)

    # Night time
    schedule.every().day.at('20:00').do(animation.pikachu)
    schedule.every().day.at('21:00').do(animation.pikachu)
    schedule.every().day.at('22:00').do(animation.pikachu)
    schedule.every().day.at('23:00').do(animation.pikachu)
    schedule.every().day.at('23:00').do(animation.snakeNotify)
    schedule.every().day.at('00:00').do(animation.snakeNotify)

    # animation.snakeConfused()

    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == "__main__":
    main()
