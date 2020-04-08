

from tkinter import *
import tkinter as tk

import dir_drill_main


def load_gui(self):
    self.btn_search = tk.Button(self.master,width=12,height=2,text='search',command=lambda: dir_drill_main.get_files(self))
    self.btn_search.grid(row=2,column=0,padx=(25,0),pady=(45,10),sticky=W)
    

    self.txt_dir = tk.Entry(self.master,text='')
    self.txt_dir.grid(row=2,column=3,rowspan=1,columnspan=3,padx=(10,10),pady=(40,10),sticky=N+E+W)
    





if __name__ == "__main__":
    pass
