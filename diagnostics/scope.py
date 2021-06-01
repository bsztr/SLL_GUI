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


# import visa
# from ThorlabsPM100 import ThorlabsPM100
# rm = visa.ResourceManager()
# inst = rm.open_resource('USB::0x1313::0x8078::P0010641::INSTR', timeout=1)
# power_meter = ThorlabsPM100(inst=inst)

#TEC settings
TEC_name = "tec1"
TEC_max = 55
TEC_min = 40
TEC_step = 0.05
TEC_time = 30
TEC_interval = np.linspace(TEC_min, TEC_max, int((TEC_max-TEC_min)/TEC_step))
TEC_length = len(TEC_interval)


#Ramp settings
RAMP_name = "pzt0"
RAMP_max = 75
RAMP_min = 15
RAMP_step = 1
RAMP_time = 1
RAMP_interval = np.linspace(RAMP_min, RAMP_max, int((RAMP_max-RAMP_min)/RAMP_step))
RAMP_length = len(RAMP_interval)

print("TEC steps " + str(TEC_length))
print("RAMP steps " + str(RAMP_length))

print("STEPs overall " + str(TEC_length * RAMP_length))

# print("Power cycle starting...")
#
# comm_init()
# comm_start()
#
# print("Full mode enabled. TECs turning on")
#
# addvalue(control['address'], 1024)
#
# print("Waiting for the TEC to stabilise")
#
# time.sleep(45)
#
# addvalue(control['address'], 3)

#Enable parking
actual = getvalue(control['address'])['value']
if RAMP_name == "pzt0":
    bit = [8, 6]
else:
    bit = [9, 7]
if readbit(actual, 1) != "1":
    addvalue(control['address'], 2)
if readbit(actual, bit[1]) == "0":
    setvalue(control['address'], actual + control[RAMP_name + "_m"])
    actual = actual + control[RAMP_name + "_m"]
if readbit(actual, bit[0]) == "1":
    resvalue(control['address'], control[RAMP_name + "_l"])
    actual = actual - control[RAMP_name + "_l"]

now = time.time()

scope = DS1054Z('169.254.89.41')

# Execute TEC cycle
for i in range(TEC_length):
    # power = power_meter.read

    setvalue(getaddress(TEC_name + "_d", "set"),TEC_interval[i] ,"u", "k")
    setvalue(getaddress(RAMP_name + "_d", "park"), RAMP_min, "u", "u")
    time.sleep(25)
    print("Temperature set to: " + str(TEC_interval[i]))

    #Ramping cycle begins

    for k in range(RAMP_length):
        setvalue(getaddress(RAMP_name + "_d", "park"),RAMP_interval[k],"u","u")
        data = scope.get_waveform_samples(1)
        ramp = scope.get_waveform_samples(2)
        green = scope.get_waveform_samples(3)

        file2write=open("scope/"+"TEC" + str(round(TEC_interval[i],3)) + "RAMP" + str(round(RAMP_interval[k],2)),'w')
        file2write.write(str(data))
        file2write.close()

        file2write2 = open("scope/" + "PZT" + str(round(TEC_interval[i], 3)) + "RAMP" + str(round(RAMP_interval[k], 2)),'w')
        file2write2.write(str(ramp))
        file2write2.close()

        file2write2 = open("scope/" + "GREEN" + str(round(TEC_interval[i], 3)) + "RAMP" + str(round(RAMP_interval[k], 2)),'w')
        file2write2.write(str(green))
        file2write2.close()

        # file2write2 = open("scope/" + "POWER" + str(round(TEC_interval[i], 3)) + "RAMP" + str(round(RAMP_interval[k], 2)),'w')
        # file2write2.write(str(ramp))
        # file2write2.close()

    print("Time elapsed:" + str(time.time() - now))

resvalue(control['address'], 1)

directory = r'C:\Users\Ben\OneDrive - Mrs\Unik_GUI\scope'

for filename in os.listdir(directory):
    if "TEC" in filename:
        print(filename)
        if filename[8] == "R":
            TEC = filename[3:8]
        elif filename[7] == "R":
            TEC = filename[3:7]
        else:
            TEC = filename[3:8]

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

        file2write2 = open("scope/" + "PZT" + filename[3:], 'r')
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

        plt.savefig("scope/images/" + "TEC" +  TEC + "RAMP" + RAMP + ".png")



print("Cycles done in " + str(time.time() - now) + " seconds.")