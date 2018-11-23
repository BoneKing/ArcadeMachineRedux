import RPi.GPIO as GPIO  
from time import sleep     # this lets us have a time delay (see line 15)  
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  
try:  
    while True:            # this will carry on until you hit CTRL+C  
        if GPIO.input(4): # if port 25 == 1  
            print "pin 4"  
            GPIO.output(24, 1)         # set port/pin value to 1/HIGH/True
        if GPIO.input(17):
            print"pin 17"
        if GPIO.input(27):
            print "pin 27"
            
        else:  
            print "else"  
        sleep(0.1)         # wait 0.1 seconds  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself 
