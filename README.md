# CircuitPython
This repository will actually serve as an aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [Distance Sensor](#Distance_Sensor)
* [NextAssignment2](#NextAssignment2)
* [NextAssignment3](#NextAssignment3)
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


## CircuitPython_LCD

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
Code goes here

```

### Evidence

### Wiring

### Reflection
The wiring of this assignment was not at all hard because it remained the same from last year.




## NextAssignment2

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection





## NextAssignment3

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
