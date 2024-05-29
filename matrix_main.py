# Save a main.py in the pico
# Generate and save message.py in the pico so that it can be imported

import array, time
from machine import Pin
import rp2
from message import message_data

# Configure the number of WS2812 LEDs.
NUM_LEDS = 32
PIN_NUM = 22 # Data pin connected to the LEDs
brightness = 0.2 # Global brightness control. Numbers between 0 - 0.5 will produce a visible difference. Numbers between 0.5 - 1.0 will consume more power but with little visible effect.

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()


# Create the StateMachine with the ws2812 program, outputting on pin
sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))

# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)

##########################################################################
def pixels_show(col):
    dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
    for i in range(NUM_LEDS):
        c = message_data[col][NUM_LEDS-1-i] # Assumes the LEDs are vertical with the pico connected at the bottom so the rows are reversed
        r = int(((c >> 16) & 0xFF) * brightness)
        g = int(((c >> 8) & 0xFF) * brightness)
        b = int((c & 0xFF) * brightness)
        dimmer_ar[i] = (g<<16) + (r<<8) + b
    sm.put(dimmer_ar, 8)
    time.sleep_ms(18) # Approximately 60fps. Refresh rate can be limited by the WS2812 protocol for large numbers of LEDs or extremely high rates. You can find help online to drive several LED strips in parallel if needed.

print("Starting...")
while True:
    for c in range(len(message_data)-1,-1,-1):       
        pixels_show(c) # Scans the message in reverse assuming the resulting photo finish will be filled from right to left33