from machine import Pin
import neopixel
import time

np = neopixel.NeoPixel(Pin(28), 137)

while True:
    for i in range(137):
        for j in range(137):
            difference = j -i
            if difference > -45 and difference < 0:
                np[j] = (0, 0, 225)

            if difference > -90 and difference <-46:
                np[j] = (255, 255, 255)

            if difference > -91 and difference <-137:
                np[j] = (0, 0, 255)

            if difference < 45 and difference >= 0:
                np[j] = (255, 0, 0) 
            
            elif difference < 91 and difference > 46:
                np[j] = (255, 255, 255)

            elif difference > 92:  
                np[j] = (0, 0, 255)

            
        np.write()
    