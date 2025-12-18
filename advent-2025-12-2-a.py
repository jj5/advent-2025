# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)
        
# Select the first pixel (pixel 0)
# Set the RGB colour (red)
strip[0] = (255,0,0)
strip[1] = (255,0,0)
strip[2] = (255,0,0)
strip[3] = (255,0,0)
strip[4] = (255,0,0)
strip[5] = (255,0,0)
strip[6] = (255,0,0)
strip[7] = (255,0,0)
strip[8] = (255,0,0)
strip[9] = (255,0,0)
strip[10] = (255,0,0)
strip[11] = (255,0,0)
strip[12] = (255,0,0)
strip[13] = (255,0,0)
strip[14] = (255,0,0)

# Send the data to the strip
strip.write()