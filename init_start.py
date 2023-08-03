import time
import tkinter as tk
from COMM import setvalue, getvalue, comm_start, comm_init, comm_reset, getbit, readbit
from CONFIG import *
import threading
import queue
from tkinter import ttk
from Convert import sci, desci
from datetime import datetime
import ctypes
from tkinter.messagebox import askyesnocancel
import re

def runinit():
    return init_window('System is initialising...', lambda: time.sleep(1))

def hex2dec(b, rel):
    return hex(int(b,16)-int(rel,16))[2:]

def disp(b, rel):
    return getvalue(hex(int(base[b][0],16)-(eval(base[b][1])[rel][0]))[2:])['value']

def getaddress(b, rel):
    return hex(int(base[b][0],16)+(eval(base[b][1])[rel][0]))[2:]

def iteradr(b, rel, incr):
    result = int(base[b][0],16) - int(incr)
    return hex(result - (eval(base[b][1])[rel][0]))[2:]

def retrieve(instance):
    input=instance.get("1.0", 'end-1c')
    input=input.upper()
    if "E" in input:
        input=desci(input)
    else:
        input=float(input)
    return input

def submit(self, b, rel, thresh = "", min = "", max = ""):
    instance=eval("self.t_"+rel)
    label=eval("self.s_"+rel)
    arg1=eval(base[b][1])[rel][1]
    arg2=eval(base[b][1])[rel][2]
    if min == "" and max == "":
        exc=setvalue(getaddress(b,rel), retrieve(instance), arg1, arg2)
        if exc['success'] == 1:
            val = getvalue(getaddress(b, rel), arg1, arg2)['value']
            if abs(val) < 0.02:
                if val != 0:
                    val = sci(val)
            else:
                val = round(val, 3)
            label.configure(text=val)
        else:
            label.configure(text="error")
    else:
        vall = retrieve(instance)

        if vall > min and vall < max:
            exc = setvalue(getaddress(b, rel), retrieve(instance), arg1, arg2)
            if exc['success'] == 1:
                val = getvalue(getaddress(b, rel), arg1, arg2)['value']
                if abs(val) < 0.02:
                    if val != 0:
                        val = sci(val)
                else:
                    val = round(val, 3)
                label.configure(text=val)
        else:
            label.configure(text = "Out of limit")

    if thresh != "":
        exec("Globals." + thresh + " = " + str(retrieve(instance)))
        exec("Globals." + thresh + "_main = " + str(retrieve(instance)))

def submit_r(self, b, rel, min, max):

    instance=eval("self.t_"+rel)
    label=eval("self.s_"+rel)
    # arg1=eval(base[b][1])[rel][1]
    # arg2=eval(base[b][1])[rel][2]
    arg1="u"
    arg2="1"
    if retrieve(instance) >= min and retrieve(instance) <= max:
        exc=setvalue(getaddress(b,rel), retrieve(instance), arg1, arg2)
        if exc['success']==1:
            val=getvalue(getaddress(b,rel),arg1,arg2)['value']
            if abs(val) < 0.02:
                if val != 0:
                    val=sci(val)
            else:
                val=round(val,3)
            label.configure(text=val)
        else:
            label.configure(text="error")
    else:
        label.configure(text="not in range")

def submit_r_q(self, b, rel, min, max):
    instance=int(retrieve(eval("self.t_"+rel)))
    instance2 = int(retrieve(eval("self.tt_"+rel)))
    label=eval("self.s_"+rel)
    arg1=eval(base[b][1])[rel][1]
    arg2=eval(base[b][1])[rel][2]
    if instance >= min and instance <= max and instance2 >= min and instance2 <= max:

        first = "%02x" % instance
        second = "%02x" % instance2
        result = "0x0000" + first + second

        exc=setvalue(getaddress(b,rel), result, "1", "1")

        if exc['success']==1:
            val=getvalue(getaddress(b,rel),"1","1")['value']
            val2 = int(val[-4:-2], 16)
            val1 = int(val[-2:], 16)
            resultant = round(16*((val1*78.125)/(val2*78.125+470)),2)
            label.configure(text=str(val1) + "," + str(val2) + "," + str(resultant))
        else:
            label.configure(text="error")
    else:
        label.configure(text="not in range")

def retrieve_r_q(b, rel, label, pzt="analogue"):
    if pzt == "analogue":
        val = getvalue(getaddress(b, rel), "1", "1")['value']
        val2 = int(val[-4:-2], 16)
        val1 = int(val[-2:], 16)
        resultant = round(16*((val1*78.125)/(val2*78.125+470)),2)
        result=str(val1) + "," + str(val2) + "," + str(resultant)
    elif pzt == "quantum":
        val = getvalue(getaddress(b, rel), "u", "1")['value']
        result = val
    else:
        result = "error"
    label.configure(text=result, fg=Colours['darkgrey'], font=fonts['status'],
                        bg=Background['main'])

def retrieve_gui(instance, type="s"):
    input=instance.get("1.0", 'end-1c')
    if type == "f":
        input = float(input)
        return input
    else:
        return input

def submit_gui(self, b, rel, type="s"):
    instance=eval("self.t_"+rel)
    target = retrieve_gui(instance, type)
    label=eval("self.s_"+rel)
    arg1=eval(base[b][1])[rel][1]
    arg2=eval(base[b][1])[rel][2]
    exc=setvalue(getaddress(b,rel), target, arg1, arg2)

    if exc['success']==1:
        val=getvalue(getaddress(b,rel),arg1,arg2)['value']
        label.configure(text=val)
    else:
        label.configure(text="error")
    Globals.Names[rel] = target
    # f = open("dict/Names.json", "w+")
    # f.write(json.dumps(Names))
    # f.close()

def reset(self, b, rel):
    label=eval("self.s_"+rel)
    arg1=eval(base[b][1])[rel][1]
    arg2=eval(base[b][1])[rel][2]
    exc=setvalue(getaddress(b,rel), 4294967295, "u", "1")
    if exc['success']==1:
        label.configure(text=getvalue(getaddress(b,rel),arg1,arg2)['value'])
    else:
        label.configure(text="error")

def getmodules():
    global tec
    global pzt
    global ld
    result=comm_init()
    rem="*'b."
    for i in rem:
        result = result.replace(i, "")
    result = result.replace("\\r ", "\\r")
    result = result.replace("\\r\\r", "\\r")
    result=result.replace("\\r", "\n")
    result=result.splitlines()
    modules=[]
    Globals.errorno = []
    print((result))
    for line in result:
        if "ok" in line or "failed" in line:
            modules.append(line.split())
        elif "ERR" in line:
            Globals.errorno =[int(s) for s in re.findall(r"-?\d+", line)]
        elif "control system" in line:
            Globals.fwver = line.split()[-1]
            referencedate = fwdate = datetime.strptime("09122019", "%d%m%Y")
            try:
                fwdate = datetime.strptime(Globals.fwver[1:], "%d%m%Y")
            except:
                fwdate = datetime.strptime("09102022", "%d%m%Y")
            if fwdate > referencedate:
                Globals.newfw = 1
                Globals.tec_current = 896
                Globals.tec_reqcurrent = 897
                Globals.tec_set = 898
                Globals.tec_act = 899
                Globals.pzt_parkv = 897
                Globals.pzt_clppower = 896
                Globals.pzt_dp_power = 898
                Globals.pzt_ov = 899
                Globals.ld_act = 896
                tec = {
                    "current": [Globals.tec_current, "u", "u"],
                    "req current": [Globals.tec_reqcurrent, "i", "u"],
                    "set": [Globals.tec_set, "u", "k"],
                    "act": [Globals.tec_act, "u", "k"]
                }
                pzt = {
                    "parkv": [Globals.pzt_parkv, "u", "u"],
                    "clp_power": [Globals.pzt_clppower, "u", "u"],
                    "dp_power": [Globals.pzt_dp_power, "u", "u"],
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
                ld = {
                    "act": [Globals.ld_act, "u", "u"],
                    "curr": [26, "u", "u"],
                    "clp_error": [41, "i", "u"],
                    "Kp": [267, "f", "1"]
                }

    #modules = ["TEC0", "TEC1", "TEC2", "TEC3"]
    return modules

# def fw_verison():
#     if getvalue("bc7f", "1", "1")["value"] != "0xffffffff":
#         Globals.newfw = 1
#         print("new registers")
#     else:
#         Globals.newfw = 0
#         print("it worked")

def getnames_init():
    Names={}
    Names['low'] = getvalue(getaddress("gui", "low"), "u", "u")["value"]
    ###DPOT INIT
    dp0 = getvalue(getaddress("gui", "dpot0"))["value"]
    dp1 = getvalue(getaddress("gui", "dpot1"))["value"]
    if dp0 > 255:
        dp0 = 255
    if dp1 > 255:
        dp1 = 255
    setvalue(getaddress("dphd", "dpot0"),dp0)
    setvalue(getaddress("dphd", "dpot1"),dp1)

    ###LD INIT
    if Names['low'] > 4:
        Names['low'] = 2
        setvalue(getaddress("gui", "low"),Names["low"], "u", "u")
    Names['high'] = getvalue(getaddress("gui", "high"), "u", "u")["value"]

    if Names['high'] > 4:
        Names['high'] = getvalue(getaddress("ld_d", "curr"), "u", "u")["value"]
        if Names['high'] > 9:
            Names["high"] = 9
            setvalue(getaddress("gui", "high"), Names["high"], "u", "u")
        else:
            setvalue(getaddress("gui", "high"), Names["high"], "u", "u")
    Names['modell'] = getvalue(getaddress("gui", "modell"), "s", "1")["value"]
    Names['tec0'] = getvalue(getaddress("gui", "tec0"), "s", "1")["value"]
    Names['tec1'] = getvalue(getaddress("gui", "tec1"), "s", "1")["value"]
    Names['tec2'] = getvalue(getaddress("gui", "tec2"), "s", "1")["value"]
    Names['tec3'] = getvalue(getaddress("gui", "tec3"), "s", "1")["value"]
    Names['tec4'] = getvalue(getaddress("gui", "tec4"), "s", "1")["value"]
    Names['tec5'] = getvalue(getaddress("gui", "tec5"), "s", "1")["value"]
    Names['pzt0'] = getvalue(getaddress("gui", "pzt0"), "s", "1")["value"]
    Names['pzt1'] = getvalue(getaddress("gui", "pzt1"), "s", "1")["value"]
    Names['pzt2'] = getvalue(getaddress("gui", "pzt2"), "s", "1")["value"]
    Names['pzt3'] = getvalue(getaddress("gui", "pzt3"), "s", "1")["value"]
    Names['ldr'] = getvalue(getaddress("gui", "ldr"), "s", "1")["value"]
    Names['wavelength'] = getvalue(getaddress("lh", "wavelength"), "u", "1")["value"]


    for item in Names:
        if Names[item] == "Empty":
            Names[item] = DefaultNames[item]

    Globals.Names = Names
    # RPMC Fix for dpot setting
    # setvalue(getaddress("pzt0_d","dpota_cr"),11,"u","1")
    # setvalue(getaddress("pzt0_d", "dpota_amp"), 11, "u", "1")
    # setvalue(getaddress("pzt0_d", "dpotb_cr"), 10, "u", "1")
    # setvalue(getaddress("pzt0_d", "dpotb_amp"), 6, "u", "1")
    # setvalue(getaddress("pzt0_d", "clp_ci"), 1, "f", "1")
    # setvalue(getaddress("pzt0_d", "clp_cr"), 250, "u", "1")
    # setvalue(getaddress("pzt0_d", "clp_amp"), 251, "u", "1")
    ######

    # f = open("dict/Names.json", "w+")
    # f.write(json.dumps(Names))
    # f.close()

def diagnose():

    comm_start()
    full_active = activate["tec0"] + activate["tec1"] + activate["tec2"] + activate["tec3"] + activate["pzt0"] + activate["pzt1"] + activate["ldr"]
    preset = getvalue(activate["address"])["value"]
    setvalue(activate['address'], full_active)
    query = getmodules()

    while query[-1][-1] == "failed":
        remove = query[-1][-3].lower()
        setvalue(activate['address'], full_active - activate[remove])
        full_active = full_active - activate[remove]
        query = getmodules()

    available = []
    for item in query:
        available.append(item[0])
    setvalue(activate["address"], preset)
    comm_reset()
    #setvalue("03F6",0,"u","1")
    #print(available)
    return available


def init():

    comm_start()

    available = ["LH", "CB"]
    fwv = str(getvalue("0004", "u", "1")["value"])
    #setvalue("0001", 256, "u", "1")
    Globals.fwver = f"v{fwv[0]}.{fwv[1]}.{fwv[2]}"

    valu  = int(getvalue(activate["address"], "u", "1")["value"])

    for item in activate:
        if item != "address" and item != "LH" and item != "CB" and valu != 0:
            if readbit(valu, mod_check[item]) == "1":
                available.append(item.upper())
    getnames_init()
    print(available)


    # if Globals.shiftenabled > 0:
    #
    #     address = getaddress("gui", "shift_threshold")
    #     result = getvalue(address, "u", "u")["value"]
    #     Globals.shiftlimit = result
    #     address = getaddress("gui", "shift_mincurrent")
    #     result = getvalue(address, "u", "u")["value"]
    #     if result > 3e+6:
    #         result = 3e+6
    #     Globals.shiftmincurrent = result
    #     Globals.shiftldrange = Globals.shiftlimit - Globals.shiftmincurrent
    #     if Globals.shiftldrange < 0:
    #         Globals.shiftldrange = 0
    #
    #     Globals.opmsetting = getvalue(getaddress("gui", "opm_setting"), "u", "u")["value"]
    #     #print("opm set to", Globals.opmsetting)
    # #comm_reset()
    # #print(available)
    return available



def init_window(text, function):
        window = tk.Tk()
        window.geometry("400x100")
        window.title("Initialisation")
        message = tk.Label(window, text=text, font=("Helvetica", 20, "italic"))
        bar=ttk.Progressbar(window, orient=tk.HORIZONTAL, length=200)

        message.pack()
        bar.pack(pady=5)
        bar.config(mode="determinate", max=100, value=5)
        step=0

        queues = queue.Queue()

        def target_method(queue):
            modules = init()
            queue.put(modules)


        thread1 = threading.Thread(
            target=target_method,
            name="Main",
            args=[queues]
        )
        thread1.start()

        while thread1.is_alive():
            step = step + 8
            window.update()
            bar.step(step)
            time.sleep(4)

        thread1.join()
        available=queues.get()

        window.destroy()
        #available = init()
        return available
