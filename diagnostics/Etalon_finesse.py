import CONFIG
from COMM import getvalue, setvalue
from init_start import getaddress
import numpy as np
import pandas
import os
import time

#Welcome Stewart

TEC_etalon = "tec1"
TEC_ic = "tec2"
dset = 3000

TEMP_min = 28
TEMP_max = 40
TEMP_step = 61


TEMP = np.linspace(TEMP_min, TEMP_max, TEMP_step)
print(TEMP)

Etalon_setaddress = getaddress(TEC_etalon+"_d", "set")
Etalon_readaddress = getaddress(TEC_etalon, "act")
IC_readaddress = getaddress(TEC_ic, "act")
DPHD_readaddress = getaddress("pzt1", "dp_power")
CLP_readaddress = getaddress("pzt1", "clp_power")


print ("total hours: " + str((dset*TEMP_step)/(60*60*5)))

df_folder = "C:/813_temp/"
if not os.path.exists(df_folder):
    os.makedirs(df_folder)
file = df_folder + "Etalon finesse 27012020" + ".csv"
for i in TEMP:
    setvalue(Etalon_setaddress, i, "u", "k")
    time.sleep(300)

    for m in range(dset):
        inst = getvalue(Etalon_readaddress, "u", "k")["value"]
        inst2 = getvalue(IC_readaddress, "u", "k")["value"]
        inst3 = getvalue(CLP_readaddress, "u", "k")["value"]
        inst4 = getvalue(DPHD_readaddress, "u", "k")["value"]

        if m % 200 == 0:
            print(m,i)

        df = pandas.DataFrame(data={"time": [time.time()], "Etalon": [inst], "IC": [inst2], "CLP": [inst3], "DPHD": [inst4]})
        df.to_csv(file, sep=',', index=False, mode="a", header = False)

