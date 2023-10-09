import tkinter as tk
from build import gui

root = tk.Tk()
root.attributes('-fullscreen', True)
# Create an instance of the generated GUI class

def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

root.bind('<Escape>', exit_fullscreen)

app = gui(root)



# Start the GUI event loop
root.mainloop()

