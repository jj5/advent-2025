# Imports
from machine import Pin
import time

# Set up our button names and GPIO pin numbers
# Also set pins as inputs and use pull downs
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up our LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

while True:
    time.sleep(0.5)
    if button1.value() == 1:
        print("Button 1 pressed")
        red.toggle() # Toggle Red LED on/off
    if button2.value() == 1:
        print("Button 2 pressed")
        amber.toggle()
    if button3.value() == 1:
        print("Button 3 pressed")
        green.toggle()
