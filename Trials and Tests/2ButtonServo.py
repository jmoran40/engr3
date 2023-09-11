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

servo = servo.Servo(pwn)
Rotation = 90

while True:
    if buttonRED:
        Rotation = Rotation + 1
        if Rotation > 180:
            Rotation = 180
        print(Rotation)
        time.sleep(0.1)
    
    if buttonBLUE:
        Rotation = Rotation - 1
        if Rotation < 0:
            Rotation = 0
        print(Rotation)
        time.sleep(0.1)