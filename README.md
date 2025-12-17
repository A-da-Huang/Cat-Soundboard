# 🎵 Cat-Soundboard
Cat Soundboard is an interactive, keyboard controlled soundboard built with p5.js that combines sound effects with simple animations. Each key press plays a sound and controls the cat to move it's arm.

## Overview
This was created by me during my Creative Coding class as a final project. One of the requirements for this final was to be able to incorporate anything outside of just keyboard and mouse. For this project I decided to go with a macro pad from [pimoroni](https://shop.pimoroni.com/products/keybow-2040?variant=39328275300435) which uses CircuitPython. 

## Usage
1. Connect the macropad to your computer via USB  
2. Open the Cat Soundboard in your browser using a local server
3. Select which instrument you want to play
4. Piano controls are A and D
5. Drum controls are E, F, I and J
6. Press the keys on the macropad or keyboard to trigger cat sound effects
7. Each key press also animates the cat’s arm on screen  

## Installation
Need the [macropad](https://shop.pimoroni.com/products/keybow-2040?variant=39328275300435)

Install CircuitPython, which should automatically install once you build and plug the macro pad into your computer. If not then here is the link to [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/)

The Cat Soundboard is a browser-based p5.js project and must be run using a local web server for audio and assets to load correctly.
1. Open the project folder in Visual Studio Code
2. Install the Live Server extension
3. Right click index.html
4. Select "Open with Live Server"
This project will open in your browser.







