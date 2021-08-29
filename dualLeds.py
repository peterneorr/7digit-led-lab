import RPi.GPIO as GPIO
import time,sys

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
PIN_LEDA  = 4
PIN_LEDB  = 3
GPIO.setup(PIN_LEDA,  GPIO.OUT)
GPIO.setup(PIN_LEDB,  GPIO.OUT)

try: 
    while True:
        GPIO.output(PIN_LEDA, 1)
        GPIO.output(PIN_LEDB, 0)
        time.sleep(.2)
        GPIO.output(PIN_LEDA, 0)
        GPIO.output(PIN_LEDB, 1)
        time.sleep(.2)
except KeyboardInterrupt:
    print('interrupted!')
    GPIO.cleanup()
sys.exit()    
  
