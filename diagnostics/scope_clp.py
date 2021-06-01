from ds1054z import DS1054Z
import time
import matplotlib
matplotlib.use("QT5Agg")
import matplotlib.pyplot as plt
import numpy as np
import PyQt5
from COMM import comm_init, comm_start, addvalue, setvalue, getvalue, readbit, getbit, resvalue
from init_start import getaddress
from CONFIG import *
import os
import ast
from datetime import datetime
import time

samples = 12*60*60*2

for i in range(samples):
    time.sleep(0.5)
    date = time.time()
    clp = getvalue("ec7f")["value"]
    dphd = getvalue("ec7d")["value"]

    result = str(date) + "," + str(clp) + "," + str(dphd)+"\n"

    file2write2 = open("clp/" + "clp_gain" + ".csv", 'a', newline="\n")
    file2write2.write(result)
    file2write2.close()



