# Imports
from machine import Pin, PWM
import time, sys

# Set up LED pins
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# Set up the Break Beam pin
beam = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13))

# Set buzzer PWM frequency to 1000
buzzer.freq(1000)

# Start with the buzzer volume off (duty 0)
buzzer.duty_u16(0)

# Create game variables
starttime = 0
timecheck = 0
scorecounter = 0
state = 0
targetscore = 60
timelimit = 10

print("Game starts after the beep!")

#Long beep to signal game start
buzzer.duty_u16(10000)
time.sleep(2)
buzzer.duty_u16(0)

print("GO!")
print("-------------------------------")

# Store our start time (seconds)
starttime = time.time()

def set_led(red_val,amber_val,green_val):
    
    red.value(red_val)
    amber.value(amber_val)
    green.value(green_val)

def alarm():
    
    buzzer.duty_u16(10000)
    time.sleep(0.2)
    buzzer.duty_u16(0)

while True: # Run this block until code stopped

    time.sleep(0.0001) # Very short delay

    # Take the current time and minus the original start time
    # This gives us the number of seconds since we started the game
    timecheck = time.time() - starttime

    if timecheck >= timelimit: # If 30 or more seconds have passed
                
        # LEDs off
        set(0,0,0)
        
        # Beep to signal game end
        alarm()
        
        # Print the target and player's score
        print("-------------------------------")
        print("GAME OVER! YOU LOSE :(")
        print("The target was",targetscore,", you scored",scorecounter)
        print("-------------------------------")
        
        # Exit the program
        sys.exit()
        
    elif scorecounter >= targetscore: # If player's score has hit the target
        
        # LEDs off
        set_led(0,0,0)
        
        # Beep to signal game end
        alarm()
        
        # Print time taken to win
        print("-------------------------------")
        print("YOU WIN!")
        print("You took",timecheck,"seconds!")
        print("-------------------------------")
        
        # Exit the program
        sys.exit()
   
    elif state == 0 and beam.value() == 0: # If state is 0 AND our pin is LOW
        
         scorecounter = scorecounter + 1 # Add +1 to our score counter
        
         state = 1 # Change state to 1
        
         print("SCORE =",scorecounter,"/",targetscore) # Print the score and target
         print("Time remaining:", (30 - timecheck)) # take our timecheck variable away from 30 - gives the remaining time
         
         if scorecounter < (targetscore / 100 * 60): # If our score is less than 33% of the target

            set_led(1,0,0)
            
         elif (targetscore/ 100 * 60) < scorecounter < (targetscore / 100 * 90): # If our score is between 33% and 66% of the target

            set_led(1,1,0)
            
         elif scorecounter > (targetscore / 100 * 90): # If our score is over 66% of the target

            set_led(1,1,1)
        
    elif state == 1 and beam.value() == 1: # If state is 1 AND our pin is HIGH
                        
        state = 0 # Change the state to 0
