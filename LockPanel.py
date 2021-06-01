import tkinter as tk
import tkinter.ttk as ttk
from LockArch import *
import Globals
from init_start import *
from Dynamic import Logo

class LockPanel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg=Background['main'])
        #Lock Definition
        available = Globals.available
        self.l_logo = Logo(self)
        self.l_logo.update_logo()

        if "PZT0" in available:
            self.bp = LockArch(self, "PZT0 Settings", "pzt0", 1)
        if "PZT1" in available:
            self.bp = LockArch(self, "PZT1 Settings", "pzt1", 11)

        self.l_logo.grid(row=0, column=15, columnspan=4, rowspan=1, sticky="e", pady=5)
        self.geths(self).grid(row=1, column=1, columnspan=20, sticky="we", pady=5)
        self.b_pzton = tk.Button(self, text="PZT ON", font=fonts['main'], bg=Colours['green'], fg=Colours["white"],
                                 height=1, width=8, command=lambda: self.pzt_on())
        self.b_pztoff = tk.Button(self, text="PZT OFF", font=fonts['main'], bg=Colours['red'], fg=Colours["white"],
                                  height=1, width=8, command=lambda: self.pzt_off())
        self.b_pzton.grid(row=0, column=1, columnspan=2, sticky="nswe", pady=10, padx=2)
        self.b_pztoff.grid(row=0, column=3, columnspan=2, sticky="nswe", pady=10, padx=2)

    def geths(self, parent):
        hs = ttk.Separator(parent, orient=tk.HORIZONTAL)
        return hs

    def getvs(self, parent):
        vs = ttk.Separator(parent, orient=tk.VERTICAL)
        return vs

    def pzt_on(self):
        if getbit(control["address"], 1) != "1":
            addvalue(control['address'], 2)
            Globals.incident_message = "PZTs are initialising."

        else:
            Globals.incident_message="PZTs are already turned on."

    def pzt_off(self):
        if getbit(control["address"], 1) == "1":
            resvalue(control['address'], 2)
            Globals.incident_message = "PZTs are turned off."
        else:
            Globals.incident_message="PZTs are already switched off."