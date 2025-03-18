from machine import Pin
import time
import neopixel

striplen = 75
np = neopixel.NeoPixel(Pin(28), striplen)

for i in range(striplen):
    np[i] = (255, 255, 255)
    np.write()