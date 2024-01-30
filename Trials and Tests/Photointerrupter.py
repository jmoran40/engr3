# Library Imports
import time
import digitalio
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# Setting Up Photointerrupter and LCD and also TIME ITSELF (but actually just monotonic)
photointerrupter = digitalio.DigitalInOut(board.D5)
photointerrupter.direction = digitalio.Direction.INPUT
photointerrupter.pull = digitalio.Pull.UP
photointerrupter_state = None
interrupt_counter = 0
lcd = LCD(I2CPCF8574Interface(board.I2C(), 0X27), num_rows = 2, num_cols = 16)
now = time.monotonic()

while True:
    # Making the Photointerrupter do its thing
    if photointerrupter.value and photointerrupter_state is None:
        photointerrupter_state = "interrupted"
    if photointerrupter_state == "interrupted":
        print("interrupted")
        interrupt_counter = interrupt_counter+1
        photointerrupter_state = "Still Blocked"
    if not photointerrupter.value and photointerrupter_state == "Still Blocked":
        photointerrupter_state = None
    if not photointerrupter.value and photointerrupter_state is None:
        print("All Clear")

    # Making the LCD do its thing
    lcd.set_cursor_pos(0,0)
    lcd.print("Interrupts: ")
    # 4-Second LCD Update
    if (now + 4) < time.monotonic():
        lcd.set_cursor_pos(1,0)
        lcd.print(str(interrupt_counter))
        now = time.monotonic()