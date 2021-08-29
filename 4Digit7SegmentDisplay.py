import RPi.GPIO as GPIO
import time,sys

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
PIN_DATA  = 17
PIN_LATCH = 27
PIN_CLOCK = 22
PIN_D1 = 25
PIN_D2 = 24
PIN_D3 = 23
PIN_D4 = 18
GPIO.setup(PIN_D1,  GPIO.OUT)
GPIO.setup(PIN_D2,  GPIO.OUT)
GPIO.setup(PIN_D3,  GPIO.OUT)
GPIO.setup(PIN_D4,  GPIO.OUT)
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

GPIO.output(PIN_D1, 0)
GPIO.output(PIN_D2, 0)
GPIO.output(PIN_D3, 0)
GPIO.output(PIN_D4, 0)
decimal = 0x80
shiftout(decimal)
time.sleep(3)
#sys.exit("done")
while True:
  for x in range(256):
    shiftout(x)
    print(x)
    time.sleep(1)
  
