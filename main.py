from sense_hat import SenseHat
import time

# from util import pixelArt
from util import animation

sense = SenseHat()
sense.low_light = True

# starting point of the code


def main():
    print("Testing the code structure")
    animation.pikachu()
    animation.snake()


if __name__ == "__main__":
    main()