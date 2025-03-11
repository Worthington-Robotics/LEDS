from machine import Pin
import time
import neopixel

striplen = 156
np = neopixel.NeoPixel(Pin(28), striplen)

def main(rest):
    np.fill((255, 0, 0))
    np.write()
    while True:
        for i in range(striplen):
            np[i] = (0, 0, 255)
            np.write()
            time.sleep(rest)
        
        for i in range(striplen):
            np[i] = (255, 255, 255)
            np.write()
            time.sleep(rest)

        for i in range(striplen):
            np[i] = (255, 0, 0)
            np.write()
            time.sleep(rest)

main(0.000000001)
        
