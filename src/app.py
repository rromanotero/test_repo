from flask import Flask, jsonify
import os
import sys
import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
# Import the SSD1306 module.
import adafruit_ssd1306
# Import the RFM69 radio module.
import adafruit_rfm69

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# 128x32 OLED Display
reset_pin = DigitalInOut(board.D4)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, reset=reset_pin)
# Clear the display.
display.fill(0)
display.show()
width = display.width
height = display.height

# RFM69 Configuration
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Attempt to set up the RFM69 Module
try:
    rfm69 = adafruit_rfm69.RFM69(spi, CS, RESET, 915.0)
    display.text('RFM69: Detected', 0, 0, 1)
except RuntimeError as error:
    # Thrown on version mismatch
    display.text('RFM69: ERROR', 0, 0, 1)
    print('RFM69 Error: ', error)

app = Flask(__name__)

@app.route("/")
def health_check():
    print("Hey there, this is STDOUT")
    print("Hey there, this is STDERR", file=sys.stderr)

    display.fill(0) # Draw a black filled box to clear the image.
    display.text('Server Up', width-85, height-7, 1)
    display.show()

    return jsonify({
        "server_status" : 'OKKKAAAAAYYY'
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
