from machine import Pin
import time, neopixel

striplen = 138
np = neopixel.NeoPixel(Pin(28), striplen)
button_pin = Pin(18, Pin.IN, Pin.PULL_UP)


MODES = [(0, 0, 0), (255, 0, 0), (0, 0, 255), "chase"] #off,red,blue,chase
state = 0
i = 0
last_press = 0

def toggle(pin):
    global state, i, last_press
    if (time.ticks_ms() - last_press) > 500: # debounce for 500ms
        state = (state + 1) % len(MODES) # cycle through modes
        i = 0
        last_press = time.ticks_ms() 

button_pin.irq(trigger=Pin.IRQ_FALLING, handler=toggle) # Set up an interrupt on the button pin to call toggle() when pressed

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

    elif state == 3:  # Chase mode 

        OUTER_COUNT = 96
        INNER_COUNT = 42

        outer_start = 0
        inner_start = 96  

        third = OUTER_COUNT // 3   # 32 LEDs per color

        # Animate OUTER ring 
        for j in range(OUTER_COUNT):

            position = (j + i) % OUTER_COUNT

            if position < third:
                color = (255, 0, 0)          # Red
            elif position < 2 * third:
                color = (255, 255, 255)      # White
            else:
                color = (0, 0, 255)          # Blue

            np[outer_start + j] = color

        # distribute inner LEDs around outer loop
        for k in range(INNER_COUNT):

            
            reversed_k = INNER_COUNT - 1 - k #inner loop was reversed for some reason


            # Matching the Outerloop with Innerloop    (OUTER_COUNT//INNER_COUNT) = 96/42 = 2.2857
            matchingFactor = (reversed_k * OUTER_COUNT) // INNER_COUNT

            np[inner_start + k] = np[outer_start + matchingFactor]

           


        np.write()

        i = (i + 1) % OUTER_COUNT
        time.sleep(0.01)


#TODO figure out why micropython wont run on this project 
