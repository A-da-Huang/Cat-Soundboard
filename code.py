# SPDX-FileCopyrightText: 2021 Sandy Macdonald
#
# SPDX-License-Identifier: MIT

# A simple example of how to set up a keymap and HID keyboard on Keybow 2040.

# You'll need to connect Keybow 2040 to a computer, as you would with a regular
# USB keyboard.

# Drop the keybow2040.py file into your `lib` folder on your `CIRCUITPY` drive.

# NOTE! Requires the adafruit_hid CircuitPython library also!

import board
from keybow2040 import Keybow2040

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Set up Keybow
i2c = board.I2C()
keybow = Keybow2040(i2c)
keys = keybow.keys

# Set up the keyboard and layout
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

#####TEST BLOCK######2222222222
#25e9pppp6a6adefji37bf048c37bfeeadi12
#37bfe1fadj2ic8840
#
#

mode = "piano"

# A map of keycodes that will be mapped sequentially to each of the keys, 0-15
keymap =    [Keycode.ZERO,
             Keycode.ONE,
             Keycode.E,
             Keycode.THREE,
             Keycode.FOUR,
             Keycode.F,
             Keycode.A,
             Keycode.SEVEN,
             Keycode.EIGHT,
             Keycode.J,
             Keycode.D,
             Keycode.B,
             Keycode.C,
             Keycode.TWO,
             Keycode.I,
             Keycode.F]

# The colour to set the keys when pressed, yellow 
rgb = (150, 0, 200)

# Attach handler functions to all of the keys
for i, key in enumerate(keys):
    # A press handler that sends the keycode and turns on the LED
    @keybow.on_press(key)
    def press_handler(key):
        keycode = keymap[key.number]
        keyboard.press(keycode)
        #key.set_led(*rgb)

    # A release handler that turns off the LED
    @keybow.on_release(key)
    def release_handler(key):
        keycode = keymap[key.number]
        keyboard.release(keycode)
        #key.led_off()


switch_key = keys[0]

red = (255, 0, 0)
green = (0, 255, 0)
purple = (255, 0, 100)
white = (255, 255, 255)

def press_func():
    return

def piano_lights():
    for i, key in enumerate(keys):
        if i in [6, 10]:
            key.set_led(*green)
        else:
            key.set_led(*purple)
            #key.led_off()

def drum_lights():
    for i, key in enumerate(keys):
        if i in [2, 5, 9, 14]:
            key.set_led(*green)
        else:
            key.set_led(*purple)
            #key.led_off()

piano_lights()
updated = False

while True:
    # Always remember to call keybow.update()!
    if switch_key.get_state() and switch_key.last_state != None and switch_key.last_state != switch_key.get_state():
        if mode == "piano":
            drum_lights()
            mode = "drums"
        else:
            piano_lights()
            mode = "piano"
        
    keybow.update()
