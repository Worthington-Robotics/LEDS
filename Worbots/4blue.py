from machine import Pin
import time
import neopixel

striplen = 138
np = neopixel.NeoPixel(Pin(28), striplen)

def main(rest):
    for i in range(striplen):
        np.fill((0, 0, 255))
        np[(i - 1)] = (255, 255, 255)
        np[i] = (255, 255, 255)
        np[i - 2] = (255, 255, 255)
        np.write()
        time.sleep(rest)

while True:
    main(0.01)