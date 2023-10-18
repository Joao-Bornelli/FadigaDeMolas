class TextBox:
    
    def __init__(self, Xposition, Yposition, canvas) -> None:
        self.Xposition = Xposition
        self.Yposition = Yposition
        self.canvas = canvas
        self.cycleNumber = 0
        self.isBroken = False
        
        #Create the background rectangle for the number of cycles text
        self.CreateBackgroundRectangle()
        
        #Create the number of cycles text
        self.textBox = self.canvas.create_text(
            Xposition, #143.0,
            Yposition, #61.0,
            anchor="center",
            text="1",
            fill="#000000",
            font=("Inter Bold", 14)
        )
        
        
    def SetBackgroungColor(self, status):
        if status: self.canvas.itemconfig(self.bgRectangle, fill = "#f55151")
        # self.CreateBackgroundRectangle("#f55151")
        else: self.canvas.itemconfig(self.bgRectangle, fill = "#D9D9D9")
        
    def SetCycles(self, number):
        self.cycleNumber = number
        
    
    def GetCycles(self):
        return self.cycleNumber   
    
    def SetBrokenStatus(self, status):
        self.SetBackgroungColor(status)
        self.isBroken = status
        print(self.GetBrokenStatus())
    
    def GetBrokenStatus(self):
        return self.isBroken
    
    
    def CreateBackgroundRectangle(self,color = "#D9D9D9"):
        self.bgRectangle = self.canvas.create_rectangle(
            self.Xposition - 90,
            self.Yposition - 20,
            self.Xposition + 90,
            self.Yposition + 20,
            fill = color,
            outline=""
        )