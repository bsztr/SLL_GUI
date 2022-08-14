import tkinter as tk
from CONFIG import *
from COMM import *
from init_start import *
from tkinter import ttk
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use("TkAgg")
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import pandas, os
from Dynamic import *
from tkinter.messagebox import showinfo

class LockArch(tk.Frame):
    def __init__(self, master, title, base, y):
        tk.Frame.__init__(self, master)

        self.base = base
        self.pady=2
        self.configure(bg=Background['main'])

        self.pzttype = {"PZT1": "digital driver","PZT2":"analogue driver","PZTA":"analogue driver","PZTQ":"quantum driver"}
        try:
            self.pztselect = self.pzttype[eval("Globals." + base+"type")]
        except KeyError:
            self.pztselect = "unknown driver"



        self.l_title = tk.Label(master, text=title + " (" + str(self.pztselect) + ")", font=fonts['title'], bg=Background['main'])

        self.l_p = tk.Label(master, text="P gain", font=fonts['main'], bg=Background['main'])
        self.t_p = tk.Text(master, width=6, height=1)
        self.s_p = pzt_label(self.master)

        if "analogue" in self.pztselect:
            retrieve_r_q( base+"_d", "p", self.s_p)
            self.tt_p = tk.Text(master, width=6, height=1)
            self.tt_p.grid(row=4, column=y + 1, columnspan=1, sticky="nw", pady=self.pady)
            self.b_p = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                 command=lambda: submit_r_q(self, base+"_d", "p", 0, 255))
        elif "quantum" in self.pztselect:
            retrieve_r_q( base+"_d", "p", self.s_p, "quantum")
            self.b_p = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                 command=lambda: submit_r(self, base+"_d", "p", 0, 1023))

        else:
            self.s_p.update_status(getaddress(base + "_d", "p"), "p", "driver")
            self.b_p = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                 command=lambda: submit(self, base+"_d", "p"))

        self.l_i = tk.Label(master, text="I gain", font=fonts['main'], bg=Background['main'])
        self.t_i = tk.Text(master, width=6, height=1)
        self.s_i = pzt_label(self.master)

        if "analogue" in self.pztselect:
            retrieve_r_q(base + "_d", "i", self.s_i)
            self.tt_i = tk.Text(master, width=6, height=1)
            self.tt_i.grid(row=6, column=y + 1, columnspan=1, sticky="nw", pady=self.pady)
            self.b_i = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                 command=lambda: submit_r_q(self, base+"_d", "i", 0, 255))
        elif "quantum" in self.pztselect:
            retrieve_r_q( base+"_d", "i", self.s_i, "quantum")
            self.b_i = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                 command=lambda: submit_r(self, base+"_d", "i", 0, 1023))

        else:
            self.s_i.update_status(getaddress(base + "_d", "i"), "i", "driver")
            self.b_i = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                 command=lambda: submit(self, base+"_d", "i"))

        self.l_d = tk.Label(master, text="D gain", font=fonts['main'], bg=Background['main'])
        self.t_d = tk.Text(master, width=6, height=1)
        self.s_d = pzt_label(self.master)

        if "analogue" in self.pztselect:
            retrieve_r_q(base + "_d", "d", self.s_d)
            self.tt_d = tk.Text(master, width=6, height=1)
            self.tt_d.grid(row=8, column=y + 1, columnspan=1, sticky="nw", pady=self.pady)
            self.b_d = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                 command=lambda: submit_r_q(self, base+"_d", "d", 0, 255))
        elif "quantum" in self.pztselect:
            retrieve_r_q(base + "_d", "d", self.s_d, "quantum")
            self.b_d = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                 command=lambda: submit_r(self, base+"_d", "d", 0, 1023))

        else:
            self.s_d.update_status(getaddress(base + "_d", "d"), "d", "driver")
            self.b_d = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                 command=lambda: submit(self, base+"_d", "d"))

        self.l_cmin = tk.Label(master, text="Lock window, min (V)", font=fonts['main'], bg=Background['main'])
        self.t_cmin = tk.Text(master, width=6, height=1)
        self.s_cmin = pzt_label(self.master)
        self.s_cmin.update_status(getaddress(base + "_d", "cmin"), "cmin", "driver")
        self.b_cmin = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                             command=lambda: submit(self, base+"_d", "cmin"))

        self.l_cmax = tk.Label(master, text="Lock window, max (V)", font=fonts['main'], bg=Background['main'])
        self.t_cmax = tk.Text(master, width=6, height=1)
        self.s_cmax = pzt_label(self.master)
        self.s_cmax.update_status(getaddress(base + "_d", "cmax"), "cmax", "driver")
        self.b_cmax = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                             command=lambda: submit(self, base+"_d", "cmax"))

        self.l_offset = tk.Label(master, text="Reg offset (V)", font=fonts['main'], bg=Background['main'])
        self.t_offset = tk.Text(master, width=6, height=1)
        self.s_offset = pzt_label(self.master)
        self.s_offset.update_status(getaddress(base + "_d", "offset"), "offset", "driver")
        self.b_offset = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                             command=lambda: submit(self, base+"_d", "offset"))

        self.l_adelay = tk.Label(master, text="Activation delay (s)", font=fonts['main'], bg=Background['main'])
        self.t_adelay = tk.Text(master, width=6, height=1)
        self.s_adelay = pzt_label(self.master)
        self.s_adelay.update_status(getaddress(base + "_d", "adelay"), "p", "adelay")
        self.b_adelay = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                             command=lambda: submit(self, base+"_d", "adelay"))

        self.l_difftitle=tk.Label(master, text="Diff Photodiode Settings", font=fonts['title'], bg=Background['main'])

        self.l_dpota_cr = tk.Label(master, text="Diff A Input(0 to 255)", font=fonts['main'], bg=Background['main'])
        self.t_dpota_cr = tk.Text(master, width=6, height=1)
        self.s_dpota_cr = pzt_label(self.master)
        self.s_dpota_cr.update_status(getaddress(base + "_d", "dpota_cr"), "dpota_cr", "driver")
        self.b_dpota_cr = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                command=lambda: submit_r(self, base + "_d", "dpota_cr",0,255))

        self.l_dpota_amp = tk.Label(master, text="Diff A Gain(0 to 255)", font=fonts['main'], bg=Background['main'])
        self.t_dpota_amp = tk.Text(master, width=6, height=1)
        self.s_dpota_amp = pzt_label(self.master)
        self.s_dpota_amp.update_status(getaddress(base + "_d", "dpota_amp"), "dpota_amp", "driver")
        self.b_dpota_amp = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                command=lambda: submit_r(self, base + "_d", "dpota_amp",0,255))

        self.l_dpotb_cr = tk.Label(master, text="Diff B Input(0 to 255)", font=fonts['main'], bg=Background['main'])
        self.t_dpotb_cr = tk.Text(master, width=6, height=1)
        self.s_dpotb_cr = pzt_label(self.master)
        self.s_dpotb_cr.update_status(getaddress(base + "_d", "dpotb_cr"), "dpotb_cr", "driver")
        self.b_dpotb_cr = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'],
                                     bg=Background['submit'],
                                     command=lambda: submit_r(self, base + "_d", "dpotb_cr",0,255))

        self.l_dpotb_amp = tk.Label(master, text="Diff B Gain(0 to 255)", font=fonts['main'], bg=Background['main'])
        self.t_dpotb_amp = tk.Text(master, width=6, height=1)
        self.s_dpotb_amp = pzt_label(self.master)
        self.s_dpotb_amp.update_status(getaddress(base + "_d", "dpotb_amp"), "dpotb_amp", "driver")
        self.b_dpotb_amp = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'],
                                     bg=Background['submit'],
                                     command=lambda: submit_r(self, base + "_d", "dpotb_amp",0,255))

        self.l_dpot_sampl = tk.Label(master, text="Sampling (ms)", font=fonts['main'], bg=Background['main'])
        self.t_dpot_sampl = tk.Text(master, width=6, height=1)
        self.b_dpot_sampl = tk.Button(master, width=3, height=1, text="Plot", font=fonts['submit'],
                                  bg=Background['plot'], fg="white",
                                  command=lambda: self.plot(base, "DPhD power", "dp_power", self.t_dpot_sampl))


        self.l_clptitle = tk.Label(master, text="CLP Photodiode Settings", font=fonts['title'], bg=Background['main'])

        self.l_clp_ci = tk.Label(master, text="CLP V-I Conversion", font=fonts['main'], bg=Background['main'])
        self.t_clp_ci = tk.Text(master, width=6, height=1)
        self.s_clp_ci = pzt_label(self.master)
        self.s_clp_ci.update_status(getaddress(base + "_d", "clp_ci"), "clp_ci", "driver")
        self.b_clp_ci = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'],
                                  bg=Background['submit'],
                                  command=lambda: submit(self, base + "_d", "clp_ci"))

        self.l_clp_cr = tk.Label(master, text="CLP Input(0 to 255)", font=fonts['main'], bg=Background['main'])
        self.t_clp_cr = tk.Text(master, width=6, height=1)
        self.s_clp_cr = pzt_label(self.master)
        self.s_clp_cr.update_status(getaddress(base + "_d", "clp_cr"), "clp_cr", "driver")
        self.b_clp_cr = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'],
                                   bg=Background['submit'],
                                   command=lambda: submit_r(self, base + "_d", "clp_cr",0,255))

        self.l_clp_amp = tk.Label(master, text="CLP Gain(0 to 255)", font=fonts['main'], bg=Background['main'])
        self.t_clp_amp = tk.Text(master, width=6, height=1)
        self.s_clp_amp = pzt_label(self.master)
        self.s_clp_amp.update_status(getaddress(base + "_d", "clp_amp"), "clp_amp", "driver")
        self.b_clp_amp = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'],
                                     bg=Background['submit'],
                                     command=lambda: submit_r(self, base + "_d", "clp_amp",0,255))

        self.l_clp_power = tk.Label(master, text="CLP Power (W)", font=fonts['main'], bg=Background['main'])
        self.s_clp_power = pzt_label(self.master)
        self.s_clp_power.update_clp(self.s_clp_power)

        self.l_clptitle = tk.Label(master, text="CLP Photodiode Settings", font=fonts['title'], bg=Background['main'])

        self.l_clp_sampl = tk.Label(master, text="Sampling (ms)", font=fonts['main'], bg=Background['main'])
        self.t_clp_sampl = tk.Text(master, width=6, height=1)
        self.b_clp_sampl = tk.Button(master, width=3, height=1, text="Plot", font=fonts['submit'],
                                  bg=Background['plot'], fg="white",
                                  command=lambda: self.plot(base, "CLP power", "clp_power", self.t_clp_sampl))


        #Secondary display
        self.l_parkp = tk.Label(master, text="Park position (V)", font=fonts['main'], bg=Background['main'])
        self.t_parkp = tk.Text(master, width=13, height=1)

        # self.s_parkp = pzt_label(self.master)
        # self.s_parkp.update_status(getaddress(base + "_d", "park"), "park", "driver")
        self.b_park = tk.Button(master, text="PARK", bg=Colours['orange'], fg="white", width=9, font=fonts['status'],
                                command=lambda: self.park(base, self.t_parkp))

        self.l_park = tk.Label(master, text="Set voltage (V)", font=fonts['main'], bg=Background['main'])
        self.s_park = pzt_label(self.master)
        self.s_park.update_voltage(base, "ov")
        self.b_park_sampl = tk.Button(master, width=3, height=1, text="Plot", font=fonts['submit'],
                                     bg=Background['plot'], fg="white",
                                     command=lambda: self.plot(base, "PZT Voltage", "ov"))

        self.l_rate = tk.Label(master, text="Ramp rate (V/step)", font=fonts['main'], bg=Background['main'])
        self.t_rate = tk.Text(master, width=12, height=1, font=fonts['status'])
        self.s_rate = pzt_label(self.master)
        self.s_rate.update_status(getaddress(base + "_d", "rate"), "rate", "driver")
        self.b_rate = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                             command=lambda: submit(self, base+"_d", "rate"))


        self.l_control = tk.Label(master, text= base.upper() + " Control", font=fonts['title'], bg=Background['main'])
        self.b_lock= tk.Button(master, text="Lock/Relock", width=15, bg=Colours['grey'], font=fonts['main'], command= lambda: self.lock(base))
        self.b_scan=tk.Button(master, text="Ramp",bg=Colours['lightgrey'], fg="black", width=15, font=fonts['main'], command= lambda: self.ramp(base))
        #self.b_park=tk.Button(master, text="Park",bg=Colours['orange'], fg="white", width=9, font=fonts['main'], command= lambda: self.park(base))

        self.status=tk.Label(master, text="Status:     ", font=fonts['title'], bg=Background['main'])
        self.formatstatus(self.status, base)

        self.l_lockm = tk.Label(master, text="Lock mechanism", font=fonts['main'], bg=Background['main'])
        self.lock_option=tk.StringVar(master)
        self.t_lockm=tk.OptionMenu(master, self.lock_option, *lock_mech)
        self.t_lockm.config(font=fonts['main'], bg=Background['main'], height=1, width=9)
        self.s_lockm = lockm_label(self.master)
        self.s_lockm.read_lockm(base+"_d", self.lock_option)
        self.b_lockm = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                command= self.write_lockm)

        self.l_phase = tk.Label(master, text="Phase reverse(1 or 0)", font=fonts['main'], bg=Background['main'])
        self.t_phase = tk.Text(master, width=12, height=1, font=fonts['status'])
        self.s_phase = pzt_label_bit(self.master)
        self.s_phase.update_status(base + "_d",5,"lockm")
        self.b_phase = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                             command=lambda: self.phaserev(self.t_phase, self.s_phase, base))

        self.b_advanced = tk.Button(master, text="Advanced settings", width=20, font=fonts['main'], bg=Background['submit'],
                                  command=lambda: self.openadvance(master, base))

        self.pzt_ramp = iterate(master, "Scan voltage", base, "ov", 13, y+5, True)

        self.l_errorl = tk.Label(master, text="Error signal acquisition", font=fonts['title'], bg=Background['main'])
        self.l_errord = tk.Label(master, text="Ensure system is locked!", font=fonts['main'], bg=Background['main'])
        self.l_errorc = tk.Label(master, text="This operation will take at least one hour to complete.", font=fonts['main'], bg=Background['main'])
        self.b_errorb = tk.Button(master, text="ACQUIRE", bg=Background['main'], width=9, font=fonts['status'],
                                command=lambda: self.signalac(base))
        self.minv = round(getvalue(getaddress(base+"_d", "min"), "u", "u")["value"],1)
        self.maxv = round(getvalue(getaddress(base + "_d", "max"), "u", "u")["value"],1)
        self.error_min = tk.Label(master, text="Min: " + str(self.minv) + " V", font=fonts['main'], bg=Background['main'])
        self.error_max = tk.Label(master, text="Max: " + str(self.maxv) + " V", font=fonts['main'], bg=Background['main'])



        #20

        self.l_title.grid(row=2, column=y, columnspan=2, sticky="nw", pady=self.pady)
        self.l_p.grid(row=3, column=y, columnspan=1, sticky="nw", pady=self.pady)
        self.t_p.grid(row=3, column=y + 1, columnspan=1, sticky="nw", pady=self.pady)
        self.s_p.grid(row=3, column=y+2, columnspan=1, sticky="nw", pady=self.pady)
        self.b_p.grid(row=3, column=y + 3, columnspan=1, sticky="nw", pady=self.pady)
        self.l_i.grid(row=5, column=y, columnspan=1, sticky="nw", pady=self.pady)
        self.t_i.grid(row=5, column=y + 1, columnspan=1, sticky="nw", pady=self.pady)
        self.s_i.grid(row=5, column=y + 2, columnspan=1, sticky="nw", pady=self.pady)
        self.b_i.grid(row=5, column=y + 3, columnspan=1, sticky="nw", pady=self.pady)
        self.l_d.grid(row=7, column=y, columnspan=1, sticky="nw", pady=self.pady)
        self.t_d.grid(row=7, column=y + 1, columnspan=1, sticky="nw", pady=self.pady)
        self.s_d.grid(row=7, column=y + 2, columnspan=1, sticky="nw", pady=self.pady)
        self.b_d.grid(row=7, column=y + 3, columnspan=1, sticky="nw", pady=self.pady)
        self.l_cmin.grid(row=9, column=y, columnspan=1, sticky="nw", pady=self.pady)
        self.t_cmin.grid(row=9, column=y + 1, columnspan=1, sticky="nw", pady=self.pady)
        self.s_cmin.grid(row=9, column=y + 2, columnspan=1, sticky="nw", pady=self.pady)
        self.b_cmin.grid(row=9, column=y + 3, columnspan=1, sticky="nw", pady=self.pady)
        self.l_cmax.grid(row=10, column=y, columnspan=1, sticky="nw", pady=self.pady)
        self.t_cmax.grid(row=10, column=y + 1, columnspan=1, sticky="nw", pady=self.pady)
        self.s_cmax.grid(row=10, column=y + 2, columnspan=1, sticky="nw", pady=self.pady)
        self.b_cmax.grid(row=10, column=y + 3, columnspan=1, sticky="nw", pady=self.pady)
        self.l_offset.grid(row=11, column=y, columnspan=1, sticky="nw", pady=self.pady)
        self.t_offset.grid(row=11, column=y + 1, columnspan=1, sticky="nw", pady=self.pady)
        self.s_offset.grid(row=11, column=y + 2, columnspan=1, sticky="nw", pady=self.pady)
        self.b_offset.grid(row=11, column=y + 3, columnspan=1, sticky="nw", pady=self.pady)
        self.l_adelay.grid(row=12, column=y, columnspan=1, sticky="nw", pady=self.pady)
        self.t_adelay.grid(row=12, column=y + 1, columnspan=1, sticky="nw", pady=self.pady)
        self.s_adelay.grid(row=12, column=y + 2, columnspan=1, sticky="nw", pady=self.pady)
        self.b_adelay.grid(row=12, column=y + 3, columnspan=1, sticky="nw", pady=self.pady)

        self.l_difftitle.grid(row=13, column=y, columnspan=4, sticky="nw", pady=self.pady)
        self.l_dpota_cr.grid(row=14, column=y, columnspan=1, sticky="nw", pady=self.pady)
        self.t_dpota_cr.grid(row=14, column=y+1, columnspan=1, sticky="nw", pady=self.pady)
        self.s_dpota_cr.grid(row=14, column=y+2, columnspan=1, sticky="nw", pady=self.pady)
        self.b_dpota_cr.grid(row=14, column=y + 3, columnspan=1, sticky="nw", pady=self.pady)
        self.l_dpota_amp.grid(row=15, column=y, columnspan=1, sticky="nw", pady=self.pady)
        self.t_dpota_amp.grid(row=15, column=y+1, columnspan=1, sticky="nw", pady=self.pady)
        self.s_dpota_amp.grid(row=15, column=y+2, columnspan=1, sticky="nw", pady=self.pady)
        self.b_dpota_amp.grid(row=15, column=y + 3, columnspan=1, sticky="nw", pady=self.pady)
        self.l_dpotb_cr.grid(row=16, column=y, columnspan=1, sticky="nw", pady=self.pady)
        self.t_dpotb_cr.grid(row=16, column=y+1, columnspan=1, sticky="nw", pady=self.pady)
        self.s_dpotb_cr.grid(row=16, column=y+2, columnspan=1, sticky="nw", pady=self.pady)
        self.b_dpotb_cr.grid(row=16, column=y + 3, columnspan=1, sticky="nw", pady=self.pady)
        self.l_dpotb_amp.grid(row=17, column=y, columnspan=1, sticky="nw", pady=self.pady)
        self.t_dpotb_amp.grid(row=17, column=y+1, columnspan=1, sticky="nw", pady=self.pady)
        self.s_dpotb_amp.grid(row=17, column=y+2, columnspan=1, sticky="nw", pady=self.pady)
        self.b_dpotb_amp.grid(row=17, column=y + 3, columnspan=1, sticky="nw", pady=self.pady)
        self.l_dpot_sampl.grid(row=18, column=y, columnspan=1, sticky="nw", pady=self.pady)
        self.t_dpot_sampl.grid(row=18, column=y+1, columnspan=1, sticky="nw", pady=self.pady)
        self.b_dpot_sampl.grid(row=18, column=y+3, columnspan=1, sticky="nw", pady=self.pady)

        self.l_clptitle.grid(row=19, column=y, columnspan=4, sticky="nw", pady=self.pady)
        self.l_clp_ci.grid(row=20, column=y, columnspan=1, sticky="nw", pady=self.pady)
        self.t_clp_ci.grid(row=20, column=y+1, columnspan=1, sticky="nw", pady=self.pady)
        self.s_clp_ci.grid(row=20, column=y+2, columnspan=1, sticky="nw", pady=self.pady)
        self.b_clp_ci.grid(row=20, column=y+3, columnspan=1, sticky="nw", pady=self.pady)
        self.l_clp_cr.grid(row=21, column=y, columnspan=1, sticky="nw", pady=self.pady)
        self.t_clp_cr.grid(row=21, column=y+1, columnspan=1, sticky="nw", pady=self.pady)
        self.s_clp_cr.grid(row=21, column=y+2, columnspan=1, sticky="nw", pady=self.pady)
        self.b_clp_cr.grid(row=21, column=y+3, columnspan=1, sticky="nw", pady=self.pady)
        self.l_clp_amp.grid(row=22, column=y, columnspan=1, sticky="nw", pady=self.pady)
        self.t_clp_amp.grid(row=22, column=y+1, columnspan=1, sticky="nw", pady=self.pady)
        self.s_clp_amp.grid(row=22, column=y+2, columnspan=1, sticky="nw", pady=self.pady)
        self.b_clp_amp.grid(row=22, column=y+3, columnspan=1, sticky="nw", pady=self.pady)
        self.l_clp_power.grid(row=23, column=y, columnspan=1, sticky="nw", pady=self.pady)
        self.s_clp_power.grid(row=23, column=y+1, columnspan=3, sticky="nwes", pady=self.pady)
        self.l_clp_sampl.grid(row=24, column=y, columnspan=1, sticky="nw", pady=self.pady)
        self.t_clp_sampl.grid(row=24, column=y+1, columnspan=1, sticky="nw", pady=self.pady)
        self.b_clp_sampl.grid(row=24, column=y+3, columnspan=1, sticky="nw", pady=self.pady)


        self.getvs(master).grid(row=1, column=y+4, rowspan=22, sticky="ns", padx=10)

        self.l_control.grid(row=2, column=y+5, columnspan=2, sticky="nw", pady=self.pady)
        self.status.grid(row=2, column=y + 7, columnspan=1, sticky="nw", pady=self.pady)
        self.b_lock.grid(row=3, column=y+5, columnspan=1, sticky="nw", pady=self.pady, padx=2)
        self.b_scan.grid(row=3, column=y+6, columnspan=1, sticky="nw", pady=self.pady, padx=2)
        self.b_park.grid(row=5, column=y+7, columnspan=2, sticky="nw", pady=3*self.pady, padx=2)
        self.l_parkp.grid(row=5, column=y+5, columnspan=1, sticky="nw", pady=4*self.pady)
        self.t_parkp.grid(row=5, column=y+6, columnspan=1, sticky="nw", pady=4*self.pady)
        #self.s_parkp.grid(row=5, column=y + 7, columnspan=1, sticky="nwse", pady=3 * self.pady, padx=2)
        self.l_park.grid(row=7, column=y+5, columnspan=1, sticky="nw", pady=self.pady)
        self.s_park.grid(row=7, column=y+6, columnspan=1, sticky="nw", pady=self.pady)
        self.b_park_sampl.grid(row=7, column=y + 8, columnspan=1, sticky="nw", pady=self.pady)
        self.l_rate.grid(row=9, column=y+5, columnspan=1, sticky="nw", pady=self.pady)
        self.t_rate.grid(row=9, column=y+6, columnspan=1, sticky="nw", pady=self.pady)
        self.s_rate.grid(row=9, column=y+7, columnspan=1, sticky="nwse", pady=self.pady)
        self.b_rate.grid(row=9, column=y+8, columnspan=1, sticky="nw", pady=self.pady)

        self.l_lockm.grid(row=10, column=y + 5, columnspan=1, sticky="nw", pady=self.pady)
        self.t_lockm.grid(row=10, column=y + 6, columnspan=1, sticky="nw", pady=self.pady)
        self.s_lockm.grid(row=10, column=y + 7, columnspan=1, sticky="nwse", pady=self.pady)
        self.b_lockm.grid(row=10, column=y + 8, columnspan=1, sticky="nw", pady=self.pady)
        self.l_phase.grid(row=11, column=y + 5, columnspan=1, sticky="nw", pady=self.pady)
        self.t_phase.grid(row=11, column=y + 6, columnspan=1, sticky="nw", pady=self.pady)
        self.s_phase.grid(row=11, column=y + 7, columnspan=1, sticky="nwse", pady=self.pady)
        self.b_phase.grid(row=11, column=y + 8, columnspan=1, sticky="nw", pady=self.pady)
        self.b_advanced.grid(row=12, column=y + 5, columnspan=2, sticky="nw", pady=self.pady)

        self.getvs(master).grid(row=1, column=y + 9, rowspan=22, sticky="ns", padx=10)

        self.l_errorl.grid(row=19, column=y+5, columnspan=3, sticky="nw", pady=self.pady)
        self.l_errord.grid(row=20, column=y+5, columnspan=4, sticky="nw", pady=self.pady, padx=2)
        self.b_errorb.grid(row=21, column=y + 5, columnspan=1, sticky="nw", pady=self.pady, padx=2)
        self.error_max.grid(row=21, column=y + 6, columnspan=1, sticky="nw", pady=self.pady, padx=2)
        self.error_min.grid(row=21, column=y + 7, columnspan=2, sticky="nw", pady=self.pady, padx=2)

    def geths(self, parent):
            hs = ttk.Separator(parent, orient=tk.HORIZONTAL)
            return hs

    def getvs(self, parent):
            vs = ttk.Separator(parent, orient=tk.VERTICAL)
            return vs

    def get_lockm(self,b):
        address=getaddress(b,"lockm")
        arg1=eval(base[b][1])["lockm"][1]
        arg2=eval(base[b][1])["lockm"][2]
        self.lock=int(getvalue(address, arg1, arg2)['value'])

    def ramp(self, bas):
        actual = getvalue(control['address'])['value']
        if bas=="pzt0":
            bit=[8,6]
        else:
            bit=[9,7]
        if readbit(actual, 1) != "1":
            addvalue(control['address'], 2)

        if readbit(actual, bit[1]) == "1":
            resvalue(control['address'], control[bas + "_m"])
            actual=actual-control[bas + "_m"]

        if readbit(actual, bit[0]) == "1":
            resvalue(control['address'], control[bas + "_l"])
            actual=actual-control[bas + "_l"]

        Globals.incident_message=bas.upper() + " is now ramping."

    def park(self, bas, text):

        actual = getvalue(control['address'])['value']
        if bas=="pzt0":
            bit=[8,6]
        else:
            bit=[9,7]
        if readbit(actual, 1) != "1":
            addvalue(control['address'], 2)
        if readbit(actual, bit[1]) == "0":
            setvalue(control['address'], actual+control[bas + "_m"])
            actual=actual+control[bas + "_m"]
        if readbit(actual, bit[0]) == "1":
            resvalue(control['address'], control[bas + "_l"])
            actual=actual-control[bas + "_l"]

        instance = float(text.get("1.0", 'end-1c'))
        setvalue(getaddress(bas, "ov"), instance,"u" ,"u")

        Globals.incident_message = bas.upper() + " is now parked."

    def lock(self, bas):
        actual = getvalue(control['address'])['value']
        if bas=="pzt0":
            bit=[8,6]
        else:
            bit=[9,7]

        if readbit(actual, 1) != "1":
            addvalue(control['address'], 2)
        if readbit(actual, bit[1]) == "1":
            resvalue(control['address'], control[bas + "_m"])
            actual=actual-control[bas + "_m"]
        if readbit(actual, bit[0]) == "0":
            setvalue(control['address'], actual+control[bas + "_l"])
            actual=actual+control[bas + "_l"]
        else:
            setvalue(base[bas][0], "0x4043b000", "1", "1")
            Globals.incident_message = bas.upper() + " is now relocked."

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
            return "OFF","grey"
        else:
            if lock==0:
                if manual==0:
                    return "RAMPING","blue"

                if manual==1:
                    return "PARK", "orange"
            if lock==1:
                if manual==0:
                    if readbit(actual, 21) == "1":
                        return "LOCKED", "darkgreen"
                    else:
                        return "LOCKING", "green"
                else:
                    return "ERROR", "red"
            else:
                return "ERROR", "red"

    def formatstatus(self, text, bas):
        result = self.getstatus(bas)
        text.configure(text="Status: " + result[0], fg = result[1])
        status_after = text.after(2000, lambda: self.formatstatus(text, bas))

    def write_lockm(self):
        b = self.base+"_d"
        status = self.s_lockm
        address=getaddress(b,"lockmode")
        val=self.lock_option.get()

        #print(val)
        if val != "":
            arg1=eval(base[b][1])["lockmode"][1]
            arg2=eval(base[b][1])["lockmode"][2]
            # curr = getbit(address, 5)
            # if curr == "1":
            #     addit = 32
            # else:
            #     addit = 0

            val=lock_dict.get(val, 2)#+addit
            setvalue(address, val, arg1, arg2)
            status.read_lockm(b, self.lock_option)
        else:
            showinfo("Error","Select a lock mode.")

    def plot(self, base, subject, type="clp", interval=1000):
        if interval == 1000 or interval.get("1.0", 'end-1c') == "":
            self.duration = 1000
        else:
            self.duration=int(round(float(interval.get("1.0", 'end-1c')),0))
        plot=graph(self, base, subject, type)

    def phaserev(self, instance, status, base):
        address = getaddress(base+"_d", "lockm")
        instance = int(instance.get("1.0", 'end-1c'))
        if instance == 0:
            if getbit(address, 5) == "1":
                resvalue(address, 32)
                print(getvalue(address)["value"])
                status.configure(text="off")
            else:
                status.configure(text="already off")
        elif instance == 1:
            if getbit(address, 5) == "0":
                addvalue(address, 32)
                print(getvalue(address)["value"])
                status.configure(text = "on")
            else:
                status.configure(text="already on")
        else:
            status.configure(text = "not valid")

    def signalac(self, base):
        plot = graph_error(self, base)

    def openadvance(self, master, base):
        adv = advanced(master, base)

class lockm_label(tk.Label):

    def __init__(self, parent):
        tk.Label.__init__(self, parent)


    def read_lockm(self, b, s):

        address=getaddress(b,"lockmode")
        arg1=eval(base[b][1])["lockmode"][1]
        arg2=eval(base[b][1])["lockmode"][2]
        self.lock=int(getvalue(address, arg1, arg2)['value'])
        # curr = readbit(self.lock, 5)
        # if curr == "1":
        #     addit = 32
        # else:
        #     addit = 0
        # self.lock = self.lock - addit
        mech=lock_dict.get(self.lock)
        try:
            value = lock_mech.index(mech)
            s.set(mech)

        except ValueError:
            value = 0
            s.set("Not selected.")


        self.configure(text=mech, fg=Colours['darkgrey'], font=fonts['status'],
                       bg=Background['main'])

class graph(tk.Toplevel):

    def __init__(self, master, b, subject, rel):
        tk.Toplevel.__init__(self)
        # self.grab_set()
        self.configure(background=Background['main'])
        self.geometry("750x600")
        self.title("Plotting")
        self.address = getaddress(b, rel)
        self.arg1 = eval(base[b][1])[rel][1]
        self.arg2 = eval(base[b][1])[rel][2]
        self.interval = master.duration
        self.x = []
        self.y = []
        self.z = []
        self.base = b
        #self.check = box.get()
        self.run = self.setup(master, b, subject)

    def setup(self, master, b, subject):

        l = tk.Label(self, text=subject.upper() + " is being plotted for " + b.upper() + ".",
                     bg=Background['main'], font=fonts['title'])
        l.grid(row=0, column=0, columnspan=8, sticky="esnw", pady=(15, 0))

        b1 = tk.Button(self, text="Done", command=self.destroy, font=fonts['main'], bg=Background['submit'])
        # if self.check == 1:
        #     b2 = tk.Button(self, text="Write", command=lambda: self.write(self.x, self.y, self.z, True),
        #                    font=fonts['main'],
        #                    bg=Background['submit'])
        #else:
        b2 = tk.Button(self, text="Write", command=lambda: self.write(self.x, self.y, subject), font=fonts['main'],
                           bg=Background['submit'])
        b1.grid(row=1, column=2, columnspan=2, sticky="esnw", padx=2)
        b2.grid(row=1, column=4, columnspan=2, sticky="esnw", padx=2)
        #self.set = master.set

        font = {'weight': 'normal',
                'size': 10}
        matplotlib.rc('font', **font)
        plt.rc('font', family='serif')
        plt.rc('xtick', labelsize='x-small')
        plt.rc('ytick', labelsize='x-small')

        fig = plt.Figure(figsize=(7, 5), dpi=100)

        self.plot_data = PlotMagic()

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=2, columnspan=8)

        toolbar_frame = tk.Frame(self)
        toolbar_frame.grid(row=3, column=0, columnspan=8, sticky="eswn")
        toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
        toolbar.update()

        self.ax = fig.add_subplot(111)

        boxo = self.ax.get_position()
        self.ax.set_position([boxo.x0, boxo.y0 + boxo.height * 0.1,
                              boxo.width, boxo.height * 0.9])

        # Put a legend below current axis

        #self.ax.axhline(y=self.set, color='r', linestyle='-', label="Set temperature")
        self.ax.plot(self.x, self.y, color='darkviolet', label=subject + " (V)")
        #if self.check == 1:
        #    self.ax.plot(self.x, self.z, color='b', label="BP temperature")

        # ax.plot([1,2,3,4,5],[1,2,3,4,5])
        self.ax.set_xlabel('time (s)')
        self.ax.xaxis.set_label_position('top')
        self.ax.set_ylabel('Power (V)')
        self.ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
                       fancybox=True, shadow=True, ncol=5)

        ani = animation.FuncAnimation(fig, self.animate, frames=self.frames, interval=self.interval)
        plt.show()
        # print(ani)

        return ani

    def frames(self):
        while True:
            yield self.plot_data(self.address, self.interval)

    def animate(self, args):
        self.x.append(args[0])
        self.y.append(args[1])
        #if self.check == 1:
        #    self.z.append(args[2])
        #    return self.ax.plot(self.x, self.y, color='g', label=self.base.upper() + " temperature"), self.ax.plot(
        #        self.x, self.z, color='b', label="BP temperature")

        #else:
        return self.ax.plot(self.x, self.y, color='darkviolet', label=self.base.upper() + " power")

    def write(self, x, y, z=[], type=False, subject=""):
        if type == True:
            df = pandas.DataFrame(data={"time(s)": x, "selected temperature(C)": y, "tec0 temperature": z})
        else:
            df = pandas.DataFrame(data={"time(s)": x,subject.upper() + " (V)" : y})
        df_folder = "C:/Plotting/"
        if not os.path.exists(df_folder):
            os.makedirs(df_folder)
        file = df_folder + subject.upper() + str(time.time()) + ".csv"
        df.to_csv(file, sep=',', index=False)


class PlotMagic(object):

    def __init__(self):
        self.x = 0
        print("Plotmagic started")

    def __call__(self, address, interval=1000):
        self.x = self.x + interval / 1000
        self.y = getvalue(address, "u", "u")['value']
        # if box == 1:
        #     self.z = getvalue("dfd4", "u", "k")['value']
        #     return self.x, self.y, self.z
        #else:
        return self.x, self.y

class graph_error(tk.Toplevel):

    def __init__(self, master, b):
        tk.Toplevel.__init__(self)
        # self.grab_set()
        self.configure(background=Background['main'])
        self.geometry("750x650")
        self.title("Error signal acquisiton")
        self.v0 = getaddress(b, "v0")
        self.clp = getaddress(b, "clp")
        self.dphd = getaddress(b, "dphd")
        self.x = []
        self.y = []
        self.z = []
        self.base = b
        #self.check = box.get()
        self.run = self.setup(master, b)

    def setup(self, master, b):

        self.nrecs = max(getvalue(getaddress(b, "nrd"), "u", "1")["value"],getvalue(getaddress(b, "nrc"), "u", "1")["value"],getvalue(getaddress(b, "nrv"), "u", "1")["value"])

        self.min = getvalue(getaddress(b+"_d", "min"), "u", "u")["value"]
        self.max = getvalue(getaddress(b + "_d", "max"), "u", "u")["value"]
        self.rate = getvalue(getaddress(b+"_d", "rate"), "u", "u")["value"]
        l = tk.Label(self, text="The error signal is being acquired for " + b.upper() + ".",
                     bg=Background['main'], font=fonts['title'])
        self.l2 = tk.Label(self, text="Please wait... Records remaining: " + str(self.nrecs),
                     bg=Background['main'], font=fonts['main'])
        l.grid(row=0, column=0, columnspan=8, sticky="esnw", pady=(15, 0))
        self.l2.grid(row=1, column=0, columnspan=8, sticky="esnw", pady=(15, 0))

        b1 = tk.Button(self, text="Done", command=self.destroy, font=fonts['main'], bg=Background['submit'])
        # if self.check == 1:
        #     b2 = tk.Button(self, text="Write", command=lambda: self.write(self.x, self.y, self.z, True),
        #                    font=fonts['main'],
        #                    bg=Background['submit'])
        #else:
        b2 = tk.Button(self, text="Write", command=lambda: self.write(self.x, self.y, self.z, "Lock signal"), font=fonts['main'],
                           bg=Background['submit'])
        b1.grid(row=2, column=2, columnspan=2, sticky="esnw", padx=2)
        b2.grid(row=2, column=4, columnspan=2, sticky="esnw", padx=2)
        #self.set = master.set

        font = {'weight': 'normal',
                'size': 10}
        matplotlib.rc('font', **font)
        plt.rc('font', family='serif')
        plt.rc('xtick', labelsize='x-small')
        plt.rc('ytick', labelsize='x-small')

        fig = plt.Figure(figsize=(7, 5), dpi=100)

        self.plot_data = PlotMagic_msr()

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=3, columnspan=8)

        toolbar_frame = tk.Frame(self)
        toolbar_frame.grid(row=4, column=0, columnspan=8, sticky="eswn")
        toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
        toolbar.update()

        self.ax = fig.add_subplot(111)

        boxo = self.ax.get_position()
        self.ax.set_position([boxo.x0, boxo.y0 + boxo.height * 0.1,
                              boxo.width, boxo.height * 0.9])

        # Put a legend below current axis

        #self.ax.axhline(y=self.set, color='r', linestyle='-', label="Set temperature")
        self.ax.plot(self.y, self.z, color='darkviolet', label="CLP power")
        self.ax.plot(self.y, self.z, color='b', label="DPhD power")
        #if self.check == 1:
        #    self.ax.plot(self.x, self.z, color='b', label="BP temperature")

        # ax.plot([1,2,3,4,5],[1,2,3,4,5])
        self.ax.set_xlabel('Voltage (V)')
        self.ax.xaxis.set_label_position('top')
        self.ax.set_ylabel('Power (W)')
        self.ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
                       fancybox=True, shadow=True, ncol=5)

        ani = animation.FuncAnimation(fig, self.animate, frames=self.frames, interval=100, repeat=False)
        plt.show()
        # print(ani)

        return ani

    def frames(self):
        while self.nrecs > 0:
            yield self.plot_data(self.v0, self.clp, self.dphd, self.min, self.rate)
        else:
            self.l2.configure(text="Acquisition complete")
            return 0

    def animate(self, args):
        self.x.append(args[0])
        self.y.append(args[1])
        self.z.append(args[2])
        self.nrecs -= 1
        self.l2.configure(text="Please wait... Records remaining: " + str(self.nrecs))
        #if self.check == 1:
        #    self.z.append(args[2])
        #    return self.ax.plot(self.x, self.y, color='g', label=self.base.upper() + " temperature"), self.ax.plot(
        #        self.x, self.z, color='b', label="BP temperature")

        #else:
        return self.ax.plot(self.x, self.y, color='darkviolet', label="CLP signal"), self.ax.plot(self.x, self.z, color ="b", label="DPhD signal")

    def write(self, x, y, z, subject=""):
        df = pandas.DataFrame(data={"Voltage": x, "CLP signal": y, "DPhD signal": z})
        df_folder = "C:/Plotting/"
        if not os.path.exists(df_folder):
            os.makedirs(df_folder)
        file = df_folder + subject.upper() + str(time.time()) + ".csv"
        df.to_csv(file, sep=',', index=False)

class PlotMagic_msr(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        print("Plotmagic started for msr")

    def __call__(self, V0, CLP, DPHD, min, rate):
        #self.x = getvalue(V0, "u", "1")['value']
        if self.x == 0:
            self.x = min
        else:
            self.x=self.x + rate
        self.y = getvalue(CLP, "u", "u")['value']
        self.z = getvalue(DPHD, "u", "u")['value']
        print(self.x)
        print(self.y)
        print(self.z)
        # if box == 1:
        #     self.z = getvalue("dfd4", "u", "k")['value']
        #     return self.x, self.y, self.z
        #else:
        return self.x, self.y, self.z

class advanced(tk.Toplevel):

    def __init__(self, master, b):
        tk.Toplevel.__init__(self)
        # self.grab_set()
        self.configure(background=Background['main'])
        self.geometry("750x500")
        self.title("PZT advanced settings")
        self.pady = 3


        self.c_data = tk.Canvas(self, width=300, height=500, scrollregion=(0, 0, 300, 1500))
        self.vbar_data = tk.Scrollbar(self, orient=tk.VERTICAL)

        self.vbar_data.config(command=self.c_data.yview)
        self.c_data.config(yscrollcommand=self.vbar_data.set)
        self.c_data.create_window(0, 0, anchor="nw", width=700, height=1200, window=advdata(self, b))


        self.c_data.grid(row=2, column=2, sticky="nwse")
        self.vbar_data.grid(row=2, column=1, sticky='nsw', padx=5)


class advdata(tk.Frame):
    def __init__(self, master, b):
        tk.Frame.__init__(self, master)
        self.configure(bg=Background['main'])
        self.pady = 3


        self.title = tk.Label(self, text=b.upper() + " advanced settings", font=fonts['title'], bg=Background['main'])

        self.l_minm = tk.Label(self, text="Minimum mirror voltage", font=fonts['main'], bg=Background['main'])
        self.t_minm = tk.Text(self, width=6, height=1)
        self.s_minm = pzt_label(self)
        self.s_minm.update_status(getaddress(b + "_d", "minm"), "minm", "driver")
        self.b_minm = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                  bg=Background['submit'],
                                  command=lambda: submit(self, b + "_d", "minm"))

        self.l_maxm = tk.Label(self, text="Maximum mirror voltage", font=fonts['main'], bg=Background['main'])
        self.t_maxm = tk.Text(self, width=6, height=1)
        self.s_maxm = pzt_label(self)
        self.s_maxm.update_status(getaddress(b + "_d", "maxm"), "maxm", "driver")
        self.b_maxm = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                  bg=Background['submit'],
                                  command=lambda: submit(self, b + "_d", "maxm"))

        # self.l_minsl = tk.Label(self, text="Minimum slope", font=fonts['main'], bg=Background['main'])
        # self.t_minsl = tk.Text(self, width=6, height=1)
        # self.s_minsl = pzt_label(self)
        # self.s_minsl.update_status(getaddress(b + "_d", "minsl"), "minsl", "driver")
        # self.b_minsl = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
        #                           bg=Background['submit'],
        #                           command=lambda: submit(self, b + "_d", "minsl"))
        #
        # self.l_maxsl = tk.Label(self, text="Maximum slope", font=fonts['main'], bg=Background['main'])
        # self.t_maxsl = tk.Text(self, width=6, height=1)
        # self.s_maxsl = pzt_label(self)
        # self.s_maxsl.update_status(getaddress(b + "_d", "maxsl"), "maxsl", "driver")
        # self.b_maxsl = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
        #                           bg=Background['submit'],
        #                           command=lambda: submit(self, b + "_d", "maxsl"))

        self.l_minwp = tk.Label(self, text="Minimum WP offset", font=fonts['main'], bg=Background['main'])
        self.t_minwp = tk.Text(self, width=6, height=1)
        self.s_minwp = pzt_label(self)
        self.s_minwp.update_status(getaddress(b + "_d", "minwp"), "minwp", "driver")
        self.b_minwp = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                  bg=Background['submit'],
                                  command=lambda: submit(self, b + "_d", "minwp"))

        self.l_maxwp = tk.Label(self, text="Maximum WP offset", font=fonts['main'], bg=Background['main'])
        self.t_maxwp = tk.Text(self, width=6, height=1)
        self.s_maxwp = pzt_label(self)
        self.s_maxwp.update_status(getaddress(b + "_d", "maxwp"), "maxwp", "driver")
        self.b_maxwp = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                  bg=Background['submit'],
                                  command=lambda: submit(self, b + "_d", "maxwp"))

        self.l_clpt = tk.Label(self, text="CLP unlock window (s)", font=fonts['main'], bg=Background['main'])
        self.t_clpt = tk.Text(self, width=6, height=1)
        self.s_clpt = pzt_label(self)
        self.s_clpt.update_status(getaddress(b + "_d", "clpt"), "clpt", "driver")
        self.b_clpt = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                  bg=Background['submit'],
                                  command=lambda: submit(self, b + "_d", "clpt"))
        
        self.l_lock_tune = tk.Label(self, text="Lock tuning (1-on)", font=fonts['main'], bg=Background['main'])
        self.t_lock_tune = tk.Text(self, width=6, height=1)
        self.s_lock_tune = gui_label(self)
        self.s_lock_tune.update_status(getaddress("gui", "lock_tune"), "lock_tune")
        self.b_lock_tune = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                  bg=Background['submit'],
                                  command=lambda: submit(self, "gui", "lock_tune"))
        
        self.l_tec_tune = tk.Label(self, text="TEC select (1 or 2)", font=fonts['main'], bg=Background['main'])
        self.t_tec_tune = tk.Text(self, width=6, height=1)
        self.s_tec_tune = gui_label(self)
        self.s_tec_tune.update_status(getaddress("gui", "tec_tune"), "tec_tune")
        self.b_tec_tune = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                  bg=Background['submit'],
                                  command=lambda: submit(self, "gui", "tec_tune"))
        
        self.l_dphd_thres = tk.Label(self, text="DPhD threshold (V)", font=fonts['main'], bg=Background['main'])
        self.t_dphd_thres = tk.Text(self, width=6, height=1)
        self.s_dphd_thres = gui_label(self)
        self.s_dphd_thres.update_status(getaddress("gui", "dphd_thres"), "dphd_thres")
        self.b_dphd_thres = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                  bg=Background['submit'],
                                  command=lambda: submit(self, "gui", "dphd_thres"))
        
        self.l_pid_timer = tk.Label(self, text="PID stabilisation", font=fonts['main'], bg=Background['main'])
        self.t_pid_timer = tk.Text(self, width=6, height=1)
        self.s_pid_timer = gui_label(self)
        self.s_pid_timer.update_status(getaddress("gui", "pid_timer"), "pid_timer")
        self.b_pid_timer = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                  bg=Background['submit'],
                                  command=lambda: submit(self, "gui", "pid_timer"))


        self.l_tec0_pid = tk.Label(self, text="TEC0 PID DISABLE (==0)", font=fonts['main'], bg=Background['main'])
        self.t_tec0_pid = tk.Text(self, width=6, height=1)
        self.s_tec0_pid = gui_label(self)
        self.s_tec0_pid.update_status(getaddress("gui", "tec0_pid"), "tec0_pid")
        self.b_tec0_pid = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                     bg=Background['submit'],
                                     command=lambda: submit(self, "gui", "tec0_pid"))

        self.l_tec1_pid = tk.Label(self, text="TEC1 PID DISABLE (==0)", font=fonts['main'], bg=Background['main'])
        self.t_tec1_pid = tk.Text(self, width=6, height=1)
        self.s_tec1_pid = gui_label(self)
        self.s_tec1_pid.update_status(getaddress("gui", "tec1_pid"), "tec1_pid")
        self.b_tec1_pid = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                     bg=Background['submit'],
                                     command=lambda: submit(self, "gui", "tec1_pid"))

        self.l_tec2_pid = tk.Label(self, text="TEC2 PID DISABLE (==0)", font=fonts['main'], bg=Background['main'])
        self.t_tec2_pid = tk.Text(self, width=6, height=1)
        self.s_tec2_pid = gui_label(self)
        self.s_tec2_pid.update_status(getaddress("gui", "tec2_pid"), "tec2_pid")
        self.b_tec2_pid = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                     bg=Background['submit'],
                                     command=lambda: submit(self, "gui", "tec2_pid"))
        self.l_lock_timer = tk.Label(self, text="TEC2 PID DISABLE (==0)", font=fonts['main'], bg=Background['main'])
        self.t_lock_timer = tk.Text(self, width=6, height=1)
        self.s_lock_timer = gui_label(self)
        self.s_lock_timer.update_status(getaddress("gui", "lock_timer"), "lock_timer")
        self.b_lock_timer = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                     bg=Background['submit'],
                                     command=lambda: submit(self, "gui", "lock_timer"))

        self.b_wpq = tk.Button(self, text="Acquire potential lock points", bg=Background['submit'], width=35, font=fonts['main'],
                                command=lambda: self.wpaq(self, b))

        self.title.grid(row=1, column=1, columnspan=2, sticky="nw", pady=self.pady)

        self.l_minm.grid(row=2, column=1, columnspan=1, sticky="nw", pady=self.pady)
        self.t_minm.grid(row=2, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_minm.grid(row=2, column=3, columnspan=1, sticky="nw", pady=self.pady)
        self.b_minm.grid(row=2, column=4, columnspan=1, sticky="nw", pady=self.pady)

        self.l_maxm.grid(row=3, column=1, columnspan=1, sticky="nw", pady=self.pady)
        self.t_maxm.grid(row=3, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_maxm.grid(row=3, column=3, columnspan=1, sticky="nw", pady=self.pady)
        self.b_maxm.grid(row=3, column=4, columnspan=1, sticky="nw", pady=self.pady)

        # self.l_minsl.grid(row=4, column=1, columnspan=1, sticky="nw", pady=self.pady)
        # self.t_minsl.grid(row=4, column=2, columnspan=1, sticky="nw", pady=self.pady)
        # self.s_minsl.grid(row=4, column=3, columnspan=1, sticky="nw", pady=self.pady)
        # self.b_minsl.grid(row=4, column=4, columnspan=1, sticky="nw", pady=self.pady)
        #
        # self.l_maxsl.grid(row=5, column=1, columnspan=1, sticky="nw", pady=self.pady)
        # self.t_maxsl.grid(row=5, column=2, columnspan=1, sticky="nw", pady=self.pady)
        # self.s_maxsl.grid(row=5, column=3, columnspan=1, sticky="nw", pady=self.pady)
        # self.b_maxsl.grid(row=5, column=4, columnspan=1, sticky="nw", pady=self.pady)

        self.l_minwp.grid(row=6, column=1, columnspan=1, sticky="nw", pady=self.pady)
        self.t_minwp.grid(row=6, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_minwp.grid(row=6, column=3, columnspan=1, sticky="nw", pady=self.pady)
        self.b_minwp.grid(row=6, column=4, columnspan=1, sticky="nw", pady=self.pady)

        self.l_maxwp.grid(row=7, column=1, columnspan=1, sticky="nw", pady=self.pady)
        self.t_maxwp.grid(row=7, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_maxwp.grid(row=7, column=3, columnspan=1, sticky="nw", pady=self.pady)
        self.b_maxwp.grid(row=7, column=4, columnspan=1, sticky="nw", pady=self.pady)

        self.l_clpt.grid(row=8, column=1, columnspan=1, sticky="nw", pady=self.pady)
        self.t_clpt.grid(row=8, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_clpt.grid(row=8, column=3, columnspan=1, sticky="nw", pady=self.pady)
        self.b_clpt.grid(row=8, column=4, columnspan=1, sticky="nw", pady=self.pady)

        self.l_lock_tune.grid(row=9, column=1, columnspan=1, sticky="nw", pady=self.pady)
        self.t_lock_tune.grid(row=9, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_lock_tune.grid(row=9, column=3, columnspan=1, sticky="nw", pady=self.pady)
        self.b_lock_tune.grid(row=9, column=4, columnspan=1, sticky="nw", pady=self.pady)
        
        self.l_tec_tune.grid(row=10, column=1, columnspan=1, sticky="nw", pady=self.pady)
        self.t_tec_tune.grid(row=10, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_tec_tune.grid(row=10, column=3, columnspan=1, sticky="nw", pady=self.pady)
        self.b_tec_tune.grid(row=10, column=4, columnspan=1, sticky="nw", pady=self.pady)
        
        self.l_dphd_thres.grid(row=11, column=1, columnspan=1, sticky="nw", pady=self.pady)
        self.t_dphd_thres.grid(row=11, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_dphd_thres.grid(row=11, column=3, columnspan=1, sticky="nw", pady=self.pady)
        self.b_dphd_thres.grid(row=11, column=4, columnspan=1, sticky="nw", pady=self.pady)
        
        self.l_pid_timer.grid(row=12, column=1, columnspan=1, sticky="nw", pady=self.pady)
        self.t_pid_timer.grid(row=12, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_pid_timer.grid(row=12, column=3, columnspan=1, sticky="nw", pady=self.pady)
        self.b_pid_timer.grid(row=12, column=4, columnspan=1, sticky="nw", pady=self.pady)
        
        self.l_tec0_pid.grid(row=13, column=1, columnspan=1, sticky="nw", pady=self.pady)
        self.t_tec0_pid.grid(row=13, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_tec0_pid.grid(row=13, column=3, columnspan=1, sticky="nw", pady=self.pady)
        self.b_tec0_pid.grid(row=13, column=4, columnspan=1, sticky="nw", pady=self.pady)
        
        self.l_tec1_pid.grid(row=14, column=1, columnspan=1, sticky="nw", pady=self.pady)
        self.t_tec1_pid.grid(row=14, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_tec1_pid.grid(row=14, column=3, columnspan=1, sticky="nw", pady=self.pady)
        self.b_tec1_pid.grid(row=14, column=4, columnspan=1, sticky="nw", pady=self.pady)
        
        self.l_tec2_pid.grid(row=15, column=1, columnspan=1, sticky="nw", pady=self.pady)
        self.t_tec2_pid.grid(row=15, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_tec2_pid.grid(row=15, column=3, columnspan=1, sticky="nw", pady=self.pady)
        self.b_tec2_pid.grid(row=15, column=4, columnspan=1, sticky="nw", pady=self.pady)

        self.l_lock_timer.grid(row=16, column=1, columnspan=1, sticky="nw", pady=self.pady)
        self.t_lock_timer.grid(row=16, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_lock_timer.grid(row=16, column=3, columnspan=1, sticky="nw", pady=self.pady)
        self.b_lock_timer.grid(row=16, column=4, columnspan=1, sticky="nw", pady=self.pady)

        self.b_wpq.grid(row=18, column=1, columnspan=6, sticky="nw", pady=self.pady)

    def wpaq(self, master, b):

        self.padyy = 5
        self.l_pztt = tk.Label(self, text="PZT (V)", font=fonts['title'], bg=Background['main'])
        self.l_clpp = tk.Label(self, text="CLP (V)", font=fonts['title'], bg=Background['main'])
        self.l_regtt = tk.Label(self, text="Reg Target (V)", font=fonts['title'], bg=Background['main'])
        self.l_regpp = tk.Label(self, text="Phase(+/-)", font=fonts['title'], bg=Background['main'])
        self.l_regss = tk.Label(self, text="Reg score", font=fonts['title'], bg=Background['main'])

        self.l_pztt.grid(row=10, column=1, columnspan=2, sticky="nw", pady=self.padyy)
        self.l_clpp.grid(row=10, column=3, columnspan=2, sticky="nw", pady=self.padyy)
        self.l_regtt.grid(row=10, column=5, columnspan=2, sticky="nw", pady=self.padyy)
        self.l_regpp.grid(row=10, column=7, columnspan=2, sticky="nw", pady=self.padyy)
        self.l_regss.grid(row=10, column=9, columnspan=2, sticky="nw", pady=self.padyy)

        self.geths(self).grid(row=11, column=1, columnspan=10, sticky="we", pady=self.padyy, padx=2)
        self.row = 12
        self.error = 1

        for i in range(50):
            #print("getting" + str(i))
            coord = round(getvalue(iteradr(b, "wploc", 5*i+0),"u","u")["value"],2)
            if not coord > 0:
                self.coord = 0
                #self.error = 1
                #i = 51
            else:
                clp = round(getvalue(iteradr(b, "wploc", 5*i+1),"u","u")["value"],2)
                reg = round(getvalue(iteradr(b, "wploc", 5*i+2),"u","u")["value"],2)
                phase = round(getvalue(iteradr(b, "wploc", 5*i+3),"u","u")["value"],2)
                score = round(getvalue(iteradr(b, "wploc", 5*i+4),"u","u")["value"],2)
                #print(clp)

                self.l_coord = tk.Label(self, text=coord, font=fonts['main'], bg=Background['main'])
                self.l_clp = tk.Label(self, text=clp, font=fonts['main'], bg=Background['main'])
                self.l_reg = tk.Label(self, text=reg, font=fonts['main'], bg=Background['main'])
                self.l_phase = tk.Label(self, text=phase, font=fonts['main'], bg=Background['main'])
                self.l_score = tk.Label(self, text=score, font=fonts['main'], bg=Background['main'])

                self.l_coord.grid(row=self.row+i, column=1, columnspan=2, sticky="nw", pady=self.padyy)
                self.l_clp.grid(row=self.row + i, column=3, columnspan=2, sticky="nw", pady=self.padyy)
                self.l_reg.grid(row=self.row + i, column=5, columnspan=2, sticky="nw", pady=self.padyy)
                self.l_phase.grid(row=self.row + i, column=7, columnspan=2, sticky="nw", pady=self.padyy)
                self.l_score.grid(row=self.row + i, column=9, columnspan=2, sticky="nw", pady=self.padyy)
                self.error = 0

                if i == 0:
                    self.l_coord.configure(font=fonts['title'])
                    self.l_clp.configure(font=fonts['title'])
                    self.l_reg.configure(font=fonts['title'])
                    self.l_phase.configure(font=fonts['title'])
                    self.l_score.configure(font=fonts['title'])
        if self.error == 0:
            self.msg = "Lock points listed, selected WP shown with bold."
        else:
            self.msg = "No potential lock points detected."

        self.finish = tk.Label(self, text=self.msg, font=fonts['title'], bg=Background['main'])
        self.finish.grid(row=self.row + 51, column=1, columnspan=10, sticky="nw", pady=self.padyy)

    def geths(self, parent):
            hs = ttk.Separator(parent, orient=tk.HORIZONTAL)
            return hs

