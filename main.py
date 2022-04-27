from machine import Pin
import time
led = Pin(25, Pin.OUT)
led.value(1)

STEP_DELAY = 20 # ms

IN1 = Pin(11, Pin.OUT)
IN2 = Pin(12, Pin.OUT)
IN3 = Pin(13, Pin.OUT)
IN4 = Pin(14, Pin.OUT)

while True:
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)
    time.sleep_ms(STEP_DELAY)
    IN1.value(0)
    IN2.value(1)
    IN3.value(0)
    IN4.value(0)
    time.sleep_ms(STEP_DELAY)
    IN1.value(0)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)
    time.sleep_ms(STEP_DELAY)
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(1)
    time.sleep_ms(STEP_DELAY)
    
