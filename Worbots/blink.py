from machine import Pin
from utime import sleep
import neopixel
import time


np = neopixel.NeoPixel(Pin(28), 136)

# Number of LEDs for each color
color_block_size = 48

def multi_chase(delay_time=0.02):
    for i in range(136):
        # Set blocks of LEDs with different colors
        for j in range(color_block_size):
            if i + j < 136:
                np[i + j] = (255, 0, 0)   # Red block
                np[(i + j + color_block_size) % 136] (255, 255, 255)   # white block
                np[(i + j + 2 * color_block_size) % 136] (0, 0, 225)   # Blue block

        np.write()
        time.sleep(delay_time)

       
    time.sleep(0.0)

while True:
    multi_chase()  # Multi-color chase with blocks of colors