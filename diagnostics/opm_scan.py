import CONFIG
from COMM import getvalue, setvalue
from init_start import getaddress
import numpy as np
import pandas
import os
import time
from ds1054z import DS1054Z

dset = 15000
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
tec0_address_c = getaddress("tec0", "current")
tec1_address_c = getaddress("tec1", "current")
tec2_address_c = getaddress("tec2", "current")
tec3_address_c = getaddress("tec3", "current")
tec0_set = getaddress("tec0_d", "set")
ldact_address = getaddress("ld", "act")
ld_curr_address = getaddress("ld_d", "curr")
clp_address = "eff7"

df_folder = "C:/349_OPM/"
if not os.path.exists(df_folder):
    os.makedirs(df_folder)
file = df_folder + "OPM_periodic_test" + ".csv"

for i in range(10):
    if i%2 == 0:
        print("disabled")
        setvalue("ff9d", "0x55500aaa", "1", "1")
    else:
        setvalue("ff9d", "0x55532aaa", "1", "1")

    for m in range(dset):
        inst = getvalue(tec0_address, "u", "k")["value"]
        inst2 = getvalue(tec1_address, "u", "k")["value"]
        inst3 = getvalue(tec2_address, "u", "k")["value"]
        inst4 = getvalue(tec3_address, "u", "k")["value"]
        inst5= getvalue(clp_address, "u", "u")["value"]
        inst6 = getvalue(ldact_address, "u", "u")["value"]
        inst7 = getvalue(tec0_address_c, "u", "u")["value"]
        inst8 = getvalue(tec1_address_c, "u", "u")["value"]
        inst9 = getvalue(tec2_address_c, "u", "u")["value"]
        inst10 = getvalue(tec3_address_c, "u", "u")["value"]
        try:
            diffa = np.mean(scope.get_waveform_samples(1))
            diffb = np.mean(scope.get_waveform_samples(2))
        except:
            diffa = 0
            diffb = 0

        print(m, inst, inst2, inst3, inst4, inst5, inst6)
        df = pandas.DataFrame(data={"time": [time.time()], "ch0": [diffa], "ch1": [diffb], "tec0": [inst], "tec1": [inst2], "tec2": [inst3], "tec3": [inst4], "tec0_c": [inst7], "tec1_c": [inst8], "tec2_c": [inst9], "tec3_c": [inst10], "clp": [inst5], "ld": [inst6]})
        df.to_csv(file, sep=',', index=False, mode="a", header = False)

