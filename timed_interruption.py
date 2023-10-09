import threading


class InterruptionGenerator:
    def __init__(self, interval, window) -> None:
        self.interval = interval
        self.timer = None
        self.is_running = False
        self.interruptionNumber = 0
        self.window = window

    
    def interrupt(self):
        print("Interruption!")
        if self.is_running:  # Check if it's still running before rescheduling
            self.timer = threading.Timer(self.interval, self.interrupt)
            self.timer.start()
            self.interruptionNumber+=1
            self.window.change_text(str(self.interruptionNumber))

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.timer = threading.Timer(self.interval, self.interrupt)
            self.timer.start()

    def stop(self):
        if self.is_running:
            self.timer.cancel()
            self.is_running = False
    
    def resetCounter(self):
        self.interruptionNumber = 0