import CONFIG
from COMM import getvalue, setvalue
from init_start import getaddress
import numpy as np
import pandas
import os
import time
import visa
from ThorlabsPM100 import ThorlabsPM100

TEC = "tec2"
#TEC_b = "tec2"
dset = 300

savefolder = r"desktop"

TEMP_min = 25.1
TEMP_max = 25.9
TEMP_step = 3

# P_min = 3
# P_max =  24
# P_step = 4
# I_min = 2
# I_max = 8
# I_step = 3
#
# D_min = 0
# D_max = 1
# D_step = 2

TEMP = np.round(np.linspace(TEMP_min, TEMP_max, TEMP_step),2)
# print(TEMP)
# P = np.round(np.linspace(P_min, P_max, P_step),2)
# I = np.round(np.linspace(I_min, I_max, I_step),2)
# D = np.round(np.linspace(D_min, D_max, D_step),2)

T_address = getaddress(TEC, "set")
Tread_address = getaddress(TEC, "act")
#T_address2 = getaddress(TEC_b+"_d", "set")
#Tread_address2 = getaddress(TEC_b, "act")
#P_address = getaddress(TEC+"_d", "p")
#I_address = getaddress(TEC+"_d", "i")
#D_address = getaddress(TEC+"_d", "d")

rm = visa.ResourceManager()
print(rm.list_resources())
inst = rm.open_resource('USB::0x1313::0x8078::P0010641::INSTR', timeout=1)
power_meter = ThorlabsPM100(inst=inst)

print(power_meter.read)
output = []
for i in TEMP:
    setvalue(T_address, i, "u", "k")
    #setvalue(T_address2, i, "u", "k")
    time.sleep(300)
    for m in range(dset):
        inst = getvalue(Tread_address, "u", "k")["value"]
        #inst2 = getvalue(Tread_address2, "u", "k")["value"]
        if m % 200 == 0:
            setvalue(T_address, inst, "u", "k")
        output.append(inst)
        #output2.append(inst2)
    fluct = np.round(1000*np.std(output),2)
    df = pandas.DataFrame(data={"data": output, "data2": output2, "set temp": i, "p": j, "i": k, "d": l})
    df_folder = savefolder
    if not os.path.exists(df_folder):
        os.makedirs(df_folder)
    file = df_folder + str(fluct) +"_" + str(j) + "_" + str(k) + "_" +  str(l) + ".csv"
    df.to_csv(file, sep=',', index=False)

