import time
import sys
import RPi.GPIO as GPIO

# On/off from remote
on = '102020111112011111210112021021020'
off = '102020111112011111210112021111020'
# working on/off signals
#on = '102020111112011111210112021021020'
#on = '102020111112011111210112021021021'
#on = '102020111112011111210112021021022'
#off = '102020111112011111210112021111020'
#off = '102020111112011111210112021111021'
#off = '102020111112011111210112021111022'


init_delay = 0.002676
pulse_delay = 0.000265
word_separator = 0.001295
repeate_delay = 0.010255

NUM_ATTEMPTS = 5
TRANSMIT_PIN = 23

def transmit_code(code):
    print("Transmitting");
    print(code);
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
    for t in range(NUM_ATTEMPTS):
        GPIO.output(TRANSMIT_PIN, 1)
        time.sleep(pulse_delay)
        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(init_delay)
        for i in code:
            if i == '0':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(pulse_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(word_separator)
            elif i == '1':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(pulse_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(pulse_delay)
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(pulse_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(word_separator)
            elif i == '2':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(pulse_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(pulse_delay)
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(pulse_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(pulse_delay)
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(pulse_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(word_separator)
            else:
                continue
        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(repeate_delay)
    GPIO.cleanup()

if __name__ == '__main__':
    for argument in sys.argv[1:]:
        exec('transmit_code(' + str(argument) + ')')

