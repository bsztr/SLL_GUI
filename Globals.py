global tec0
global tec1
global tec2
global tec3
global tec0_set
global tec1_set
global tec2_set
global tec3_set
global ld
global power
global tec
global ld_d
global pzt
global error
global error_disp
global error_count
global incident_error
global incident_error_n
global recorded_error
global incident_message
global recorded_message
global refresh
global tec0r
global tec1r
global tec2r
global tec3r
global pzt0r
global pzt1r
global ldrr
global cdr
global lhr
global modules
global available
global quit
global status_bit
global laser_off
global row
global rowtec
global clp_power
global Names
global subscription_off
global tec0_statusbit
global tec1_statusbit
global tec2_statusbit
global tec3_statusbit
global regoffset
global ramp_enabled
global ser
global disconnect
global engineer
global newfw
global guiver
global fwver

global tec_current
global tec_reqcurrent
global tec_set
global tec_act
global pzt_parkv
global pzt_clppower
global pzt_dp_power
global pzt_ov
global ld_act
global logoff
global logfile
global errorno
global pztreset

fwver = "0"
guiver = "3.5.2"
#Fixed analogue pzt driver bugs.



####Firmware controls####

tec_current = 19
tec_reqcurrent = 8
tec_set = 42
tec_act = 43
pzt_parkv = 27
pzt_clppower = 58
pzt_dp_power = 11
pzt_ov = 12
ld_act = 8

serdo = object
stageon = 0
opmrunning = 0
runnning_PROC = []
Colours={

    "lightgrey": "#b2bec3"
}
logoff = 0
logfile = ""
errorno = ""
pztreset = 0

tec0_set=25
tec1_set=25
tec2_set=25
tec3_set=25
tec4_set = 25
tec5_set = 25
tec0_set_init=25
tec1_set_init=25
tec2_set_init=25
tec3_set_init=25
tec4_set_init = 25
tec5_set_init = 25

tec0 = [0,0]
tec1 = [0,0]
tec2 = [0,0]
tec3 = [0,0]
tec4 = [0,0]
tec5 = [0,0]
ld_d = [0,0]
shiftlimit = 4
shiftpopup = 0
shiftenabled = 0
shiftmincurrent = 0
shiftldrange = 0
shiftNOW = 0
opmsetting = 0
tec0threshold = 0
tec1threshold = 0
tec2threshold = 0
tec3threshold = 0
tec4threshold = 0
tec5threshold = 0
tec0threshold_main = 0
tec1threshold_main = 0
tec2threshold_main = 0
tec3threshold_main = 0
tec4threshold_main = 0
tec5threshold_main = 0

power=Colours['lightgrey']
tec=Colours['lightgrey']
ld=Colours['lightgrey']
pzt=Colours['lightgrey']
error=Colours['lightgrey']

laser_off = 0

error=""
error_disp=0
error_count = 0
incident_error=""
incident_errorn=""
recorded_error=""

incident_message=""
recorded_message=""
status_bit = 0


available=[]
modules=[]
row=6
rowtec=6

clp_power=""

Names={"tec0": "TEC0",
       "tec1": "TEC1",
       "tec2": "TEC2",
       "tec3": "TEC3",
       "tec4": "TEC4",
       "tec5": "TEC5",
       "ldr": "LD",
       "pzt0": "PZT0",
       "pzt1": "PZT1",
       "pzt2": "PZT2",
       "pzt3": "PZT3"
       }

refresh=0
Toplevel = 0
quit=0
subscription_off = 0

tec0r = 0
tec1r = 0
tec2r = 0
tec3r = 0
tec4r = 0
tec5r = 0
pzt0r = 0
pzt1r = 0
ldrr = 0
cbr = 0
lhr = 0

tec0_statusbit = 0
tec1_statusbit = 0
tec2_statusbit = 0
tec3_statusbit = 0
tec4_statusbit = 0
tec5_statusbit = 0

tec_stab = 0

regoffset0=0
regoffset1=0
pzt0type = 0
pzt1type = 0

ramp_enabled = 0

ser=""
disconnect =0
COMport = 0
disconnect_trigger = 0

engineer = 0
laser_turnhigh = 0

newfw = 0
engauth = 'ff36ebad45f301f1a56104defa235bdc66a8d984f3915eb23425fe1aede576b1'
