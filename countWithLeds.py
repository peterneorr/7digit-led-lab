import RPi.GPIO as GPIO
import time,sys

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
PIN_DATA  = 17
PIN_LATCH = 27
PIN_CLOCK = 22
GPIO.setup(PIN_DATA,  GPIO.OUT)
GPIO.setup(PIN_LATCH, GPIO.OUT)
GPIO.setup(PIN_CLOCK, GPIO.OUT)

def shiftout(byte):
  GPIO.output(PIN_LATCH, 0)
  for x in range(8):
    GPIO.output(PIN_DATA, (byte >> x) & 1)
    GPIO.output(PIN_CLOCK, 1)
    GPIO.output(PIN_CLOCK, 0)
  GPIO.output(PIN_LATCH, 1)

shiftout(255)
time.sleep(.5)
#sys.exit("done")
while True:
  for x in range(256):
    shiftout(x)
    print(x)
    time.sleep(1)
  
