import time
import tkinter as tk
from gui import DevProGUI
from utils import respond, record_audio, speak

class person:
    name = ''
    def setName(self, name):
        self.name = name

time.sleep(1)

person_obj = person()

if __name__ == "__main__":
    # Initialize the GUI
    root = tk.Tk()
    gui = DevProGUI(root, respond, record_audio, speak, person_obj)
    root.mainloop()