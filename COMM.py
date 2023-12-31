import serial
import re
import ctypes
from Convert import *
import Globals
import CONFIG
from serial.tools.list_ports import comports
global incident_error
from CONFIG import error
import importlib

available_ports=list(comports())
COMM_port = ""

for p in available_ports:
    if "USB Serial Port" in p.description:
        COMM_port = p.device

if COMM_port == "":
    raise EnvironmentError("Device not connected.")
COMport = COMM_port
ser = serial.Serial(
    #port=COMM_port,
    port=COMM_port,
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=1,
    bytesize=8,
    timeout=8
)

Globals.ser = ser

def init_COMM():
    available_ports = list(comports())
    COMM_port = ""

    for p in available_ports:
        if "USB Serial Port" in p.description:
            COMM_port = p.device

    if COMM_port == "":
        raise EnvironmentError("Device not connected.")

    Globals.ser = serial.Serial(
        port=COMM_port,
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=1,
        bytesize=8,
        timeout=5
    )

def stop_COMM():
    Globals.ser.close()

def getvalue(address, type="u", conv="1"):
    ser=Globals.ser
    if address[:2]=="0x" or address[:2]=="0X":
        address=address[2:]
    arg="0x"+str(address.lower())
    #print("GET$"+arg)
    ser.write((chr(13)+"GET$"+arg+chr(13)).encode())
    result = dict()
    reply = str(ser.read(31))
    #print(reply)
    hex = re.findall(r'0x[0-9A-F]+', reply, re.I)
    if "OK" in reply:
        result['success']=1
        if hex[0] == arg:
            result['valid'] = 1
        else:
            result['valid'] = 0
    else:
        result['success']=0
        result['valid']=0
        Globals.error=1
        code=str(re.search(r'-?(?:\d+,?)+', reply).group())
        if code == None:
            result['error']=error["-1"]
            result["errorn"]="-1"
        else:
            result['error']=error[code]
            Globals.error=1
            Globals.incident_errorn= code
            Globals.incident_error = result['error']
            result["errorn"] = code

    dtype = {
        'u': hex2uint,
        'i': hex2signed,
        'f': hex2float,
        '1': hex2hex,
        's': hex2str,
        't': hex2time
        }

    result['value']=dtype[type](hex[1])

    dconv ={
        'k': kelvin,
        'u': micro,
        '1': hex2hex,
        'm': mili
        }

    result['value'] = dconv[conv](result['value'])
    #print(result)
    return result

def getbit(address, bit):
    return bin(getvalue(address)['value']>>bit & 1)[2:]

def readbit(it, bit):
    return bin(it>>bit & 1)[2:]

def setvalue(address, val, type="u", conv="1"):
    global incident_error

    ser = Globals.ser

    dconv = {
        'k': dekelvin,
        'u': demicro,
        '1': hex2hex,
        'm': demili
        }

    val=dconv[conv](val)
    dtype = {
        'u': uint2hex,
        'i': signed2hex,
        'f': float2hex,
        '1': hex2hex,
        's': str2hex,
        't': time2hex
        }

    val=dtype[type](val)

    # val=ctypes.c_uint32(val).value
    # val="0x%08x" %val
    if address[:2]=="0x" or address[:2]=="0X":
         address=address[2:]
    #
    # if val[:2]=="0x" or val[:2]=="0X":
    #     val=val[2:]

    arg="0x"+str(address.lower())
    ser.write(("SET$"+arg+"$"+str(val)+chr(13)).encode())
    #print("SET$"+arg+"$"+str(val)+chr(13))
    result = dict()
    reply = str(ser.read(8))
    #print(reply)
    check=getvalue(address, type, conv)
    if check["success"]==1:
            result['success']=1
            result['value']=check['value']
    else:
            #Globals.incident_error=check["error"]
            #Globals.error=1
            result['value']="0"
            result['success']=0
    return result

def resvalue(address, value, arg1="u", arg2="1"):
    #print(value, "REM")
    target=getvalue(address, arg1, arg2)['value']-value
    #print(target)
    setvalue(address, target, arg1, arg2)

def addvalue(address, value, arg1="u", arg2="1"):
    #print(value, "ADD")
    target=getvalue(address, arg1, arg2)['value']+value
    #print(target)
    setvalue(address, target, arg1, arg2)

def comm_reset():
    ser = Globals.ser
    ser.reset_output_buffer()
    ser.write(("RST" + chr(13)).encode())
    # result=str(ser.read(800).decode())
    result = "OK"
    if"OK" in result:
        return "Reset complete"
    else:
        return "Error has occured"

def comm_init():
    ser = Globals.ser
    ser.reset_output_buffer()
    #ser.write(("RST" + chr(13)).encode())
    #reply = str(ser.read(800))
    reply = "OK"
    return reply

def comm_start():
    ser = Globals.ser
    ser.reset_output_buffer()
    reply = "OK"
    # val=8
    # address="03fa"
    # val=ctypes.c_uint32(val).value
    # val="0x%08x" %val
    # arg="0x"+str(address.lower())
    # ser.write(("SET$"+arg+"$"+val+chr(13)).encode())
    # reply = str(ser.read(800))
    return reply

def save_regs(mode="all"):
    if "tec" in mode:
        print("tec selected")
        address = ["1932"]
    elif "pzt" in mode:
        address = ["2932"]
    elif "ld" in mode:
        address = ["3932"]

    else:
        address = ["1932", "2932", "3932"]
    for item in address:
        val = "0x00000000"
        arg = "0x" + str(item.lower())
        ser.write(("SET$" + arg + "$" + str(val) + chr(13)).encode())
        result = dict()
        reply = str(ser.read(8))
    Globals.incident_message = mode.upper() + " registers are saved."
