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
from serial.tools.list_ports import comports
import serial


def init_COMM(port):
    available_ports = list(comports())
    COMM_port = ""

    for p in available_ports:
        if "Silicon Labs CP210x USB to UART Bridge" in p.description:
            COMM_port = p.device

    if COMM_port == "":
        raise EnvironmentError("Device not connected.")

    Globals.ser = serial.Serial(
        # port=port,
        port=port,
        baudrate=57600,
        parity=serial.PARITY_NONE,
        stopbits=1,
        bytesize=8,
        timeout=8
    )

def stop_COMM():
    Globals.ser.close()

# import visa
# from ThorlabsPM100 import ThorlabsPM100
# rm = visa.ResourceManager()
# inst = rm.open_resource('USB::0x1313::0x8078::P0010641::INSTR', timeout=1)
# power_meter = ThorlabsPM100(inst=inst)

#BP - TEC3
#Ambient - TEC1
#LD - TEC0

main_port = "COM4"
amb_port = "COM3"

now = time.time()

LD_temp = []
BP_temp = []
Amb_temp = []
LD_current = []

init_COMM(main_port)

LD_current_add=getaddress("ld", "act")
LD_temp_add = getaddress("tec0", "act")
BP_temp_add = getaddress("tec3", "act")
Amb_temp_add = getaddress("tec0", "act")

addvalue(control['address'], 1)
setvalue(getaddress("ld_d", "curr"), "3.8", "u", "u")

for i in range(6*3600):

    LD_temp.append(getvalue(LD_temp_add, "u", "k")["value"])
    BP_temp.append(getvalue(BP_temp_add, "u", "k")["value"])
    LD_current.append(getvalue(LD_current_add, "u", "u")["value"])

    stop_COMM()
    init_COMM(amb_port)
    Amb_temp.append(getvalue(Amb_temp_add, "u", "k")["value"])
    stop_COMM()
    time.sleep(1)
    init_COMM(main_port)
    print(i)

resvalue(control['address'], 1)

file2write = open("ldstab/LD_temp", 'w')
file2write.write(str(LD_temp))
file2write.close()

file2write2 = open("ldstab/BP_temp", 'w')
file2write2.write(str(BP_temp))
file2write2.close()

file2write = open("ldstab/LD_current", 'w')
file2write.write(str(LD_current))
file2write.close()

file2write2 = open("ldstab/Amb_temp", 'w')
file2write2.write(str(Amb_temp))
file2write2.close()

long = "Cycles done in " + str(time.time() - now) + " seconds."

file2write2 = open("ldstab/timestamp", 'w')
file2write2.write(str(long))
file2write2.close()
