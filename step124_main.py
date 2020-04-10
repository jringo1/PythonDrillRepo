
import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog

import step124_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)

        self.master.title("Directory search")
        self.master.configure(bg="#F0F0F0")
            
        step124_gui.load_gui(self)




    



def get_source(self):
    path = filedialog.askdirectory(initialdir = r'C:\Users\Meerkat\Desktop\python_projects', title="Select a directory")
    file_list = os.listdir(path)
    self.txt_source_dir.insert(2,file_list)
    return file_list

def get_final(self):
    path = filedialog.askdirectory(initialdir = '/', title="Select a directory")
    file_list2 = os.listdir(path)
    self.txt_final_dir.insert(2,file_list2)
    return file_list2

def send_files(self):
    for fileName in file_list:
        filePath = ('Folder Path: ' + os.path.abspath(os.path.join(dirName, filename)))

    
    


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
