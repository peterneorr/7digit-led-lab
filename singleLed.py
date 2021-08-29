import RPi.GPIO as GPIO
import time,sys

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
PIN_LED  = 4
GPIO.setup(PIN_LED,  GPIO.OUT)

try: 
    while True:
        GPIO.output(PIN_LED, 1)
        time.sleep(.2)
        GPIO.output(PIN_LED, 0)
        time.sleep(.2)
except KeyboardInterrupt:
    print('interrupted!')
    GPIO.cleanup()
sys.exit()    
  
