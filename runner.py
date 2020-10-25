import RPi.GPIO as GPIO
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI
import time
import subprocess
import blink001

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO23
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO24

# Configure the count of pixels:
PIXEL_COUNT = 219
 
# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

#try:
while True:
        black_button_state = GPIO.input(23)
        red_button_state = GPIO.input(24)
        if black_button_state == False:
                print('Black Button Pressed...')
                blink001.rainbow_cycle_successive(pixels, wait=0.1)
                time.sleep(0.2)
        elif red_button_state == False:
                print('Red Button Pressed...')
                blink001.pixels.clear()
                blink001.pixels.show() 
                time.sleep(0.2)
        else:
                time.sleep(0.2)
#except:
#        GPIO.cleanup()
