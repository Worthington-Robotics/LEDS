from machine import Pin
import time
import neopixel

striplen = 138
np = neopixel.NeoPixel(Pin(28), striplen)

np.fill()