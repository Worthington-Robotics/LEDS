from machine import Pin
import time, neopixel

# Setup
striplen = 138
np = neopixel.NeoPixel(Pin(28), striplen)
button_pin = Pin(18, Pin.IN, Pin.PULL_UP)


MODES = [(0, 0, 0), (255, 0, 0), (0, 0, 255), "chase"] #off,red,blue
state = 0
i = 0
last_press = 0

def toggle(pin):
    global state, i, last_press
    if (time.ticks_ms() - last_press) > 500:
        state = (state + 1) % len(MODES)
        i = 0
        last_press = time.ticks_ms()

button_pin.irq(trigger=Pin.IRQ_FALLING, handler=toggle)

while True:
    bg = MODES[state]
    if state == 0:
        np.fill(bg)
        np.write()
        time.sleep(0.1) 
    elif state in [1,2]:
        np.fill(bg)
        for offset in [0, -1, -2]:
            np[(i + offset) % striplen] = (255, 255, 255)
        np.write()
        
        i = (i + 1) % striplen
        time.sleep(0.01)

    elif state == 3:  #Chase mode 
        for j in range(striplen):
            if (j + i) % 3 == 0:
                np[j] = (255, 0, 0)  # Red
            elif (j + i) % 3 == 1:
                np[j] = (255, 255, 255)  # White
            else:
                np[j] = (0, 0, 255)  # Blue
        np.write()
        i = (i + 1) % striplen
        time.sleep(0.05)  

#TODO figure out why micropython wont run on this project 