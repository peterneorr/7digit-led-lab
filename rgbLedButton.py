import RPi.GPIO as GPIO
import time,sys

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
PIN_BLUE = 11
PIN_GREEN = 9
PIN_RED = 10

PIN_LEDA  = 4
PIN_LEDB  = 3
PIN_LEDC  = 2
GPIO.setup(PIN_LEDA,  GPIO.OUT)
GPIO.setup(PIN_LEDB,  GPIO.OUT)
GPIO.setup(PIN_LEDC,  GPIO.OUT)
GPIO.setup(PIN_RED,  GPIO.OUT)
GPIO.setup(PIN_GREEN,  GPIO.OUT)
GPIO.setup(PIN_BLUE,  GPIO.OUT)


PIN_BUTTONA  = 7
GPIO.setup(PIN_BUTTONA,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
PIN_BUTTONB  = 8
GPIO.setup(PIN_BUTTONB,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try: 
    while True:
        if GPIO.input(PIN_BUTTONA) == GPIO.HIGH and  GPIO.input(PIN_BUTTONB) == GPIO.HIGH:
            GPIO.output(PIN_RED, 1)
            GPIO.output(PIN_GREEN, 0)
            GPIO.output(PIN_BLUE, 0)

        elif GPIO.input(PIN_BUTTONA) == GPIO.HIGH:
            GPIO.output(PIN_LEDA, 1)
            GPIO.output(PIN_LEDB, 0)
            GPIO.output(PIN_LEDC, 0)
            time.sleep(.1)
            GPIO.output(PIN_LEDA, 0)
            GPIO.output(PIN_LEDB, 1)
            GPIO.output(PIN_LEDC, 0)
            time.sleep(.1)                       
            GPIO.output(PIN_LEDA, 0)
            GPIO.output(PIN_LEDB, 0)
            GPIO.output(PIN_LEDC, 1)
            time.sleep(.1)                       
        elif GPIO.input(PIN_BUTTONB) == GPIO.HIGH:
            GPIO.output(PIN_RED, 1)
            GPIO.output(PIN_GREEN, 1)
            GPIO.output(PIN_BLUE, 0)
            GPIO.output(PIN_LEDA, 0)
            GPIO.output(PIN_LEDB, 0)        
        else:
            GPIO.output(PIN_RED, 0)
            GPIO.output(PIN_GREEN, 1)
            GPIO.output(PIN_BLUE, 0)
            GPIO.output(PIN_LEDA, 0)
            GPIO.output(PIN_LEDB, 0)

            
except KeyboardInterrupt:
    print('interrupted!')
    GPIO.cleanup()
sys.exit()    
  
