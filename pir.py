
import RPi.GPIO as GPIO
import time, threading
import trippy

countLimit = 30
noOneThereCount = 0

pinmap = {
        'PIR':19
    }

def initpins():
    GPIO.setmode(GPIO.BCM)
    for pin in pinmap.keys():
        GPIO.setup(pinmap[pin], GPIO.IN)

def detected(pin):
    global noOneThereCount, countLimit
    noOneThereCount = countLimit
    print 'DETECTED at time:', time.time()
    print '\ttrippy.tripstop =', trippy.tripstop
    print '\tnoOneThereCount =', noOneThereCount
    print '******************************'
    if trippy.tripstop:
        trippy.tripstop = False
        t = threading.Thread(target=trippy.trip)
        t.start()

def lightMinder():
    global noOneThereCount
    func = GPIO.gpio_function(19)
    print 'lightMinder says:'
    print '\tnoOneThereCount =', noOneThereCount
    print '\ttrippy.tripstop:', trippy.tripstop
    print '\ttrippy.trippping:', trippy.tripping
    print '\tpin 19 function:', func
    print '*****************************'
    if noOneThereCount > 0:
        noOneThereCount -= 1
    else:
        trippy.tripstop = True

def run():
    try:
        print 'starting...'
        initpins()
        while True:
            lightMinder()
            GPIO.remove_event_detect(19)
            GPIO.add_event_detect(19, GPIO.RISING, callback=detected)
            time.sleep(1)
    finally:
        GPIO.cleanup()
        print 'PIR.py did GPIO cleanup'

if __name__ == '__main__':
    run()
