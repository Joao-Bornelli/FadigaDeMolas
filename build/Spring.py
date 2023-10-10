class Spring:
    
    def __init__(self, Xposition, Yposition, canvas) -> None:
        self.Xposition = Xposition
        self.Yposition = Yposition
        self.canvas = canvas
        self.cycleNumber = 0
        
        
        self.textBox = self.canvas.create_text(
            Xposition, #143.0,
            Yposition, #61.0,
            anchor="center",
            text="1",
            fill="#000000",
            font=("Inter Bold", 14 * -1)
        )
    
    def SetCycles(self, number):
        self.cycleNumber = number
        
    
    def GetCycles(self):
        return self.cycleNumber   
    
    
    