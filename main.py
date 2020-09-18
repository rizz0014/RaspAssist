from time import sleep
import schedule
import sys
from util import animation
from util import sensor
from util import automation
from util import config
from sense_hat import SenseHat

sense = SenseHat()
sense.low_light = True

# starting point of the code


def main():
    print("Snaky, the Raspberry Assistant.")

    for i in range(5):
        animation.snake()
        sense.show_message("Hi! I'm Snaky, your friend!", text_colour=(0, 160, 77), scroll_speed=0.1)

    sense.clear()


if __name__ == "__main__":
    main()
