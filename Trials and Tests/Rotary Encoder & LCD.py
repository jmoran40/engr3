# This code is for importing libraries
import rotaryio
import board
import neopixel
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# This code is for setting up the Encoder, LCD, and Neopixel
enc = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor=2)
lcd = LCD(I2CPCF8574Interface(board.I2C(), 0X3F), num_rows = 2, num_colms = 16)
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3
led[0] = (255, 0, 0)