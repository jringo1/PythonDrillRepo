
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
import sqlite3
import sys
import time
import shutil

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
        
     
def get_source(self):
    self.path = filedialog.askdirectory(title="Select a directory")
    #self.file_list = os.listdir(self.path)
    self.txt_source_dir.insert(2,self.path)
    

def get_final(self):
    self.path2 = filedialog.askdirectory(initialdir = '/', title="Select a directory")
    #self.file_list2 = os.listdir(self.path2)
    self.txt_final_dir.insert(2,self.path2)
    


conn = sqlite3.connect('file_drill.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_Name VARCHAR(50), \
        col_Type VARCHAR(50) \
        )")
    

def send_files(self):
    self.file_list = os.listdir(self.path)
    for fileName in self.file_list:
            if fileName.endswith('.txt'):
                with conn:
                    cur = conn.cursor()
                    cur.execute('INSERT INTO tbl_files(col_name) VALUES (?)', (fileName,))
                    filePath = (os.path.join(self.path, fileName))
                    print(fileName)
                    mod_time = os.path.getmtime(filePath)
                    print(mod_time)
                    shutil.move(filePath,self.path2)
         

    
            
    




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
