from machine import Pin
import time
import neopixel

striplen = 138
np = neopixel.NeoPixel(Pin(28), striplen)
button_pin = Pin(18, Pin.IN, Pin.PULL_UP)

def main(rest):
    while True:
        for i in range(striplen):
            np.fill((0, 0, 255))
            np[(i - 1)] = (255, 255, 255)
            np[i] = (255, 255, 255)
            np[i - 2] = (255, 255, 255)
            np.write()
            time.sleep(rest)
            if button_pin.value == 0:
                break


def button_pressed():
    time.sleep(1)
    main(0.01)

while True:
    np.fill((0, 0, 0))
    np.write()
    if button_pin.value() == 0: # Check if the button is pressed
        button_pressed() # Execute the code if the button is pressed
        while button_pin.value() == 0:
            time.sleep(0.1) # Debounce the button press
    time.sleep(0.1) # Small delay to prevent excessive checking