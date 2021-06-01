import tkinter as tk
import tkinter.ttk as ttk
from CONFIG import *
from TecArch import *
from init_start import *
import Globals
from Dynamic import temp_label


class TECPanel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg=Background['main'])
        available=Globals.available
        # TEC - Def
        # self.l_warm=tk.Label(self,text="Warm up time (s)", font=fonts['main'], bg=Background['main'])
        # self.t_warm=tk.Text(self, width=6, height=1)
        # self.s_warm = tk.Label(self, text="120", fg="gray25", font=fonts['status'], bg=Background['main'])
        # self.b_warm = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'])

        self.l_logo = Logo(self)
        self.l_logo.update_logo()
        self.b_tecon=tk.Button(self, text="TEC ON", font=fonts['main'], bg=Colours['green'], fg=Colours["white"], height=1, width=8, command=lambda: self.tec_on())
        self.b_tecoff = tk.Button(self, text="TEC OFF", font=fonts['main'], bg=Colours['red'], fg=Colours["white"], height=1, width=8, command=lambda: self.tec_off())

        if "TEC0" in available:
            self.bp = TECArch(self, "BP TEC", "tec0", 1)
        if "TEC1" in available:
            self.ld = TECArch(self, "NLC 1 TEC", "tec1", 6)
        if "TEC2" in available:
            self.ntc1 = TECArch(self, "NLC 2 TEC", "tec2", 11)
        if "TEC3" in available:
            self.ntc2 = TECArch(self, "LD TEC", "tec3", 16)

        #TEC - Grid
        # self.l_warm.grid(row=1, column=1, sticky="nw", pady=(12,0))
        # self.t_warm.grid(row=1, column=2, sticky="nw", pady=(12,0))
        # self.s_warm.grid(row=1, column=3, sticky="nw", pady=(12,0))
        # self.b_warm.grid(row=1, column=4, sticky="nw", pady=(12,0))
        self.l_logo.grid(row=0, column=15, columnspan=4, rowspan=2, sticky="e", pady=5)
        self.b_tecon.grid(row=0, column=1, columnspan=2, sticky="nswe", pady=10, padx=2)
        self.b_tecoff.grid(row=0, column=3, columnspan=2, sticky="nswe", pady=10, padx=2)
        self.geths(self).grid(row=2, column=1, columnspan=20, sticky="we", pady=5)

    def geths(self, parent):
        hs = ttk.Separator(parent, orient=tk.HORIZONTAL)
        return hs

    def getvs(self, parent):
        vs = ttk.Separator(parent, orient=tk.VERTICAL)
        return vs

    def tec_on(self):
        if getbit(control["address"], 3) == "1" and getbit(control["address"], 10) != "1":
            addvalue(control['address'], 1024)
            Globals.incident_message = "TECs are initialising."
            Globals.tec_stab = 1

        elif Globals.tec_stab != 1:
            Globals.incident_message = "TECs are currently initialising."

        else:
            Globals.incident_message="TECs are already initialised. \nIf the third LED is not constant green, reset the system."

    def tec_off(self):
        if getbit(control["address"], 10) == "1":
            resvalue(control['address'], 1024)
            Globals.incident_message = "TECs are turned off."
            Globals.tec_stab = 0
        else:
            Globals.incident_message="TECs already switched off."

