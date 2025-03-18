from machine import Pin
import time
import neopixel

outerRing = 96
innerRing = 42
np = neopixel.NeoPixel(Pin(28), outerRing)


def main(rest):
    for i in range(2, outerRing + innerRing + 2):
        np.fill((255, 0, 0))
        np[(i - 1)] = (255, 255, 255)
        np[i] = (255, 255, 255)
        np[i - 2] = (255, 255, 255)
    np.write()
    time.sleep(rest)
    if bp.value() == 0:
        np.fill((0, 0, 0))

def button_pressed():
    while True:
        main(0.01)
    
bp = Pin(18, Pin.IN, Pin.PULL_UP)
while True:
    if bp.value() == 0: # Check if the button is pressed
         # Execute the code if the button is pressed
        while bp.value() == 0:
            time.sleep(0.1) # Debounce the button press
    time.sleep(0.1) # Small delay to prevent excessive checking
    button_pressed()