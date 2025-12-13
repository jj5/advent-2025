from machine import Pin
onboardLED = Pin(25, Pin.OUT)
onboardLED.value(1)
print("The LED is on, baby!")

