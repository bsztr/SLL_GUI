import CONFIG
from COMM import getvalue, setvalue, readbit, addvalue, resvalue
from init_start import getaddress
import numpy as np
import pandas
import os
import time
import csv

TEC0 = "tec0"
TEC1 = "tec1"
TEC2 = "tec2"
TEC3 = "tec3"

T_address0 = getaddress(TEC0+"_d", "set")
Tread_address0 = getaddress(TEC0, "act")
Tread_curr0 = getaddress(TEC0, "current")
Tread_req0 = getaddress(TEC0, "req current")
T_address1 = getaddress(TEC1+"_d", "set")
Tread_address1 = getaddress(TEC1, "act")
Tread_curr1 = getaddress(TEC1, "current")
Tread_req1 = getaddress(TEC1, "req current")
T_address2 = getaddress(TEC2+"_d", "set")
Tread_address2 = getaddress(TEC2, "act")
Tread_curr2 = getaddress(TEC2, "current")
Tread_req2 = getaddress(TEC2, "req current")
T_address3 = getaddress(TEC3+"_d", "set")
Tread_address3 = getaddress(TEC3, "act")
Tread_curr3 = getaddress(TEC3, "current")
Tread_req3 = getaddress(TEC3, "req current")

TEC0_set = getvalue(T_address0, "u", "k")["value"]
TEC1_set = getvalue(T_address1, "u", "k")["value"]
TEC2_set = getvalue(T_address2, "u", "k")["value"]
TEC3_set = getvalue(T_address3, "u", "k")["value"]

#INIT

setvalue(T_address0, 25, "u", "k")
setvalue(T_address1, 25, "u", "k")
setvalue(T_address2, 25, "u", "k")
setvalue(T_address3, 25, "u", "k")
time.sleep(300)

dstep = int(10*60*60*1.2)

setvalue(T_address0, TEC0_set, "u", "k")
setvalue(T_address1, TEC1_set, "u", "k")
setvalue(T_address2, TEC2_set, "u", "k")
setvalue(T_address3, TEC3_set, "u", "k")

File = r"C:/Plotting/813_TECtest.csv"

fields=["time", "TEC0", "TEC1", "TEC2", "TEC3", "TEC0 curr", "TEC1 curr", "TEC2 curr", "TEC3 curr", "TEC0 req", "TEC1 req", "TEC2 req", "TEC3 req"]
with open(File, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(fields)

for i in range(dstep):
    time = time.time()
    TEC0_act = getvalue(Tread_address0, "u", "k")["value"]
    TEC1_act = getvalue(Tread_address1, "u", "k")["value"]
    TEC2_act = getvalue(Tread_address2, "u", "k")["value"]
    TEC3_act = getvalue(Tread_address3, "u", "k")["value"]
    TEC0_curr = getvalue(Tread_curr0, "u", "u")["value"]
    TEC1_curr = getvalue(Tread_curr1, "u", "u")["value"]
    TEC2_curr = getvalue(Tread_curr2, "u", "u")["value"]
    TEC3_curr = getvalue(Tread_curr3, "u", "u")["value"]
    TEC0_req = getvalue(Tread_req0, "u", "u")["value"]
    TEC1_req = getvalue(Tread_req1, "u", "u")["value"]
    TEC2_req = getvalue(Tread_req2, "u", "u")["value"]
    TEC3_req = getvalue(Tread_req3, "u", "u")["value"]
    data = [time, TEC0_act, TEC1_act, TEC2_act, TEC3_act, TEC0_curr, TEC1_curr, TEC2_curr, TEC3_curr, TEC0_req, TEC1_req, TEC2_req, TEC3_req]
    with open(File, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

time.sleep(240)

actual = getvalue("03FA")["value"]

if readbit(actual, 17) == "1":
    if readbit(actual, 0) != "1":
        addvalue("03FA", 1)

ddstep = int(10*20*60*1.2)
LD_address_curr = getaddress("ld", "act")
LD_address_req = getaddress("ld_d", "curr")

File = r"C:/Plotting/813_LDtest.csv"

fields=["time", "LD current", "LD req current"]
with open(File, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(fields)

for i in range (ddstep):
    time = time.time()
    LD_curr = getvalue(LD_address_curr, "u", "u")["value"]
    LD_req = getvalue(LD_address_req, "u", "u")["value"]
    data = [time, LD_curr, LD_req]
    with open(File, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

resvalue("03FA", 1)
print("Test complete.")

