import RPi.GPIO as GPIO

class RaspGPIO:
    def __init__(self, pin,window, spring = None):
        self.GPIOpin = pin
        self.window = window
        self.spring = spring
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIOpin,GPIO.IN,pull_up_down = GPIO.PUD_UP)
        self.isRunning = False
        self.StopInterruption
    
        
    def cleanup(self):
        print('Interruption erased')
        GPIO.remove_event_detect(self.GPIOpin)
    
        
    def AddSpringEvent(self):
        GPIO.add_event_detect(self.GPIOpin,GPIO.FALLING,callback = self.SpringInterruption, bouncetime = 200)
        self.StartInterruption()
    
    def AddCounterEvent(self):
        GPIO.add_event_detect(self.GPIOpin,GPIO.FALLING,callback = self.CounterInterruption, bouncetime = 200)
        self.StartInterruption()
        
        
    def SpringInterruption(self, channel):
        
        if(self.window.testMode.GetTestMode() == 0):
            print("Interruption" + str(self.GPIOpin))
            self.window.BreakSpring(self.spring)
            
        elif(self.window.testMode.GetTestMode() == 1):
            print("Interruption" + str(self.GPIOpin))
            self.window.BreakSpring(self.spring)
            self.window.StopButton()
        
        
    def CounterInterruption(self,channel):
        if self.isRunning: 
            self.window.change_text()
            print("pulso")
    
    def StartInterruption(self):
        self.isRunning = True
        
    def StopInterruption(self):
        self.isRunning = False
        self.cleanup()
        
    def GetInterruptionStatus(self):
        return self.isRunning
        