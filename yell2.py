import time
import sys
import gpiod

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

NUM_ATTEMPTS = 1
TRANSMIT_PIN = 23

HIGH = []
HIGH.append(1)
LOW = []
LOW.append(0)

def transmit_code(code):
    print("Transmitting");
    print(code);
    with gpiod.Chip("gpiochip0") as chip:
        pin = []
        pin.append(TRANSMIT_PIN)
        lines = chip.get_lines(pin)
        lines.request(consumer="gpiochip0", type=gpiod.LINE_REQ_DIR_OUT)

        for t in range(NUM_ATTEMPTS):
            lines.set_values(HIGH)
            time.sleep(pulse_delay)
            lines.set_values(LOW)
            time.sleep(init_delay)
            for i in code:
                if i == '0':
                    lines.set_values(HIGH)
                    time.sleep(pulse_delay)
                    lines.set_values(LOW)
                    time.sleep(word_separator)
                elif i == '1':
                    lines.set_values(HIGH)
                    time.sleep(pulse_delay)
                    lines.set_values(LOW)
                    time.sleep(pulse_delay)
                    lines.set_values(HIGH)
                    time.sleep(pulse_delay)
                    lines.set_values(LOW)
                    time.sleep(word_separator)
                elif i == '2':
                    lines.set_values(HIGH)
                    time.sleep(pulse_delay)
                    lines.set_values(LOW)
                    time.sleep(pulse_delay)
                    lines.set_values(HIGH)
                    time.sleep(pulse_delay)
                    lines.set_values(LOW)
                    time.sleep(pulse_delay)
                    lines.set_values(HIGH)
                    time.sleep(pulse_delay)
                    lines.set_values(LOW)
                    time.sleep(word_separator)
                else:
                    continue
            lines.set_values(LOW)
            time.sleep(repeate_delay)

if __name__ == '__main__':
    for argument in sys.argv[1:]:
        exec('transmit_code(' + str(argument) + ')')

