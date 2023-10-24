import time
import board
from analogio import AnalogIn
import pwmio

pwn = pwmio.PWMOut(board.D3)
potentiometer = AnalogIn(board.A0)

while True:
    print((potentiometer.value))
    time.sleep(0.1)
    pwn.duty_cycle = potentiometer.value
    time.sleep(0.1)