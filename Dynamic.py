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
            self.threshold = round(getvalue(target, "f", "1")['value'], 2)

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

            if result > value - 0.45 and result<value + 0.45:
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

        self.result = round(getvalue(address, eval("pzt"+nd)[rel][1], eval("pzt"+nd)[rel][2])['value'], 6)

        if abs(self.result) < 0.02:
            if self.result != 0:
                self.result = sci(self.result)
        else:
            self.result = round(self.result, 2)
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
        actual = Globals.status_bit

        if bas == "pzt0":
            if readbit(actual, status["STATUS_OK"]) == "1" and readbit(actual, status["PZT_0_PARK"]) == "1":
                return "PARK"
            elif readbit(actual, status["STATUS_OK"]) == "1" and readbit(actual, status["PZT_0_RAMP"]) == "1":
                return "RAMP"
            elif readbit(actual, status["STATUS_OK"]) == "1" and readbit(actual, status["PZT_0_Locking"]) == "1":
                return "Locking"
            elif readbit(actual, status["STATUS_OK"]) == "1" and readbit(actual, status["PZT_0_Tuning"]) == "1":
                return "Tuning"
            elif readbit(actual, status["STATUS_OK"]) == "1" and readbit(actual, status["PZT_0_Locked"]) == "1":
                return "Locked"
            elif readbit(actual, status["STATUS_OK"]) == "1":
                return "OFF"
            else:
                return "ERROR"
        if bas == "pzt1":
            if readbit(actual, status["STATUS_OK"]) == "1" and readbit(actual, status["PZT_1_PARK"]) == "1":
                return "PARK"
            elif readbit(actual, status["STATUS_OK"]) == "1" and readbit(actual, status["PZT_1_RAMP"]) == "1":
                return "RAMP"
            elif readbit(actual, status["STATUS_OK"]) == "1" and readbit(actual, status["PZT_1_Locking"]) == "1":
                return "Locking"
            elif readbit(actual, status["STATUS_OK"]) == "1" and readbit(actual, status["PZT_1_Tuning"]) == "1":
                return "Tuning"
            elif readbit(actual, status["STATUS_OK"]) == "1" and readbit(actual, status["PZT_1_Locked"]) == "1":
                return "Locked"
            elif readbit(actual, status["STATUS_OK"]) == "1":
                return "OFF"
            else:
                return "ERROR"

    def getcolour(self, result):
        return Colours['green']

class dpot_label(tk.Label):
    def __init__(self, parent):
        tk.Label.__init__(self, parent)
        self.parent=parent


    def update_status(self, address, rel="p", loc="slot"):

        self.result = round(getvalue(address, eval("dphd")[rel][1], eval("dphd")[rel][2])['value'], 2)
        self.configure(text=str(self.result), fg=Colours['darkgrey'], font=fonts['status'],
                        bg=Background['main'])

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
             self.lock =0# control[b[:4] + "_l"]
             self.manual =0# control[b[:4] + "_m"]
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
            type = "NX"
        fontuse = fonts['submodel']
        if type != "NX":
            fontuse = fonts['model']
        try:
            logo=str(Names["wavelength"])+ " " + str(type)
        except:
            logo = str("0" + " " + str(type))
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


            self.l_opm_enable = tk.Label(self, text="Enable OPM (1)", font=fonts['main'], bg=Background['main'])
            self.t_opm_enable = tk.Text(self, width=6, height=1)
            self.s_opm_enable = ld_label(self)
            self.s_opm_enable.update_status(getaddress("ld", "opm_enable"), "opm_enable", "slot")
            self.b_opm_enable = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                          bg=Background['submit'],
                                          command=lambda: submit(self, "ld", "opm_enable"))

            self.l_opm_period = tk.Label(self, text="OPM period (ms)", font=fonts['main'],
                                         bg=Background['main'])
            self.t_opm_period = tk.Text(self, width=6, height=1)
            self.s_opm_period = ld_label(self)
            self.s_opm_period.update_status(getaddress("ld", "opm_period"), "opm_period", "slot")
            self.b_opm_period = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                          bg=Background['submit'],
                                          command=lambda: submit(self, "ld", "opm_period", min=100, max=120000))

            self.l_opm_init = tk.Label(self, text="After lock delay (ms)", font=fonts['main'], bg=Background['main'])
            self.t_opm_init = tk.Text(self, width=6, height=1)
            self.s_opm_init = ld_label(self)
            self.s_opm_init.update_status(getaddress("ld", "opm_init"), "opm_init", "slot")
            self.b_opm_init = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                             bg=Background['submit'],
                                             command=lambda: submit(self, "ld", "opm_init", min=120000, max=6666666666))

            self.l_opm_step = tk.Label(self, text="OPM step size (uA)", font=fonts['main'], bg=Background['main'])
            self.t_opm_step = tk.Text(self, width=6, height=1)
            self.s_opm_step = ld_label(self)
            self.s_opm_step.update_status(getaddress("ld", "opm_step"), "opm_step", "slot")
            self.b_opm_step = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                            bg=Background['submit'],
                                            command=lambda: submit(self, "ld", "opm_step", min = 50, max = 5000))

            self.l_opm_threshold = tk.Label(self, text="OPM threshold (0.02 - 2%)", font=fonts['main'], bg=Background['main'])
            self.t_opm_threshold = tk.Text(self, width=6, height=1)
            self.s_opm_threshold = ld_label(self)
            self.s_opm_threshold.update_status(getaddress("ld", "opm_threshold"), "opm_threshold", "slot")
            self.b_opm_threshold = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                             bg=Background['submit'],
                                             command=lambda: submit(self, "ld", "opm_threshold"))

            self.l_opm_large_threshold = tk.Label(self, text="OPM large step threshold (0.05-5%)", font=fonts['main'], bg=Background['main'])
            self.t_opm_large_threshold = tk.Text(self, width=6, height=1)
            self.s_opm_large_threshold = ld_label(self)
            self.s_opm_large_threshold.update_status(getaddress("ld", "opm_large_threshold"), "opm_large_threshold", "slot")
            self.b_opm_large_threshold = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                             bg=Background['submit'],
                                             command=lambda: submit(self, "ld", "opm_large_threshold"))

            self.l_opm_large = tk.Label(self, text="OPM large step size (uA)", font=fonts['main'], bg=Background['main'])
            self.t_opm_large = tk.Text(self, width=6, height=1)
            self.s_opm_large = ld_label(self)
            self.s_opm_large.update_status(getaddress("ld", "opm_large"), "opm_large")
            self.b_opm_large = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                             bg=Background['submit'],
                                             command=lambda: submit(self, "ld", "opm_large", min = 100, max = 5000))

            self.l_opm_low = tk.Label(self, text="OPM min current (uA)", font=fonts['main'], bg=Background['main'])
            self.t_opm_low = tk.Text(self, width=6, height=1)
            self.s_opm_low = ld_label(self)
            self.s_opm_low.update_status(getaddress("ld", "opm_low"), "opm_low", "slot")
            self.b_opm_low = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                            bg=Background['submit'],
                                            command=lambda: submit(self, "ld", "opm_low"))

            self.l_opm_high = tk.Label(self, text="OPM max current (uA)", font=fonts['main'], bg=Background['main'])
            self.t_opm_high = tk.Text(self, width=6, height=1)
            self.s_opm_high = ld_label(self)
            self.s_opm_high.update_status(getaddress("ld", "opm_high"), "opm_high", "slot")
            self.b_opm_high = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                             bg=Background['submit'],
                                             command=lambda: submit(self, "ld", "opm_high"))

            self.l_opm_target = tk.Label(self, text="OPM target (mW)", font=fonts['main'], bg=Background['main'])
            self.t_opm_target = tk.Text(self, width=6, height=1)
            self.s_opm_target = ld_label(self)
            self.s_opm_target.update_status(getaddress("ld", "opm_target"), "opm_target", "slot")
            self.b_opm_target = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                             bg=Background['submit'],
                                             command=lambda: submit(self, "ld", "opm_target"))

            self.l_clp_power = tk.Label(self, text="CLP level (mV)", font=fonts['main'], bg=Background['main'])
            self.s_clp_power = pzt_label(self)
            self.s_clp_power.update_status(getaddress("pzt0", "clp_power"), "clp_power", "slot")
            self.b_clp_power = tk.Button(self, width=3, height=1, text="GET", font=fonts['submit'],
                                         bg="blue", fg="white",
                                         command=lambda: self.getclplevel())

            self.title.grid(row=1, column=1, columnspan=2, sticky="nw", pady=self.pady)

            self.l_opm_enable.grid(row=3, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_opm_enable.grid(row=3, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_opm_enable.grid(row=3, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_opm_enable.grid(row=3, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_opm_period.grid(row=4, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_opm_period.grid(row=4, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_opm_period.grid(row=4, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_opm_period.grid(row=4, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_opm_init.grid(row=5, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_opm_init.grid(row=5, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_opm_init.grid(row=5, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_opm_init.grid(row=5, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_opm_step.grid(row=6, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_opm_step.grid(row=6, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_opm_step.grid(row=6, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_opm_step.grid(row=6, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_opm_threshold.grid(row=7, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_opm_threshold.grid(row=7, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_opm_threshold.grid(row=7, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_opm_threshold.grid(row=7, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_opm_large_threshold.grid(row=8, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_opm_large_threshold.grid(row=8, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_opm_large_threshold.grid(row=8, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_opm_large_threshold.grid(row=8, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_opm_large.grid(row=9, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_opm_large.grid(row=9, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_opm_large.grid(row=9, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_opm_large.grid(row=9, column=4, columnspan=1, sticky="nw", pady=self.pady)
            
            self.l_opm_low.grid(row=10, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_opm_low.grid(row=10, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_opm_low.grid(row=10, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_opm_low.grid(row=10, column=4, columnspan=1, sticky="nw", pady=self.pady)
            
            self.l_opm_high.grid(row=11, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_opm_high.grid(row=11, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_opm_high.grid(row=11, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_opm_high.grid(row=11, column=4, columnspan=1, sticky="nw", pady=self.pady)
                                 
            self.l_opm_target.grid(row=12, column=1, columnspan=1, sticky="nw", pady=self.pady)
            self.t_opm_target.grid(row=12, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_opm_target.grid(row=12, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_opm_target.grid(row=12, column=4, columnspan=1, sticky="nw", pady=self.pady)

            self.l_clp_power.grid(row=13, column=1, columnspan=1, sticky="nw", pady=self.pady)
            # self.t_clp_power.grid(row=10, column=2, columnspan=1, sticky="nw", pady=self.pady)
            self.s_clp_power.grid(row=13, column=3, columnspan=1, sticky="nw", pady=self.pady)
            self.b_clp_power.grid(row=13, column=4, columnspan=1, sticky="nw", pady=self.pady)



            self.disc = tk.Label(self, text="", font=fonts['main'], bg=Background['main'])

            self.disc.grid(row=21, column=1, columnspan=4, sticky="nw", pady=self.pady)

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
                new_current = Globals.shiftmincurrent
                setvalue(getaddress("ld_d", "curr"), new_current, "u", "u")
                Globals.shiftpopup = 0
                if getbit(control['address'], 1) == "1":
                    resvalue(control['address'], 2)
                if getbit(control['address'], 0) == "1":
                    resvalue(control['address'], 1)
                if getbit(control['address'], 10) == "1":
                    resvalue(control['address'], 1024)

                messagebox.showinfo("Laser restart",
                                    "Please wait until motor stops, then close GUI.\nRestart software.")
                if getbit(control['address'], 1) == "1":
                    resvalue(control['address'], 2)
                if getbit(control['address'], 0) == "1":
                    resvalue(control['address'], 1)
                if getbit(control['address'], 10) == "1":
                    resvalue(control['address'], 1024)
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
                if "CH340" in port.description or "Arduino" in port.description:
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

    def getpowerlvl(self):
        self.opm_ratio = getvalue(getaddress("ld_d", "clp_constant_M"), "f", "u")["value"]
        if Globals.stageon == 0:
            self.piezoserial()
        if Globals.stageon ==1:
            pwr = []
            for i in range(5):
                value = str(self.serstage.read_all().decode()).splitlines()[:-1]
                print(value)
                if len(value) == 1:
                    power_reading = (int(value[0]))
                    pwr.append(power_reading)
                time.sleep(1)

            try:
                target = np.mean(pwr)/self.opm_ratio
            except:
                self.opm_off()
                self.message_trigger("Regulation failed.\n")
            return target
        else:
            return -1

    def getclplevel(self):
        dset = 10  #
        power = []
        power2 = []
        clp_pzt0 = ""
        clp_pzt1 = ""
        val = self.getpowerlvl()
        if val == -1:
            for i in range(dset):
                if "PZT0" in Globals.available:
                    val = getvalue(getaddress("pzt0", "clp_power"),"u","m")["value"]
                    power.append(val)
                if "PZT1" in Globals.available:
                    val = getvalue(getaddress("pzt1", "clp_power"),"u","m")["value"]
                    power2.append(val)
            if "PZT0" in Globals.available:
                clp_pzt0 = (np.round(np.mean(power)/1, 3) * 1)
            if "PZT1" in Globals.available:
                clp_pzt1 = (np.round(np.mean(power2)/1, 3) * 1)

            self.s_clp_power.configure(text=f"{str(clp_pzt0)},{str(clp_pzt1)} V")
        else:
            self.s_clp_power.configure(text=f"{np.round(val, 3)}, from EXT")


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