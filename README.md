# photofinish
Raspberry pico prototype to show message in a photofinish picture

Setup the pico to run MicroPython. Shortcut is to use the Thonny Python IDE which is built to work with picos

Install pygame and numpy libraries (use the packages menu if using Thonny)

## Text based messages
Update textexport.py with the message text, colours and LED count required. This will generate a message.py module to load up to the pico (using Thonny or similar)

## Images based messages
As for text but update imageexport.py with the image files and LED count required.

Update matrix_main.py with the physical details such as the pin number, time delay, and LED count. This should be saved to the pico as "main.py". This imports the message module which defines the message and then streams it, column by column to the LEDs.

Once you have videoed the finish use photofinish.py to process this into a photofinish jpeg. Adjust the size and offset of the video slices to capture the message LEDs.
