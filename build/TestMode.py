
class TestMode:
    
    def __init__(self):
        # 0 - Until Failure
        # 1 - First To Fail
        self.testMode = None
    
    def GetTestMode(self):
        return self.testMode
    
    def SetTestMode(self,mode):
        self.testMode = mode