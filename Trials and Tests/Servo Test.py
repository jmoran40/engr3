"""CircuitPython Essentials Servo standard servo example"""
import pulseio
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin D5.
pwm = pwmio.PWMOut(board.D5, duty_cycle=0, frequency=50)

# Create a servo object, my_servo.
servo = servo.Servo(pwm)
angle = 90
angle2 = 180
while True:
        servo.angle = angle
        time.sleep(0.5)
        servo.angle = angle2
        time.sleep(0.5)