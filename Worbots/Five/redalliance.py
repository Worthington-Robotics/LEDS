from machine import Pin
import neopixel
import time

np = neopixel.NeoPixel(Pin(28), 156)

def main(rest):
    for i in range(156):
        np.fill((255, 0, 0))
        np[i] = (255, 255, 255)
        np.write()
        time.sleep(rest)

while True:
    main(0.01)            

            
       
    