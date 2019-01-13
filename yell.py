import time
import sys
import RPi.GPIO as GPIO

on = 'I102020111112011111210112021021020'
off = 'I102020111112011111210112021111020'

init_delay = 0.002676
on_delay = 0.000265
short_off_delay = 0.00027 # this might be same os on_delay
long_off_delay = 0.001295
repeate_delay = 0.010255

NUM_ATTEMPTS = 10
TRANSMIT_PIN = 23

def transmit_code(code):
    print("Transmitting");
    print(code);
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
    for t in range(NUM_ATTEMPTS):
        for i in code:
            if i == 'I':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(on_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(init_delay)
            elif i == '0':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(on_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(long_off_delay)
            elif i == '1':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(on_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(short_off_delay)
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(on_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(long_off_delay)
            elif i == '2':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(on_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(short_off_delay)
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(on_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(short_off_delay)
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(on_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(long_off_delay)
            else:
                continue
        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(repeate_delay)
    GPIO.cleanup()

if __name__ == '__main__':
    for argument in sys.argv[1:]:
        exec('transmit_code(' + str(argument) + ')')

