import tkinter as tk
from COMM import *
from CONFIG import *
import Globals
import time
import math
import numpy as np
from init_start import *
from tkinter.messagebox import askyesnocancel
from tkinter import messagebox
import pandas, os, sys, time
#import clr
#from LDPanel import compensation
import serial
from serial.tools.list_ports import comports

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS

        return base_path + relative_path
    except Exception:
        base_path = os.getcwd()

        return base_path + relative_path



# if Globals.shiftenabled == 1:
#
#     targetpath = resource_path(r"\DLLs")
#     sys.path.append(targetpath)
#     clr.AddReference("Thorlabs.MotionControl.DeviceManagerCLI")
#     clr.AddReference("Thorlabs.MotionControl.KCube.InertialMotorCLI")
#     clr.AddReference("System")
#     from Thorlabs.MotionControl.DeviceManagerCLI import DeviceManagerCLI
#     from Thorlabs.MotionControl.KCube.InertialMotorCLI import KCubeInertialMotor, InertialMotorStatus
#     from System import Decimal

class temp_label(tk.Label):
    def __init__(self, parent):
        tk.Label.__init__(self, parent)
        self.parent=parent
        self.threshold =""

    def update_temp(self, base, rel="act", loc="slot"):
        address=getaddress(base, rel)
        if loc == "slot":
            nd = ""
        else:
            nd = "_d"
        self.result = round(getvalue(address, eval("tec"+nd)[rel][1], eval("tec"+nd)[rel][2])['value'],2)
        exec("Globals." + base + "_set" + "= self.result")

        if loc == "slot":
            self.configure(text=str(self.result), fg=self.getcolour(self.result), font=fonts['status'], bg=Background['main'])
        else:
            self.configure(text=str(self.result), fg=Colours["black"], font=fonts['status'],bg=Background['main'])
        self.temp_timer = self.after(2500, lambda: self.update_temp(base, rel, loc))
        Globals.runnning_PROC.append(self.temp_timer)

    def update_temp_main(self, base, rel):
        if self.threshold == "":
            target = getaddress(base+"_d", "set")
            self.threshold = round(getvalue(target, "u", "k")['value'], 2)

        if eval("Globals." + base + "threshold_main" ) != 0:
            self.threshold = eval("Globals." + base + "threshold_main" )
            #print(self.threshold)
            exec("Globals." + base + "threshold_main = 0")

        address=getaddress(base, rel)
        self.result = round(getvalue(address, tec[rel][1], tec[rel][2])['value'], 2)
        self.colour=self.getcolour(self.result, base)
        self.configure(text=str(self.result) + " C", fg=self.colour, font=fonts['temperature_b'],
                       bg=Background['main'])
        self.timer=self.after(2000, lambda: self.update_temp_main(base, rel))
        Globals.runnning_PROC.append(self.timer)
        exec("Globals."+base + "=[ self.result, self.colour]")
        return

    def update_status(self, address, rel="", loc="slot"):
        if loc=="slot":
            nd=""
        else:
            nd="_d"
        self.result = round(getvalue(address, eval("tec"+nd)[rel][1], eval("tec"+nd)[rel][2])['value'], 2)
        self.configure(text=str(self.result), fg=Colours['darkgrey'], font=fonts['status'],
                       bg=Background['main'])
        #self.after(20000, lambda: self.update_status(address, rel))

    def readin_temp(self, bas):
        self.configure(text=eval("Globals."+bas)[0], fg=self.getcolour(eval("Globals."+bas)[0]), font=fonts['status'],
                       bg=Background['main'])
        if eval("Globals." + bas + "threshold" ) != 0:
            self.threshold = eval("Globals." + bas + "threshold" )
            exec("Globals." + bas + "threshold = 0")
        self.timer_panel = self.after(3000, lambda: self.readin_temp(bas))
        Globals.runnning_PROC.append(self.timer_panel)

    def stop_temp_main(self):
        self.configure(text="")
        self.after_cancel(self.timer)

    def getcolour(self, result, base = ""):
        if self.threshold != "":
            value =  float(self.threshold)

            if result > value - 0.35 and result<value + 0.35:
                return Colours['green']
            else:
                return Colours['red']
        else:
            return Colours["red"]

class ld_label(tk.Label):
    def __init__(self, parent):
        tk.Label.__init__(self, parent)
        self.parent=parent

    def update_ld_main(self, base, rel):

        address = getaddress(base, rel)
        self.result = round(getvalue(address, ld[rel][1], ld[rel][2])['value'], 2)
        self.colour = self.getcolour(self.result)
        self.configure(text=str(self.result) + " A", fg=self.getcolour(self.result), font=fonts['temperature_b'], bg=Background['main'])
        exec("Globals." + base + "_d" + "=[self.result, self.colour]")
        self.timer=self.after(2000, lambda: self.update_ld_main(base, rel))
        Globals.runnning_PROC.append(self.timer)

        if Globals.engineer == 0 and Globals.shiftpopup==0 and Globals.shiftenabled>0:
            if eval("Globals."+base+"_d")[0] > Globals.shiftlimit or Globals.shiftNOW == 1:
                Globals.shiftpopup=1
                bool = askyesnocancel("Confirm to proceed", "The crystal needs to be shifted. \nReady to shift crystal?")
                if bool:
                    comp = compensation(self.parent, base)
                else:
                    Globals.shiftpopup =0



    def update_status(self, address, rel="", loc="slot"):
        if loc == "slot":
            nd = ""
        else:
            nd = "_d"

        self.result = round(getvalue(address, eval("ld"+nd)[rel][1], eval("ld"+nd)[rel][2])['value'], 2)
        self.configure(text=str(self.result), fg=Colours['darkgrey'], font=fonts['status'],
                        bg=Background['main'])

    def readin_ld(self, bas):
        self.configure(text=eval("Globals."+bas+"_d")[0], bg=Background['main'], fg=eval("Globals."+bas+"_d")[1], font=fonts['status'])
        self.readin_ld_after = self.after(3000, lambda: self.readin_ld(bas))
        Globals.runnning_PROC.append(self.readin_ld_after)




    def getcolour(self, result):
            if result > 6:
                return Colours['red']
            else:
                return Colours['green']

    def stop_ld_main(self):
        self.configure(text="")
        self.after_cancel(self.timer)


class pzt_label(tk.Label):
    def __init__(self, parent):
        tk.Label.__init__(self, parent)
        self.parent=parent


    def update_status(self, address, rel="p", loc="slot"):

        if loc=="slot":
            nd=""
        else:
            nd="_d"

        self.result = round(getvalue(address, eval("pzt"+nd)[rel][1], eval("pzt"+nd)[rel][2])['value'], 2)
        self.configure(text=str(self.result), fg=Colours['darkgrey'], font=fonts['status'],
                        bg=Background['main'])

    def update_clp_main(self, address, rel="clp_power"):
        self.result = round(getvalue(address,pzt[rel][1],pzt[rel][2])['value'],2)
        self.configure(text=str(self.result), font=fonts['temperature_b'], bg=Background['main'], fg=Colours["darkgrey"])
        Globals.clp_power = self.result
        self.timer_clp = self.after(2000, lambda: self.update_clp_main(address, rel))
        Globals.runnning_PROC.append(self.timer_clp)

    def update_clp(self, status):
        status.configure(text=Globals.clp_power, font=fonts['status'], bg=Background['main'], fg=Colours["darkgrey"])
        self.update_clp_after = self.after(2000, lambda: self.update_clp(status))
        Globals.runnning_PROC.append(self.update_clp_after)

    def update_voltage(self, bas, rel="parkv"):
        address=getaddress(bas, rel)
        self.result = round(getvalue(address,pzt[rel][1],pzt[rel][2])['value'],2)
        self.configure(text=str(self.result), font=fonts['main'], bg=Background['main'], fg=Colours["darkgrey"])
        self.voltage_after = self.after(5000, lambda: self.update_voltage(bas, rel))
        Globals.runnning_PROC.append(self.voltage_after)

    def update_status_main(self, bas):
        self.configure(text=self.getstatus(bas).upper(), font=fonts['pzt_status'], bg=Background['main'], fg=Colours["darkgrey"])
        self.timer_status = self.after(2000, lambda: self.update_status_main(bas))
        Globals.runnning_PROC.append(self.timer_status)

    def stop_clp(self):
        self.configure(text="")
        self.after_cancel(self.timer_clp)

    def stop_status(self):
        self.configure(text="", font=fonts['pzt_status'], bg=Background['main'],
                       fg=Colours["darkgrey"])
        self.after_cancel(self.timer_status)

    def getstatus(self, bas):
        if bas=="pzt0":
            bit=[8,6]
        else:
            bit=[9,7]
        actual = Globals.status_bit
        pzt= int(readbit(actual, 1))
        lock=int(readbit(actual, bit[0]))
        manual=int(readbit(actual, bit[1]))
        if pzt==0:
            return "Off"
        else:
            if lock==0:
                if manual==0:
                    return "Ramping"

                if manual==1:
                    return "Park"
            if lock==1:
                if manual==0:
                    if readbit(actual, 21) == "1":
                        return "Locked"
                    else:
                        return "Locking"
                else:
                    return "Error"
            else:
                return "Error"

    def getcolour(self, result):
        return Colours['green']

class pzt_label_bit(tk.Label):
    def __init__(self, parent):
        tk.Label.__init__(self, parent)
        self.parent=parent

    def update_status(self, bas, bit, rel, loc="slot"):

        if loc=="slot":
            nd=""
        else:
            nd="_d"
        address = getaddress(bas, rel)
        #print(address)

        self.result = getbit(address, bit)
        if self.result == "1":
            self.result = "on"
        else:
            self.result ="off"
        self.configure(text=str(self.result), fg=Colours['darkgrey'], font=fonts['status'],
                        bg=Background['main'])

    def getcolour(self, result):
        return Colours['green']

class lh_label(tk.Label):
    def __init__(self, parent):
        tk.Label.__init__(self, parent)
        self.parent=parent

    def update_status(self, address, rel="p"):
        self.result = round(getvalue(address, lh[rel][1], lh[rel][2])['value'], 2)
        self.configure(text=str(self.result), fg=Colours['darkgrey'], font=fonts['status'],
                        bg=Background['main'])

    def getcolour(self, result):
        return Colours['green']

class gui_label(tk.Label):
    def __init__(self, parent):
        tk.Label.__init__(self, parent)
        self.parent=parent

    def update_status(self, address, rel="modeln"):
        self.result = getvalue(address, gui[rel][1], gui[rel][2])['value']
        self.configure(text=str(self.result), fg=Colours['darkgrey'], font=fonts['status'],
                        bg=Background['main'])

    def getcolour(self, result):
        return Colours['green']


class led_indicator(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self, parent)
        self.count=0
        self.countLimit=100

    def update_led(self, address):

        return 0

    def getcolour(self, result):
        if result == 1:
            return "green"
        if result == 0:
            return "red"
        else:
            return "amber"

class iterate(tk.Label):
    def __init__(self, master, title, b, rel, row, column, pztv=False):
        tk.Frame.__init__(self, master)
        self.pdy=3
        self.pdx = 2
        self.address=getaddress(b, rel)
        self.arg1= eval(base[b][1])[rel][1]
        self.arg2=eval(base[b][1])[rel][2]
        self.pzt=pztv
        self.sign="(C)"
        self.lock=0
        self.manual=0
        self.stop = 0

        if self.pzt==True:
             self.lock = control[b[:4] + "_l"]
             self.manual = control[b[:4] + "_m"]
             self.sign="(V)"

        self.l_status = tk.Label(master, text="", font=fonts['main'], bg=Background['main'])
        self.l_name = tk.Label(master, text=title, font=fonts['main'], bg=Background['main'])
        self.l_min = tk.Label(master, text="Min "+self.sign, font=fonts['main'], bg=Background['main'])
        self.t_min = tk.Text(master, font=fonts['main'], width=6, height=1)
        self.l_max = tk.Label(master, text="Max "+self.sign, font=fonts['main'], bg=Background['main'])
        self.t_max = tk.Text(master, font=fonts['main'], width=6, height=1)
        self.l_step = tk.Label(master, text="Steps", font=fonts['main'], bg=Background['main'])
        self.t_step = tk.Text(master, font=fonts['main'], width=6, height=1)
        self.l_step = tk.Label(master, text="Steps", font=fonts['main'], bg=Background['main'])
        self.t_step = tk.Text(master, font=fonts['main'], width=6, height=1)
        self.l_time = tk.Label(master, text="Time (ms)", font=fonts['main'], bg=Background['main'])
        self.t_time = tk.Text(master, font=fonts['main'], width=6, height=1)
        self.l_value_a= tk.Label(master, text="Actual", font=fonts['main'], bg=Background['main'])
        self.l_value= tk.Label(master, text="0.00", font=fonts['main'], bg=Background['main'])
        self.b_button = tk.Button(master, text="Run", font=fonts['submit'], bg=Background['submit'], command= lambda: self.run(self.address,
                                                                                                                      self.t_max,
                                                                                                                      self.t_min,
                                                                                                                      self.t_step,
                                                                                                                      self.arg1,
                                                                                                                      self.arg2,
                                                                                                                      self.l_value,
                                                                                                                      self.t_time,
                                                                                                                      self.l_status,
                                                                                                                      self.manual,
                                                                                                                      self.lock))
        self.b_stop = tk.Button(master, text="Stop", font=fonts['submit'], bg=Colours['red'], command= lambda: self.stopnow())
        self.l_status.grid(row=row + 1, column=column, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.l_name.grid(row=row+2, column=column, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.l_min.grid(row=row+1, column=column+1, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.t_min.grid(row=row+2, column=column+1, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.l_max.grid(row=row+1, column=column+2, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.t_max.grid(row=row+2, column=column+2, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.l_step.grid(row=row+3, column=column+1, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.t_step.grid(row=row+4, column=column+1, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.l_value_a.grid(row=row + 3, column=column + 2, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.l_value.grid(row=row+4, column=column+2, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.b_button.grid(row=row+2, column=column+3, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.l_time.grid(row=row+3, column=column, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.t_time.grid(row=row+4, column=column, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.geths(master).grid(row=row, column=column, columnspan= 5, sticky="we", pady=self.pdy, padx=self.pdx)
        self.geths(master).grid(row=row+5, column=column, columnspan=5, sticky="we", pady=self.pdy, padx=self.pdx)
        self.getvs(master).grid(row=row, column=column+4, rowspan=6, sticky="sn", pady=self.pdy, padx=self.pdx)
        self.b_stop.grid(row=row + 4, column=column + 3, sticky="nw", pady=self.pdy, padx=self.pdx)

    def stopnow(self):
        self.stop = 1

    def geths(self, parent):
            hs = ttk.Separator(parent, orient=tk.HORIZONTAL)
            return hs

    def getvs(self, parent):
            hs = ttk.Separator(parent, orient=tk.VERTICAL)
            return hs

    def run(self, address, maxi, mini, stepi, arg1, arg2, value, timer, status, m=0, l=0):

        self.times=300
        self.pzt=pzt
        self.stop = 0

        self.timing = int(timer.get("1.0", 'end-1c'))

        if l>0:
            self.manual=m
            self.lock=l
            self.controlbit=getvalue(control['address'])['value']
            if readbit(self.controlbit,int(math.log(self.manual,2))) == "0":
                setvalue(control['address'], self.manual+self.controlbit)
            if readbit(self.controlbit, int(math.log(self.lock,2))) == "1":
                resvalue(control['address'], self.lock)

        self.min = mini.get("1.0", 'end-1c')
        self.min = int(round(float(self.min.upper()),0))
        self.max = maxi.get("1.0", 'end-1c')
        self.max = int(round(float(self.max.upper()),0))
        self.steping=stepi.get("1.0", 'end-1c')
        self.steping=int(round(float(self.steping.upper()),0))
        if self.steping == 0:
            self.steping = 1
        #self.timing=self.steping
        self.step=(int(round(self.max-self.min,0)))/(self.steping)
        #print(self.step)

        self.arg1=arg1
        self.arg2=arg2
        self.i=self.min

        self.runupdate(address, value, status)

    def runupdate(self, address, value, status):
        if self.stop == 1:
            status.configure(text = "Stopped")
            self.after_cancel(self.looping)
        elif self.i <= self.max:
            status.configure(text="Running")
            setvalue(address, self.i, self.arg1, self.arg2)
            self.i=round(self.i+self.step,2)
            val=round(self.i-self.step,3)
            value.configure(text=val)

            self.looping=value.after(self.timing, lambda: self.runupdate(address, value, status))

        else:
            status.configure(text = "Complete")
            self.after_cancel(self.looping)

class Logo(tk.Label):
    def __init__(self, parent):
        tk.Label.__init__(self, parent)
        self.parent = parent

    def update_logo(self):
        Names = getNames()
        try:
            type = rang[Names["modell"]]
        except KeyError:
            type = "Solo"
        fontuse = fonts['submodel']
        if type != "Solo":
            fontuse = fonts['model']
        logo=str(type) + " " + str(Names["wavelength"])
        self.configure(text=logo, fg=Colours['solo'], font=fontuse, bg=Background['main'])
        self.logo_after = self.after(1500, lambda: self.update_logo())

def getNames():

   return Globals.Names


class compensation(tk.Toplevel):

    def __init__(self, master, b):
        tk.Toplevel.__init__(self)
        # self.grab_set()
        self.configure(background=Background['main'])
        self.geometry("750x520")
        self.title("LD advanced settings")
        self.pady = 3

        self.c_data = tk.Canvas(self, width=300, height=500, scrollregion=(0, 0, 300, 1500))
        self.vbar_data = tk.Scrollbar(self, orient=tk.VERTICAL)

        self.vbar_data.config(command=self.c_data.yview)
        self.c_data.config(yscrollcommand=self.vbar_data.set)
        self.c_data.create_window(0, 0, anchor="nw", width=700, height=1200, window=clpdata(self, b))

        self.c_data.grid(row=2, column=2, sticky="nwse")
        self.vbar_data.grid(row=2, column=1, sticky='nsw', padx=5)


class clpdata(tk.Frame):
    def __init__(self, master, b):
        tk.Frame.__init__(self, master)
        self.configure(bg=Background['main'])
        self.pady = 3

        if Globals.engineer == 1:

            self.title = tk.Label(self, text="OPM settings", font=fonts['title'], bg=Background['main'])

            self.l_clpe = tk.Label(self, text="OPM mode", font=fonts['main'], bg=Background['main'])

            self.opm_option = tk.StringVar(self)
            self.t_clp_enable = tk.OptionMenu(self, self.opm_option, *opm_mech)
            self.t_clp_enable.config(font=fonts['main'], bg=Background['main'], height=1, width=8)

            #self.t_clp_enable = tk.Text(self, width=6, height=1)
            self.s_clp_enable = ld_label(self)
            #self.s_clp_enable.update_status(getaddress("ld_d", "clp_enable"), "clp_enable", "driver")
            self.b_clpe = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                    bg=Background['submit'],
                                    command=lambda: self.enableclp())

            self.l_clp_target = tk.Label(self, text="CLP target level (V)", font=fonts['main'], bg=Background['main'])
            self.t_clp_target = tk.Text(self, width=6, height=1)
            self.s_clp_target = ld_label(self)
            self.s_clp_target.update_status(getaddress("ld_d", "clp_target"), "clp_target", "driver")
            self.b_clp_target = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                          bg=Background['submit'],
                                          command=lambda: submit(self, "ld_d", "clp_target"))

            self.l_clp_repeat = tk.Label(self, text="CLP repeat interval (s)", font=fonts['main'],
                                         bg=Background['main'])
            self.t_clp_repeat = tk.Text(self, width=6, height=1)
            self.s_clp_repeat = ld_label(self)
            self.s_clp_repeat.update_status(getaddress("ld_d", "clp_repeat"), "clp_repeat", "driver")
            self.b_clp_repeat = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                          bg=Background['submit'],
                                          command=lambda: submit(self, "ld_d", "clp_repeat", min=0, max=3600))

            self.l_clp_constant_M = tk.Label(self, text="CLP M constant (or IV for Ard.)", font=fonts['main'], bg=Background['main'])
            self.t_clp_constant_M = tk.Text(self, width=6, height=1)
            self.s_clp_constant_M = ld_label(self)
            self.s_clp_constant_M.update_status(getaddress("ld_d", "clp_constant_M"), "clp_constant_M", "driver")
            self.b_clp_constant_M = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                             bg=Background['submit'],
                                             command=lambda: submit(self, "ld_d", "clp_constant_M"))

            self.l_clp_constant_I = tk.Label(self, text="CLP I constant", font=fonts['main'], bg=Background['main'])
            self.t_clp_constant_I = tk.Text(self, width=6, height=1)
            self.s_clp_constant_I = ld_label(self)
            self.s_clp_constant_I.update_status(getaddress("ld_d", "clp_constant_I"), "clp_constant_I", "driver")
            self.b_clp_constant_I = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                            bg=Background['submit'],
                                            command=lambda: submit(self, "ld_d", "clp_constant_I"))

            self.l_clp_constant_P = tk.Label(self, text="CLP P constant", font=fonts['main'], bg=Background['main'])
            self.t_clp_constant_P = tk.Text(self, width=6, height=1)
            self.s_clp_constant_P = ld_label(self)
            self.s_clp_constant_P.update_status(getaddress("ld_d", "clp_constant_P"), "clp_constant_P", "driver")
            self.b_clp_constant_P = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                             bg=Background['submit'],
                                             command=lambda: submit(self, "ld_d", "clp_constant_P"))

            self.l_clp_ldmax = tk.Label(self, text="OPM max accumulated current (100 uA)", font=fonts['main'], bg=Background['main'])
            self.t_clp_ldmax = tk.Text(self, width=6, height=1)
            self.s_clp_ldmax = ld_label(self)
            self.s_clp_ldmax.update_status(getaddress("ld_d", "clp_ldmax"), "clp_ldmax", "driver")
            self.b_clp_ldmax = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                             bg=Background['submit'],
                                             command=lambda: submit(self, "ld_d", "clp_ldmax"))

            self.l_clp_error = tk.Label(self, text="OPM accumulated current (uA)", font=fonts['main'], bg=Background['main'])
            self.t_clp_error = tk.Text(self, width=6, height=1)
            self.s_clp_error = ld_label(self)
            self.s_clp_error.update_status(getaddress("ld", "clp_error"), "clp_error")
            self.retrieveclpstep()
            self.b_clp_error = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                        bg=Background['submit'],
                                        command=lambda: self.setclpstep())

            self.l_opm_target = tk.Label(self, text="GUI target level (mW)", font=fonts['main'], bg=Background['main'])
            self.t_opm_target = tk.Text(self, width=6, height=1)
            self.s_opm_target = gui_label(self)
            self.s_opm_target.update_status(getaddress("gui", "opm_target"), "opm_target")
            self.b_opm_target = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                          bg=Background['submit'],
                                          command=lambda: submit(self, "gui", "opm_target"))

            self.l_clp_power = tk.Label(self, text="CLP level (mV)", font=fonts['main'], bg=Background['main'])
            # self.t_clp_power = tk.Text(self, width=6, height=1)
            self.s_clp_power = pzt_label(self)
            self.s_clp_power.update_status(getaddress("pzt0", "clp_power"), "clp_power", "slot")
            self.b_clp_power = tk.Button(self, width=3, height=1, text="GET", font=fonts['submit'],
                                         bg="blue", fg="white",
                                         command=lambda: self.getclplevel())

            self.title2 = tk.Label(self, text="Crystal shifter settings (2-Stage, 1-Screw)", font=fonts['title'], bg=Background['main'])

            self.l_shifte = tk.Label(self, text="Enable shifting (1-on)", font=fonts['main'], bg=Background['main'])
            self.t_shift_enable = tk.Text(self, width=6, height=1)
            self.s_shift_enable = gui_label(self)
            self.s_shift_enable.update_status(getaddress("gui", "shift_enable"), "shift_enable")
            self.b_shifte = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                      bg=Background['submit'],
                                      command=lambda: submit(self, "gui", "shift_enable", min=-0.1, max=2.1))

            self.retrieveclp()
            self.retrieveclpstep()

            self.l_shifts = tk.Label(self, text="Shift step (20-150um)", font=fonts['main'], bg=Background['main'])
            self.t_shift_step = tk.Text(self, width=6, height=1)
            self.s_shift_step = gui_label(self)
            self.s_shift_step.update_status(getaddress("gui", "shift_step"), "shift_step")
            self.b_shifts = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                      bg=Background['submit'],
                                      command=lambda: submit(self, "gui", "shift_step"))

            self.l_shiftser = tk.Label(self, text="Driver serial no", font=fonts['main'], bg=Background['main'])
            self.t_shift_serial = tk.Text(self, width=6, height=1)
            self.s_shift_serial = gui_label(self)
            self.s_shift_serial.update_status(getaddress("gui", "shift_serial"), "shift_serial")
            self.b_shiftser = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                        bg=Background['submit'],
                                        command=lambda: submit(self, "gui", "shift_serial"))

            self.l_shiftth = tk.Label(self, text="Max LD current", font=fonts['main'], bg=Background['main'])
            self.t_shift_threshold = tk.Text(self, width=6, height=1)
            self.s_shift_threshold = gui_label(self)
            self.s_shift_threshold.update_status(getaddress("gui", "shift_threshold"), "shift_threshold")
            self.b_shiftth = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                       bg=Background['submit'],
                                       command=lambda: submit(self, "gui", "shift_threshold"))

            self.l_shiftc = tk.Label(self, text="Shift count", font=fonts['main'], bg=Background['main'])
            self.t_shift_count = tk.Text(self, width=6, height=1)
            self.s_shift_count = gui_label(self)
            self.s_shift_count.update_status(getaddress("gui", "shift_count"), "shift_count")
            # self.b_shiftc = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
            #                           bg=Background['submit'],
            #                           command=lambda: submit(self, "gui", "shift_count"))

            self.l_shiftpos = tk.Label(self, text="Shifter position", font=fonts['main'], bg=Background['main'])
            self.t_shift_position = tk.Text(self, width=6, height=1)
            self.s_shift_position = gui_label(self)
            self.s_shift_position.update_status(getaddress("gui", "shift_position"), "shift_position")
            self.b_shiftpos = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                        bg=Background['submit'],
                                        command=lambda: self.submit_q())

            self.l_shift_mincurrent = tk.Label(self, text="Shifter min current", font=fonts['main'], bg=Background['main'])
            self.t_shift_mincurrent = tk.Text(self, width=6, height=1)
            self.s_shift_mincurrent = gui_label(self)
            self.s_shift_mincurrent.update_status(getaddress("gui", "shift_mincurrent"), "shift_mincurrent")
            self.b_shift_mincurrent = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                        bg=Background['submit'],
                                        command=lambda: submit(self, "gui", "shift_mincurrent"))
            
            self.l_opm_setting = tk.Label(self, text="OPM setting for GUI (1)", font=fonts['main'], bg=Background['main'])
            self.t_opm_setting = tk.Text(self, width=6, height=1)
            self.s_opm_setting = gui_label(self)
            self.s_opm_setting.update_status(getaddress("gui", "opm_setting"), "opm_setting")
            self.b_opm_setting = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                        bg=Background['submit'],
                                        command=lambda: submit(self, "gui", "opm_setting"))

            self.b_connect = tk.Button(self, text="CONNECT", bg=Colours['green'], width=12, font=fonts['main'],
                                       command=lambda: self.connectit())

            self.b_shift = tk.Button(self, text="SHIFT", bg=Colours['amber'], width=5, font=fonts['main'],
                                     command=lambda: self.shiftit())

            self.disc = tk.Label(self, text="", font=fonts['main'], bg=Background['main'])
            self.cdisc = tk.Label(self, text="", font=fonts['main'], bg=Background['main'])

            self.title.grid(row=1, column=1, columnspan=2, sticky="nw", pady=self.pady)

            self.l_clpe.grid(row=2, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_clp_enable.grid(row=2, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_clp_enable.grid(row=2, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_clpe.grid(row=2, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_clp_target.grid(row=3, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_clp_target.grid(row=3, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_clp_target.grid(row=3, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_clp_target.grid(row=3, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_clp_repeat.grid(row=4, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_clp_repeat.grid(row=4, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_clp_repeat.grid(row=4, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_clp_repeat.grid(row=4, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_clp_constant_M.grid(row=5, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_clp_constant_M.grid(row=5, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_clp_constant_M.grid(row=5, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_clp_constant_M.grid(row=5, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_clp_constant_I.grid(row=6, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_clp_constant_I.grid(row=6, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_clp_constant_I.grid(row=6, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_clp_constant_I.grid(row=6, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_clp_constant_P.grid(row=7, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_clp_constant_P.grid(row=7, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_clp_constant_P.grid(row=7, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_clp_constant_P.grid(row=7, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_clp_ldmax.grid(row=8, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_clp_ldmax.grid(row=8, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_clp_ldmax.grid(row=8, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_clp_ldmax.grid(row=8, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_clp_error.grid(row=9, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_clp_error.grid(row=9, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_clp_error.grid(row=9, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_clp_error.grid(row=9, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_opm_target.grid(row=10, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_opm_target.grid(row=10, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_opm_target.grid(row=10, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_opm_target.grid(row=10, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_clp_power.grid(row=11, column=1, columnspan=1, sticky="nw", pady=self.pady)
            # self.t_clp_step.grid(row=5, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_clp_power.grid(row=11, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_clp_power.grid(row=11, column=4, columnspan=1, sticky="nw", pady=self.pady)
            self.cdisc.grid(row=12, column=1, columnspan=4, sticky="nw", pady=self.pady)

            self.title2.grid(row=15, column=1, columnspan=2, sticky="nw", pady=self.pady)

            self.l_shifte.grid(row=16, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_shift_enable.grid(row=16, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_shift_enable.grid(row=16, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_shifte.grid(row=16, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_shifts.grid(row=17, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_shift_step.grid(row=17, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_shift_step.grid(row=17, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_shifts.grid(row=17, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_shiftser.grid(row=18, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_shift_serial.grid(row=18, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_shift_serial.grid(row=18, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_shiftser.grid(row=18, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_shiftth.grid(row=19, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_shift_threshold.grid(row=19, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_shift_threshold.grid(row=19, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_shiftth.grid(row=19, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_shiftc.grid(row=20, column=1, columnspan=1, sticky="nw", pady=self.pady)
            # self.t_shift_count.grid(row=15, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_shift_count.grid(row=20, column=3, columnspan=1, sticky="nw", pady=self.pady)
            # self.b_shiftc.grid(row=15, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_shiftpos.grid(row=21, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_shift_position.grid(row=21, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_shift_position.grid(row=21, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_shiftpos.grid(row=21, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_shift_mincurrent.grid(row=22, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_shift_mincurrent.grid(row=22, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_shift_mincurrent.grid(row=22, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_shift_mincurrent.grid(row=22, column=4, columnspan=1, sticky="nw", pady=self.pady)
            
            self.l_opm_setting.grid(row=23, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_opm_setting.grid(row=23, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_opm_setting.grid(row=23, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_opm_setting.grid(row=23, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.b_shift.grid(row=25, column=2, columnspan=2, sticky="nw", pady=self.pady)
            self.b_connect.grid(row=25, column=3, columnspan=2, sticky="nw", pady=self.pady)
            self.disc.grid(row=26, column=1, columnspan=4, sticky="nw", pady=self.pady)
        else:
            self.l_disc1 = tk.Label(self,
                                    text="Ensure USB connection is maintained through shifting process.\nAfter the cables are connected, click the connect button.",
                                    font=fonts['main'], bg=Background['main'])
            self.l_disc2 = tk.Label(self, text="Once the shifter connects, click on shift.", font=fonts['main'],
                                    bg=Background['main'])
            self.l_disc3 = tk.Label(self, text="The laser will restart.", font=fonts['main'], bg=Background['main'])

            self.disc = tk.Label(self, text="", font=fonts['main'], bg=Background['main'])
            # self.cdisc = tk.Label(self, text="", font=fonts['main'], bg=Background['main'])
            self.b_connect = tk.Button(self, text="CONNECT", bg=Colours['green'], width=12, font=fonts['main'],
                                       command=lambda: self.connectit(user=0))

            self.b_shift = tk.Button(self, text="SHIFT", bg=Colours['amber'], width=5, font=fonts['main'],
                                     command=lambda: self.shiftit(user=0))
            self.b_shift.grid(row=20, column=2, columnspan=2, sticky="nw", pady=self.pady)
            self.b_connect.grid(row=20, column=3, columnspan=2, sticky="nw", pady=self.pady)
            self.disc.grid(row=21, column=1, columnspan=4, sticky="nw", pady=self.pady)
            self.l_disc1.grid(row=16, column=1, columnspan=4, sticky="nw", pady=self.pady)
            self.l_disc2.grid(row=17, column=1, columnspan=4, sticky="nw", pady=self.pady)
            self.l_disc3.grid(row=18, column=1, columnspan=4, sticky="nw", pady=self.pady)
        self.shifter_connect = 0
        self.seron = 0

    def geths(self, parent):
        hs = ttk.Separator(parent, orient=tk.HORIZONTAL)
        return hs

    def retrieveclp(self):
        try:
            val = getvalue(getaddress("ld_d", "clp_enable"), "1", "1")["value"]
            instr = int(val[5:7])
            instr = f"{instr:02d}"
            #print(instr)
        except:
            instr = "00"
            setvalue(getaddress("ld_d", "clp_enable"), "0x55500AAA", "1", "1")

        mode = opm_dict[instr]

        self.s_clp_enable.configure(text=mode, font=fonts['status'],fg=Colours['darkgrey'], bg=Background['main'])
        self.opm_option.set(mode)

    def enableclp(self):
        try:
            val = getvalue(getaddress("ld_d", "clp_enable"), "1", "1")["value"]
            instr = int(val[5:7])
            target = opm_dict[self.opm_option.get()]
            #print(target)
            setvalue(getaddress("ld_d", "clp_enable"), "0x555" + target + "AAA", "1", "1")
            self.s_clp_enable.configure(text=self.opm_option.get())
        except:
            instr = 0
            setvalue(getaddress("ld_d", "clp_enable"), "0x55500AAA", "1", "1")
            self.s_clp_enable.configure(text="Error")
        # # print(val, instr, vall)
        # if vall == 1:
        #     if instr == 2:
        #         self.s_clp_enable.configure(text="Already on")
        #     else:
        #         setvalue(getaddress("ld_d", "clp_enable"), "0x55532AAA", "1", "1")
        #         self.s_clp_enable.configure(text="Activated")
        # elif vall == 0:
        #     if instr == 0:
        #         self.s_clp_enable.configure(text="Already off")
        #     else:
        #         setvalue(getaddress("ld_d", "clp_enable"), "0x55500AAA", "1", "1")
        #         self.s_clp_enable.configure(text="Turned off")
        # else:
        #     self.s_clp_enable.configure(text="Error")
        #     self.cdisc.configure(text="Use 1 or 0 to turn compensation on or off.")

    def setclpstep(self):
        vall = retrieve(self.t_clp_error)
        # val = 1000000*val
        if vall > 30000 or vall < -30000:
            self.cdisc.configure(text="Step size is out of limit.")
            self.s_clp_error.configure(text="error")
        elif vall < 100 and vall > -100:
            self.cdisc.configure(text="Min step size is abs(100).")
            self.s_clp_error.configure(text="error")
        else:
            val = int(vall / 100)
            val = self.int2hex4(val)
            # val = val[:-4]
            subval = "0x55" + val + "AA"
            setvalue(getaddress("ld", "clp_error"), subval, "1", "1")
            self.cdisc.configure(text=f"Step set to {str(vall)} uA.")
            self.retrieveclpstep()

    def int2hex4(self, hx):

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
                # print(format(float((1 << 32) + val), '04x'))
            return val

    def retrieveclpstep(self):
        steps = getvalue(getaddress("ld_d", "clp_step"), "1", "1")["value"]
        step = steps[4:8]
        # print(steps, step)
        val = hex2signed(step)
        if val > 2 ** 15:
            val = -(2 ** 16 - val)
        self.s_clp_error.configure(text=100 * val)

    def getshifterstatus(self):
        bool1 = int(getvalue(getaddress("gui", "shift_enable"))["value"])
        if bool1 > 0 and self.shifter_connect == 1:
            return 1
        else:
            return 0

    def shiftit(self, user=1):
        if self.getshifterstatus() == 1:
            if self.stageon == 0:
                stp = getvalue(getaddress("gui", "shift_step"), "i", "1")["value"]
                self.dev.move(stp)



            else:
                    stp = getvalue(getaddress("gui", "shift_step"), "i", "1")["value"]

                    if stp > 0:
                        direction = 1
                    else:
                        direction = 0
                    if abs(stp) > 99:
                        stp = 99
                    self.serstage.write(f"{abs(1)}{direction}\n".encode("UTF-8"))
                    time.sleep(2)
                    self.serstage.write(f"{abs(stp)}{direction}\n".encode("UTF-8"))

            pos = getvalue(getaddress("gui", "shift_position"), "i", "1")["value"]
            newpos = pos + stp
            setvalue(getaddress("gui", "shift_position"), newpos, "i", "1")
            if user == 1:
                self.s_shift_position.configure(text=str(newpos))

            c = getvalue(getaddress("gui", "shift_count"), "u", "1")["value"]
            newc = c + 1
            setvalue(getaddress("gui", "shift_count"), newc, "u", "1")
            if user == 1:
                self.s_shift_count.configure(text=str(newc))
            if user == 0:
                current_ld = getvalue(getaddress("ld", "act"), "u", "u")["value"]
                new_current = current_ld - 0.1
                setvalue(getaddress("ld_d", "curr"), new_current, "u", "u")
                Globals.shiftpopup = 0
                if getbit(control['address'], 1) == "1":
                    resvalue(control['address'], 2)
                if getbit(control['address'], 0) == "1":
                    resvalue(control['address'], 1)
                if getbit(control['address'], 10) == "1":
                    resvalue(control['address'], 1024)

                messagebox.showinfo("Laser restart",
                                    "Please wait until motor stops, then disconnect shifter cables.\nRestart GUI.")

                self.destroy()

        else:
            self.disc.configure(text="Connect driver first, enable shifting.")

    def submit_q(self):
        bool = askyesnocancel("Confirm to proceed",
                              "Are you sure you want to move shifter reference position? \nThis will zero counter, the shifter will NOT actuate.")
        if bool:
            vall = retrieve(self.t_shift_position)
            setvalue(getaddress("gui", "shift_position"), vall, "i", "1")
            setvalue(getaddress("gui", "shift_count"), 0)
            self.s_shift_position.configure(text=vall)
            self.s_shift_count.configure(text=0)

    def connectit(self, user=1):
        if int(getvalue(getaddress("gui", "shift_enable"))["value"]) == 1:
            #self.dev = BenchtopPiezoWrapper(getvalue(getaddress("gui", "shift_serial"))["value"])
            #self.dev.connect()
            #self.shifter_connect = 1
            self.disc.configure(text="Not available in this GUI version")
            #self.b_connect.configure(text="DISCONNECT", command=lambda: self.disconnectit(), bg=Colours['red'], fg="white")
        if int(getvalue(getaddress("gui", "shift_enable"))["value"]) == 2:
            self.piezoserial()
            if self.stageon==1:
                self.shifter_connect = 1
                self.disc.configure(text="Stage connected")
                self.b_connect.configure(text="DISCONNECT", command=lambda: self.disconnectit(), bg=Colours['red'],fg="white")
            else:
                return 0



    def piezoserial(self):
        ports = comports()
        selected_port = None


        if Globals.stageon == 0:
            for port in ports:
                if "CH340" in port.description:
                    selected_port = port.device

            if selected_port == None:
                self.stageon = 0
            else:

                ser = serial.Serial(
                    port=selected_port,
                    baudrate=19200,
                    parity=serial.PARITY_NONE,
                    stopbits=1,
                    bytesize=8,
                    timeout=10
                )

                self.serstage = ser
                self.stageon = 1
                Globals.serdo = self.serstage
                Globals.stageon = 1
        else:
            self.serstage = Globals.serdo
            self.stageon = 1

    def disconnectit(self):
        if self.stageon == 1:
            self.serstage.close()
            self.stageon =0
            Globals.stageon  = 0
        else:
            self.dev.close()
        self.b_connect.configure(text="CONNECT", command=lambda: self.connectit(), bg=Colours['green'], fg="black")
        self.shifter_connect = 0
        self.disc.configure(text="Driver disconnected")

    def getclplevel(self):
        dset = 10  #
        power = []
        power2 = []
        clp_pzt0 = ""
        clp_pzt1 = ""
        for i in range(dset):
            if "PZT0" in Globals.available:
                val = getvalue(getaddress("pzt0", "clp_power"))["value"]
                power.append(val)
            if "PZT1" in Globals.available:
                val = getvalue(getaddress("pzt1", "clp_power"))["value"]
                power2.append(val)
        if "PZT0" in Globals.available:
            clp_pzt0 = (np.round(np.mean(power)/1000000, 3) * 1)
        if "PZT1" in Globals.available:
            clp_pzt1 = (np.round(np.mean(power2)/1000000, 3) * 1)

        self.s_clp_power.configure(text=f"{str(clp_pzt0)},{str(clp_pzt1)} V")


# class BenchtopPiezoWrapper():
#     def __init__(self, serial_number):
#         self._ser = str(serial_number)
#         # print("serial",self._ser)
#         DeviceManagerCLI.BuildDeviceList()
#         # print("avail device", DeviceManagerCLI.GetDeviceList())
#         self._pzt = KCubeInertialMotor.CreateKCubeInertialMotor(self._ser)
#         self.channels = []
#         self.connected = False
#
#     def connect(self):
#         """Initialise communications, populate channel list, etc."""
#         assert not self.connected
#         self._pzt.Connect(self._ser)
#         self.connected = True
#         # print(self._pzt.GetDeviceInfo().Name)
#         self._pzt.StartPolling(250)
#         self._pzt.EnableDevice()
#
#         assert len(self.channels) == 0, "Error connecting: we've already initialised channels!"
#         # #for i in range(self._piezo.ChannelCount):
#         # for i in range(1):
#         #     #chan = self._piezo.GetChannel(i + 1)  # Kinesis channels are one-indexed
#         #     chan = self._piezo.channel()
#         #     chan.WaitForSettingsInitialized(5000)
#         #     chan.StartPolling(250)  # getting the voltage only works if you poll!
#         #     time.sleep(0.5)  # ThorLabs have this in their example...
#         #     chan.EnableDevice()
#         #     # I don't know if the lines below are necessary or not - but removing them
#         #     # may or may not work...
#         #     time.sleep(0.5)
#         #     config = chan.GetPiezoConfiguration(chan.DeviceID)
#         #     info = chan.GetDeviceInfo()
#         #     max_v = Decimal.ToDouble(chan.GetMaxOutputVoltage())
#         #     self.channels.append(chan)
#         #     print("succes")
#
#     def close(self):
#         """Shut down communications"""
#         # if not self.connected:
#         #     print(f"Not closing piezo device {self._ser}, it's not open!")
#         #     return
#         self._pzt.StopPolling()
#         try:
#             self._pzt.Disconnect(True)
#         except:
#             pass
#         # for chan in self.channels:
#         #     chan.StopPolling()
#         # self.channels = []
#         # self._pzt.Disconnect(True)
#
#     def move(self, target):
#         self._pzt.SetPositionAs(InertialMotorStatus.MotorChannels.Channel1, 0);
#         self._pzt.MoveTo(InertialMotorStatus.MotorChannels.Channel1, target, 60000)
#         time.sleep(1)
#         curr = self._pzt.GetPosition(InertialMotorStatus.MotorChannels.Channel1)
#
#         return curr
#
#     def __del__(self):
#         try:
#             if self.connected:
#                 self.close()
#         except:
#             print(f"Error closing communications on deletion of device {self._ser}")
#
#     def set_output_voltages(self, voltages):
#         """Set the output voltage"""
#         assert len(voltages) == len(self.channels), "You must specify exactly one voltage per channel"
#         for chan, v in zip(self.channels, voltages):
#             chan.SetOutputVoltage(Decimal(v))
#
#     def get_output_voltages(self):
#         """Retrieve the output voltages as a list of floating-point numbers"""
#         return [Decimal.ToDouble(chan.GetOutputVoltage()) for chan in self.channels]
#
#     # def resource_path(self, relative_path):
#     #     try:
#     #         base_path = sys._MEIPASS
#     #     except Exception:
#     #         base_path = os.path.abspath(".")
#     #
#     #     return os.path.join(base_path, relative_path)
#
#     output_voltages = property(get_output_voltages, set_output_voltages)