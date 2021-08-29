import RPi.GPIO as GPIO
import time,sys

#GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
digits = [
    0x3f,
    0x06,
    0x5b,
    0x4f,
    0x66,
    0x6d,
    0x7d,
    0x07,
    0x7f,
    0x6f,
    0x77,
    0x7c,
    0x39,
    0x5e,
    0x79,
    0x71 ]

#wait this long after digit led updates
delay =.005
DECIMAL = 0x80

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

def shift_out(byte):  
  GPIO.output(PIN_LATCH, 0)
  for x in range(8):
    GPIO.output(PIN_DATA, (byte >> x) & 1)
    GPIO.output(PIN_CLOCK, 1)
    GPIO.output(PIN_CLOCK, 0)
  GPIO.output(PIN_LATCH, 1)

def select_digit(pos):
    if pos == 1:
        GPIO.output(PIN_D1, 0)
        GPIO.output(PIN_D2, 1)
        GPIO.output(PIN_D3, 1)
        GPIO.output(PIN_D4, 1)
    elif pos == 2:
        GPIO.output(PIN_D1, 1)
        GPIO.output(PIN_D2, 0)
        GPIO.output(PIN_D3, 1)
        GPIO.output(PIN_D4, 1)
    elif pos == 3:
        GPIO.output(PIN_D1, 1)
        GPIO.output(PIN_D2, 1)
        GPIO.output(PIN_D3, 0)
        GPIO.output(PIN_D4, 1)
    elif pos == 4:
        GPIO.output(PIN_D1, 1)
        GPIO.output(PIN_D2, 1)
        GPIO.output(PIN_D3, 1)
        GPIO.output(PIN_D4, 0)
    else: 
        return

def clear_digit(pos):
    select_digit(pos)
    shift_out(0)
 
def write_byte(pos,byte):
    select_digit(pos)
    shift_out(byte)
    time.sleep(delay)
    shift_out(0)

def write_digit(pos,n):
    if n < 0 or n > 15:
        return    
    select_digit(pos)
    shift_out(digits[n])
    time.sleep(delay)
    shift_out(0)

def show_time(t):
    hr = t.tm_hour    
    if hr>12:
        hr = hr - 12        
    d1 = hr / 10
    d2 = hr % 10        
    d3 = t.tm_min / 10
    d4 = t.tm_min % 10    
    if d1==0:
        clear_digit(1)
    else:
        write_digit(1,d1)            
    write_byte(2, digits[d2] ^ DECIMAL)
    write_digit(3,d3)
    write_digit(4,d4)       

try:
    while True:        
        t = time.localtime()
        show_time(t)                       
        
except KeyboardInterrupt:
    print('interrupted!')
    GPIO.cleanup()
sys.exit()