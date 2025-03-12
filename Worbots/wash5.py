from machine import Pin
import time
import neopixel

bness = 255

striplen = 156
np = neopixel.NeoPixel(Pin(28), striplen)

def main(rest):
    np.fill((bness, 0, 0))
    np.write()
    while True:
        for i in range(striplen):
            np[i] = (0, 0, bness)
            np.write()
            time.sleep(rest)
        
        for i in range(striplen):
            np[i] = (bness, bness, bness)
            np.write()
            time.sleep(rest)

        for i in range(striplen):
            np[i] = (bness, 0, 0)
            np.write()
            time.sleep(rest)

main(0.005)
        
