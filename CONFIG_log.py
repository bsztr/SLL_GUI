#3 data types: float, uint32 and int32, indicated by f,u,i as second element of tuple
#3 conversion factors: microKelvin, micro, one to one, indicated by k,u,1 as third element of tuple
#passing tuple as *tuple

import json
import Globals

tec = {
    "current": [Globals.tec_current, "u", "u"],
    "req current": [Globals.tec_reqcurrent, "u", "u"],
    "set": [Globals.tec_set, "u", "k"],
    "act": [Globals.tec_act, "u", "k"]
}

base_l = {
    "tec0_l": ["DFFF", "tecAddr"],
    "tec1_l": ["DBFF", "tecAddr"],
    "tec2_l": ["D7FF", "tecAddr"],
    "tec3_l": ["D3FF", "tecAddr"],
    "tec0_l_d": ["FFF5", "tec_d"],
    "tec1_l_d":["FFE1","tec_d"],
    "tec2_l_d":["FFCD","tec_d"],
    "tec3_l_d":["FFB9","tec_d"],
    "pzt0_l":["EFFF","pztAddr"],
    "pzt1_l":["EBFF","pztAddr"],
    "pzt0_d":["FF91","pztAddr_lh"],
    "pzt1_d":["FF66","pztAddr_lh"],
    "lh":["FFFF","lh"],
    "ld_d": ["FFA5","ld_d"],
    "ld": ["BFFF","ldAddr"],
    "cb":["03FF","cbAddr"],
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
    "tec0": 0,      # These were changed from original
    "tec1": 1,
    "tec2": 2,
    "tec3": 3,
    "pzt0": 4,
    "pzt1": 5,
    "ldr": 6,
    "dpot": "FFFD",
    "dpot0": 63,
    "dpot1": 4032
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
    "dp_power": [Globals.pzt_dp_power, "u", "u"],
    "id": [1, "s", "1"],
    "dphd": [770, "u", "1"],
    "clp": [773, "u", "1"],
    "v0": [776, "u", "1"],
    "nrd": [768, "u", "1"],
    "nrc": [771, "u", "1"],
    "nrv": [774, "u", "1"]
}




pzt_d = {
    "self": [0, "u", "1"],
    "cmin": [23, "u", "u"],
    "cmax": [22, "u", "u"],
    "p": [24, "f", "1"],
    "i": [25, "f", "1"],
    "d": [26, "f", "1"],
    "LH_PZTx_REG_TARGET_V": [27, "u", "u"],
    "adelay": [39, "u", "1"],
    "offset": [27, "i", "u"],
    "rate": [41,"u","u"],
    "LH_PZTx_MODE_BITS": [42, "u", "1"],
    "park": [21, "u", "u"],
    "dpota_cr": [8, "u", "1"],
    "dpota_amp": [11, "u", "1"],
    "dpotb_cr": [15, "u", "1"],
    "dpotb_amp": [18, "u", "1"],
    "clp_cr": [1, "u", "u"],
    "clp_amp": [4, "u", "u"],
    "clp_ci":[0, "f", "1"],
    "lockm": [42, "u", "1"],
    "min":[29, "u", "u"],
    "max":[28, "u", "u"]

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
    "act": [Globals.ld_act, "u", "u"],
}


ld_d={    "curr": [1, "u", "u"],
          "dc": [0, "u", "u"],
          "cl": [4, "u", "u"],
          "cerror": [5, "u", "u"],
          "delay": [7,"u","1"]
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
    "ban": [15, "u", "1"]
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

    "main": ("Proxima Nova Rg", 10),
    "button": ("Proxima Nova Rg", 16),
    "mainbutton": ("Proxima Nova Rg", 20),
    "subbutton": ("Proxima Nova Rg", 11),
    "title": ("Proxima Nova Bl", 10),
    "detection": ("Proxima Nova Th", 11),
    "status": ("Proxima Nova Alt Lt", 8),
    "indicator": ("Proxima Nova Alt Bl", 8),
    "calibration": ("Proxima Nova Alt Lt", 7),
    "submit": ("Proxima Nova Rg", 6),
    "messages": ("Proxima Nova Th", 8),
    "model": ("Proxima Nova Bl", 24, "italic"),
    "submodel": ("Proxima Nova Bl", 14, "italic"),
    "actual": ("Proxima Nova Th", 9),
    "info":  ("Proxima Nova Th", 16, "italic"),
    "temperature": ("Proxima Nova Rg", 9),
    "temperature_b": ("Proxima Nova Rg", 10),
    "pzt_status": ("Proxima Nova Rg", 8)
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

    "main": "#ffffff",
    "submit": "#b2bec3",
    "alert": "#ffeaa7",
    "plot": "#0984e3"

}

Colours={

    #"red": "#d63032221",
    "red": "#ff4d4d",
    "amber": "#fdcb6e",
    "green": "#00b894",
    "orange": "#f39c12",
    "grey": "ghost white",
    "lightgrey": "#b2bec3",
    "darkgrey": "#636e72",
    "solo": "#262626",
    "white": "#ecf0f1",
    "darkred": "#b33939"
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

# ======================================================================== #


cbAddr = {
    "REG_CB_STATUS": [0, "u", "1"],
    "REG_CB_ID": [1, "s", "1"],
    "REG_CB_SERIAL": [2, "u", "1"],
    "REG_CB_VREF": [3, "u", "u"],
    "REG_CB_05VREF": [4, "u", "u"],
    "REG_CB_SYSTEM_STATUS": [5, "u", "1"],
    "REG_CB_OUTPUT_STATE": [6, "u", "1"],
    "REG_CB_CONTROL_LINES": [7, "u", "1"],
    "REG_CB_WH_COUNTER": [8, "u", "1"],
    "REG_CB_NR_ERROR_LOG": [9, "u", "1"],
    "REG_CB_ERROR_RANGE_TOP": [10, "u", "1"]
}
tecAddr = {
    "REG_TECx_STATUS": [0, "u", "1"],
    "REG_TECx_ID": [1, "s", "1"],
    "REG_TECx_SERIAL": [2, "u", "1"],
    "REG_TECx_DRIVER_MAX_I": [3, "u", "u"],
    "REG_TECx_DRIVER_MAX_V": [4, "u", "u"],
    "REG_TECx_NTC_ABS_OFF": [5, "i", "u"],
    "REG_TECx_NTC_ABS_GCOR": [6, "f", "1"],
    "REG_TECx_NTC_VOLTAGE/REG_TECx_AT_VOLTAGE": [7, "u", "u"],
    "REG_TECx_CD_CURRENT": [8, "i", "u"],
    "REG_TECx_CD_VIRATE": [9, "f", "1"],
    "REG_TECx_CD_VOLTAGE": [10, "u", "u"],
    "REG_TECx_CD_ABS_OFF": [11, "i", "u"],
    "REG_TECx_CD_ABS_GCOR": [12, "f", "1"],
    "REG_TECx_VD_IVRATE": [13, "f", "1"],
    "REG_TECx_VD_ABS_OFF": [14, "i", "u"],
    "REG_TECx_VD_ABS_GCOR": [15, "f", "1"],
    "REG_TECx_CO_ABS_OFF": [16, "i", "u"],
    "REG_TECx_CO_ABS_GCOR": [17, "f", "1"],
    "REG_TECx_CO_IVRATE": [18, "f", "1"],
    "REG_TECx_OUT_CURRENT": [19, "u", "u"],
    "REG_TECx_TARGET_V/REG_TECx_SP_V": [20, "i", "u"],
    "REG_TECx_CB_VREF": [21, "u", "u"],
    "REG_TECx_CB_05VREF": [22, "u", "u"],
    "REG_TECx_CUR_ERR_THR/REG_TECx_REG_ERR_THR_V": [23, "u", "u"],
    "REG_TECx_REG_ERR_THR_S": [24, "u", "1"],
    "REG_TECx_STAB_THR_V": [25, "u", "u"],
    "REG_TECx_MAX_V": [26, "u", "u"],
    "REG_TECx_MAX_I": [27, "u", "u"],
    "REG_TECx_P": [28, "f", "1"],
    "REG_TECx_I": [29, "f", "1"],
    "REG_TECx_D": [30, "f", "1"],
    "REG_TECx_ACC_I": [31, "f", "u"],
    "REG_TECx_PID_ERROR": [32, "f", "u"],
    "REG_TECx_DIFF ": [33, "f", "u"],
    "REG_TECx_CURR_MIS_ACC": [34, "u", "u"],
    "REG_TECx_NTC_A": [35, "f", "1"],
    "REG_TECx_NTC_B ": [36, "f", "1"],
    "REG_TECx_NTC_C": [37, "f", "1"],
    "REG_TECx_NTC_BALAST": [38, "f", "1"],
    "REG_TECx_LH_VREF_OFF": [39, "i", "u"],
    "REG_TECx_NTC_AMP_OFF": [40, "i", "u"],
    "REG_TECx_NTC_AMP_GAIN": [41, "f", "1"],
    "REG_TECx_TARGET_T": [42, "u", "k"],
    "REG_TECx_CURRENT_T": [43, "u", "k"],
    "REG_TECx_STAB_THR_K": [44, "u", "k"],
    "REG_TECx_ERR_MIN_START_T": [45, "u", "k"],
    "REG_TECx_ERR_MAX_START_T": [46, "u", "k"],
    "REG_TECx_PRIORITY": [47, "u", "1"],
    "REG_TECx_DELAY": [48, "u", "1"],
    "REG_TECx_NTC_ABS_OFF_FLASH": [256, "i", "u"],
    "REG_TECx_NTC_ABS_GCOR_FLASH": [257, "f", "1"],
    "REG_TECx_CD_ABS_OFF_FLASH": [258, "i", "u"],
    "REG_TECx_CD_ABS_GCOR_FLASH": [259, "f", "1"],
    "REG_TECx_VD_ABS_OFF_FLASH": [260, "i", "u"],
    "REG_TECx_VD_ABS_GCOR_FLASH": [261, "f", "1"],
    "REG_TECx_CO_ABS_OFF_FLASH": [262, "i", "u"],
    "REG_TECx_CO_ABS_GCOR_FLASH": [263, "f", "1"],
    "REG_TECx_CD_VIRATE_FLASH": [264, "f", "1"],
    "REG_TECx_VD_IVRATE_FLASH": [265, "f", "1"],
    "REG_TECx_CO_IVRATE_FLASH": [266, "f", "1"],
    "REG_TECx_OUT_CURRENT_FIX": [896, "u", "u"],
    "REG_TECx_CD_CURRENT_FIX": [897, "u", "u"],
    "REG_TECx_TARGET_T_FIX": [898, "u", "k"],
    "REG_TECx_CURRENT_T_FIX": [899, "u", "k"],
    "REG_TECx_TARGET_V_FIX/REG_TECx_SP_V_FIX": [900, "u", "u"],
    "REG_TECx_NTC_VOLTAGE_FIX/REG_TECx_AT_VOLTAGE_FIX": [901, "u", "u"],

    "LH_TEC0_MAX_V": [-8182, "u", "u"],
    "LH_TEC1_MAX_V": [-9186, "u", "u"],
    "LH_TEC2_MAX_V": [-10190, "u", "u"]
}

ldAddr = {
    "REG_LD_STATUS": [0, "u", "1"],
    "REG_LD_ID": [1, "1", "1"],
    "REG_LD_CR32": [2, "u", "1"],
    "REG_LD_DRIVER_MAX_I": [3, "u", "u"],
    "REG_LD_DRIVER_MAX_V": [4, "u", "u"],
    "REG_LD_CO_ABS_OFF": [5, "u", "u"],
    "REG_LD_CO_ABS_GCOR": [6, "f", "1"],
    "REG_LD_CO_IVRATE": [7, "f", "1"],
    "REG_LD_CO_CURRENT": [8, "u", "u"],
    "REG_LD_CD_VIRATE": [9, "u", "u"],
    "REG_LD_CD_ABS_OFF": [10, "i", "u"],
    "REG_LD_CD_ABS_GCOR": [11, "f", "1"],
    "REG_LD_COC_IIRATE/REG_LD_COC_IVRATE": [12, "f", "1"],
    "REG_LD_COC_ABS_OFF": [13, "i", "u"],
    "REG_LD_COC_ABS_GCOR": [14, "i", "1"],
    "REG_LD_OV_ABS_OFF": [15, "i", "u"],
    "REG_LD_OV_ABS_GCOR": [16, "f", "1"],
    "REG_LD_OV_VOLTAGE": [17, "u", "u"],
    "REG_LD_ACCI_ERR": [18, "u", "u"],
    "REG_LD_CB_VREF": [19, "u", "u"],
    "REG_LD_CB_05VREF": [20, "u", "u"],
    "REG_LD_CUR_ERR_THR": [21, "u", "u"],
    "REG_LD_ERR_DCOV_MIN_V": [22, "u", "u"],
    "REG_LD_ERR_DCOV_TIME": [23, "u", "1"],
    "REG_LD_MAX_V": [24, "u", "u"],
    "REG_LD_MAX_I": [25, "u", "u"],
    "REG_LD_NOM_I": [26, "u", "u"],
    "REG_LD_Kp": [27, "f", "1"],
    "REG_LD_Ki": [28, "f", "1"],
    "REG_LD_Kd": [29, "f", "1"],
    "REG_LD_VTARGET": [30, "u", "u"],
    "REG_LD_DCOV": [31, "u", "u"],
    "REG_LD_PRIORITY": [32, "u", "1"],
    "REG_LD_DELAY": [33, "u", "1"],
    "REG_LD_LDV": [34, "u", "u"],
    "REG_LD_OP_MAINTAIN_TARGET": [35, "u", "u"],
    "REG_LD_OP_MAINTAIN_I_ACC": [36, "s", "u"],
    "REG_LD_OP_MAINTAIN_I_CONST": [37, "f", "u"],
    "REG_LD_OP_MAINTAIN_C_CONST": [38, "f", "1"],
    "REG_LD_OP_MAINTAIN_PERIOD": [39, "u", "1"],
    "REG_LD_OP_MAINTAIN_MODE_BITS": [40, "1", "1"],
    "REG_LD_OP_MAINTAIN_CORRECTION": [41, "1", "1"],
    "REG_LD_CO_ABS_OFF_FLASH": [256, "i", "u"],
    "REG_LD_CO_ABS_GCOR_FLASH": [257, "f", "1"],
    "REG_LD_CD_ABS_OFF_FLASH": [258, "i", "u"],
    "REG_LD_CD_ABS_GCOR_FLASH": [259, "f", "1"],
    "REG_LD_COC_ABS_OFF_FLASH": [260, "i", "u"],
    "REG_LD_COC_ABS_GCOR_FLASH": [261, "f", "1"],
    "REG_LD_OV_ABS_OFF_FLASH": [262, "i", "u"],
    "REG_LD_OV_ABS_GCOR_FLASH": [263, "f", "1"],
    "REG_LD_CO_IVRATE_FLASH": [264, "f", "1"],
    "REG_LD_CD_VIRATE_FLASH": [265, "f", "1"],
    "REG_LD_COC_IIRATE_FLASH/REG_LD_COC_IVRATE_FLASH": [266, "f", "1"],
    "REG_LD_Kp_FLASH": [267, "f", "1"],
    "REG_LD_Ki_FLASH": [268, "f", "1"],
    "REG_LD_Kd_FLASH": [269, "f", "1"],
    "REG_LD_VTARGET_FLASH": [270, "u", "u"],
    "REG_LD_CO_CURRENT_FIX": [896, "u", "u"],
    "REG_LD_OV_VOLTAGE_FIX": [897, "u", "u"],
    "REG_LD_LDV_FIX": [898, "u", "u"]
}


pztAddr = {
    "REG_PZTx_STATUS": [0, "u", "1"],
    "REG_PZTx_ID": [1, "s", "1"],
    "REG_PZTx_SERIAL": [2, "u", "1"],
    "REG_PZTx_DRIVER_MAX_V": [3, "u", "u"],
    "REG_PZTx_DRIVER_MIN_V": [4, "u", "u"],
    "REG_PZTx_DRIVER_MAX_CLOAD": [5, "u", "1"],
    "REG_PZTx_CLP_ABS_OFF": [6, "i", "u"],
    "REG_PZTx_CLP_ABS_GCOR": [7, "f", "1"],
    "REG_PZTx_CLP_VOLTAGE": [8, "u", "u"],
    "REG_PZTx_DPhD_ABS_OFF": [9, "i", "u"],
    "REG_PZTx_DPhD_ABS_GCOR": [10, "f", "1"],
    "REG_PZTx_DPhD_VOLTAGE": [11, "i", "u"],
    "REG_PZTx_OV": [12, "u", "u"],
    "REG_PZTx_OV_ABS_OFF": [13, "i", "u"],
    "REG_PZTx_OV_ABS_GCOR": [14, "f", "1"],
    "REG_PZTx_TARGET_V": [15, "i", "u"],
    "REG_PZTx_CB_VREF": [16, "u", "u"],
    "REG_PZTx_CB_05VREF": [17, "u", "u"],
    "REG_PZTx_CLP_ERR_MIN_V": [18, "u", "u"],
    "REG_PZTx_CLP_ERR_MAX_V": [19, "u", "u"],
    "REG_PZTx_CLP_ERR_TIME": [20, "u", "1"],
    "REG_PZTx_UNLOCK_MIN_WP_OFF/REG_PZTx_UNLOCK_LOW_V": [21, "i", "u"],
    "REG_PZTx_UNLOCK_MAX_WP_OFF/REG_PZTx_UNLOCK_HIGH_V": [22, "i", "u"],
    "REG_PZTx_CLPW_UNLOCK_TIME": [23, "u", "1"],
    "REG_PZTx_LOCKING_TIMEOUT": [24, "u", "1"],
    "REG_PZTx_MAX_V": [25, "u", "u"],
    "REG_PZTx_MIN_V": [26, "u", "u"],
    "REG_PZTx_PARK_V": [27, "u", "u"],
    "REG_PZTx_P": [28, "f", "1"],
    "REG_PZTx_I": [29, "f", "1"],
    "REG_PZTx_D": [30, "f", "1"],
    "REG_PZTx_LW_CLP_MIN": [31, "u", "u"],
    "REG_PZTx_LW_CLP_MAX": [32, "u", "u"],
    "REG_PZTx_UNLOCK_STEPAWAY": [33, "u", "u"],
    "REG_PZTx_RAMP_RATE": [34, "u", "u"],
    "REG_PZTx_CLP_CMP_REF": [35, "u", "u"],
    "REG_PZTx_DPhD_CMP_REF": [36, "u", "u"],
    "REG_PZTx_SLOPE_MIN": [37, "u", "1"],
    "REG_PZTx_SLOPE_MAX": [38, "u", "1"],
    "REG_PZTx_HV_O_ABS_GCOR": [39, "f", "1"],
    "REG_PZTx_HV_O_ABS_OFF": [40, "i", "u"],
    "REG_PZTx_CLP_CMP_REF_ABS_GCOR": [41, "f", "1"],
    "REG_PZTx_CLP_CMP_REF_ABS_OFF": [42, "i", "u"],
    "REG_PZTx_DPhD_CMP_REF_ABS_GCOR": [43, "f", "1"],
    "REG_PZTx_DPhD_CMP_REF_ABS_OFF": [44, "i", "u"],
    "REG_PZTx_TRG_OFF_ABS_GCOR": [45, "f", "1"],
    "REG_PZTx_TRG_OFF_ABS_OFF": [46, "i", "u"],
    "REG_PZTx_DPhD_P_ABS_GCOR": [47, "f", "1"],
    "REG_PZTx_DPhD_P_ABS_OFF": [48, "i", "u"],
    "REG_PZTx_DPhD_P_VOLTAGE": [49, "u", "u"],
    "REG_PZTx_CLP_IPRATE": [50, "u", "u"],
    "REG_PZTx_CLP_CR_DPOT": [51, "u", "1"],
    "REG_PZTx_CLP_AMP_DPOT": [52, "u", "1"],
    "REG_PZTx_DPhA_CR_DPOT": [53, "u", "1"],
    "REG_PZTx_DPhA_AMP_DPOT": [54, "u", "1"],
    "REG_PZTx_DPhB_CR_DPOT": [55, "u", "1"],
    "REG_PZTx_DPhB_AMP_DPOT": [56, "u", "1"],
    "REG_PZTx_CLP_PWR": [57, "u", "u"],
    "REG_PZTx_PRIORITY": [58, "u", "1"],
    "REG_PZTx_DELAY": [59, "u", "1"],
    "REG_PZTx_MODE_BITS": [60, "u", "1"],
    "REG_PZTx_CLP_ABS_OFF_FLASH": [256, "i", "u"],
    "REG_PZTx_CLP_ABS_GCOR_FLASH": [257, "f", "1"],
    "REG_PZTx_DPhD_ABS_OFF_FLASH": [258, "i", "u"],
    "REG_PZTx_DPhD_ABS_GCOR_FLASH": [259, "f", "1"],
    "REG_PZTx_OV_ABS_OFF_FLASH": [260, "i", "u"],
    "REG_PZTx_OV_ABS_GCOR_FLASH": [261, "f", "1"],
    "REG_PZTx_TRG_OFF_ABS_OFF_FLASH": [262, "i", "u"],
    "REG_PZTx_TRG_OFF_ABS_GCOR_FLASH": [263, "f", "1"],
    "REG_PZTx_DPhD_CMP_REF_ABS_OFF_FLASH": [264, "i", "u"],
    "REG_PZTx_DPhD_CMP_REF_ABS_GCOR_FLASH": [265, "f", "1"],
    "REG_PZTx_CLP_CMP_REF_ABS_OFF_FLASH": [266, "i", "u"],
    "REG_PZTx_CLP_CMP_REF_ABS_GCOR_FLASH": [267, "f", "1"],
    "REG_PZTx_HV_O_ABS_OFF_FLASH": [268, "i", "u"],
    "REG_PZTx_HV_O_ABS_GCOR_FLASH": [269, "f", "1"],
    "REG_PZTx_DPhD_P_ABS_OFF_FLASH": [270, "i", "u"],
    "REG_PZTx_DPhD_P_ABS_GCOR_FLASH": [271, "f", "1"],
    "WP registers start": [512, "n", "1"],
    "WP registers end": [761, "n", "1"],
    "REG_PZTx_DPhD_CNT": [768, "u", "1"],
    "REG_PZTx_DPhD_ADDR": [769, "u", "1"],
    "REG_PZTx_DPhD_READ": [770, "u", "u"],
    "REG_PZTx_CLP_CNT": [771, "u", "1"],
    "REG_PZTx_CLP_ADDR": [772, "u", "1"],
    "REG_PZTx_CLP_READ": [773, "u", "u"],
    "REG_PZTx_CLP_PWR_FIX": [896, "u", "u"],
    "REG_PZTx_PARK_V_FIX": [897, "u", "u"],
    "REG_PZTx_DPhD_VOLTAGE_FIX": [898, "u", "u"],
    "REG_PZTx_OV_FIX": [899, "u", "u"],
    "REG_PZTx_TARGET_V_FIX": [900, "i", "u"]
}

pztAddr_lh = {
    "LH_PZTx_CLP_IPRATE": [0, "f", "u"],
    "LH_PZTx_CLP_CR_DPOT": [1, "u", "1"],
    "LH_PZTx_CLP_AMP_DPOT": [4, "u", "1"],
    "LH_PZTx_DPHA_CR_DPOT": [8, "u", "1"],
    "LH_PZTx_CLP_CMP_REF": [9, "u", "u"],
    "LH_PZTx_CMP_REF": [10, "u", "u"],
    "LH_PZTx_DPHA_AMP_DPOT": [11, "u", "1"],
    "LH_PZTx_SLOPE_MIN": [12, "u", "u"],
    "LH_PZTx_SLOPE_MAX": [13, "u", "u"],
    "LH_PZTx_DPHB_CR_DPOT": [15, "u", "1"],
    "LH_PZTx_DPHB_AMP_DPOT": [18, "u", "1"],
    "LH_PZTx_PARK_V": [21, "u", "u"],
    "LH_PZTx_LCKWIN_MAX_V": [22, "u", "u"],
    "LH_PZTx_LCKWIN_MIN_V": [23, "u", "u"],
    "LH_PZTx_P": [24, "f", "1"],
    "LH_PZTx_I": [25, "f", "1"],
    "LH_PZTx_D": [26, "f", "1"],
    "LH_PZTx_REG_TARGET_V": [27, "i", "u"],
    "LH_PZTx_MAX_V": [28, "u", "u"],
    "LH_PZTx_MIN_V": [29, "u", "u"],
    "LH_PZTx_CLOAD": [30, "u", "u"],
    "LH_PZTx_CLP_ERR_MIN_V": [31, "u", "u"],
    "LH_PZTx_CLP_ERR_MAX_V": [32, "u", "u"],
    "LH_PZTx_CLP_ERR_TIME": [33, "u", "1"],
    "LH_PZTx_UNLOCK_MIN_WP_OFF": [34, "i", "u"],
    "LH_PZTx_UNLOCK_MAX_WP_OFF": [35, "i", "u"],
    "LH_PZTx_CLPW_UNLOCK_TIME": [36, "u", "1"],
    "LH_PZTx_LOCKING_TIMEOUT": [37, "u", "1"],
    "LH_PZTx_PRIORITY": [38, "u", "1"],
    "LH_PZTx_DELAY": [39, "u", "1"],
    "LH_PZTx_UNLOCK_STEPAWAY": [40, "u", "u"],
    "LH_PZTx_RAMP_RATE": [41, "u", "u"],
    "LH_PZTx_MODE_BITS": [42, "u", "1"]
}

tec_cal = ["REG_TECx_NTC_ABS_OFF",
           "REG_TECx_NTC_ABS_GCOR",
           "REG_TECx_CD_ABS_OFF",
           "REG_TECx_CD_ABS_GCOR",
           "REG_TECx_VD_ABS_OFF",
           "REG_TECx_VD_ABS_GCOR",
           "REG_TECx_CO_ABS_OFF",
           "REG_TECx_CO_ABS_GCOR",
           "REG_TECx_VD_IVRATE",
           "REG_TECx_CD_VIRATE",
           "REG_TECx_CO_IVRATE"]

pzt_cal = ["REG_PZTx_CLP_ABS_OFF",
            "REG_PZTx_CLP_ABS_GCOR",
            "REG_PZTx_DPhD_ABS_OFF",
            "REG_PZTx_DPhD_ABS_GCOR",
            "REG_PZTx_OV_ABS_OFF",
            "REG_PZTx_OV_ABS_GCOR",
            "REG_PZTx_TRG_OFF_ABS_OFF",
            "REG_PZTx_TRG_OFF_ABS_GCOR",
            "REG_PZTx_DPhD_CMP_REF_ABS_OFF",
            "REG_PZTx_DPhD_CMP_REF_ABS_GCOR",
            "REG_PZTx_CLP_CMP_REF_ABS_OFF",
            "REG_PZTx_CLP_CMP_REF_ABS_GCOR",
            "REG_PZTx_HV_O_ABS_OFF",
            "REG_PZTx_HV_O_ABS_GCOR",
            "REG_PZTx_DPhD_P_ABS_OFF",
            "REG_PZTx_DPhD_P_ABS_GCOR"]

ld_cal = ["REG_LD_CO_ABS_OFF",
          "REG_LD_CO_ABS_GCOR",
          "REG_LD_CD_ABS_OFF",
          "REG_LD_CD_ABS_GCOR",
          "REG_LD_COC_ABS_OFF",
          "REG_LD_COC_ABS_GCOR",
]