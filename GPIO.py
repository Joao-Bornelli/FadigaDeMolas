import RPi.GPIO as GPIO

class RaspGPIO:
    def __init__(self, pin,window, spring = None):
        self.GPIOpin = pin
        self.window = window
        self.spring = spring
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIOpin,GPIO.IN,pull_up_down = GPIO.PUD_UP)
        self.isRunning = False
        
    
        
    def cleanup(self):
        GPIO.cleanup()
    
        
    def AddSpringEvent(self):
        GPIO.add_event_detect(self.GPIOpin,GPIO.FALLING,callback = self.SpringInterruption, bouncetime = 200)
    
    def AddCounterEvent(self):
        GPIO.add_event_detect(self.GPIOpin,GPIO.FALLING,callback = self.CounterInterruption, bouncetime = 200)
  
    def SpringInterruption(self, channel):
        print("Interruption" + str(self.GPIOpin))
        self.window.BreakSpring(self.spring)
        
    def CounterInterruption(self,channel):
        self.window.change_text()
        print("pulso")
    
    
    
    def StartInterruption(self):
        self.isRunning = True
        
    def StopInterruption(self):
        self.isRunning = False