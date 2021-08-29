import RPi.GPIO as GPIO
import time,sys

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
PIN_LEDA  = 4
PIN_LEDB  = 3
GPIO.setup(PIN_LEDA,  GPIO.OUT)
GPIO.setup(PIN_LEDB,  GPIO.OUT)

PIN_BUTTONA  = 7
GPIO.setup(PIN_BUTTONA,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
PIN_BUTTONB  = 8
GPIO.setup(PIN_BUTTONB,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try: 
    while True:
        if GPIO.input(PIN_BUTTONA) == GPIO.HIGH:
            GPIO.output(PIN_LEDA, 1)
        else:
            GPIO.output(PIN_LEDA, 0)
        if GPIO.input(PIN_BUTTONB) == GPIO.HIGH:
            GPIO.output(PIN_LEDB, 1)
        else:
            GPIO.output(PIN_LEDB, 0)            
            
except KeyboardInterrupt:
    print('interrupted!')
    GPIO.cleanup()
sys.exit()    
  
