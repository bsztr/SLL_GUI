import CONFIG
from COMM import getvalue, setvalue
from init_start import getaddress
import numpy as np
import pandas
import os
import time

#Welcome Stewart

TEC_bottom = "tec1" #etalon
TEC_top = "tec2" #IC etalon
dset = 3000

TEMP_min = 25
TEMP_max = 40
TEMP_step = 61


TEMP = np.linspace(TEMP_min, TEMP_max, TEMP_step)
print(TEMP)

dphd_readdress = getaddress(TEC_top+"_d", "set")
clp_readaddress = getaddress(TEC_top+"_d", "set")
ic_readaddress = getaddress(TEC_top, "act")
etalon_setaddress = getaddress(TEC_bottom+"_d", "set")
etalon_readaddress = getaddress(TEC_bottom, "act")


print ("total hours: " + str((dset*TEMP_step)/(60*60*5)))


timest = []
etalon_temp = []
ic_temp = []
df_folder = "C:/813_temp/"
if not os.path.exists(df_folder):
    os.makedirs(df_folder)
file = df_folder + "etalon finesse data 27012021" + ".csv"
for i in TEMP:
    setvalue(Bottom_setaddress, i, "u", "k")
    inst = getvalue(Bottom_readaddress, "u", "k")["value"]
    setvalue(Top_setaddress, i, "u", "k")
    print(i)
    time.sleep(300)

    for m in range(dset):
        inst = getvalue(Bottom_readaddress, "u", "k")["value"]
        inst2 = getvalue(Top_readaddress, "u", "k")["value"]
        if m % 200 == 0:
            setvalue(Top_setaddress, inst2, "u", "k")
            print(m,i)
        # bot_temp.append(inst)
        # top_temp.append(inst2)
        # timest.append(time.time())
        #time.sleep(1)
        df = pandas.DataFrame(data={"top": [inst], "bottom": [inst2], "time": [time.time()]})
        df.to_csv(file, sep=',', index=False, mode="a", header = False)
        #print(m, dset, round(m/dset,1)*100)
# df = pandas.DataFrame(data={"top": top_temp, "bottom": bot_temp, "time": timest})
# df_folder = "C:/813_temp/"
# if not os.path.exists(df_folder):
#     os.makedirs(df_folder)
# file = df_folder + "tempdata_licaf_allbonded_twosidetest" + ".csv"
# df.to_csv(file, sep=',', index=False)
