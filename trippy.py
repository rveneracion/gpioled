import RPi.GPIO as GPIO
import time
import random

pinmap = {
    'r':16
    ,'g':20
    ,'b':21
    }


def initpins():
    GPIO.setmode(GPIO.BCM)
    for pin in pinmap.keys():
        GPIO.setup(pinmap[pin], GPIO.OUT)

tripstop = False
tripping = False

def trip():
    global tripstop
    global tripping
    try:
        tripping = True
        maxdc = 50.0
        mhz = 100
        initpins()
        pwmdict = {}
        for pin in pinmap.keys():
            pwmdict[pin] = GPIO.PWM(pinmap[pin], mhz)
            
        #set the initial state for each led
        state = {
            'r':random.randint(0,maxdc)
            ,'g':random.randint(0,maxdc)
            ,'b':random.randint(0,maxdc)
        }

        #start the leds at the state
        for pwm in pwmdict.keys():
            pwmdict[pwm].start(state[pwm])


        step = .2 

        while not tripstop:
            #select a random led to start modifying
            current = random.choice(['r','g','b'])

            runs = random.randint(100,250)

            for r in range(runs):
                if tripstop: break

                if state[current] <= (abs(step)):
                    state[current] = abs(step) 
                    step = -step
                elif state[current] > (maxdc - abs(step)):
                    state[current] = maxdc - abs(step)
                    step = -step

                state[current] += step

                for pwm in pwmdict.keys():
                    pwmdict[pwm].ChangeDutyCycle(state[pwm])

                time.sleep(.01)

    finally:
        GPIO.cleanup(tuple(pinmap.values()))
        print 'exited cleanly'
        tripping = False

if __name__ == '__main__':
    try:
        trip()
    finally:
        GPIO.cleanup()
