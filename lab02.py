import RPi.GPIO as GPIO

import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#Set up GPIO Outputs (LEDs)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

#Set up GPIO Inputs (Switches)

GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.IN)
GPIO.setup(25,GPIO.IN)


try:
    while True:
        #your code here 
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.output(4,0)
    GPIO.output(17,0)
    GPIO.output(27,0)
    GPIO.cleanup()
finally:
    GPIO.output(4,0)
    GPIO.output(17,0)
    GPIO.output(27,0)
    GPIO.cleanup()





