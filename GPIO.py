import RPi.GPIO as GPIO

class RaspGPIO:
    def __init__(self, pin):
        self.GPIOpin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIOpin,GPIO.IN,pull_up_down = GPIO.PUD_UP)
        GPIO.add_event_detect(self.GPIOpin,GPIO.FALLING,callback = self.SpringInterruption, bouncetime = 200)
        
    def cleanup(self):
        GPIO.cleanup()
    
    def SpringInterruption(self):
        print("Interruption" + str(self.GPIOpin))