from tkinter import filedialog
import numpy as np
from tkinter import *
import pandas as pd
import os, ast
from ds1054z import DS1054Z
import time
#Welcome Stewart
TEC_etalon = "tec1"
TEC_ic = "tec2"
dset = 300
TEMP_min = 27
TEMP_max = 46
TEMP_step = 48
scope = DS1054Z('169.254.76.43')
channel = 2
rampchannel = 1
df_folder_scope = "C:/Plotting/813/"
root = Tk()
def getname(Entry):
    name = inp.get()
    df_folder_scope = "C:/Plotting/813/"
    clp = scope.get_waveform_samples(3)
    diff = scope.get_waveform_samples(4)
    etalon = scope.get_waveform_samples(channel)
    ramp = scope.get_waveform_samples(rampchannel)

    file = df_folder_scope + name + ".csv"
    df = pd.DataFrame(data={"etalon": etalon, "ramp": ramp, "diff": diff, "clp": clp})
    df.to_csv(file, sep=',', index=False, mode="a", header=True)
    print("Saved")


inp = StringVar()
Label(root, text = "Graph name").pack()
Entry(root, textvariable=inp, width=30).pack()
Button(root, text="Save", command=lambda: getname(inp)).pack()

root.mainloop()
