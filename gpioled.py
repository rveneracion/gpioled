import RPi.GPIO as GPIO
import time

pinlist = [26]
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
            onoff(pin, interval)
            time.sleep(interval)

times = input("Enter the number of times you want the light to blink: ")
interval = float(raw_input("Enter the blink interval in seconds: "))


try:
    initpins()
    blinkpins(times, interval)
finally:
    GPIO.cleanup()
