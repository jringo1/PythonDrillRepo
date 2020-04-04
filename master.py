import os

import time

path = os.getcwd()

Repo_List = os.listdir(path)

print(Repo_List)

print(os.path.join(path, "Meerkat/Desktop/PythonDrillRepo", "a.txt"))

path2 = '/Meerkat/Desktop/PythonDrillRepo/'


modification_time = os.path.getmtime(path)
print("Last modification time since the epoch:", modification_time)

local_time = time.ctime(modification_time)
print("Last modification time(Local time):", local_time)

def open_txt():
    f = open("a.txt","r")
    if f.mode == 'r':
        content = f.read()
        print(content)
        mod_time2 = os.path.getmtime("a.txt")
        local_time2 = time.ctime(mod_time2)
        print(local_time2)
open_txt()

def open_txt2():
    f = open("b.txt","r")
    if f.mode == 'r':
        content = f.read()
        print(content)
        mod_time2 = os.path.getmtime("b.txt")
        local_time2 = time.ctime(mod_time2)
        print(local_time2)
open_txt2()


