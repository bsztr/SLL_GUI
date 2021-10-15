import CONFIG
from COMM import getvalue, setvalue
from init_start import getaddress
import numpy as np
import pandas
import os
import time
from ds1054z import DS1054Z

dset = 600

t_vbg_min = 26
t_vbg_max = 38
t_etalon_min = 20
t_etalon_max = 37



TSET_vbg = np.linspace(t_vbg_min, t_vbg_max, 49)
TSET_etalon = np.linspace(t_etalon_min, t_etalon_max, 49)


tec0_address = getaddress("tec0", "act")
tec1_address = getaddress("tec1", "act")
tec2_address = getaddress("tec2", "act")
tec3_address = getaddress("tec3", "act")
tec1_set_etalon = getaddress("tec1_d", "set")
tec2_set_vbg = getaddress("tec2_d", "set")
# ldact_address = getaddress("ld", "act")
# ld_curr_address = getaddress("ld_d", "curr")
# clp_address = "eff7"

df_folder = "C:/Plotting/"
if not os.path.exists(df_folder):
    os.makedirs(df_folder)
file = df_folder + "VBG_tune_magic_10092021" + ".csv"


for i in range(len(TSET_etalon)):
    setvalue(tec1_set_etalon, TSET_etalon[i], "u", "k")
    setvalue(tec2_set_vbg, TSET_vbg[i], "u", "k")
    time.sleep(120)
    print(i, len(TSET_etalon))
    for m in range(dset):
        inst = getvalue(tec0_address, "u", "k")["value"]
        inst2 = getvalue(tec1_address, "u", "k")["value"]
        inst3 = getvalue(tec2_address, "u", "k")["value"]
        inst4 = getvalue(tec3_address, "u", "k")["value"]

        print(m, inst, inst2, inst3, inst4)
        df = pandas.DataFrame(data={"time": [time.time()], "tec0": [inst], "tec1": [inst2], "tec2": [inst3], "tec3": [inst4]})
        df.to_csv(file, sep=',', index=False, mode="a", header = False)


t_vbg_min = 38
t_vbg_max = 46
t_etalon_min = 19
t_etalon_max = 29



TSET_vbg = np.linspace(t_vbg_min, t_vbg_max, 33)
TSET_etalon = np.linspace(t_etalon_min, t_etalon_max, 33)



setvalue(tec1_set_etalon, t_etalon_min, "u", "k")
setvalue(tec2_set_vbg, t_vbg_min, "u", "k")
time.sleep(300)

for i in range(len(TSET_etalon)):
    setvalue(tec1_set_etalon, TSET_etalon[i], "u", "k")
    setvalue(tec2_set_vbg, TSET_vbg[i], "u", "k")
    time.sleep(120)
    print(i, len(TSET_etalon))
    for m in range(dset):
        inst = getvalue(tec0_address, "u", "k")["value"]
        inst2 = getvalue(tec1_address, "u", "k")["value"]
        inst3 = getvalue(tec2_address, "u", "k")["value"]
        inst4 = getvalue(tec3_address, "u", "k")["value"]

        print(m, inst, inst2, inst3, inst4)
        df = pandas.DataFrame(data={"time": [time.time()], "tec0": [inst], "tec1": [inst2], "tec2": [inst3], "tec3": [inst4]})
        df.to_csv(file, sep=',', index=False, mode="a", header = False)

