#3 data types: float, uint32 and int32, indicated by f,u,i as second element of tuple
#3 conversion factors: microKelvin, micro, one to one, indicated by k,u,1 as third element of tuple
#passing tuple as *tuple

import json

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
        "cb":["03FF","cb"]
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
        "tec0": 1,
        "tec1": 2,
        "tec2":4,
        "tec3":8,
        "pzt0":16,
        #"pzt0":32,
        "pzt1":32,
        "ld":64,
        "dpot": "FFFD",
        "dpot0": 63,
        "dpot1": 4032
}

tec = {
        "current": [19, "u", "u"],
        "set": [42, "u", "k"],
        "act": [43, "u", "k"]

}

tec_d= {
    "maxc": [1, "u", "u"],
    "maxv": [0, "u", "u"],
    "delay":[18,"u","1"],
    "set": [11, "u", "k"],
    "p": [2, "f", "1"],
    "i": [3, "f", "1"],
    "d": [4, "f", "1"]

}

pzt = {
    "cmin": [22, "u", "u"],
    "cmax": [23, "u", "u"],
    "p": [24, "f", "1"],
    "i": [25, "f", "1"],
    "d": [26, "f", "1"],
    "adelay": [39, "u", "1"],
    "offset": [27, "i", "u"],
    "rate": [41, "u", "u"],
    "park": [21, "u", "u"],
    "clp_power": [8, "u", "u"],
    "dp_power": [11, "u", "u"]
}

pzt_d = {

    "cmin": [23, "u", "u"],
    "cmax": [22, "u", "u"],
    "p": [24, "f", "1"],
    "i": [25, "f", "1"],
    "d": [26, "f", "1"],
    "adelay": [39, "u", "1"],
    "offset": [27, "i", "1"],
    "rate": [41,"u","u"],
    "park": [21, "u", "u"],
    "dpota_cr": [8, "u", "1"],
    "dpota_amp": [11, "u", "1"],
    "dpotb_cr": [15, "u", "1"],
    "dpotb_amp": [18, "u", "1"],
    #"clp_cr": [1, "u", "u"],
    #"clp_amp": [4, "u", "u"],
    "clp_ci":[0, "f", "1"],
    "lockm": [42, "u", "1"]

}

lock_mech=["MAN", "LEV", "MIH"]

lock_dict={
    0: "MAN",
    1: "LEV",
    3: "MIH",
    "MAN": 0,
    "LEV": 1,
    "MIH": 3
}

lh={
    "serial": [8,"u","1"],
    "date": [5,"u","1"],
    "power": [9,"u","1"],
    "wavelength": [6,"u","1"],
    "model": [7,"u","1"]
}

ld={
    "act": [8, "u", "u"],
    "alignment": 400000,
    "high": 3000000
}

ld_d={    "curr": [1, "u", "u"],
        "dc": [0, "u", "u"],
        "cl": [4, "u", "u"],
        "cerror": [5, "u", "u"],
        "delay": [7,"u","1"]
    }

indicator = {
    "write": "03FA",
    "read": "03FF",
    "tec": {
        "on": 1024,
        "grey": 26,
        "red": 25,
        "orange": 15,
        "green": 16,
    },
    "ld": {
        "on": 1,
        "red": 16,
        "orange": 17,
        "green": 18
    },
    "pzt": {
        "on": 2,
        "red": 18,
        "orange": 19,
        "green": 20
    },
    "power": {
        "red": 26,
        "orange": 25,
        "green": 16
    },
    "error": {
        "red": 26,
        "orange": 25,
        "green": 16
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

    "main": ("Proxima Nova Rg", 10),
    "button": ("Proxima Nova Rl", 16),
    "mainbutton": ("Proxima Nova Rl", 20),
    "subbutton": ("Proxima Nova Rl", 12),
    "title": ("Proxima Nova Bl", 10),
    "detection": ("Proxima Nova Th", 11),
    "status": ("Proxima Nova Alt Lt", 8),
    "indicator": ("Proxima Nova Alt Bl", 8),
    "calibration": ("Proxima Nova Alt Lt", 7),
    "submit": ("Proxima Nova Rg", 6),
    "messages": ("Proxima Nova Th", 8),
    "model": ("Proxima Nova Bl", 24, "italic"),
    "actual": ("Proxima Nova Th", 9),
    "info":  ("Proxima Nova Th", 16, "italic"),
    "temperature": ("Proxima Nova Rg", 9),
    "temperature_b": ("Proxima Nova Rg", 10)
}

# Names={
#
#     "tec0": "BP TEC",
#     "tec1": "NLC1 TEC",
#     "tec2": "NLC2 TEC",
#     "tec3": "LD TEC",
#     "pzt0": "PZT0",
#     "pzt1": "PZT1",
#     "ldr": "LD",
#     "cb": "CB",
#     "lh": "LH"
#
# }
#
# with open('dict/Names.json', 'w') as f:
#     json.dump(Names, f)


Background={

    "main": "#ffffff",
    "submit": "#b2bec3",
    "alert": "#ffeaa7",
    "plot": "#0984e3"

}



Colours={

    "red": "#d63031",
    "amber": "#fdcb6e",
    "green": "#00b894",
    "orange": "#f39c12",
    "grey": "ghost white",
    "lightgrey": "#b2bec3",
    "darkgrey": "#636e72",
    "solo": "#262626",
    "white": "#ecf0f1"
}

# with open('dict/Colours.json', 'w') as f:
#     json.dump(Colours, f)

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
# with open('dict/Calibration.json', 'w') as f:
#     json.dump(Calibration, f)

subCalibration=["dump", "ref_voltage", "ld_current", "ld_voltage", "tec_current", "tec_voltage", "thermistor", "pzt_voltage", "diff_pd", "cop_diode"]

# with open('dict/subCalibration.json', 'w') as f:
#     json.dump(subCalibration, f)

error={

    "0":"No errors",
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
    "-23":"TEC0 start-up temperature is our of range",
    "-24":"TEC1 communications with driver failed",
    "-25":"TEC1 driver do not meet specified requirements or not programmed",
    "-26":"TEC1 driver Initialization error",
    "-27":"TEC1 driver error",
    "-28":"TEC1 driver regulation error, can not handle temperature mode with current settings",
    "-29":"TEC1 hardware error, can not ensure required output current",
    "-30":"TEC1 start-up temperature is our of range",
    "-31":"TEC2 communications with driver failed",
    "-32":"TEC2 driver do not meet specified requirements or not programmed",
    "-33":"TEC2 driver Initialization error",
    "-34":"TEC2 driver error",
    "-35":"TEC2 driver regulation error, can not handle temperature mode with current settings",
    "-36":"TEC2 hardware error, can not ensure required output current",
    "-37":"TEC2 start-up temperature is our of range",
    "-38":"TEC3 communications with driver failed",
    "-39":"TEC3 driver do not meet specified requirements or not programmed",
    "-40":"TEC3 driver Initialization error",
    "-41":"TEC3 driver error",
    "-42":"TEC3 driver regulation error, can not handle temperature mode with current settings",
    "-43":"TEC3 hardware error, can not ensure required output current",
    "-44":"TEC3 start-up temperature is our of range",
    "-45":"CB communication erroor",
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


