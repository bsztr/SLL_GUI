import tkinter as tk
from COMM import *
from CONFIG import *
import Globals
import time
import math
from init_start import *

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
            print(self.threshold)
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
        print(address)

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
        print(self.step)

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