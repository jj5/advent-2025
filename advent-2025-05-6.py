# Imports
from machine import Pin, PWM
import time

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode

# Create our library of tone variables for "Jingle Bells"
A = 440
As = 466
B = 494
C = 523
Cs = 554
D = 587
Ds = 622
E = 659
F = 698
Fs = 740
G = 784
Gs = 830

# Create volume variable (Duty cycle)
volume = 32768

# Create our function with arguments
def playtone(note,vol,delay1,delay2):
    buzzer.duty_u16(vol)
    buzzer.freq(note)
    time.sleep(delay1)
    buzzer.duty_u16(0)
    time.sleep(delay2)

playtone(Fs,volume,0.1,0.2)
playtone(E,volume,0.1,0.2)
playtone(Fs,volume,0.1,0.2)
playtone(E,volume,0.1,0.2)
playtone(Fs,volume,0.1,0.2)
playtone(E,volume,0.1,0.2)
playtone(Fs,volume,0.1,0.2)
playtone(E,volume,0.1,0.2)
playtone(Fs,volume,0.1,0.2)


# Duty to 0 to turn the buzzer off
buzzer.duty_u16(0)
