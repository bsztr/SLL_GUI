from ds1054z import DS1054Z
import time
import matplotlib

matplotlib.use("QT5Agg")
import matplotlib.pyplot as plt
import numpy as np
import PyQt5
#from COMM import comm_init, comm_start, addvalue, setvalue, getvalue, readbit, getbit, resvalue
#from init_start import getaddress
#from CONFIG import *
import os
import ast

directory = r'C:\Users\Ben\OneDrive - Mrs\Unik_GUI\scope'

for filename in os.listdir(directory):
    if "GREEN" in filename:
        print(filename)
        # if filename[8] == "R":
        #     TEC = filename[3:8]
        # elif filename[7] == "R":
        #     TEC = filename[3:7]
        # else:
        #     TEC = filename[3:8]

        if filename[10] == "R":
            TEC = filename[5:10]
        elif filename[9] == "R":
            TEC = filename[5:9]
        else:
            TEC = filename[5:10]

        if filename[-5] == "P":
            RAMP = filename[-4:]
        elif filename[-4] == "P":
            RAMP = filename[-3:]
        elif filename[-3] == "P":
            RAMP = filename[-2:]
        else:
            RAMP = filename[-5:]

        file2write = open("scope/" + filename, 'r')
        data = ast.literal_eval(file2write.read())
        file2write.close()

        file2write2 = open("scope/" + "PZT" + filename[5:], 'r')
        pzt = ast.literal_eval(file2write2.read())
        file2write2.close()

        print(TEC)

        fig = plt.Figure(figsize=(7, 5), dpi=100)
        x = np.linspace(0, 10, len(data))

        plt.clf()
        plt.title("TEC temperature " + TEC + ", Ramp voltage " + RAMP + " .")
        plt.xlabel('time (s)')
        #plt.xaxis.set_label_position('top')
        plt.ylabel('Amplitude (V)')
        plt.plot(x, data, label="Frequency amplitude")
        plt.plot(x, np.multiply(pzt,0.03), label="Ramp amplitude")
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
                       fancybox=True, shadow=True, ncol=5)

        plt.savefig("scope/images/green/" + "Green" +  TEC + "RAMP" + RAMP + ".png")
