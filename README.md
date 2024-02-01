# photofinish
Raspberry pico prototype to show message in a photofinish picture

Setup the pico to run MicroPython

Update textexport.py with the message text, size and colours required. This will generate a message.py module to load up to the pico (using Thonny or similar)

Update matrix_main.py with the physical details such as the pin number, time delay, and number of LEDs. This should be saved to the pico as "main.py". This imports the message module which defines the message and then streams it, column by column to the LEDs.

Once you have videoed the finish use photofinish.py to process this into a photofinish jpeg. Adjust the size and offset of the video slices to make use the capture the message LEDs.
