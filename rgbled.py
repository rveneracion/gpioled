import RPi.GPIO as GPIO
import time

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

times = input("Enter the number of times to blink: ")
interval = float(raw_input("Enter the blink interval in seconds: "))

try:
    initpins()
    blinkpins(times, interval)

    for pin in pinlist:
        pinOff(pin)

finally:
    GPIO.cleanup()
