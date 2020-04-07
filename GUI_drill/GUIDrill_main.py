
from tkinter import *
import tkinter as tk

import GUIDrill_gui

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)

        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")
            
        GUIDrill_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
