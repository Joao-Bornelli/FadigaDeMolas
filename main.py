import tkinter as tk
from build.gui import MainWindow



def main():

    root = tk.Tk()
    window = MainWindow(root)

    window.Run()  

if __name__ == "__main__":
    main()