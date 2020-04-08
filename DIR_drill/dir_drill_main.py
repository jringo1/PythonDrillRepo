
from tkinter import *
import tkinter as tk
from tkinter import filedialog

import dir_drill_gui

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)

        self.master.title("Directory search")
        self.master.configure(bg="#F0F0F0")
            
        dir_drill_gui.load_gui(self)
         
def get_files(self):
    filename = filedialog.askdirectory(initialdir="/", title="Select a File",)
    self.txt_dir.insert(2,filename)
    
            
    




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
