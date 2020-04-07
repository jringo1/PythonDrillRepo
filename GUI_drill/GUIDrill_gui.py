from tkinter import *
import tkinter as tk

import GUIDrill_main

def load_gui(self):

    self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Browse')
    self.btn_browse1.grid(row=1,column=0,padx=(25,0),pady=(45,10),sticky=W)
    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse')
    self.btn_browse2.grid(row=3,column=0,padx=(25,0),pady=(10,10),sticky=W)
    self.btn_chk = tk.Button(self.master,width=12,height=2,text='Check for files...')
    self.btn_chk.grid(row=5,column=0,padx=(25,0),pady=(15,15))
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program')
    self.btn_close.grid(row=5,column=7,padx=(25,0),pady=(15,15))

    self.txt_files1 = tk.Entry(self.master,text='')
    self.txt_files1.grid(row=1,column=1,rowspan=5,columnspan=5,padx=(25,0),pady=(46,10),sticky=N+E+W)
    self.txt_files2 = tk.Entry(self.master,text='')
    self.txt_files2.grid(row=3,column=1,rowspan=5,columnspan=5,padx=(25,0),pady=(10,10),sticky=N+E+W)
if __name__ == "__main__":
    pass
