import RPi.GPIO as GPIO
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI
import time
import threading
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

index = 0

#try:
while True:
        black_button_state = GPIO.input(23)
        red_button_state = GPIO.input(24)
        if black_button_state == False:
                print('Black Button Pressed...')
                if index < 2:
                        index = index + 1
                else:
                        index = 0
                blink001.stop_threads = False
                if index == 1:
                        t = threading.Thread(target=blink001.appear_from_back, args=(pixels,))
                        t.start()
                elif index == 2:
                        t = threading.Thread(target=rainbow_cycle_successive, args=(pixels,))
                        t.start()
                time.sleep(0.2)
                print('Black Button Pressed...End')
        elif red_button_state == False:
                print('Red Button Pressed...')
                blink001.stop_threads = True
                blink001.pixels.clear()
                blink001.pixels.show() 
                time.sleep(0.2)
        else:
                time.sleep(0.2)
#except:
#        GPIO.cleanup()
