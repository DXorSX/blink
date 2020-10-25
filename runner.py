import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO23
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO24
# GPIO.setup(24, GPIO.OUT)  #LED to GPIO24

try:
        while True:
                black_button_state = GPIO.input(23)
                red_button_state = GPIO.input(24)
                if black_button_state == False:
                        print('Black Button Pressed...')
                        time.sleep(0.2)
                elif red_button_state == False:
                        print('Red Button Pressed...')
                        time.sleep(0.2)
                else:
                        time.sleep(0.2)
except:
        GPIO.cleanup()
