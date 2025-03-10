from machine import Pin
import time
import neopixel
striplen = 96

np = neopixel.NeoPixel(Pin(28), striplen)



def main(rest):
    for i in range(striplen):
        for j in range(striplen):
            difference = j - i
            if difference < -(2 * striplen // 3):
                np[j] = (255, 0, 0) 
            elif difference < -(striplen // 3):
                np[j] = (0, 0, 255)
            elif difference < 0:
                np[j] = (255, 255, 255)
            elif difference < striplen // 3:
                np[j] = (255, 0, 0)
            elif difference < 2 * striplen // 3:
                np[j] = (0, 0, 255)
            else:
                np[j] = (255, 255, 255)
        np.write()
        time.sleep(rest)
        
while True:
    main(0.00001)


                 


