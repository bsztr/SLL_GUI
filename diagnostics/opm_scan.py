import CONFIG
from COMM import getvalue, setvalue
from init_start import getaddress
import numpy as np
import pandas
import os
import time
from ds1054z import DS1054Z

dset = 600
imin = 2.5
imax = 2.7

tmin = 17.8
tmax = 28.1

item = "230"
#now = str(time.time())
now =""

scope = DS1054Z('169.254.76.41')

LDCURR = np.linspace(imin, imax, 4)
TSETC = np.linspace(tmax, tmin, 4)
print(LDCURR)
print(TSETC)

tec0_address = getaddress("tec0", "act")
tec1_address = getaddress("tec1", "act")
tec2_address = getaddress("tec2", "act")
tec3_address = getaddress("tec3", "act")
tec0_set = getaddress("tec0_d", "set")
ldact_address = getaddress("ld", "act")
ld_curr_address = getaddress("ld_d", "curr")
clp_address = "eff7"

df_folder = "C:/349_OPM/"
if not os.path.exists(df_folder):
    os.makedirs(df_folder)
file = df_folder + "OPM_locked_03082021" + ".csv"
scope_f = df_folder + "OPM_locked_03082021_scope"
for i in LDCURR:
    # setvalue(ld_curr_address, i, "u", "u")
    # pp = int(np.where(LDCURR == i)[0])
    # setvalue(ld_curr_address, TSETC[pp], "u", "k")
    # print(i, TSETC[pp], "set")
    # time.sleep(75)
    LDc = []
    for q in range(10):
        LDc.append(getvalue(ldact_address, "u", "u")["value"])


    LDcurrent = np.mean(LDc)
    print(LDcurrent)
    TCHECK = ((LDcurrent - imin) / (imax - imin))*(tmax - tmin)
    print(TCHECK)
    #setvalue(tec0_set,TCHECK, "u", "k")


    for m in range(dset):
        inst = getvalue(tec0_address, "u", "k")["value"]
        inst2 = getvalue(tec1_address, "u", "k")["value"]
        inst3 = getvalue(tec2_address, "u", "k")["value"]
        inst4 = getvalue(tec3_address, "u", "k")["value"]
        inst5= getvalue(clp_address, "u", "u")["value"]
        inst6 = getvalue(ldact_address, "u", "u")["value"]
        if m % 601 == 0:
            diffa = scope.get_waveform_samples(1)
            diffb = scope.get_waveform_samples(2)
            ramp = scope.get_waveform_samples(4)
            df = pandas.DataFrame(data={"etalon": diffa, "clp": diffb, "ramp": ramp})
            df.to_csv(scope_f + "_" + str(i) + "_" + str(m) + ".csv", sep=',', index=False, mode="a", header=False)
        print(m, inst, inst2, inst3, inst4, inst5, inst6)
        df = pandas.DataFrame(data={"time": [time.time()], "tec0": [inst], "tec1": [inst2], "tec2": [inst3], "tec3": [inst4], "clp": [inst5], "ld": [inst6]})
        df.to_csv(file, sep=',', index=False, mode="a", header = False)

