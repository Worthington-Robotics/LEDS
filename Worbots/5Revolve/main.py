from machine import Pin
import time
import neopixel

striplen = 157
np = neopixel.NeoPixel(Pin(28), striplen)
button_pin = Pin(18, Pin.IN, Pin.PULL_UP)

blue = 0
red = 255
i = 0
firstPress = False
start = time.time()

def irq_handler(pin):
    global firstPress, blue, red, i, start
    if (time.time() - start > 0.5):
        start = time.time()
        if not firstPress:
            firstPress = True
        else:
            blue = abs(255 - blue)
            red = abs(255 - red)
            i = 0
            # print(f"Pressed, {blue} {red}")

button_pin.irq(trigger=button_pin.IRQ_FALLING, handler=irq_handler)

def main(rest):
    global i
    while True:
        while i < striplen:
            np.fill((red, 0, blue))
            np[(i - 1)] = (255, 255, 255)
            np[i] = (255, 255, 255)
            np[i - 2] = (255, 255, 255)
            np.write()
            time.sleep(rest)
            i += 1
        i = 0

np.fill((0, 0, 0))
np.write()
while True:
    if firstPress:
        break
main(0.01)