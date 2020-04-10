

from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
import sqlite3
import sys
import time
import shutil

import dir_drill_main


def load_gui(self):
    self.btn_source_dir = tk.Button(self.master,width=12,height=2,text='select the source directory',command=lambda: dir_drill_main.get_source(self))
    self.btn_source_dir.grid(row=1,column=0,padx=(25,0),pady=(45,10),sticky=W)

    self.btn_final_dir = tk.Button(self.master,width=12,height=2,text='select the destination directory',command=lambda: dir_drill_main.get_final(self))
    self.btn_final_dir.grid(row=3,column=0,padx=(25,0),pady=(45,10),sticky=W)

    self.btn_move_files = tk.Button(self.master,width=12,height=2,text='move txt fils',command=lambda: dir_drill_main.send_files(self))
    self.btn_move_files.grid(row=5,column=0,padx=(25,0),pady=(45,10),sticky=W)

    self.txt_source_dir = tk.Entry(self.master,text='')
    self.txt_source_dir.grid(row=1,column=3,rowspan=4,columnspan=4,padx=(10,10),pady=(40,10),sticky=N+E+W)
    
    self.txt_final_dir = tk.Entry(self.master,text='')
    self.txt_final_dir.grid(row=3,column=3,rowspan=4,columnspan=4,padx=(10,10),pady=(40,10),sticky=N+E+W)

    self.txt_file_path = tk.Entry(self.master,text='')
    self.txt_file_path.grid(row=5,column=3,rowspan=4,columnspan=4,padx=(10,10),pady=(40,10),sticky=N+E+W)
    





if __name__ == "__main__":
    pass
