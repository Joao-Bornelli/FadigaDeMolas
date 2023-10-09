import tkinter as tk
from build import gui

root = tk.Tk()

# Create an instance of the generated GUI class
app = gui(root)

# Start the GUI event loop
root.mainloop()

