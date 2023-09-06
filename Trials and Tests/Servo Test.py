"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin D5.
pwm = pwmio.PWMOut(board.D5, duty_cycle=0, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
        my_servo.angle = 90
        time.sleep(0.5)
        my_servo.angle = 150
        time.sleep(0.5)