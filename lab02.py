import RPi.GPIO as GPIO

import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#Set up GPIO Outputs (LEDs)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

#Set up GPIO Inputs (Switches)

GPIO.setup(16,GPIO.IN)
GPIO.setup(20,GPIO.IN)
GPIO.setup(21,GPIO.IN)


try:
    while True:
        print 'Switch 1: '+ str(GPIO.input(16))+' Switch 2: '+ str(GPIO.input(20))+' Switch 3: '+ str(GPIO.input(21))
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










    
##try:
##    while True:
##        #your code here:
##        if GPIO.input(16)==1:
##            GPIO.output(4,0)
##        else:
##            GPIO.output(4,1)
##        if GPIO.input(20)==1:
##            GPIO.output(17,1)
##        else:
##            GPIO.output(17,0)
##        if GPIO.input(21)==1:
##            GPIO.output(27,0)
##        else:
##            GPIO.output(27,1)
##        time.sleep(0.1)
##except KeyboardInterrupt:
##    GPIO.output(4,0)
##    GPIO.output(17,0)
##    GPIO.output(27,0)
##    GPIO.cleanup()
##finally:
##    GPIO.output(4,0)
##    GPIO.output(17,0)
##    GPIO.output(27,0)
##    GPIO.cleanup()

