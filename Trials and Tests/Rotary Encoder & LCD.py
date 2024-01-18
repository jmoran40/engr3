# This code is for importing libraries
import rotaryio
import board
import neopixel
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# This code is for setting up the Encoder, LCD, and Neopixel
enc = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor=2)
#lcd = LCD(I2CPCF8574Interface(board.I2C(), 0X3F), num_rows = 2, num_colms = 16)
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3
led[0] = (255, 0, 0)
button = digitalio.DigitalInOut(board.D2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_state = None

# Menu/List Setup
menu = ["stop", "caution", "go" ]
last_index = None
menu_index = 0

while True:
    # This code registers when the button is pressed
    if not button.value and button_state is None:
        button_state = "pressed"
    if button.value and button_state == "pressed":
        print("Button Is Pressed")
        button_state = None
    # Code for the Coder to Code the Encoder
    menu_index = enc.position
    if last_index is None or menu_index != last_index:
        print(menu_index)
    last_index = menu_index