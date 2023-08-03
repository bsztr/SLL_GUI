import tkinter as tk
import tkinter.ttk as ttk
from CONFIG import *
from TecArch import *
from init_start import *
import Globals
from COMM import save_regs
from Dynamic import temp_label


class TECPanel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # self.grab_set()
        self.configure(background=Background['main'])
        # self.geometry("750x500")
        # self.title("PZT advanced settings")
        self.pady = 3


        self.c_data = tk.Canvas(self, width=1400, height=730, scrollregion=(0, 0, 2200, 730))
        self.hbar_data = tk.Scrollbar(self, orient=tk.HORIZONTAL)

        self.hbar_data.config(command=self.c_data.xview)
        self.c_data.config(xscrollcommand=self.hbar_data.set)
        self.c_data.create_window(0, 0, anchor="nw", width=2200, height=730, window=TECData(master))


        self.c_data.grid(row=2, column=1, sticky="nwse")
        self.hbar_data.grid(row=3, column=1, sticky='nwe', padx=5)


class TECData(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg=Background['main'])
        available=Globals.available
        fwv = str(getvalue(getaddress("tec0", "fw"), "u", "1")["value"])

        try:
            tec_fwv = f"ver: {fwv[0]}.{fwv[1]}.{fwv[2]}"
        except:
            tec_fwv = f"ver: {fwv}"

        self.l_logo = Logo(self)
        self.l_logo.update_logo()
        self.b_tecon=tk.Button(self, text="TEC ON", font=fonts['main'], bg=Colours['green'], fg=Colours["white"], height=1, width=8, command=lambda: self.tec_on())
        self.b_tecoff = tk.Button(self, text="TEC OFF", font=fonts['main'], bg=Colours['red'], fg=Colours["white"], height=1, width=8, command=lambda: self.tec_off())
        self.b_tecsave = tk.Button(self, text="SAVE", font=fonts['main'], bg=Colours['grey'], fg=Colours["black"], height=1, width=8, command=lambda: save_regs('tec'))
        self.l_tecver = tk.Label(self, text=tec_fwv, font=fonts['main'], bg=Background['main'])

        if "TEC0" in available:
            self.bp = TECArch(self, "BP TEC", "tec0", 1)
        if "TEC1" in available:
            self.ld = TECArch(self, "NLC 1 TEC", "tec1", 6)
        if "TEC2" in available:
            self.ntc1 = TECArch(self, "NLC 2 TEC", "tec2", 11)
        if "TEC3" in available:
            self.ntc2 = TECArch(self, "LD TEC", "tec3", 16)
        if "TEC4" in available:
            self.ntc2 = TECArch(self, "N3 TEC", "tec4", 21)
        if "TEC5" in available:
            self.ntc2 = TECArch(self, "N4 TEC", "tec5", 26)

        #TEC - Grid
        # self.l_warm.grid(row=1, column=1, sticky="nw", pady=(12,0))
        # self.t_warm.grid(row=1, column=2, sticky="nw", pady=(12,0))
        # self.s_warm.grid(row=1, column=3, sticky="nw", pady=(12,0))
        # self.b_warm.grid(row=1, column=4, sticky="nw", pady=(12,0))
        self.l_logo.grid(row=0, column=15, columnspan=4, rowspan=2, sticky="e", pady=5)
        self.b_tecon.grid(row=0, column=1, columnspan=2, sticky="nswe", pady=10, padx=2)
        self.b_tecoff.grid(row=0, column=3, columnspan=2, sticky="nswe", pady=10, padx=2)
        self.b_tecsave.grid(row=0, column=5, columnspan=2, sticky="nswe", pady=10, padx=2)
        self.l_tecver.grid(row=0, column=7, columnspan=1, sticky="nswe", pady=10, padx=2)
        self.geths(self).grid(row=2, column=1, columnspan=20, sticky="we", pady=5)

    def geths(self, parent):
        hs = ttk.Separator(parent, orient=tk.HORIZONTAL)
        return hs

    def getvs(self, parent):
        vs = ttk.Separator(parent, orient=tk.VERTICAL)
        return vs

    def tec_on(self):
        if getbit(status["address"], status["STATUS_OK"]) == "1" and getbit(status["address"], status["TEC_WARMING_UP"]) == "0":
            addvalue(control['address'], 2**control["tec0"]+2**control["tec1"]+2**control["tec2"]+2**control["tec3"]+2**control["tec4"]+2**control["tec5"])
            Globals.incident_message = "TECs are initialising."
            Globals.tec_stab = 1

        elif Globals.tec_stab != 1:
            Globals.incident_message = "TECs are currently initialising."

        else:
            Globals.incident_message="TECs are already initialised. \nIf the third LED is not constant green, reset the system."

    def tec_off(self):
        if getbit(status["address"], status["TEC_WARMING_UP"]) == "1":
            resvalue(control['address'], 2**control["tec0"]+2**control["tec1"]+2**control["tec2"]+2**control["tec3"]+2**control["tec4"]+2**control["tec5"])
            Globals.incident_message = "TECs are turned off."
            Globals.tec_stab = 0
        else:
            Globals.incident_message="TECs already switched off."

