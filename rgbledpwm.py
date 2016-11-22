import RPi.GPIO as GPIO
import time
import random

pinmap = {
    'r':16
    ,'g':20
    ,'b':21
    }

pinlist = [16,20,21]

GPIO.setmode(GPIO.BCM)

def initpins():
    for pin in pinlist:
        GPIO.setup(pin, GPIO.OUT)

def pinOn(pin):
    GPIO.output(pin, GPIO.HIGH)

def pinOff(pin):
    GPIO.output(pin, GPIO.LOW)

def onoff(pin, sec):
    pinOff(pin)
    pinOn(pin)
    time.sleep(sec)
    pinOff(pin)

def blinkpins(times, interval):
    for t in range(times):
        for pin in pinlist:
            pinOn(pin)
        time.sleep(interval)

        for pin in pinlist:
            pinOff(pin)
        time.sleep(interval)

try:
    initpins()
    pwmlist = []
    for pin in pinlist:
        pwmlist.append(GPIO.PWM(pin, 50))
        
    for pwm in pwmlist:
        pwm.start(0)

    dc = 0
    step = -5

    while True:
        if dc <= 0 or dc >= 100:
            step = -step
            print 'flipping'

        for pwm in pwmlist:
            rdc = random.randint(0,100)
            pwm.ChangeDutyCycle(rdc)
        time.sleep(.2)
        dc += step
        
    print 'success!'


finally:
    GPIO.cleanup()
