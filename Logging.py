from time import sleep
from CONFIG_log import *
from COMM import *
from init_start import *
from datetime import datetime, timedelta
from csv import DictWriter, writer
from os.path import expanduser, exists
from os import makedirs
from COMM import getvalue
import re

def getaddress_l(b, rel):
    return hex(int(base_l[b][0],16)+(eval(base_l[b][1])[rel][0]))[2:]


def get_value(module, address):
    register = eval(base_l[module][1])[address]
    address = getaddress_l(module, address)
    return getvalue(address, register[1], register[2])



def Logger_wrap(modules, name):

    documents_path = expanduser("~\\Documents")
    path = f"{documents_path}\\SLL Logging\\"
    if not exists(path):
        makedirs(path)

    start = datetime.now()
    if Globals.logoff == 0:
        Globals.logfile = f"{path}\\{name} {start.strftime('%d-%m-%y %f')}.csv"
        Globals.logoff = 2
    file = Globals.logfile
    pzts = []
    tecs = []
    lds = ["ld"]
    if "PZT0" in modules:
        pzts.append("pzt0_l")
    if "PZT1" in modules:
        pzts.append("pzt1_l")
    if "TEC0" in modules:
        tecs.append("tec0_l")
    if "TEC1" in modules:
        tecs.append("tec1_l")
    if "TEC2" in modules:
        tecs.append("tec2_l")
    if "TEC3" in modules:
        tecs.append("tec3_l")
    if "TEC4" in modules:
        tecs.append("tec4_l")
    if "TEC5" in modules:
        tecs.append("tec5_l")

    pzt_measurements = ["REG_PZTx_OV",
                        "REG_PZTx_CLP_VOLTAGE",
                        "REG_PZTx_DPhD_VOLTAGE",
                        "REG_PZTx_DPhD1_VOLTAGE"]


    tec_measurements = ["REG_TECx_OUT_CURRENT",
                        "REG_TECx_CURRENT_T"]


    ld_measurements = ["REG_LD_CO_CURRENT"]

    labels = {"REG_PZTx_OV": "Output Voltage",
              "REG_PZTx_CLP_VOLTAGE": "CLP Voltage",
              "REG_PZTx_DPhD_VOLTAGE": "DPhD 0",
              "REG_PZTx_DPhD1_VOLTAGE": "DPhD 1",
              "REG_TECx_OUT_CURRENT": "Current",
              "REG_TECx_CURRENT_T": "Temperature",
              "REG_LD_CO_CURRENT": "Laser Driver Current",
              "PCB_TEMP": "PCB Temperature"}

    results = {}

    field_names = []

    field_names.append("time")

    for pzt in pzts:
        for measurement in pzt_measurements:
            field_names.append(f"{pzt} - {labels[measurement]}")
    for tec in tecs:
        for measurement in tec_measurements:
            field_names.append(f"{tec} - {labels[measurement]}")
    for ld in lds:
        for measurement in ld_measurements:
            field_names.append(f"{ld} - {labels[measurement]}")
    field_names.append("PCB temperature")

    if Globals.logoff == 2:
        with open(file, "a", newline="") as f:
            csv_writer = writer(f)
            csv_writer.writerow(field_names)
        Globals.logoff = 3

    last_controller = start

    #try:

    if Globals.regoffset0<1000:
        last_controller = datetime.now()
        for pzt in pzts:
            for measurement in pzt_measurements:
                results[f"{pzt} - {labels[measurement]}"] = get_value(pzt, measurement)["value"]

        for tec in tecs:
            for measurement in tec_measurements:
                results[f"{tec} - {labels[measurement]}"] = get_value(tec, measurement)["value"]

        for ld in lds:
            for measurement in ld_measurements:
                results[f"{ld} - {labels[measurement]}"] = get_value(ld, measurement)["value"]

        results["time"] = datetime.now()
        results["PCB temperature"] = getvalue("0x1654", "u", "1")["value"]

        with open(file, "a", newline="") as f:
            csv_writer = DictWriter(f, fieldnames=field_names)
            csv_writer.writerow(results)

    # except IndexError:
    #     pass

    # except:
    #     Globals.logoff == 1
    #     return 0

