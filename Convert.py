import struct
import binascii
import ctypes
import codecs
import datetime
import time
from decimal import Decimal

def uint2hex(hx):
    if isinstance(int(hx), int):
        if isinstance(hx, int):
            val = int(round(hx, 0))
        else:
            val=int(round(int(hx),0))
        val = ctypes.c_uint64(val).value
        val = "0x%08x" % val
    else:
        val=0
    return val

def hex2uint(hx):
    return int(hx,16)

def hex2hex(hx):
    return hx

def signed2hex(hx):
    # if isinstance(int(hx), int):
    #     if hx > 0:
    #         hx = int(round(hx, 0))
    #         # print(str(hx) + "this is hx")
    #         print("positive")
    #         #val = (hx << 16)+2
    #         val = -(hx - 2 ** 31)
    #         val = ctypes.c_uint32(val).value
    #         val = "0x%08x" % val
    #         return val
    #     else:
    #         hx = -int(round(hx, 0))
    #         #val=hx << 0
    #         val = (hx << 1) + 2
    #         val = ctypes.c_uint32(val).value
    #         val = "0x%08x" % val
    #         return val
    # else:
    #     val=0
    # return val
    if isinstance(hx, int):
        val = int(round(hx, 0))
    else:
        val = int(round(int(hx), 0))
    if val == 0:
        val = ctypes.c_uint32(val).value
        val= "0x%08x" % val
        return val
    else:
        #print(val)
        if val > 1:
            val = ctypes.c_uint32(val).value
            val = "0x%08x" % val
            #print(val)
        else:
            val=hex((1 << 32) + val)
        return val


def hex2signed(hx):

    val=int(hx,16)
    #print(val)
    val = ctypes.c_int32(val).value
    return val

def float2hex(hx):
    val=hex(struct.unpack('<I', struct.pack('<f', hx))[0])
    return val

def hex2float(hx):
    hx = int(hx, 16)
    hx = ctypes.c_uint32(hx).value
    hx = "0x%08x" % hx
    data=hx[2:]
    return struct.unpack('>f', binascii.unhexlify(data.replace(' ', '')))[0]

# def str2hex(hx):
#     result=binascii.hexlify(hx.encode())
#     return result

def hex2str(hx):
    if hx == "ffffffff":
        return "Empty"
    try:
        result=codecs.decode(hx[2:], "hex").decode("utf-8")
        result = result.strip("")
        result = result.replace(u"\u0000", "")
        result = result.replace(u"\x00", "")
        return result
    except UnicodeDecodeError:
        return "Empty"

def str2hex(strr):
    strr = binascii.hexlify(str(strr).encode()).decode("utf-8")
    hx = "0x%08x" % int(strr, 16)
    return hx

# def hex2str(hx):
#     if hx[2:] == "ffffffff":
#         result = "s"
#     else:
#         result = binascii.unhexlify(hx[2:]).decode('utf-8')
#     print(result + "this is the string")
#     return result

def time2hex(tim):
    tim=time.mktime(datetime.datetime.strptime(tim, "%Y%m%d").timetuple())
    tim = uint2hex(tim)
    return tim

def hex2time(hx):
    hx = hex2uint(hx)
    hx = datetime.datetime.utcfromtimestamp(hx).strftime("%Y%m%d")
    return hx

def kelvin(inte):
    result = round((inte / 10e+5) - 273.15,10)
    return result

def dekelvin(kelvin):
    result= int(round((float(kelvin)+273.15)*10e+5,10))
    return result

def micro(inte):
    result = round((inte/10e+5),10)
    return result

def int2hex4(hx):

        if isinstance(hx, int):

            val = int(round(hx, 0))
        else:
            val = int(round(int(hx), 0))
        if val == 0:
            val = ctypes.c_uint32(val).value
            val = "%04x" % val
            return val
        else:

            if val > 1:
                val = ctypes.c_uint32(val).value
                val = "%04x" % val
            else:
                # print(hex((1 << 32) + val))
                val = format((1 << 32) + val, '04x')[4:8]
                # val = hex((1 << 32) + val)[9:12]
                #print(format(float((1 << 32) + val), '04x'))
            return val


def demicro(micro):
    result=float(micro)
    result=result*10e+5
    result=int(round(result,10))
    #print(result)
    return result

def sci(val):
    return "{:.2E}".format(Decimal(val))

def desci(val):
    desc="{:.8f}".format(float(val))
    return float(desc)
