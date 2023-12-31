
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

import sys




from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
# from timed_interruption import InterruptionGenerator
from build.TestMode import TestMode
from build.TextBox import TextBox
from build.GPIO import RaspGPIO


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/fadiga/Documents/FadigaDeMolas/build/assets/frame0")
print(ASSETS_PATH)
# if sys.platform.startswith('linux'):
#     ASSETS_PATH = OUTPUT_PATH / Path(r"\home\fadiga\Documents\FadigaDeMolas\build\assets\frame0")
# elif sys.platform == 'win32':
#     ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\joaobo\Documents\FadigaDeMolas\build\assets\frame0")
# else:
#     print("The app is running on an unknown or unsupported OS.")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MainWindow:

    
    def __init__(self, root):

        self.root = root
        
        # Set the size of the screen to 800x480 (Size of the 7" touch display)
        # Configure the background color to white
        self.root.geometry("800x480")
        self.root.configure(bg = "#FFFFFF")
        
        


        self.canvas = Canvas(
            self.root,
            bg = "#FFFFFF",
            height = 480,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        
        # List of cycles attributes
        self.cyclesText = []
        
        
        self.springsInterruptions = []
        

        # Create background squares
        self.canvas.create_rectangle(
            0.0,
            0.0,
            800.0,
            480.0,
            fill="#FFFFFF",
            outline="")
        self.canvas.create_rectangle(
            0.0,
            0.0,
            540.0,
            480.0,
            fill="#009B4A",
            outline="")



        # Create "Spring #x" Texts
        self.canvas.create_text(
            360.0,
            381.0,
            anchor="nw",
            text="Spring #10",
            fill="#FFFFFF",
            font=("Inter Bold", 14 * -1)
        )

        self.canvas.create_text(
            360.0,
            291.0,
            anchor="nw",
            text="Spring #9",
            fill="#FFFFFF",
            font=("Inter Bold", 14 * -1)
        )

        self.canvas.create_text(
            360.0,
            201.0,
            anchor="nw",
            text="Spring #8",
            fill="#FFFFFF",
            font=("Inter Bold", 14 * -1)
        )

        self.canvas.create_text(
            360.0,
            111.0,
            anchor="nw",
            text="Spring #7",
            fill="#FFFFFF",
            font=("Inter Bold", 14 * -1)
        )

        self.canvas.create_text(
            360.0,
            21.0,
            anchor="nw",
            text="Spring #6",
            fill="#FFFFFF",
            font=("Inter Bold", 14 * -1)
        )

        self.canvas.create_text(
            103.0,
            382.0,
            anchor="nw",
            text="Spring #5",
            fill="#FFFFFF",
            font=("Inter Bold", 14 * -1)
        )

        self.canvas.create_text(
            103.0,
            293.0,
            anchor="nw",
            text="Spring #4",
            fill="#FFFFFF",
            font=("Inter Bold", 14 * -1)
        )

        self.canvas.create_text(
            103.0,
            203.0,
            anchor="nw",
            text="Spring #3",
            fill="#FFFFFF",
            font=("Inter Bold", 14 * -1)
        )

        self.canvas.create_text(
            103.0,
            113.0,
            anchor="nw",
            text="Spring #2",
            fill="#FFFFFF",
            font=("Inter Bold", 14 * -1)
        )

        self.canvas.create_text(
            103.0,
            21.0,
            anchor="nw",
            text="Spring #1",
            fill="#FFFFFF",
            font=("Inter Bold", 14 * -1)
        )


        #Create background rectangles for number of cycles
        # # self.canvas.create_rectangle(
        #     53.0,
        #     43.0,
        #     233.0,
        #     83.0,
        #     fill="#D9D9D9",
        #     outline="")

        # self.canvas.create_rectangle(
        #     53.0,
        #     135.0,
        #     233.0,
        #     175.0,
        #     fill="#D9D9D9",
        #     outline="")

        # self.canvas.create_rectangle(
        #     53.0,
        #     225.0,
        #     233.0,
        #     265.0,
        #     fill="#D9D9D9",
        #     outline="")

        # self.canvas.create_rectangle(
        #     53.0,
        #     315.0,
        #     233.0,
        #     355.0,
        #     fill="#D9D9D9",
        #     outline="")

        # self.canvas.create_rectangle(
        #     53.0,
        #     404.0,
        #     233.0,
        #     444.0,
        #     fill="#D9D9D9",
        #     outline="")

        # self.canvas.create_rectangle(
        #     310.0,
        #     43.0,
        #     490.0,
        #     83.0,
        #     fill="#D9D9D9",
        #     outline="")

        # self.canvas.create_rectangle(
        #     310.0,
        #     135.0,
        #     490.0,
        #     175.0,
        #     fill="#D9D9D9",
        #     outline="")

        # self.canvas.create_rectangle(
        #     310.0,
        #     225.0,
        #     490.0,
        #     265.0,
        #     fill="#D9D9D9",
        #     outline="")

        # self.canvas.create_rectangle(
        #     310.0,
        #     315.0,
        #     490.0,
        #     355.0,
        #     fill="#D9D9D9",
        #     outline="")

        # # self.canvas.create_rectangle(
        #     310.0,
        #     404.0,
        #     490.0,
        #     444.0,
        #     fill="#D9D9D9",
        #     outline="")


        # Create Number of cycles texts and append them to a list
        # self.cyclesText.append(self.canvas.create_text(
        #     143.0,
        #     63.0,
        #     anchor="center",
        #     text="1",
        #     fill="#000000",
        #     font=("Inter Bold", 14 * -1)
        # ))
        
        
        
        #Create Texts Objects For the Cycles number
        for leftColumn in range(63,424,90):
            print(leftColumn)
            self.cyclesText.append(TextBox(143,leftColumn,self.canvas))
            
        for rightColumn in range(63,424,90):
            self.cyclesText.append(TextBox(400,rightColumn,self.canvas))
        
        
        # self.cyclesText.append(self.spring1)

        # self.cyclesText.append(self.canvas.create_text(
        #     143.0,
        #     153.0,
        #     anchor="center",
        #     text="2",
        #     fill="#000000",
        #     font=("Inter Bold", 14 * -1)
        # ))

        # self.cyclesText.append(self.canvas.create_text(
        #     143.0,
        #     243.0,
        #     anchor="center",
        #     text="3",
        #     fill="#000000",
        #     font=("Inter Bold", 14 * -1)
        # ))

        # self.cyclesText.append(self.canvas.create_text(
        #     143.0,
        #     333.0,
        #     anchor="center",
        #     text="4",
        #     fill="#000000",
        #     font=("Inter Bold", 14 * -1)
        # ))

        # self.cyclesText.append(self.canvas.create_text(
        #     143.0,
        #     423.0,
        #     anchor="center",
        #     text="Cycles",
        #     fill="#000000",
        #     font=("Inter Bold", 14 * -1)
        # ))

        # self.cyclesText.append(self.canvas.create_text(
        #     400.0,
        #     61.0,
        #     anchor="center",
        #     text="Cycles",
        #     fill="#000000",
        #     font=("Inter Bold", 14 * -1)
        # ))

        # self.cyclesText.append(self.canvas.create_text(
        #     400.0,
        #     153.0,
        #     anchor="center",
        #     text="Cycles",
        #     fill="#000000",
        #     font=("Inter Bold", 14 * -1)
        # ))

        # self.cyclesText.append(self.canvas.create_text(
        #     400.0,
        #     243.0,
        #     anchor="center",
        #     text="Cycles",
        #     fill="#000000",
        #     font=("Inter Bold", 14 * -1)
        # ))

        # self.cyclesText.append(self.canvas.create_text(
        #     400.0,
        #     332.0,
        #     anchor="center",
        #     text="Cycles",
        #     fill="#000000",
        #     font=("Inter Bold", 14 * -1)
        # ))

        # self.cyclesText.append(self.canvas.create_text(
        #     400.0,
        #     422.0,
        #     anchor="center",
        #     text="Cycles",
        #     fill="#000000",
        #     font=("Inter Bold", 14 * -1)
        # ))


        # Create Buttons 

        # FirstToFail  Button
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.FirstToFailTest,
            relief="flat"
        )
        self.button_1.place(
            x=683.0,
            y=287.0,
            width=105.0,
            height=48.0
        )

        # UntilFailure  Button
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.UntilFailureTest,
            relief="flat"
        )
        self.button_2.place(
            x=552.0,
            y=287.0,
            width=105.0,
            height=48.0
        )
        
        # Stop Button
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.StopButton,
            relief="flat"
        )
        self.button_3.place(
            x=683.0,
            y=139.0,
            width=105.0,
            height=48.0
        )

        # Start Button
        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.StartButton,
            relief="flat"
        )
        self.button_4.place(
            x=552.0,
            y=139.0,
            width=105.0,
            height=48.0
        )
        
        # Interruption Generator
        # self.generator = InterruptionGenerator(interval=0.5, window=self)
        
        # Create the Interruptions for the Springs
        springGPIOPins = [26,19,13,6,5,21,20,16]
        for i in range(len(springGPIOPins)):
            self.springsInterruptions.append(RaspGPIO(springGPIOPins[i],window=self, spring=self.cyclesText[i]))
        
        # Create Interruption for the cycle Counter
        self.cycleCounter = RaspGPIO(12,window=self)
        
        
        #Add Nidec-GA Logo to the UI
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            670.0,
            43.0,
            image=self.image_image_1
        )

        
        self.statusText = TextBox(670,404,self.canvas)
        self.UpdateInterface(self.statusText,"Idle")
        # self.canvas.create_rectangle(
        #     580.0,
        #     404.0,
        #     760.0,
        #     444.0,
        #     fill="#D9D9D9",
        #     outline="")

        # self.canvas.create_text(
        #     580.0,
        #     414.0,
        #     anchor="nw",
        #     text="status",
        #     fill="#000000",
        #     font=("Inter Bold", 14 * -1)
        # )
                
        
        
        self.testMode = TestMode()
        
        # self.root.attributes("-fullscreen",True)
        self.root.resizable(False, False)


    # Function to alter number of cycles text
    def change_text(self):
        for springCycle in self.cyclesText:
            springCycle.SetCycles(springCycle.GetCycles() + 1)
            if not springCycle.GetBrokenStatus():
                self.UpdateInterface(springCycle,springCycle.GetCycles())



    def ResetCounter(self):
        for springCycle in self.cyclesText:
            springCycle.SetCycles(0)
            self.UpdateInterface(springCycle,springCycle.GetCycles())
            springCycle.SetBrokenStatus(False)
    
    # Start of the interface running loop
    def Run(self):
        self.root.mainloop()

    # Start the interruption
    def StartButton(self):
        selectedMode = self.testMode.GetTestMode()
        if(selectedMode == None): self.UpdateInterface(self.statusText,"Select Test Mode")
        else:
            
            if(selectedMode == 0):
                self.UpdateInterface(self.statusText,"Running Until Failure")
            else:
                self.UpdateInterface(self.statusText,"Running Until First Fail")
                
            self.ResetCounter()
    
            self.cycleCounter.AddCounterEvent()
            
            for interruption in self.springsInterruptions:
                interruption.AddSpringEvent()
                

        

    # Stop the interruption
    def StopButton(self):
        self.cycleCounter.StopInterruption()
        
        if(self.testMode.GetTestStatus()):
            self.UpdateInterface(self.statusText,"Test Stopped")
        
        self.testMode.StopTest()
        
        for interruption in self.springsInterruptions:
            interruption.StopInterruption()
        
    
    def UpdateInterface(self, spring, number):
        self.canvas.itemconfig(spring.textBox, text=str(number))
    
    
    def BreakSpring(self,spring):
        spring.SetBrokenStatus(True)
        
        
    def UntilFailureTest(self):
        if(not self.testMode.GetTestStatus()):
            self.testMode.SetTestMode(0)
            self.testMode.SetTestStatus(True)
            self.UpdateInterface(self.statusText,"Until Failure Selected")
            
        else: self.UpdateInterface(self.statusText,"Test Already Running")
    
    def FirstToFailTest(self):
        if(not self.testMode.GetTestStatus()):
            self.testMode.SetTestMode(1)
            self.testMode.SetTestStatus(True)
            self.UpdateInterface(self.statusText,"First To Fail Selected")
            
        else: self.UpdateInterface(self.statusText,"Test Already Running")
        
        
        
        
        #Try to add a temporary text that says test already running and return to previous text