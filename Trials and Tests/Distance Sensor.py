import time
import board
import adafruit_hcsr04
import neopixel

NUMPIXELS = 1  # Update this to match the number of LEDs.
SPEED = 0.1  # Increase to slow down the rainbow. Decrease to speed it up.
BRIGHTNESS = 0.2  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
PIN = board.NEOPIXEL  # This is the default pin on the 5x5 NeoPixel Grid BFF.

pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

while True:
    try:
        print((sonar.distance))
        time.sleep(0.1)
        if (sonar.distance < 5):
            pixels.fill(RED)
            pixels.show()
            time.sleep(0.1)
        elif (sonar.distance > 35):
            pixels.fill(GREEN)
            pixels.show()
            time.sleep(0.1)
        else:
            pixels.fill(BLUE)
            pixels.show()
            time.sleep(0.1)
    except RuntimeError:
        print("Retrying!")