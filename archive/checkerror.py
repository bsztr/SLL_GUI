# import tkinter as tk
# from tkinter import ttk
# import serial
# import re
# import ctypes
# import struct
# import binascii
# global message

message=""

Background={
            "main": "#ffffff",
            "submit": "#b2bec3",
            "green": "#00b894",
            "alert": "#00b894"

}

fonts={
        "main": ("Proxima Nova Rg", 10),
        "status": ("Proxima Nova Rg", 9),
        "message": ("Proxima Nova Rg", 12),
        "title": ("Proxima Nova Bl", 10),
        "submit": ("Proxima Nova Rg", 6)
}

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
        "cb":["3FF","cb"]
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

pzt_d = {

        "cmin": [23, "u", "u"],
        "cmax": [22, "u", "u"],
        "p": [24, "f", "1"],
        "i": [25, "f", "1"],
        "d": [26, "f", "1"],
        "delay": [39, "u", "1"],
        "offset": [27, "i", "1"],
        "rate": [41,"u","u"],
        "park": [21, "u", "u"],
        "dpota_cr": [8, "u", "1"],
        "dpota_amp": [11, "u", "1"],
        "dpotb_cr": [15, "u", "1"],
        "dpotb_amp": [18, "u", "1"],
        "clp_ci":[0, "f", "1"],
        "mih":  [42, "u", "1"]
}

pzt = {
    "rate": [41, "u", "u"],
    "park": [21, "u", "u"],
    "clp_power": [8, "u", "u"]
}


ser = serial.Serial(
    port="COM4",
    baudrate=57600,
    parity=serial.PARITY_NONE,
    stopbits=1,
    bytesize=8,
    timeout=5
)

def float2hex(hx):
    val=hex(struct.unpack('<I', struct.pack('<f', hx))[0])
    return val

def hex2float(hx):
    hx = int(hx, 16)
    hx = ctypes.c_uint32(hx).value
    hx = "0x%08x" % hx
    data=hx[2:]
    return struct.unpack('>f', binascii.unhexlify(data.replace(' ', '')))[0]

def uint2hex(hx):
    if isinstance(int(hx), int):
        if isinstance(hx, int):
            val = int(round(hx, 0))
        else:
            val=int(round(int(hx),0))
        val = ctypes.c_uint32(val).value
        val = "0x%08x" % val
    else:
        val=0
    return val

def hex2uint(hx):
    return int(hx,16)

def hex2hex(hx):
    return hx

def micro(inte):
    result = round((inte/10e+5),2)
    return result

def demicro(micro):
    result=micro*10e+5
    result=int(round(result,4))
    return result

def signed2hex(hx):
    if isinstance(int(hx), int):
        hx=int(round(hx,0))
        val=hex((1 << 32) + hx)
    else:
        val=0
    return val

def hex2signed(hx):

    value = int(hx, 16)

    if value & (1 << (32 - 1)):
        value -= 1 << 32
    return value

def getaddress(b, rel):
    return hex(int(base[b][0], 16) - (eval(base[b][1])[rel][0]))[2:]

def getvalue(address, type="u", conv="1"):
    arg="0x"+str(address.lower())
    ser.write(("GET$"+arg+chr(13)).encode())
    result = dict()
    reply = str(ser.read(29))
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

    dtype = {
        'u': hex2uint,
        'i': hex2signed,
        'f': hex2float,
        '1': hex2hex
        }
    result['value']=dtype[type](hex[1])

    dconv ={
        'u': micro,
        '1': hex2hex
        }

    result['value'] = dconv[conv](result['value'])

    return result

def setvalue(address, val, type="u", conv="1"):

    dconv = {
        'u': demicro,
        '1': hex2hex
        }

    val=dconv[conv](val)

    dtype = {
        'u': uint2hex,
        'i': signed2hex,
        'f': float2hex,
        '1': hex2hex
        }

    val=dtype[type](val)

    if address[:2]=="0x" or address[:2]=="0X":
         address=address[2:]

    arg="0x"+str(address.lower())
    ser.write(("SET$"+arg+"$"+val+chr(13)).encode())
    result = dict()
    reply = str(ser.read(7))
    if "OK" in reply:
        check=getvalue(address, type, conv)

        #Need to work out data type
        result['value']=check["value"]
        #Need to convert to user defined value
        result['success']=1
        message_trigger("Parameters updated.\n", True)

    else:
        result['value']="error"
        result['success']=0
        message_trigger("An error has occured.\n", True)


    return result

def resvalue(address, value):
    target=getvalue(address)['value']-value
    setvalue(address, target)

def getbit(address, bit):
    return bin(getvalue(address)['value']>>bit & 1)[2:]

def readbit(it, bit):
    return bin(it>>bit & 1)[2:]

# def comm_start():
#     ser.reset_output_buffer()
#     val=8
#     address="03fa"
#     val=ctypes.c_uint32(val).value
#     val="0x%08x" %val
#     arg="0x"+str(address.lower())
#     ser.write(("SET$"+arg+"$"+val+chr(13)).encode())
#     reply = str(ser.read(7))
#     return reply

def comm_init(first=False):
    setvalue("03fa", "0x00000008", "1", "1")
    ser.reset_output_buffer()
    ser.write(("RST" + chr(13)).encode())
    reply = str(ser.read(400).decode())
    setvalue("03fa", "00000000")
    if first==False:
        message_trigger("System reinitialised.\n", True)
    else:
        message_trigger("System initialised.\n", True)
    return reply

def reset():
    target="ffffffff"
    if hex(getvalue("ffa0")['value'])[2:]!=target:
        setvalue("03fa", "00000008")
        setvalue("ffa0", target)
        setvalue("03fa", "00000000")

def read(rel, status):
    #setvalue("03fa", "00000008")
    address=getaddress("pzt0_d", rel)
    arg1=eval(base["pzt0_d"][1])[rel][1]
    arg2=eval(base["pzt0_d"][1])[rel][2]
    result=round(getvalue(address, arg1, arg2)['value'],2)
    status.configure(text=result)
    message_trigger("System initialised.\n", True)
    #setvalue("03fa", "00000000")

def read_delay(rel, status):
    #setvalue("03fa", "00000008")
    address="ff9e"
    arg1="u"
    arg2="1"
    result=round(getvalue(address, arg1, arg2)['value'],2)
    status.configure(text=result)
    message_trigger("System initialised.\n", True)
    #setvalue("03fa", "00000000")

def read_lh(rel, status):
    #setvalue("03fa", "00000008")
    address = getaddress("pzt0", rel)
    arg1 = eval(base["pzt0"][1])[rel][1]
    arg2 = eval(base["pzt0"][1])[rel][2]
    result = round(getvalue(address, arg1, arg2)['value'],3)
    status.configure(text=result)
    status.after(2000, lambda: read_lh(rel, status))
    #setvalue("03fa", "00000000")

def submit(rel, input, status):
    setvalue("03fa", "00000008")
    target=getaddress("pzt0_d", rel)
    val=float(input.get("1.0", 'end-1c'))


    arg1=eval(base["pzt0_d"][1])[rel][1]
    arg2=eval(base["pzt0_d"][1])[rel][2]
    result=setvalue(target, val, arg1, arg2)
    setvalue("03fa", "00000000")
    status.configure(text=round(result["value"],2))

def submit_delay(input, status):
    setvalue("03fa", "00000008")
    target="ff9e"
    val=float(input.get("1.0", 'end-1c'))
    arg1="u"
    arg2="1"
    result=setvalue(target, val, arg1, arg2)
    setvalue("03fa", "00000000")
    status.configure(text=round(result["value"],2))

def relock():
    setvalue("03fa", "00000008")
    l_disclaimer.configure(text="")
    bit=getvalue("03FF")["value"]
    print(bit)
    if readbit(bit, 18) == "1":
        if readbit(bit, 19) == "1":
            actual = getvalue(control['address'])['value']
            if readbit(actual, 1) == "1":
                #resvalue(control['address'], control["pzt0_m"])
                #setvalue(control['address'], actual + control["pzt0_l"])
                setvalue(base["pzt0_d"][0], 1073741824)
                message_trigger("Relock initiated.\n", True)
            else:
                setvalue("03fa", "00000000")
                message_trigger("Turn key to lock position.\n", True)
    else:
        #setvalue("03fa", "00000000")
        message_trigger("Please turn key to lock position.\n", True)


def message_trigger(input, unique=False):
    global message
    if unique == False:
        message=message+input
    else:
        message=input

def read_message(status):
    global message
    status.configure(text=message.upper())
    status.after(1500, lambda: read_message(status))

def geths(parent):
        hs = ttk.Separator(parent, orient=tk.HORIZONTAL)
        return hs

# def check_key(gui):
#
#     gui.withdraw()
#     win=tk.Toplevel()
#     l_info=tk.Label(win, text="Check key is in middle position. Press OK to continue.")
#     l_info.pack()
#     b_confirm=tk.Button(win, text="OK", command=win.destroy)
#     b_confirm.pack()
#     gui.wait_window(win)
#     gui.update()
#     gui.deiconify()

comm_init(True)

gui = tk.Tk()
gui.geometry("285x635")
gui.title("UniKLasers check error")
gui.configure(bg=Background['main'])

pady=2
y=1
based="random"

Unik = tk.PhotoImage(file="unik.png")
l_unik = tk.Label(image=Unik, bg=Background['main'])
l_ver = tk.Label(gui, text="v 0.01", font=fonts['main'], bg=Background['main'])

l_title = tk.Label(text="PZT0 setttings", font=fonts['title'], bg=Background['main'])

disclaimer="Ensure key is in the middle position (warm-up)."
l_disclaimer = tk.Label(gui, text=disclaimer,font=fonts['main'], bg=Background['main'])
l_message_s=tk.Label(gui, text="Status:",font=fonts['title'], bg=Background['main'])
l_message=tk.Label(gui, text="",font=fonts['status'], bg=Background['main'])
read_message(l_message)

l_p = tk.Label(gui, text="P gain", font=fonts['main'], bg=Background['main'])
t_p = tk.Text(gui, width=6, height=1)
s_p = tk.Label(gui, text="", font=fonts['main'], bg=Background['main'])
read("p", s_p)
b_p = tk.Button(gui, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                     command=lambda: submit("p", t_p, s_p))

l_i = tk.Label(gui, text="I gain", font=fonts['main'], bg=Background['main'])
t_i = tk.Text(gui, width=6, height=1)
s_i = tk.Label(gui, text="", font=fonts['main'], bg=Background['main'])
read("i", s_i)
b_i = tk.Button(gui, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                     command=lambda: submit("i", t_i, s_i))

l_d = tk.Label(gui, text="D gain", font=fonts['main'], bg=Background['main'])
t_d = tk.Text(gui, width=6, height=1)
s_d = tk.Label(gui, text="", font=fonts['main'], bg=Background['main'])
read("d", s_d)
b_d = tk.Button(gui, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                     command=lambda: submit("d", t_d, s_d))

l_cmin = tk.Label(gui, text="Lock window, min (V)", font=fonts['main'], bg=Background['main'])
t_cmin = tk.Text(gui, width=6, height=1)
s_cmin = tk.Label(gui, text="", font=fonts['main'], bg=Background['main'])
read("cmin", s_cmin)
b_cmin = tk.Button(gui, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                        command=lambda: submit("cmin",t_cmin, s_cmin))

l_cmax = tk.Label(gui, text="Lock window, max (V)", font=fonts['main'], bg=Background['main'])
t_cmax = tk.Text(gui, width=6, height=1)
s_cmax = tk.Label(gui, text="", font=fonts['main'], bg=Background['main'])
read("cmax", s_cmax)
b_cmax = tk.Button(gui, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                        command=lambda: submit("cmax", t_cmax, s_cmax))

l_offset = tk.Label(gui, text="Reg offset (V)", font=fonts['main'], bg=Background['main'])
t_offset = tk.Text(gui, width=6, height=1)
s_offset = tk.Label(gui, text="", font=fonts['main'], bg=Background['main'])
read("offset", s_offset)
b_offset = tk.Button(gui, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                          command=lambda: submit("offset", t_offset, s_offset))

l_adelay = tk.Label(gui, text="Activation delay (s)", font=fonts['main'], bg=Background['main'])
t_adelay = tk.Text(gui, width=6, height=1)
s_adelay = tk.Label(gui, text="", font=fonts['main'], bg=Background['main'])
read_delay("delay", s_adelay)
b_adelay = tk.Button(gui, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                          command=lambda: submit_delay(t_adelay, s_adelay))

l_difftitle=tk.Label(gui, text="Diff Photodiode Settings", font=fonts['title'], bg=Background['main'])

l_dpota_cr = tk.Label(gui, text="Diff A Input(0 to 255)", font=fonts['main'], bg=Background['main'])
t_dpota_cr = tk.Text(gui, width=6, height=1)
s_dpota_cr = tk.Label(gui, text="", font=fonts['main'], bg=Background['main'])
read("dpota_cr", s_dpota_cr)
b_dpota_cr = tk.Button(gui, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                            command=lambda: submit("dpota_cr", t_dpota_cr, s_dpota_cr))

l_dpota_amp = tk.Label(gui, text="Diff A Gain(0 to 255)", font=fonts['main'], bg=Background['main'])
t_dpota_amp = tk.Text(gui, width=6, height=1)
s_dpota_amp = tk.Label(gui, text="", font=fonts['main'], bg=Background['main'])
read("dpota_amp", s_dpota_amp)
b_dpota_amp = tk.Button(gui, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                             command=lambda: submit("dpota_amp", t_dpota_amp, s_dpota_amp))

l_dpotb_cr = tk.Label(gui, text="Diff B Input(0 to 255)", font=fonts['main'], bg=Background['main'])
t_dpotb_cr = tk.Text(gui, width=6, height=1)
s_dpotb_cr = tk.Label(gui, text="", font=fonts['main'], bg=Background['main'])
read("dpotb_cr", s_dpotb_cr)
b_dpotb_cr = tk.Button(gui, width=3, height=1, text="OK", font=fonts['submit'],
                            bg=Background['submit'],
                            command=lambda: submit("dpotb_cr", t_dpotb_cr, s_dpotb_cr))

l_dpotb_amp = tk.Label(gui, text="Diff B Gain(0 to 255)", font=fonts['main'], bg=Background['main'])
t_dpotb_amp = tk.Text(gui, width=6, height=1)
s_dpotb_amp = tk.Label(gui, text="", font=fonts['main'], bg=Background['main'])
read("dpotb_amp", s_dpotb_amp)
b_dpotb_amp = tk.Button(gui, width=3, height=1, text="OK", font=fonts['submit'],
                             bg=Background['submit'],
                             command=lambda: submit("dpotb_amp", t_dpotb_amp, s_dpotb_amp))

l_clptitle = tk.Label(gui, text="CLP Photodiode Settings", font=fonts['title'], bg=Background['main'])

l_clp_ci = tk.Label(gui, text="CLP V-I Conversion", font=fonts['main'], bg=Background['main'])
t_clp_ci = tk.Text(gui, width=6, height=1)
s_clp_ci = tk.Label(gui, text="", font=fonts['main'], bg=Background['main'])
read("clp_ci", s_clp_ci)
b_clp_ci = tk.Button(gui, width=3, height=1, text="OK", font=fonts['submit'],
                          bg=Background['submit'],
                          command=lambda: submit("clp_ci", t_clp_ci, s_clp_ci))

l_clp_power = tk.Label(gui, text="CLP Power (W)", font=fonts['main'], bg=Background['main'])
s_clp_power = tk.Label(gui, text="", font=fonts['main'], bg=Background['main'])
read_lh("clp_power", s_clp_power)

l_mih = tk.Label(gui, text="Lock status", font=fonts['main'], bg=Background['main'])
t_mih = tk.Text(gui, width=6, height=1)
s_mih = tk.Label(gui, text="", font=fonts['main'], bg=Background['main'])
read("mih", s_mih)
b_mih = tk.Button(gui, width=3, height=1, text="OK", font=fonts['submit'],
                          bg=Background['submit'],
                          command=lambda: submit("mih", t_mih, s_mih))

b_reinit=tk.Button(gui, text="Reinitialise system", command=lambda: comm_init(), font=fonts['main'], bg=Background['submit'])

l_unik.grid(row=0, column=1, columnspan=2, sticky="nw", pady=2)
l_ver.grid(row=0, column=3, columnspan=2, sticky="wsen", pady=2, padx=3)

geths(gui).grid(row=2, column=1, columnspan=5, sticky="nwse", pady=pady*2)
l_title.grid(row=3, column=y, columnspan=2, sticky="nw", pady=pady)
l_p.grid(row=4, column=y, columnspan=1, sticky="nw", pady=pady)
t_p.grid(row=4, column=y + 1, columnspan=1, sticky="nw", pady=pady)
s_p.grid(row=4, column=y + 2, columnspan=1, sticky="nesw", pady=pady)
b_p.grid(row=4, column=y + 3, columnspan=1, sticky="nwse", pady=pady)
l_i.grid(row=5, column=y, columnspan=1, sticky="nw", pady=pady)
t_i.grid(row=5, column=y + 1, columnspan=1, sticky="nw", pady=pady)
s_i.grid(row=5, column=y + 2, columnspan=1, sticky="nesw", pady=pady)
b_i.grid(row=5, column=y + 3, columnspan=1, sticky="nswe", pady=pady)
l_d.grid(row=6, column=y, columnspan=1, sticky="nw", pady=pady)
t_d.grid(row=6, column=y + 1, columnspan=1, sticky="nw", pady=pady)
s_d.grid(row=6, column=y + 2, columnspan=1, sticky="nesw", pady=pady)
b_d.grid(row=6, column=y + 3, columnspan=1, sticky="nswe", pady=pady)
l_cmin.grid(row=7, column=y, columnspan=1, sticky="nw", pady=pady)
t_cmin.grid(row=7, column=y + 1, columnspan=1, sticky="nw", pady=pady)
s_cmin.grid(row=7, column=y + 2, columnspan=1, sticky="nsew", pady=pady)
b_cmin.grid(row=7, column=y + 3, columnspan=1, sticky="nwse", pady=pady)
l_cmax.grid(row=8, column=y, columnspan=1, sticky="nw", pady=pady)
t_cmax.grid(row=8, column=y + 1, columnspan=1, sticky="nw", pady=pady)
s_cmax.grid(row=8, column=y + 2, columnspan=1, sticky="nesw", pady=pady)
b_cmax.grid(row=8, column=y + 3, columnspan=1, sticky="wnse", pady=pady)
l_offset.grid(row=9, column=y, columnspan=1, sticky="nw", pady=pady)
t_offset.grid(row=9, column=y + 1, columnspan=1, sticky="nw", pady=pady)
s_offset.grid(row=9, column=y + 2, columnspan=1, sticky="nwes", pady=pady)
b_offset.grid(row=9, column=y + 3, columnspan=1, sticky="nswe", pady=pady)
l_adelay.grid(row=10, column=y, columnspan=1, sticky="nw", pady=pady)
t_adelay.grid(row=10, column=y + 1, columnspan=1, sticky="nw", pady=pady)
s_adelay.grid(row=10, column=y + 2, columnspan=1, sticky="nesw", pady=pady)
b_adelay.grid(row=10, column=y + 3, columnspan=1, sticky="nwse", pady=pady)
l_mih.grid(row=11, column=1, columnspan=1, sticky="nwse", pady=pady*2)
t_mih.grid(row=11, column=2, columnspan=1, sticky="nwse", pady=pady*2)
s_mih.grid(row=11, column=3, columnspan=1, sticky="nwse", pady=pady*2)
b_mih.grid(row=1, column=4, columnspan=1, sticky="nwse", pady=pady*2)

geths(gui).grid(row=12, column=1, columnspan=5, sticky="nwse", pady=2*pady)

l_difftitle.grid(row=13, column=y, columnspan=4, sticky="nw", pady=pady)
l_dpota_cr.grid(row=14, column=y, columnspan=1, sticky="nw", pady=pady)
t_dpota_cr.grid(row=14, column=y + 1, columnspan=1, sticky="nw", pady=pady)
s_dpota_cr.grid(row=14, column=y + 2, columnspan=1, sticky="nesw", pady=pady)
b_dpota_cr.grid(row=14, column=y + 3, columnspan=1, sticky="nwse", pady=pady)
l_dpota_amp.grid(row=15, column=y, columnspan=1, sticky="nw", pady=pady)
t_dpota_amp.grid(row=15, column=y + 1, columnspan=1, sticky="nw", pady=pady)
s_dpota_amp.grid(row=15, column=y + 2, columnspan=1, sticky="esnw", pady=pady)
b_dpota_amp.grid(row=15, column=y + 3, columnspan=1, sticky="nsew", pady=pady)
l_dpotb_cr.grid(row=16, column=y, columnspan=1, sticky="nw", pady=pady)
t_dpotb_cr.grid(row=16, column=y + 1, columnspan=1, sticky="nw", pady=pady)
s_dpotb_cr.grid(row=16, column=y + 2, columnspan=1, sticky="nwes", pady=pady)
b_dpotb_cr.grid(row=16, column=y + 3, columnspan=1, sticky="nswe", pady=pady)
l_dpotb_amp.grid(row=17, column=y, columnspan=1, sticky="nw", pady=pady)
t_dpotb_amp.grid(row=17, column=y + 1, columnspan=1, sticky="nw", pady=pady)
s_dpotb_amp.grid(row=17, column=y + 2, columnspan=1, sticky="esnw", pady=pady)
b_dpotb_amp.grid(row=17, column=y + 3, columnspan=1, sticky="nwse", pady=pady)
geths(gui).grid(row=18, column=1, columnspan=5, sticky="nwse", pady=2*pady)

l_clptitle.grid(row=19, column=y, columnspan=4, sticky="nw", pady=pady)
l_clp_ci.grid(row=20, column=y, columnspan=1, sticky="nw", pady=pady)
t_clp_ci.grid(row=20, column=y + 1, columnspan=1, sticky="nw", pady=pady)
s_clp_ci.grid(row=20, column=y + 2, columnspan=1, sticky="nesw", pady=pady)
b_clp_ci.grid(row=20, column=y + 3, columnspan=1, sticky="nswe", pady=pady)
l_clp_power.grid(row=21, column=y, columnspan=1, sticky="nw", pady=pady)
s_clp_power.grid(row=21, column=y + 1, columnspan=3, sticky="nwes", pady=pady)
geths(gui).grid(row=22, column=1, columnspan=5, sticky="nwse", pady=2*pady)


l_disclaimer.grid(row=23, column=1, columnspan=4, sticky="w", pady=pady)
b_reinit.grid(row=24, column=1, columnspan=1, sticky="nse", pady=pady, padx=3)
l_message_s.grid(row=24, column=1, columnspan=4, sticky="nwse", pady=pady*5)
l_message.grid(row=25, column=2, rowspan=2, columnspan=3, sticky="nwse", pady=(pady*5,0))
geths(gui).grid(row=26, column=1, columnspan=5, sticky="nwse", pady=pady*2)

gui.mainloop()



