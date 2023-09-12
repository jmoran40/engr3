import time
import board
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull

pwn = pwmio.PWMOut(board.D3, duty_cycle=2**15, frequency=50)

buttonRED = DigitalInOut(board.A4)
buttonRED.direction = Direction.INPUT
buttonRED.pull = Pull.DOWN

buttonBLUE = DigitalInOut(board.A5)
buttonBLUE.direction = Direction.INPUT
buttonBLUE.pull = Pull.DOWN

servo = servo.Servo(pwn)
Rotation = 90


while True:
    if buttonRED.value:
        Rotation = Rotation + 10
        if Rotation > 180:
            Rotation = 180
        print(Rotation)
        servo.angle = Rotation
        time.sleep(0.1)
    
    if buttonBLUE.value:
        Rotation = Rotation - 10
        if Rotation < 0:
            Rotation = 0
        print(Rotation)
        servo.angle = Rotation
        time.sleep(0.1)