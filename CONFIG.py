#3 data types: float, uint32 and int32, indicated by f,u,i as second element of tuple
#3 conversion factors: microKelvin, micro, one to one, indicated by k,u,1 as third element of tuple
#passing tuple as *tuple

import json
import Globals


#def newfw():
#     print("we are here")
#     global base
#     global control
#     global activate
#     global tec
#     global tec_d
#     global pzt
#     global pzt_d
#     global loch_mech
#     global lock_dict
#     global lh
#     global ld
#     global ld_d
#     global gui
#     global rang
#     global indicator
#     global cb
#     global Background
#     global Colours
#     global Calibration
#     global subCalibration
#     global error
#     global DefaultNames
#     # tec = {
#     #     "current": [896, "u", "u"],
#     #     "req current": [897, "u", "u"],
#     #     "set": [898, "u", "k"],
#     #     "act": [899, "u", "k"]
#     # }
#     #
#     # pzt = {
#     #     "parkv": [897, "u", "u"],
#     #     "clp_power": [896, "u", "u"],
#     #     "dp_power": [898, "u", "u"],
#     #     "id": [1, "s", "1"]
#     # }
#     #
#     # ld = {
#     #     "act": [896, "u", "u"]
#     # }


base = {
    "tec0": ["DFFF", "tec"],
    "tec1": ["DBFF", "tec"],
    "tec2": ["D7FF", "tec"],
    "tec3": ["D3FF", "tec"],
    "tec0_d": ["FFF5", "tec_d"],
    "tec1_d":["FFE1","tec_d"],
    "tec2_d":["FFCD","tec_d"],
    "tec3_d":["FFB9","tec_d"],
    "pzt0":["EFFF","pzt"],
    "pzt1":["EBFF","pzt"],
    "pzt0_d":["FF91","pzt_d"],
    "pzt1_d":["FF66","pzt_d"],
    "lh":["FFFF","lh"],
    "ld_d": ["FFA5","ld_d"],
    "ld": ["BFFF","ld"],
    "cb":["03FF","cb"],
    "gui": ["FD00", "gui"]
}

control={
    "address":"03FA",
    "full": 8,
    "ext": 4,
    "ld": 1,
    "pzt": 2,
    "tec": 1024,
    "pzt0_l": 256,
    "pzt0_m": 64,
    "pzt1_l": 512,
    "pzt1_m": 128
}

activate={
    "address": "FFFE",
    "CB": 0,
    "LH": 0,
    "tec0": 1,
    "tec1": 2,
    "tec2":4,
    "tec3":8,
    "pzt0":16,
    "pzt1":32,
    "ldr":64,
    "dpot": "FFFD",
    "dpot0": 63,
    "dpot1": 4032
}



tec = {
    "current": [Globals.tec_current, "u", "u"],
    "req current": [Globals.tec_reqcurrent, "i", "u"],
    "set": [Globals.tec_set, "u", "k"],
    "act": [Globals.tec_act, "u", "k"]
}



tec_d= {
    "maxc": [1, "u", "u"],
    "maxv": [0, "u", "u"],
    "warm":[18,"u","1"],
    "set": [11, "u", "k"],
    "p": [2, "f", "1"],
    "i": [3, "f", "1"],
    "d": [4, "f", "1"]

}


pzt = {
    "parkv": [Globals.pzt_parkv, "u", "u"],
    "clp_power": [Globals.pzt_clppower, "u", "u"],
    "dp_power": [Globals.pzt_dp_power, "i", "u"],
    "ov": [Globals.pzt_ov, "u", "u"],
    "id": [1, "s", "1"],
    "dphd": [770, "u", "1"],
    "clp": [773, "u", "1"],
    "v0": [776, "u", "1"],
    "nrd": [768, "u", "1"],
    "nrc": [771, "u", "1"],
    "nrv": [774, "u", "1"],
    "wploc": [512, "u", "u"]
}




pzt_d = {
    "self": [0, "u", "1"],
    "cmin": [23, "u", "u"],
    "cmax": [22, "u", "u"],
    "p": [24, "f", "1"],
    "i": [25, "f", "1"],
    "d": [26, "f", "1"],
    "adelay": [39, "u", "1"],
    "offset": [27, "i", "u"],
    "rate": [41,"u","u"],
    "park": [21, "u", "u"],
    "dpota_cr": [8, "u", "1"],
    "dpota_amp": [11, "u", "1"],
    "dpotb_cr": [15, "u", "1"],
    "dpotb_amp": [18, "u", "1"],
    "clp_cr": [1, "u", "1"],
    "clp_amp": [4, "u", "1"],
    "clp_ci":[0, "f", "1"],
    "lockm": [42, "u", "1"],
    "min":[29, "u", "u"],
    "max":[28, "u", "u"],
    "minm":[29, "u", "u"],
    "maxm":[28, "u", "u"],
    "minsl":[12, "u", "u"],
    "maxsl":[13, "u", "u"],
    "maxwp":[35, "i", "u"],
    "minwp":[34, "i", "u"],
    "clpt":[36, "u", "1"]
}


lock_mech=["LEV", "MIH", "EDGE_UP", "EDG_P_UP", "EDGE_DW", "EDG_P_DW"]

lock_dict={
    5: "EDGE_UP",
    1: "LEV",
    3: "MIH",
    13: "EDG_P_UP",
    21: "EDGE_DW",
    29: "EDG_P_DW",
    "EDGE_UP": 5,
    "LEV": 1,
    "MIH": 3,
    "EDG_P_UP": 13,
    "EDGE_DW":21,
    "EDG_P_DW": 29
}

opm_mech=["Slow", "Fast", "Slow & PARK", "Fast & PARK", "Off"]

opm_dict={
    "02": "Slow",
    "22": "Fast",
    "12": "Slow & PARK",
    "32": "Fast & PARK",
    "00": "Off",

    "Slow": "02",
    "Fast": "22",
    "Slow & PARK": "12",
    "Fast & PARK": "32",
    "Off":"00",

}

lh={
    "serial": [8,"u","1"],
    "date": [5,"u","1"],
    "power": [9,"u","1"],
    "wavelength": [6,"u","1"],
    "model": [7,"u","1"]
}


ld={
    "act": [Globals.ld_act, "u", "u"],
    "clp_error": [41, "i", "u"]
}


ld_d={  "curr": [1, "u", "u"],
        "dc": [0, "u", "u"],
        "cl": [4, "u", "u"],
        "cerror": [5, "u", "u"],
        "delay": [7,"u","1"],
        "clp_enable": [8,"u","1"],
        "clp_target": [9,"u","u"],
        "clp_repeat": [12,"u","1"],
        "clp_step": [13,"i","u"],
        "clp_constant_I": [11, "f", "1"],
        "clp_constant_P": [14, "f", "1"],
        "clp_constant_M": [10, "f", "1"],
        "clp_ldmax": [15, "u", "1"]
          }

gui = {

    "low":[0, "u", "u"],
    "high":[1, "u", "u"],
    "modell":[2, "s", "1"],
    "tec0":[3, "s", "1"],
    "tec1":[4, "s", "1"],
    "tec2":[5, "s", "1"],
    "tec3":[6, "s", "1"],
    "pzt0":[7, "s", "1"],
    "pzt1":[8, "s", "1"],
    "cb":[9, "s", "1"],
    "lh":[10, "s", "1"],
    "ldr":[11, "s", "1"],
    "trial":[12, "u", "1"],
    "start":[13, "t", "1"],
    "dur":[14, "t", "1"],
    "ban": [15, "u", "1"],
    "shift_enable": [17, "u", "1"],
    "shift_step": [18, "i", "1"],
    "shift_serial": [19, "u", "1"],
    "shift_threshold": [20, "u", "u"],
    "shift_count": [21, "u", "1"],
    "shift_position": [22, "i", "1"],
    "shift_mincurrent": [23, "u", "u"],
    "opm_setting": [24, "u", "u"],
    "opm_target": [25, "u", "u"]
}

rang = {

    "S": "Solo",
    "D": "Duetto",
    "Q": "Quartetto",
    "s": "Solo",
    "d": "Duetto",
    "q": "Quartetto"
}

indicator = {
    "write": "03FA",
    "read": "03FA",
    "tec": {
        "grey": 10,
        "amber": 16,
        "green": 17
    },
    "ld": {
        "grey": 0,
        "amber": 18,
        "green": 19
    },
    "pzt": {
        "grey": 1,
        "amber": 20,
        "green": 21
    },
    "power": {
        "off": "",
        "on": ""
    },
    "error": {
        "off": "",
        "on": ""
    },
    "ext": {
        "write": "03fa",
        "on": 4,
    },
    "full": {
        "write": "03fa",
        "on": 8,
    },
}

cb={
    "errornumber": [9, "u", "1"],
    "erroraddress":[8, "u", "1"]

}

fonts={

    "main": ("Jost Light", 10),
    "button": ("Proxima Nova Rg", 16),
    "mainbutton": ("Jost Regular", 20),
    "subbutton": ("Jost Regular", 12),
    "title": ("Jost Regular", 10),
    "detection": ("Proxima Nova Th", 11),
    "status": ("Jost Regular", 8),
    "indicator": ("Jost Regular", 8),
    "calibration": ("Proxima Nova Alt Lt", 7),
    "submit": ("Proxima Nova Rg", 6),
    "messages": ("Jost Light", 8),
    "model": ("Jost Regular", 20),
    "submodel": ("Jost Regular", 25),
    "actual": ("Jost Light", 9),
    "info":  ("Jost Light", 16, "italic"),
    "temperature": ("Jost Regular", 9),
    "temperature_b": ("Jost Regular", 10),
    "pzt_status": ("Jost Regular", 8),
    "copyright": ("Jost Light", 10)
}

DefaultNames={
    "low": 1.2,
    "high": 3.0,
    "modell": "s",
    "tec0": "TEC0",
    "tec1": "TEC1",
    "tec2": "TEC2",
    "tec3": "TEC3",
    "pzt0": "PZT0",
    "pzt1": "PZT1",
    "ldr": "LD",
    "cb": "CB",
    "lh": "LH",
    "wavelength": 640
}

Background={

    "main": "#F9F9F6",
    "submit": "#b2bec3",
    "alert": "#ffeaa7",
    "plot": "#0984e3"

}

Colours={

    #"red": "#d63032221",
    "red": "#D11C24",
    "amber": "#fdcb6e",
    #"green": "#00b894",
    "green": "#00874F",
    "orange": "#f39c12",
    "grey": "ghost white",
    "lightgrey": "#b2bec3",
    "darkgrey": "#636e72",
    "solo": "#262626",
    "white": "#ecf0f1",
    "darkred": "#b33939",
    "black": "#2f3640"
}

Calibration={

    "cb": ("dump","ref_voltage"),
    "lh": ("dump",""),
    "ld": ("ld_current","ld_voltage"),
    "tec0": ("tec_current","tec_voltage","thermistor"),
    "tec1": ("tec_current","tec_voltage","thermistor"),
    "tec2": ("tec_current","tec_voltage","thermistor"),
    "tec3": ("tec_current","tec_voltage"),
    "pzt0": ("pzt_voltage","diff_pd","cop_diode"),
    "pzt1": ("pzt_voltage","diff_pd","cop_diode")

}

subCalibration=["dump", "ref_voltage", "ld_current", "ld_voltage", "tec_current", "tec_voltage", "thermistor", "pzt_voltage", "diff_pd", "cop_diode"]

error={
    "address": "03f6",
    "0":"Unknown errors",
    "-1":"Module not installed",
    "-2":"Module communication error",
    "-3":"Unknown command",
    "-4":"Command queue full",
    "-5":"Overflow error",
    "-6":"Parameter out of range",
    "-7":"Control bit set failed",
    "-8":"Set ignored",
    "-13":"Communications with LH failed",
    "-14":"Error during LH initialization",
    "-15":"LH type do not match DB, or LH is not programmed",
    "-16":"Error during digital potentiometer setting",
    "-17":"TEC0 communications with driver failed",
    "-18":"TEC0 driver do not meet specified requirements or not programmed",
    "-19":"TEC0 driver Initialization error",
    "-20":"TEC0 driver error",
    "-21":"TEC0 driver regulation error, can not handle temperature mode with current settings",
    "-22":"TEC0 hardware error, can not ensure required output current",
    "-23":"TEC0 start-up temperature is out of range",
    "-24":"TEC1 communications with driver failed",
    "-25":"TEC1 driver do not meet specified requirements or not programmed",
    "-26":"TEC1 driver Initialization error",
    "-27":"TEC1 driver error",
    "-28":"TEC1 driver regulation error, can not handle temperature mode with current settings",
    "-29":"TEC1 hardware error, can not ensure required output current",
    "-30":"TEC1 start-up temperature is out of range",
    "-31":"TEC2 communications with driver failed",
    "-32":"TEC2 driver do not meet specified requirements or not programmed",
    "-33":"TEC2 driver Initialization error",
    "-34":"TEC2 driver error",
    "-35":"TEC2 driver regulation error, can not handle temperature mode with current settings",
    "-36":"TEC2 hardware error, can not ensure required output current",
    "-37":"TEC2 start-up temperature is out of range",
    "-38":"TEC3 communications with driver failed",
    "-39":"TEC3 driver do not meet specified requirements or not programmed",
    "-40":"TEC3 driver Initialization error",
    "-41":"TEC3 driver error",
    "-42":"TEC3 driver regulation error, can not handle temperature mode with current settings",
    "-43":"TEC3 hardware error, can not ensure required output current",
    "-44":"TEC3 start-up temperature is out of range",
    "-45":"CB communication error",
    "-46":"CB misstamth error - incorrect CB module, or it is not programmed",
    "-47":"CB VREF is out of range",
    "-48":"CB 0.5VREF is out of range",
    "-49":"CB initialization error",
    "-50":"PZT0 communication error",
    "-51":"PZT0 driver is not matching requirements or not programmed",
    "-52":"PZT0 initialization error",
    "-53":"PZT0 CLP level is out of range",
    "-54":"PZT0 locking timeout",
    "-55":"PZT0 HW error",
    "-56":"PZT0 driver error",
    "-57":"PZT1 communication error",
    "-58":"PZT1 driver is not matching requirements or not programmed",
    "-59":"PZT1 initialization error",
    "-60":"PZT1 CLP level is out of range",
    "-61":"PZT1 locking timeout",
    "-62":"PZT1 HW error",
    "-63":"PZT1 driver error",
    "-64":"LD communication error",
    "-65":"LD driver do not match requirements",
    "-66":"LD initialization error",
    "-67":"LD general error",
    "-68":"LD hardware error, set and actual currents do not match",
    "-69":"LD output level error, module can not ensure voltage drop on regulation element",
    "-70":"Interlock error",
    "-71":"Mode error"

}

def getNames():
    # with open('dict/Names.json') as f:
    #     Names = json.load(f)
    return Globals.Names

# with open('dict/Names.json') as f:
#     Names = json.load(f)
#
# with open('dict/Info.json') as f:
#     Info = json.load(f)
