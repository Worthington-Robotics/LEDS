from machine import Pin
import time, neopixel

# Setup
striplen = 138
np = neopixel.NeoPixel(Pin(28), striplen)
button_pin = Pin(18, Pin.IN, Pin.PULL_UP)


MODES = [(0, 0, 0), (255, 0, 0), (0, 0, 255)] #off,red,blue
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
    else:
        np.fill(bg)
        for offset in [0, -1, -2]:
            np[(i + offset) % striplen] = (255, 255, 255)
        np.write()
        
        i = (i + 1) % striplen
        time.sleep(0.01)