from machine import Pin
import neopixel
import time

np = neopixel.NeoPixel(Pin(28), 156)

while True:
    for i in range(156):
        for j in range(156):
           difference = j -i 
           if difference < 1 and difference >= 0:
                np[j] = (225, 225, 225)
            
           elif difference < 156 and difference > 1:
                np[j] = (0, 0, 255)           

           elif difference > -1 and difference < 0:
               np[j] = (0, 0, 255)

           elif difference > -156 and difference < -1:
               np[j] = (0, 0, 255)

    


            

            
        np.write()
    