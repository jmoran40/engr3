import board
import digitalio
from time import sleep
buttonRED = digitalio.DigitalInOut(board.A4)
buttonBLUE = digitalio.DigitalInOut(board.A5)

while True:
    print(buttonRED.value)
    print(buttonBLUE.value)
    sleep(0.1)