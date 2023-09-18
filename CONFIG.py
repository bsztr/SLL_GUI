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
    "tec0": ["1000", "tec"],
    "tec1": ["1100", "tec"],
    "tec2": ["1200", "tec"],
    "tec3": ["1300", "tec"],
    "tec4": ["1400", "tec"],
    "tec5": ["1500", "tec"],
    "tec0_d": ["1000", "tec_d"],
    "tec1_d":["1100","tec_d"],
    "tec2_d":["1200","tec_d"],
    "tec3_d":["1300","tec_d"],
    "tec4_d": ["1400", "tec_d"],
    "tec5_d": ["1500", "tec_d"],
    "pzt0":["2000","pzt"],
    "pzt1":["2100","pzt"],
    "pzt0_d":["2000","pzt_d"],
    "pzt1_d":["2100","pzt_d"],
    "lh":["4000","lh"],
    "ld_d": ["3000","ld_d"],
    "ld": ["3000","ld"],
    "cb":["1000","cb"],
    "gui": ["4000", "gui"],
    "dphd": ["5000", "dphd"]
}

status = {
    "address": "0002",
    "STATUS_OK": 0,
    "TEC_WARMING_UP": 1,
    "TEC_READY": 2,
    "LD_OK": 3,
    "LD_WARMING_UP": 4,
    "LD_STABLE": 5,
    "PZT_0_PARK": 6,
    "PZT_0_RAMP": 7,
    "PZT_0_Locking": 9,
    "PZT_0_Tuning": 8,
    "PZT_0_Locked": 10,
    "PZT_1_PARK": 11,
    "PZT_1_RAMP": 12,
    "PZT_1_Locking": 14,
    "PZT_1_Tuning": 13,
    "PZT_1_Locked": 15,
    "ERROR": 18
}

control={
    "address":"0000",
    "full": 0,
    "ext": 0,
    "tec0": 0,
    "tec1": 1,
    "tec2": 2,
    "tec3": 3,
    "tec4": 4,
    "tec5": 5,
    "pzt0": 6,
    "pzt1": 7,
    "ld": 8,
    "pzt0_park": 9,
    "pzt0_ramp": 10,
    "pzt0_tune": 11,
    "pzt0_lock": 12,
    "pzt1_park":13,
    "pzt1_ramp": 14,
    "pzt1_tune": 15,
    "pzt1_lock": 16,
    "reset_errors": 19
}

dphd = {
    "dpot0": [0,"u","1"],
    "dpot1": [1,"u","1"],
    "dpot2": [2,"u","1"],
    "dpot3": [3,"u","1"],
    "dpot4": [4,"u","1"],
    "dpot5": [5,"u","1"]
}

activate={
    "address": "0001",
    "CB": 0,
    "LH": 0,
    "tec0": 1,
    "tec1": 2,
    "tec2":4,
    "tec3":8,
    "tec4":16,
    "tec5": 32,
    "pzt0":64,
    "pzt1":128,
    "ldr":256,
}

mod_check = {

    "tec0": 0,
    "tec1": 1,
    "tec2":2,
    "tec3":3,
    "tec4":4,
    "tec5": 5,
    "pzt0":6,
    "pzt1":7,
    "ldr":8,

}


tec = {
    "fw": [2305, "u", "1"],
    "current": [80, "f", "1"],
    "req current": [80, "f", "1"],
    "set": [2, "f", "1"],
    "act": [82, "f", "1"]
}



tec_d= {
    "maxc": [0, "u", "1"],
    "maxv": [1, "u", "1"],
    "warm":[7,"u","1"],
    "set": [2, "f", "1"],
    "p": [4, "f", "1"],
    "i": [5, "f", "1"],
    "d": [6, "f", "1"],
    "maxt": [10, "f", "1"],
    "mint": [9, "f", "1"]

}


pzt = {
    "fw": [2305, "u", "1"],
    "parkv": [83, "u", "1"],
    "livev": [82, "u", "1"],
    "clp_power": [84, "f", "1"],
    "dp_power": [80, "u", "1"],
    "ov": [82, "u", "m"],
    "id": [1, "u", "1"],
    "dphd": [1, "u", "1"],
    "clp": [1, "u", "1"],
    "v0": [1, "u", "1"],
    "nrd": [1, "u", "1"],
    "nrc": [1, "u", "1"],
    "nrv": [1, "u", "1"],
    "wploc": [1, "u", "1"],
    "dpot0": [80, "u", "1"],
    "dpot1": [81, "u", "1"],
    "dpot2": [84, "f", "1"],
    "tune_enable": [13, "u", "1"],
    "tune_module": [14, "u", "1"],
    "display_signal": [15, "u", "1"],
    "clp_cal": [16, "f", "1"],
    "tune_threshold": [17, "u", "1"],
    "tune_normal_step": [18, "f", "1"],
    "tune_large_step": [19, "f", "1"],
    "tune_delay": [20, "u", "1"]
}




pzt_d = {
    "self": [1, "u", "1"],
    "cmin": [1, "u", "u"],
    "cmax": [1, "u", "u"],
    "p": [2, "f", "1"],
    "i": [3, "f", "1"],
    "d": [4, "f", "1"],
    "adelay": [10, "u", "1"],
    "offset": [1, "u", "1"],
    "rate": [5,"f","1"],
    "park": [9, "u", "1"],
    "dpota_cr": [1, "u", "1"],
    "dpota_amp": [1, "u", "1"],
    "dpotb_cr": [1, "u", "1"],
    "dpotb_amp": [1, "u", "1"],
    "clp_cr": [1, "u", "1"],
    "clp_amp": [1, "u", "1"],
    "clp_ci":[1, "u", "1"],
    "lockm": [1, "u", "1"],
    "min":[84, "u", "1"],
    "max":[85, "u", "1"],
    "minm":[11, "u", "m"],
    "maxm":[12, "u", "m"],
    "minsl":[1, "u", "1"],
    "lockmode":[8, "u", "1"],
    "maxwp":[1, "u", "1"],
    "minwp":[1, "u", "1"],
    "clpt":[1, "u", "1"]
}


lock_mech=["DIFFERENTIAL", "DIVISION", "MICHELSON"]

lock_dict={
    0: "DIFFERENTIAL",
    1: "DIVISION",
    2: "MICHELSON",
    "DIFFERENTIAL": 0,
    "DIVISION": 1,
    "MICHELSON": 2
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
    "serial": [0,"u","1"],
    "date": [1,"u","1"],
    "power": [2,"u","1"],
    "wavelength": [3,"u","1"],
    "model": [4,"u","1"]
}


ld={
    "fw": [2305, "u", "u"],
    "act": [82, "u", "u"],
    "curr": [80, "u", "u"],
    "clp_error": [1, "u", "1"],
    "opm_low": [8, "u", "1"],
    "opm_high": [9, "u", "1"],
    "opm_target": [10, "u", "1"],
    "opm_enable": [14, "u", "1"],
    "opm_period": [11, "u", "1"],
    "opm_init": [12, "u", "1"],
    "opm_step": [13, "u", "1"],
    "opm_threshold": [15, "f", "1"],
    "opm_large_threshold": [16, "f", "1"],
    "opm_large": [17, "u", "1"],
    "Kp": [1, "u", "1"]
}


ld_d={  "curr": [0, "u", "u"],
        "dc": [1, "u", "1"],
        "cl": [2, "u", "u"],
        "cerror": [1, "u", "1"],
        "delay": [4,"u","1"],
        "clp_enable": [1,"u","1"],
        "clp_target": [1,"u","1"],
        "clp_repeat": [1,"u","1"],
        "clp_step": [1,"u","1"],
        "clp_constant_I": [1, "u", "1"],
        "clp_constant_P": [1, "u", "1"],
        "clp_constant_M": [1, "u", "1"],
        "clp_ldmax": [1, "u", "1"]
          }

gui = {

    "low":[256, "u", "u"],
    "high":[257, "u", "u"],
    "modell":[258, "s", "1"],
    "tec0":[259, "u", "1"],
    "tec1":[260, "u", "1"],
    "tec2":[261, "u", "1"],
    "tec3":[262, "u", "1"],
    "tec4": [263, "u", "1"],
    "tec5": [264, "u", "1"],
    "pzt0":[265, "u", "1"],
    "pzt1":[266, "u", "1"],
    "pzt2": [267, "u", "1"],
    "pzt3": [268, "u", "1"],
    "ldr": [269, "u", "1"],
    "dpot0": [270, "u", "1"],
    "dpot1": [271, "u", "1"],
    "dpot2": [20482, "u", "1"],
    "dpot3": [20483, "u", "1"],
    "dpot4": [20484, "u", "1"],
    "dpot5": [20485, "u", "1"],
    "cb":[1, "u", "1"],
    "lh":[1, "u", "1"],

    "trial":[1, "u", "1"],
    "start":[1, "u", "1"],
    "dur":[1, "u", "1"],
    "ban": [1, "u", "1"],
    "shift_enable": [1, "u", "1"],
    "shift_step": [1, "u", "1"],
    "shift_serial": [1, "u", "1"],
    "shift_threshold": [1, "u", "1"],
    "shift_count": [1, "u", "1"],
    "shift_position": [1, "u", "1"],
    "shift_mincurrent": [1, "u", "1"],
    "opm_setting": [1, "u", "1"],
    "opm_target": [1, "u", "1"],
    "lock_tune": [1,"u","1"],
    "tec_tune": [1,"u","1"],
    "dphd_thres": [1,"u","1"],
    "lock_timer": [1,"u","1"],
    "pid_timer": [1,"u","1"],
    "tec3_pid": [1,"u","1"],
    "tec2_pid": [1,"u","1"],
    "tec1_pid": [1, "u", "1"],
    "tec0_pid": [1, "u", "1"],
    "tec_tune_ic":[1,"u","1"],
    "tec_tune_ramp":[1,"u","1"]
}

rang = {


    "Q": "QT",
    "q": "QT",
    "n": "NX",
    "N": "NX",
    "m": "NX mini",
    "M": "NX mini"
}

indicator = {
    "write": "0000",
    "read": "0002",
    "tec": {
        "grey": 0,
        "amber": 1,
        "green": 2
    },
    "ld": {
        "grey": 0,
        "amber": 4,
        "green": 5
    },
    "pzt0": {
        "grey": 0,
        "amber": 6,
        "blue": 7,
        "lightgreen": 8,
        "orange": 9,
        "green": 10
    },
    "pzt1": {
        "grey": 0,
        "amber": 11,
        "blue": 12,
        "lightgreen": 13,
        "orange": 14,
        "green": 15
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

    "main": ("Calibri Light", 10),
    "button": ("Calibri", 16),
    "mainbutton": ("Calibri", 20),
    "subbutton": ("Calibri", 12),
    "title": ("Calibri Bold", 10),
    "detection": ("Calibri Light", 11),
    "status": ("Calibri", 8),
    "indicator": ("Calibri", 8),
    "calibration": ("Proxima Nova Alt Lt", 7),
    "submit": ("Calibri", 6),
    "messages": ("Arial", 8),
    "model": ("Calibri", 20),
    "submodel": ("Calibri", 25),
    "actual": ("Jost Light", 9),
    "info":  ("Jost Light", 16, "italic"),
    "temperature": ("Jost Regular", 9),
    "temperature_b": ("Jost Regular", 10),
    "pzt_status": ("Jost Regular", 8),
    "copyright": ("Calibri Light", 10)
}

DefaultNames={
    "low": 1.2,
    "high": 3.0,
    "modell": "s",
    "tec0": "TEC0",
    "tec1": "TEC1",
    "tec2": "TEC2",
    "tec3": "TEC3",
    "tec4": "TEC4",
    "tec5": "TEC5",
    "pzt0": "PZT0",
    "pzt1": "PZT1",
    "pzt2": "PZT2",
    "pzt3": "PZT3",
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
    "lightgreen": "#1dd1a1",
    "green": "#00874F",
    "orange": "#f39c12",
    "grey": "ghost white",
    "lightgrey": "#b2bec3",
    "darkgrey": "#636e72",
    "blue": '#2e86de',
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
