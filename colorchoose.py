import RPi.GPIO as GPIO

pinmap = {
    'r':16
    ,'g':20
    ,'b':21
    }

GPIO.setmode(GPIO.BCM)

def initpins():
    for pin in pinmap.keys():
        GPIO.setup(pinmap[pin], GPIO.OUT)

try:
    maxdc = 100.0 
    hz = 100
    initpins()
    pwmdict = {}
    for pin in pinmap.keys():
        pwmdict[pin] = GPIO.PWM(pinmap[pin], hz)
        
    #set the initial state for each led
    state = {
        'r':0
        ,'g':0
        ,'b':0
    }

    #start the leds at the state
    for pwm in pwmdict.keys():
        pwmdict[pwm].start(state[pwm])
    while True:
        rgb = raw_input("Enter RGB values (0-255) separated by spaces: ")
        rgb = [int(x) for x in rgb.strip().split()]
        for num,val in enumerate(rgb):
            if val > 255: rgb[num] = 255
            if val < 0: rgb[num] = 0

        rgb = [(x/255.0 * 10) for x in rgb]

        r,g,b = rgb
        print "The following will be applied: {} {} {}".format(r,g,b)

        pwmdict['r'].ChangeDutyCycle(r)
        pwmdict['g'].ChangeDutyCycle(g)
        pwmdict['b'].ChangeDutyCycle(b)
        

finally:
    GPIO.cleanup()
