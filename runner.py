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

blink001.blink_color(pixels, blink_times = 1, color=(0, 155, 0))
#blink001.led_clock(pixels, color=(0, 155, 0))

index = 6
#try:
while True:
        black_button_state = GPIO.input(23)
        red_button_state = GPIO.input(24)
        if black_button_state == False and red_button_state == False:
                blink001.blink_color(pixels, blink_times = 5, color=(255, 0, 0))
        elif black_button_state == False:
                if index < 7:
                        index = index + 1
                else:
                        index = 1
                blink001.stop_threads = False
                if index == 1:
                        t = threading.Thread(target=blink001.appear_from_back, args=(pixels,))
                        t.start()
                elif index == 2:
                        t = threading.Thread(target=blink001.rainbow_cycle_successive, args=(pixels,))
                        t.start()
                elif index == 3:
                        t = threading.Thread(target=blink001.rainbow_cycle, args=(pixels,))
                        t.start()
                elif index == 4:
                        t = threading.Thread(target=blink001.rainbow_colors, args=(pixels,))
                        t.start()
                        t = threading.Thread(target=blink001.brightness_decrease, args=(pixels,))
                        t.start()
                elif index == 5:
                        t = threading.Thread(target=blink001.bump_colors, args=(pixels,))
                        t.start()
                elif index == 6:
                        t = threading.Thread(target=blink001.led_clock, args=(pixels,))
                        t.start()
                elif index == 7:
                        t = threading.Thread(target=blink001.random_blink, args=(pixels,))
                        t.start()

                print 'Black Button Pressed, starting programm #' + str(index)
                time.sleep(0.2)
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
