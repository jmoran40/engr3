import time
import board
import adafruit_hcsr04

sonar = adafruit_hcsr04(trigger_pin=board.D4, echo_pin=board.D5)