# Import the GPIO and time libraries
import RPi.GPIO as GPIO
import time

# Set the pin designation type.
# In this case, we use BCM- the GPIO number- rather than the pin number itself.
GPIO.setmode (GPIO.BCM)

# So that you don't need to manage non-descriptive numbers,
# set "LIGHT" to 4 so that our code can easily reference the correct pin.
LIGHT = 4

# Because GPIO pins can act as either digital inputs or outputs,
# we need to designate which way we want to use a given pin.
# This allows us to use functions in the GPIO library in order to properly send and receive signals.
GPIO.setup(LIGHT,GPIO.OUT)


# Cause the light to blink 7 times and print a message each time.
# To blink the light, we call GPIO.output and pass as parameters the pin number (LIGHT) and the state we want.
# True sets the pin to HIGH (sending a signal), False sets it to LOW.
# To achieve a blink, we set the pin to High, wait for a fraction of a second, then set it to Low.
# Adding keyboard interrupt with try and except so that program terminates when user presses Ctrl+C.
try:
    while True:
        GPIO.output(LIGHT,True)
        time.sleep(0.5)
        GPIO.output(LIGHT,False)
        time.sleep(0.5)
        print("blink")
except KeyboardInterrupt:
    GPIO.cleanup()
