# CircuitPython
This repository will actually serve as an aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_MotorControl](#CircuitPython_MotorControl)
* [Distance Sensor](#Distance_Sensor)
* [Onshape_Hanger](#Onshape_Hanger)
* [Onshape_Swing_Arm](#Onshape_Swing_Arm)
* [BlankAssignment](#BlankAssignment)
* [NextAssignment](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
Description goes here

Here's how you make code look like code:

```python
Code goes here

```


### Evidence


![spinningMetro_Optimized](https://user-images.githubusercontent.com/54641488/192549584-18285130-2e3b-4631-8005-0792c2942f73.gif)


And here is how you should give image credit to someone if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
Make an account with your Google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on the knowledge that will make this assignment better or easier for the next person.




## CircuitPython_Servo

### Description & Code
In this assignment I was tasked with controlling a 180 micro servo using two buttons.

```python
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
```
### Wiring

![Screenshot (2)](https://github.com/jmoran40/engr3/assets/143545030/aefc10dc-8f32-460f-9e4a-cdde9f1cb324)

### Reflection
First assignment of the year and it I feel like ive been thrown into the deep end of a pool. The good news was though I was quite lost at the start, by the end I had learned the essentials of working with CircuitPython. This not only applies in the literal sense of getting to understand the code language itself, but understanding the tools that are used to convey that language. Even now as a write this I'm learning how to utilize the connection between Visual Studio Code and Github. As for the assignment itself, the hardware was familar albeit shinier and the software took some time to understand but wasn't too overwealming.





## CircuitPython_MotorControl

### Description & Code

```python
Code goes here

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection





## Distance_Sensor

### Description & Code
In this assignment I was tasked with making an RGB LED display different colors based on the input of an Ultrasonic Sensor

```python
import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

NUMPIXELS = 1  # Update this to match the number of LEDs.
SPEED = 0.1  # Increase to slow down the rainbow. Decrease to speed it up.
BRIGHTNESS = 0.2  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
PIN = board.NEOPIXEL  # This is the default pin on the 5x5 NeoPixel Grid BFF.

pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

while True:
    try:
        print((sonar.distance))
        time.sleep(0.1)
        if (sonar.distance < 5):
            pixels.fill(RED)
            pixels.show()
            time.sleep(0.1)
        elif (5 < sonar.distance < 20):
            x = simpleio.map_range((sonar.distance),5,20,0,255)
            pixels.fill((255-x, 0, x))
            pixels.show()
            time.sleep(0.1)
        elif (sonar.distance == 20):
            pixels.fill(BLUE)
            pixels.show()
            time.sleep(0.1)
        elif (20 < sonar.distance < 35):
            x = simpleio.map_range((sonar.distance),20,35,0,255)
            pixels.fill((0, x, 255-x))
            pixels.show()
            time.sleep(0.1)
        elif (sonar.distance > 35):
            pixels.fill(GREEN)
            pixels.show()
            time.sleep(0.1)
    except RuntimeError:
        print("Retrying!")
```

### Evidence

![ezgif com-optimize](https://github.com/jmoran40/engr3/assets/143545030/0c332e21-a4b4-4b45-a37e-31cb87afc3c8)

### Wiring

![Screenshot (7)](https://github.com/jmoran40/engr3/assets/143545030/d578fd33-adc2-4b64-af84-52fbcaad6644)

### Reflection
The wiring of this assignment was not at all hard because it remained the same from last year. The coding was not so easy. In perticular it was the level of specification required for the RGB to work that caused the most issues. On the bright side (heh), this assignent has reawakened my engineering paranioa so little mistakes will hopefully be easier to spot in the future and the visual spectacle that came upon the completion of the assignment was dopamine inducing to say the least.





## Onshape_Hanger

### Assignment Description
In this assignment I was tasked with creating an Onshape model of a hanger using a provided drawing with measurements.

### Evidence

![Screenshot (8)](https://github.com/jmoran40/engr3/assets/143545030/6c0a0c7c-2276-45ed-927c-c57e23e14b3d)

### Part Link

[The Hanger](https://cvilleschools.onshape.com/documents/89cfbffc3234559d2e2b49d1/w/b9303e32817641222ffe2adb/e/7074864c13d3b3d2b6e61565?renderMode=0&uiState=651c614f733921666e1a872d).

### Reflection
This assignment was a nice little reminder of the mechanics of Onshape. Designing models from images and measurements always was a fun little puzzle to me. It also helps with reawakening the problem solving part of the brain that sometimes goes a but dormant over the summer.





## Onshape_Swing_Arm

### Assignment Description
In this assignment I was tasked with creating an Onshape model of a Swing Arm using a provided drawing with measurements.

### Evidence

![Screenshot (9)](https://github.com/jmoran40/engr3/assets/143545030/ffad2178-407a-44fd-9b50-eaf0bb8c9589)

### Part Link

[Swing Arm](https://cvilleschools.onshape.com/documents/e0feadfada2a269be91a2203/w/f2f8b52f8ca190583ea5da17/e/d6c098494ba086dd19f6edd9?renderMode=0&uiState=6525a743fcf0840f7c14adcd).

### Reflection
This one took me a couple days to sort out. The biggest thing I took away from this assignment is that when dimensioning objects, perspective is an important matter. it seemed that half the time I made something a certain distance or angle, it would be wrong because it turned out I deminsioned the object to the wrong dot or at the wrong angle with the correct position being slightly to the left.




## BlankAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
