import time
import board
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull

pwn = pwmio.PWMOut(board.D5, duty_cycle=0, frequency=50)

buttonRED = DigitalInOut(board.A4)
buttonRED.direction = Direction.INPUT
buttonRED.pull = Pull.DOWN

buttonBLUE = DigitalInOut(board.A5)
buttonBLUE.direction = Direction.INPUT
buttonBLUE.pull = Pull.DOWN