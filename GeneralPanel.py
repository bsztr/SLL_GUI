import tkinter as tk
from tkinter import ttk
from Dynamic import *
import CONFIG
from init_start import *
import math
from init_start import getmodules
import Globals
from COMM import stop_COMM
from stm32loader.main import main as smmain
import os, pandas
from tkinter.messagebox import showinfo
import numpy as np
from Logging import Logger_wrap

class GeneralPanel(tk.Frame):
    def __init__(self, master, parent):
        tk.Frame.__init__(self, master)

        self.configure(bg=Background['main'])
        self.base="lh"
        self.l_logo = Logo(self)
        self.l_logo.update_logo()
        self.reflush(master)

        # Advanced definition
        self.l_device = tk.Label(self, text="Device summary", font=fonts['title'], bg=Background['main'])

        self.l_model = tk.Label(self, text="Model ID:", font=fonts['main'], bg=Background['main'])
        self.t_model = tk.Text(self, font=fonts['main'], width=10, height=1)
        self.s_model = lh_label(self)
        self.s_model.update_status(getaddress(self.base, "model"), "model")
        self.b_model = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                  command=lambda: submit(self, self.base, "model"))

        self.l_modell = tk.Label(self, text="Model name:", font=fonts['main'], bg=Background['main'])
        self.t_modell = tk.Text(self, font=fonts['main'], width=10, height=1)
        self.s_modell = gui_label(self)
        self.s_modell.update_status(getaddress("gui", "modell"), "modell")
        self.b_modell = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                 command=lambda: submit_gui(self, "gui", "modell"))

        self.l_date = tk.Label(self, text="Date of manufacture:", font=fonts['main'], bg=Background['main'])
        self.t_date = tk.Text(self, font=fonts['main'], width=10, height=1)
        self.s_date = lh_label(self)
        self.s_date.update_status(getaddress(self.base, "date"), "date")
        self.b_date = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                  command=lambda: submit(self, self.base, "date"))

        self.l_serial = tk.Label(self, text="Serial number:", font=fonts['main'], bg=Background['main'])
        self.t_serial = tk.Text(self, font=fonts['main'], width=10, height=1)
        self.s_serial = lh_label(self)
        self.s_serial.update_status(getaddress(self.base, "serial"), "serial")
        self.b_serial = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                  command=lambda: submit(self, self.base, "serial"))

        self.l_power = tk.Label(self, text="Output power (mW):", font=fonts['main'], bg=Background['main'])
        self.t_power = tk.Text(self, font=fonts['main'], width=10, height=1)
        self.s_power = lh_label(self)
        self.s_power.update_status(getaddress(self.base, "power"), "power")
        self.b_power = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                  command=lambda: submit(self, self.base, "power"))

        self.l_wavelength = tk.Label(self, text="Wavelength (nm):", font=fonts['main'], bg=Background['main'])
        self.t_wavelength = tk.Text(self, font=fonts['main'], width=10, height=1)
        self.s_wavelength = lh_label(self)
        self.s_wavelength.update_status(getaddress(self.base, "wavelength"), "wavelength")
        self.b_wavelength = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                  command=lambda: submit(self, self.base, "wavelength"))

        self.l_high = tk.Label(self, text="High power set (A):", font=fonts['main'], bg=Background['main'])
        self.t_high = tk.Text(self, font=fonts['main'], width=10, height=1)
        self.s_high = gui_label(self)
        self.s_high.update_status(getaddress("gui", "high"), "high")
        self.b_high = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                  command=lambda: submit_gui(self, "gui", "high", "f"))

        self.l_low = tk.Label(self, text="Low power set (A):", font=fonts['main'], bg=Background['main'])
        self.t_low = tk.Text(self, font=fonts['main'], width=10, height=1)
        self.s_low = gui_label(self)
        self.s_low.update_status(getaddress("gui", "low"), "low")
        self.b_low = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                command=lambda: submit_gui(self, "gui", "low", "f"))

        self.l_trial = tk.Label(self, text="Trial On(1), Off(0):", font=fonts['main'], bg=Background['main'])
        self.t_trial = tk.Text(self, font=fonts['main'], width=10, height=1)
        self.s_trial = gui_label(self)
        self.s_trial.update_status(getaddress("gui", "trial"), "trial")
        self.b_trial = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                command=lambda: submit_gui(self, "gui", "trial", "f"))

        self.l_start = tk.Label(self, text="Starting date:", font=fonts['main'], bg=Background['main'])
        self.t_start = tk.Text(self, font=fonts['main'], width=10, height=1)
        self.s_start = gui_label(self)
        self.s_start.update_status(getaddress("gui", "start"), "start")
        self.b_start = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                command=lambda: submit_gui(self, "gui", "start"))

        self.l_dur = tk.Label(self, text="End date:", font=fonts['main'], bg=Background['main'])
        self.t_dur = tk.Text(self, font=fonts['main'], width=10, height=1)
        self.s_dur = gui_label(self)
        self.s_dur.update_status(getaddress("gui", "dur"), "dur")
        self.b_dur = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                command=lambda: submit_gui(self, "gui", "dur"))

        self.l_ban = tk.Label(self, text="Subscription reset (0 to res):", font=fonts['main'], bg=Background['main'])
        self.t_ban = tk.Text(self, font=fonts['main'], width=10, height=1)
        self.s_ban = gui_label(self)
        self.s_ban.update_status(getaddress("gui", "ban"), "ban")
        self.b_ban = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                command=lambda: submit_gui(self, "gui", "ban"))

        self.l_activate_title=tk.Label(self, text="Activate modules", font=fonts['title'], bg=Background['main'])
        self.row=3
        self.column=5
        i=0
        Globals.modules=Globals.available
        for item in ["CB", "LH", "TEC0", "TEC1", "TEC2", "TEC3", "PZT0", "PZT1", "LDR"]:
            avail_pan = activate(self)
            avail_pan(self, item,self.row+i,self.column)
            i+=1

        self.l_diagnose = tk.Label(self, text="", font=fonts['status'], bg=Background['main'], fg=Colours['darkgrey'])
        self.b_diagnose = tk.Button(self, width=8, height=1, text="DIAGNOSE", font=fonts['submit'], bg=Background['submit'],
                                      command= self.diagnose)
        self.l_diagnose.grid(row=12, column=5, columnspan=6, sticky="nwse", pady=5)
        self.b_diagnose.grid(row=12, column=11, columnspan=1, pady=5)


        self.l_advanced = tk.Label(self, text="Advanced options*", font=fonts['title'], bg=Background['main'])

        self.l_guiver = tk.Label(self, text="GUI version", font=fonts['main'], bg=Background['main'])
        self.s_guiver = tk.Label(self, text="v" + Globals.guiver, font=fonts['main'], bg=Background['main'])

        self.l_fwver = tk.Label(self, text="Firmware version", font=fonts['main'], bg=Background['main'])
        self.s_fwver = tk.Label(self, text=Globals.fwver, font=fonts['main'], bg=Background['main'])

        self.l_reset = tk.Label(self, text="System reset", font=fonts['main'], bg=Background['main'])
        self.s_reset = tk.Label(self, text="", font=fonts['main'], bg=Background['main'], fg=Colours['darkgrey'])
        self.b_reset = tk.Button(self, width=8, height=1, text="RESET", font=fonts['submit'], bg=Background['submit'],
                                      command=lambda: self.reset(self.s_reset))
        self.l_fpup = tk.Label(self, text="Firmware update", font=fonts['main'], bg=Background['main'])
        self.s_fpup = tk.Label(self, text="", font=fonts['main'], bg=Background['main'], fg=Colours['darkgrey'])
        self.b_fpup = tk.Button(self, width=8, height=1, text="UPDATE", font=fonts['submit'], bg=Background['submit'],
                                      command=lambda: self.fpup(parent))

        self.l_debug = tk.Label(self, text="Silent mode", font=fonts['main'], bg=Background['main'])
        self.s_debug = tk.Label(self, text="", font=fonts['main'], bg=Background['main'], fg=Colours['darkgrey'])
        self.b_debug = tk.Button(self, width=8, height=1, text="START", font=fonts['submit'], bg=Background['submit'],
                                 command=lambda: self.debug(self.s_debug, self.b_debug, parent))


        self.l_read = tk.Label(self, text="Read register", font=fonts['main'], bg=Background['main'])
        self.s_read = tk.Label(self, text="", font=fonts['main'], bg=Background['main'], fg=Colours['darkgrey'])
        self.t_read= tk.Text(self, font=fonts['main'], width=10, height=1)
        self.b_read = tk.Button(self, width=8, height=1, text="READ", font=fonts['submit'], bg=Background['submit'],
                                 command=lambda: self.read(self.t_read,self.s_read))

        self.l_write = tk.Label(self, text="Write register", font=fonts['main'], bg=Background['main'])
        self.s_write = tk.Label(self, text="", font=fonts['main'], bg=Background['main'], fg=Colours['darkgrey'])
        self.t_write_address= tk.Text(self, font=fonts['main'], width=10, height=1)
        self.t_write_value = tk.Text(self, font=fonts['main'], width=10, height=1)
        self.b_write = tk.Button(self, width=8, height=1, text="WRITE", font=fonts['submit'], bg=Background['submit'],
                                 command=lambda: self.write(self.t_write_address,self.t_write_value, self.s_write))

        self.l_log = tk.Label(self, text="Log laser (s)", font=fonts['main'], bg=Background['main'])
        self.s_log = tk.Label(self, text="", font=fonts['main'], bg=Background['main'], fg=Colours['darkgrey'])
        self.t_log= tk.Text(self, font=fonts['main'], width=10, height=1)
        self.b_log = tk.Button(self, width=8, height=1, text="LOG", font=fonts['submit'], bg=Background['submit'],
                                 command=lambda: self.log(self.t_log,self.s_log, self.b_log))

        self.l_conv = tk.Label(self, text="Data format", font=fonts['main'], bg=Background['main'])
        self.conv_option = tk.StringVar(self)
        self.dtype = {
            'unsigned INT': "u",
            'signed INT': "i",
            'float': "f",
            'hex': "1",
            'string': "s",
            'time': "t"
        }
        self.s_conv = tk.OptionMenu(self, self.conv_option, *list(self.dtype.keys()))
        self.conv_option.set(list(self.dtype.keys())[3])

        self.l_conv2 = tk.Label(self, text="Conversion", font=fonts['main'], bg=Background['main'])
        self.conv2_option = tk.StringVar(self)
        self.dtype2 = {
            '1in1': "1",
            'micro': "u",
            'kelvin': "k",
        }
        self.s_conv2 = tk.OptionMenu(self, self.conv2_option, *list(self.dtype2.keys()))
        self.conv2_option.set(list(self.dtype2.keys())[0])


        self.l_how=tk.Label(self, text="*Please specify register values with a hex base", font=fonts['main'], bg=Background['main'])
        self.l_how2 = tk.Label(self, text="ie.hex: dfd4 or 0x00000000, enter address and value for write.", font=fonts['main'],
                              bg=Background['main'])
        self.l_disclaimer = tk.Label(self, text="Only use these options if you have no doubt.", font=fonts['main'], bg=Background['main'])

        self.l_reg = tk.Label(self, text="Reg export", font=fonts['main'], bg=Background['main'])
        self.s_reg = tk.Label(self, text="", font=fonts['main'], bg=Background['main'], fg=Colours['darkgrey'])
        self.t_reg_start= tk.Text(self, font=fonts['main'], width=10, height=1)
        self.t_reg_stop = tk.Text(self, font=fonts['main'], width=10, height=1)
        self.b_reg = tk.Button(self, width=8, height=1, text="WRITE", font=fonts['submit'], bg=Background['submit'],
                                 command=lambda: self.LH_read(self.t_reg_start,self.t_reg_stop, self.s_reg))

        # Advanced grid        self.l_device.grid(row=2, column=1, columnspan=2, sticky="nw", pady=5)
        self.l_logo.grid(row=0, column=15, columnspan=4, rowspan=1, sticky="e", pady=10)
        self.geths(self).grid(row=1, column=1, columnspan=19, sticky="we", pady=10)
        self.l_device.grid(row=2, column=1, columnspan=4, sticky="nw", pady=5)
        self.l_model.grid(row=3, column=1, columnspan=1, sticky="nw", pady=5)
        self.t_model.grid(row=3, column=2, columnspan=1, sticky="ne", pady=5)
        self.s_model.grid(row=3, column=3, columnspan=1, sticky="ne", pady=5)
        self.b_model.grid(row=3, column=4, columnspan=1, sticky="nw", pady=5)
        self.l_modell.grid(row=4, column=1, columnspan=1, sticky="nw", pady=5)
        self.t_modell.grid(row=4, column=2, columnspan=1, sticky="ne", pady=5)
        self.s_modell.grid(row=4, column=3, columnspan=1, sticky="ne", pady=5)
        self.b_modell.grid(row=4, column=4, columnspan=1, sticky="nw", pady=5)
        self.l_date.grid(row=5, column=1, columnspan=1, sticky="nw", pady=5)
        self.t_date.grid(row=5, column=2, columnspan=1, sticky="ne", pady=5)
        self.s_date.grid(row=5, column=3, columnspan=1, sticky="ne", pady=5)
        self.b_date.grid(row=5, column=4, columnspan=1, sticky="nw", pady=5)
        self.l_serial.grid(row=6, column=1, columnspan=1, sticky="nw", pady=5)
        self.t_serial.grid(row=6, column=2, columnspan=1, sticky="ne", pady=5)
        self.s_serial.grid(row=6, column=3, columnspan=1, sticky="ne", pady=5)
        self.b_serial.grid(row=6, column=4, columnspan=1, sticky="nw", pady=5)
        self.l_power.grid(row=7, column=1, columnspan=1, sticky="nw", pady=5)
        self.t_power.grid(row=7, column=2, columnspan=1, sticky="ne", pady=5)
        self.s_power.grid(row=7, column=3, columnspan=1, sticky="ne", pady=5)
        self.b_power.grid(row=7, column=4, columnspan=1, sticky="nw", pady=5)
        self.l_wavelength.grid(row=8, column=1, columnspan=1, sticky="nw", pady=5)
        self.t_wavelength.grid(row=8, column=2, columnspan=1, sticky="ne", pady=5)
        self.s_wavelength.grid(row=8, column=3, columnspan=1, sticky="ne", pady=5)
        self.b_wavelength.grid(row=8, column=4, columnspan=1, sticky="nw", pady=5)
        self.l_high.grid(row=9, column=1, columnspan=1, sticky="nw", pady=5)
        self.t_high.grid(row=9, column=2, columnspan=1, sticky="ne", pady=5)
        self.s_high.grid(row=9, column=3, columnspan=1, sticky="ne", pady=5)
        self.b_high.grid(row=9, column=4, columnspan=1, sticky="nw", pady=5)
        self.l_low.grid(row=10, column=1, columnspan=1, sticky="nw", pady=5)
        self.t_low.grid(row=10, column=2, columnspan=1, sticky="ne", pady=5)
        self.s_low.grid(row=10, column=3, columnspan=1, sticky="ne", pady=5)
        self.b_low.grid(row=10, column=4, columnspan=1, sticky="nw", pady=5)
        self.l_trial.grid(row=11, column=1, columnspan=1, sticky="nw", pady=5)
        self.t_trial.grid(row=11, column=2, columnspan=1, sticky="ne", pady=5)
        self.s_trial.grid(row=11, column=3, columnspan=1, sticky="ne", pady=5)
        self.b_trial.grid(row=11, column=4, columnspan=1, sticky="nw", pady=5)
        self.l_start.grid(row=12, column=1, columnspan=1, sticky="nw", pady=5)
        self.t_start.grid(row=12, column=2, columnspan=1, sticky="ne", pady=5)
        self.s_start.grid(row=12, column=3, columnspan=1, sticky="ne", pady=5)
        self.b_start.grid(row=12, column=4, columnspan=1, sticky="nw", pady=5)
        self.l_dur.grid(row=13, column=1, columnspan=1, sticky="nw", pady=5)
        self.t_dur.grid(row=13, column=2, columnspan=1, sticky="ne", pady=5)
        self.s_dur.grid(row=13, column=3, columnspan=1, sticky="ne", pady=5)
        self.b_dur.grid(row=13, column=4, columnspan=1, sticky="nw", pady=5)
        self.l_ban.grid(row=14, column=1, columnspan=1, sticky="nw", pady=5)
        self.t_ban.grid(row=14, column=2, columnspan=1, sticky="ne", pady=5)
        self.s_ban.grid(row=14, column=3, columnspan=1, sticky="ne", pady=5)
        self.b_ban.grid(row=14, column=4, columnspan=1, sticky="nw", pady=5)

        self.l_activate_title.grid(row=2, column=5, columnspan=4, sticky="nw", pady=5, padx=(10,0))

        self.l_advanced.grid(row=2, column=12, columnspan=4, sticky="nw", pady=5, padx=2)
        self.l_guiver.grid(row=3, column=12, columnspan=1, sticky="nw", pady=5, padx=2)
        self.s_guiver.grid(row=3, column=16, columnspan=1, sticky="nw", pady=5, padx=2)
        self.l_fwver.grid(row=4, column=12, columnspan=1, sticky="nw", pady=5, padx=2)
        self.s_fwver.grid(row=4, column=16, columnspan=1, sticky="nw", pady=5, padx=2)



        self.l_reset.grid(row=5, column=12, columnspan=1, sticky="nw", pady=5, padx=2)
        self.s_reset.grid(row=5, column=15, columnspan=1, sticky="nw", pady=5, padx=2)
        self.b_reset.grid(row=5, column=16, columnspan=1, sticky="nw", pady=5, padx=2)

        self.l_fpup.grid(row=6, column=12, columnspan=1, sticky="nw", pady=5, padx=2)
        self.s_fpup.grid(row=6, column=15, columnspan=1, sticky="nw", pady=5, padx=2)
        self.b_fpup.grid(row=6, column=16, columnspan=1, sticky="nw", pady=5, padx=2)

        self.l_debug.grid(row=7, column=12, columnspan=1, sticky="nw", pady=5, padx=2)
        self.s_debug.grid(row=7, column=13, columnspan=3, sticky="nw", pady=5, padx=2)
        self.b_debug.grid(row=7, column=16, columnspan=1, sticky="nw", pady=5, padx=2)

        self.l_read.grid(row=8, column=12, columnspan=1, sticky="nw", pady=5, padx=2)
        self.t_read.grid(row=8, column=13, columnspan=1, sticky="nw", pady=5, padx=2)
        self.s_read.grid(row=8, column=15, columnspan=1, sticky="nw", pady=5, padx=2)
        self.b_read.grid(row=8, column=16, columnspan=1, sticky="nw", pady=5, padx=2)

        self.l_write.grid(row=9, column=12, columnspan=1, sticky="nw", pady=5, padx=2)
        self.s_write.grid(row=9, column=15, columnspan=1, sticky="nw", pady=5, padx=2)
        self.t_write_address.grid(row=9, column=13, columnspan=1, sticky="nw", pady=5, padx=2)
        self.t_write_value.grid(row=9, column=14, columnspan=1, sticky="nw", pady=5, padx=2)
        self.b_write.grid(row=9, column=16, columnspan=1, sticky="nw", pady=5, padx=2)
        self.l_conv.grid(row=10, column=12, columnspan=1, sticky="nw", pady=5, padx=2)
        self.s_conv.grid(row=10, column=13, columnspan=1, sticky="nw", pady=5, padx=2)
        self.l_conv2.grid(row=10, column=14, columnspan=1, sticky="nw", pady=5, padx=2)
        self.s_conv2.grid(row=10, column=15, columnspan=2, sticky="nw", pady=5, padx=2)
        self.l_log.grid(row=11, column=12, columnspan=1, sticky="nw", pady=5, padx=2)
        self.t_log.grid(row=11, column=13, columnspan=1, sticky="nw", pady=5, padx=2)
        self.s_log.grid(row=11, column=15, columnspan=1, sticky="nw", pady=5, padx=2)
        self.b_log.grid(row=11, column=16, columnspan=1, sticky="nw", pady=5, padx=2)


        self.l_how.grid(row=12, column=12, columnspan=4, sticky="nw", pady=5, padx=2)
        self.l_how2.grid(row=13, column=12, columnspan=4, sticky="nw", padx=2)
        self.l_disclaimer.grid(row=14, column=12, columnspan=4, sticky="nw", pady=5, padx=2)

        self.l_reg.grid(row=15, column=12, columnspan=1, sticky="nw", pady=5, padx=2)
        self.s_reg.grid(row=15, column=15, columnspan=1, sticky="nw", pady=5, padx=2)
        self.t_reg_start.grid(row=15, column=13, columnspan=1, sticky="nw", pady=5, padx=2)
        self.t_reg_stop.grid(row=15, column=14, columnspan=1, sticky="nw", pady=5, padx=2)
        self.b_reg.grid(row=15, column=16, columnspan=1, sticky="nw", pady=5, padx=2)

    def reset(self, status):
        result=comm_reset()
        status.configure(text=result)
        Globals.errorreset = 1

    def debug(self, status, button, parent):
        print("GET STOPPED")
        for item in Globals.runnning_PROC:
            self.after_cancel(item)
        status.configure(text = "Silent mode started")
        button.configure(text = "STOP", command = lambda: self.stop_debug (status, button, parent))

    def stop_debug(self,status,button, parent):
        parent.disconnect()
        self.destroy()
        tk.messagebox.showinfo("Debug done", "Reconnect the laser head to continue.")
        status.configure(text = "Silent mode stopped")
        button.configure(text = "START", command = lambda: self.debug (status, button, parent))

    def read(self, address, status):
        target = address.get("1.0", 'end-1c')
        arg1 = self.dtype[self.conv_option.get()]
        arg2 = self.dtype2[self.conv2_option.get()]
        if target == "":
            status.configure(text = "Input error")
        else:
            result=getvalue(target, arg1, arg2)['value']
            status.configure(text=result)

    def log(self, time, status, button):
        Globals.logoff = 0
        try:
            time = int(1000 * float(time.get("1.0", 'end-1c'))-1000)
            if time < 2000:
                time = 2000
        except:
            time = 2000


        status.configure(text = "Running")
        button.configure(text = "STOP", bg=Colours['red'], fg=Colours["white"],
                         command=lambda: self.log_off(self.s_log, self.b_log))
        wl = getvalue(getaddress("lh", "wavelength"),"u","1")["value"]
        self.log_run(time, wl)

    def log_run(self, time, wl):
        if not Globals.logoff == 1:
            Logger_wrap(Globals.available, wl)

        self.timer_log = self.after(time, lambda: self.log_run(time, wl))
        Globals.runnning_PROC.append(self.timer_log)

    def log_off(self, status, button):
        Globals.logoff = 1
        button.configure(width=8, height=1, text="LOG", font=fonts['submit'], bg=Background['submit'], fg=Colours["black"],
                                 command=lambda: self.log(self.t_log,self.s_log, self.b_log))
        status.configure(text="Saved")
        self.after_cancel(self.timer_log)
    def diagnose(self):
        result = diagnose()
        result = ', '.join(result)
        self.l_diagnose.configure(text = "Available: " + result)
        return "break"

    def write(self, address, value, status):
        arg1 = self.dtype[self.conv_option.get()]
        arg2 = self.dtype2[self.conv2_option.get()]
        target = address.get("1.0", 'end-1c')
        val=value.get("1.0", 'end-1c')
        if target == "" or val == "":
            status.configure(text="Input error")
        else:
            setvalue(target, val, arg1,arg2)
            result = getvalue(target, arg1, arg2)['value']
            status.configure(text=result)

    def save_mod(self, input, status, var):
        target = input.get("1.0", 'end-1c')
        Info[var] = target
        f = open("dict/Info.json", "w+")
        f.write(json.dumps(Info))
        f.close()
        status.configure(text=target)
        #Globals.refresh=1

    def LH_read(self, start, stop, status):
        start=hex2uint(start.get("1.0", 'end-1c'))
        stop =hex2uint(stop.get("1.0", 'end-1c'))
        rang = start - stop
        query = np.linspace(start, stop, rang+1)
        regs = []
        values = []
        for i in query:
            reg = "0x" + uint2hex(i)[6:]
            value = getvalue(reg, "1", "1")["value"]
            regs.append(reg)
            values.append(value)

        df_folder = r"C:/UKL/"
        df = pandas.DataFrame(data={"Registers": regs, "Values": values})
        if not os.path.exists(df_folder):
            os.makedirs(df_folder)
        file = df_folder + "Registers_" + str(time.time()) + ".csv"
        df.to_csv(file, sep=',', index=False)
        showinfo("Data saved", "File written to C:/UKL/")
        status.configure(text = "Saved")

    def geths(self, parent):
        hs = ttk.Separator(parent, orient=tk.HORIZONTAL)
        return hs

    def reflush(self, master):

        master.update_idletasks()
        master_after = master.after(2500, lambda: self.reflush(master))

    def fpup(self, parent):
        currdir = r"C:/"
        fname = tk.filedialog.askopenfilename(initialdir=currdir, title="Select file",
                                           filetypes=[('All files','*.*'), ('Bin file','*.bin')])
        print(fname[-3:])
        if fname != "":
            if fname[-3:] =="bin":

                parent.disconnect()
                smmain('-p', Globals.COMport, '-w', '-v', '-e', fname)
                tk.messagebox.showinfo("Update done",f"The firmware has updated, please reboot system,\nthen click green cross on the main console to reconnect.")
                stop_COMM()
            else:
                tk.messagebox.showinfo("Wrong file", f"Select the provided binary (.bin) file.")

class activate(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

    def __call__(self, master, module, row, column):
        Names = Globals.Names


        self.l_title = tk.Label(master, text=module.upper(), font=fonts['main'], bg=Background['main'])
        self.b_activate = tk.Button(master, width=10, height=1, text="ACTIVATE", font=fonts['submit'],
                                    bg=Colours['green'], fg=Colours["white"],
                                    command= self.activate)
        self.b_deactivate = tk.Button(master, width=10, height=1, text="DEACTIVATE", font=fonts['submit'],
                                      bg=Colours['red'], fg=Colours["white"],
                                      command= self.deactivate)
        self.l_status = tk.Label(master, text=self.check(module), font=fonts['main'], bg=Background['main'])

        self.t_name = tk.Text(master, font=fonts['main'], width=10, height=1)
        self.s_name = tk.Label(master, text=Names[module.lower()], font=fonts['main'], bg=Background['main'],
                               fg=Colours['darkgrey'])
        self.b_name = tk.Button(master, width=8, height=1, text="RENAME", font=fonts['submit'], bg=Background['submit'],
                                command= self.rename)

        self.l_title.grid(row=row, column=column, columnspan=1, sticky="nw", pady=5, padx=(10, 2))
        self.b_activate.grid(row=row, column=column + 1, columnspan=1, sticky="nw", pady=5, padx=2)
        self.b_deactivate.grid(row=row, column=column + 2, columnspan=1, sticky="nw", pady=5, padx=2)
        self.l_status.grid(row=row, column=column + 3, columnspan=1, sticky="nw", pady=5, padx=2)
        self.t_name.grid(row=row, column=column + 4, columnspan=1, sticky="nw", pady=5, padx=2)
        self.s_name.grid(row=row, column=column + 5, columnspan=1, sticky="nw", pady=5, padx=2)
        self.b_name.grid(row=row, column=column + 6, columnspan=1, sticky="nw", pady=5, padx=2)

        self.module = module
        self.status = self.l_status
        self.input = self.t_name
        self.status_rename = self.s_name


    def activate(self):
        base = self.module
        status = self.status
        if Globals.Toplevel == 1:
            baseval=CONFIG.activate[base.lower()]
            bit=int(math.log(baseval,2))
            if getbit(CONFIG.activate['address'], bit) == "1":
                status.configure(text="on")
            else:
                val=getvalue(CONFIG.activate['address'])['value']
                setvalue(CONFIG.activate['address'], val+baseval)
                comm_init()
                Globals.available.append(base)
                status.configure(text="on")
                Globals.incident_message = base.upper() + " has been activated. \n"
                Globals.refresh = 1
                exec("Globals." + base.lower() + "r" + "= 1")
                print(eval("Globals." + base.lower() + "r"))
        return "break"


    def deactivate(self):
        base = self.module
        status = self.status
        if Globals.Toplevel == 1:
            baseval = CONFIG.activate[base.lower()]
            bit = int(math.log(baseval, 2))
            if getbit(CONFIG.activate['address'], bit) != "1":
                status.configure(text="off")
            else:
                val = getvalue(CONFIG.activate['address'])['value']
                setvalue(CONFIG.activate['address'], val - baseval)
                comm_init()
                Globals.available.remove(base)
                status.configure(text="off")
                Globals.incident_message = base.upper() + " has been deactivated. \n"
                Globals.refresh = 1
        return "break"

    def rename(self):
        module = self.module
        input = self.input
        status = self.status_rename
        if Globals.Toplevel == 1:
            target = input.get("1.0", 'end-1c')
            setvalue(getaddress("gui", module.lower()), target, "s", "1")
            Globals.Names[module.lower()] = target
            # f = open("dict/Names.json", "w+")
            # f.write(json.dumps(Names))
            # f.close()
            status.configure(text=target)
            Globals.refresh=1
            Globals.incident_message = module.upper() + " has been renamed. \n"

    def check(self, module):
        if module in Globals.available:
            return "on"
        else:
            return "n/a"

