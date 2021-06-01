import tkinter as tk
from CONFIG import *
import Globals
import csv
from init_start import *

class CalPanel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg=Background['main'])
        self.padm=12
        self.pads=5

        available = Globals.available
        #Calibration definitions
        #self.l_logo = tk.Label(self, text="Solo 640", font=fonts['model'], bg=Background['main'])

        self.l_info=tk.Label(self, text="Modules are still missing calibration.", font=fonts['info'], bg=Background['alert'], fg=Colours['red'])
        self.l_disc = tk.Label(self, text="Once calibrated, disable the calibration option via the permissions tab.", font=fonts['info'],
                               bg=Background['main'], fg=Colours['darkgrey'])
        self.l_title = tk.Label(self, text="Modules detected:", font=fonts['title'], bg=Background['main'])

        self.l_cb_title = tk.Label(self, text="Control box:", font=fonts['main'], bg=Background['main'])

        if "CB" in available:
            self.l_cb0_title = tk.Label(self, text="CB0:", font=fonts['main'],
                                         bg=Background['main'])
            self._cb=CalibrationProc(self, "cb", 7)
            self.l_cb0_title.grid(row=7, column=3, columnspan=1, sticky="nw", pady=self.pads)
            self.geths(self).grid(row=8, column=1, columnspan=9, sticky="we", pady=3)

        self.l_lh_title = tk.Label(self, text="Laser head:", font=fonts['main'], bg=Background['main'])

        if "LH" in available:
            self.l_lh0_title = tk.Label(self, text="LH0:", font=fonts['main'],
                                         bg=Background['main'])
            self._lh = CalibrationProc(self, "lh", 11)
            self.l_lh0_title.grid(row=11, column=3, columnspan=1, sticky="nw", pady=self.pads)
            self.geths(self).grid(row=12, column=1, columnspan=9, sticky="we", pady=3)
        self.l_ld_title = tk.Label(self, text="Laser driver:", font=fonts['main'], bg=Background['main'])

        if "LDR" in available:
            self.l_ld0_title = tk.Label(self, text="LD0:", font=fonts['main'],
                                         bg=Background['main'])
            self._ld = CalibrationProc(self, "ld", 15)
            self.l_ld0_title.grid(row=15, column=3, columnspan=1, sticky="nw", pady=self.pads)
            self.geths(self).grid(row=16, column=1, columnspan=9, sticky="we", pady=3)
        self.l_tec_title = tk.Label(self, text="Thermoelectric controllers:", font=fonts['main'], bg=Background['main'])

        if "TEC0" in available:
            self.l_tec0_title = tk.Label(self, text="TEC0:", font=fonts['main'],
                                        bg=Background['main'])
            self._tec0 = CalibrationProc(self, "tec0", 19)
            self.l_tec0_title.grid(row=19, column=3, columnspan=1, sticky="nw", pady=self.pads)
            self.geths(self).grid(row=20, column=1, columnspan=9, sticky="we", pady=3)
        if "TEC1" in available:
            self.l_tec1_title = tk.Label(self, text="TEC1:", font=fonts['main'],
                                         bg=Background['main'])
            self._tec1 = CalibrationProc(self, "tec1", 21)
            self.l_tec1_title.grid(row=21, column=3, columnspan=1, sticky="nw", pady=self.pads)
            self.geths(self).grid(row=22, column=1, columnspan=9, sticky="we", pady=3)

        if "TEC2" in available:
            self.l_tec2_title = tk.Label(self, text="TEC2:", font=fonts['main'],
                                         bg=Background['main'])
            self._tec2 = CalibrationProc(self, "tec2", 23)
            self.l_tec2_title.grid(row=23, column=3, columnspan=1, sticky="nw", pady=self.pads)
            self.geths(self).grid(row=24, column=1, columnspan=9, sticky="we", pady=3)

        if "TEC3" in available:
            self.l_tec3_title = tk.Label(self, text="TEC3:", font=fonts['main'],
                                         bg=Background['main'])
            self._tec3 = CalibrationProc(self, "tec3", 25)
            self.l_tec3_title.grid(row=25, column=3, columnspan=1, sticky="nw", pady=self.pads)
            self.geths(self).grid(row=26, column=1, columnspan=9, sticky="we", pady=3)

        self.l_pzt_title = tk.Label(self, text="Piezoelectric controllers:", font=fonts['main'], bg=Background['main'])

        if "PZT0" in available:
            self.l_pzt0_title = tk.Label(self, text="PZT0:", font=fonts['main'],
                                         bg=Background['main'])
            self._pzt0 = CalibrationProc(self, "pzt0", 29)
            self.l_pzt0_title.grid(row=29, column=3, columnspan=1, sticky="nw", pady=self.pads)
            self.geths(self).grid(row=30, column=1, columnspan=9, sticky="we", pady=3)

        if "PZT1" in available:
            self.l_pzt1_title = tk.Label(self, text="PZT1:", font=fonts['main'],
                                         bg=Background['main'])
            self._pzt1 = CalibrationProc(self, "pzt1", 31)
            self.l_pzt1_title.grid(row=31, column=3, columnspan=1, sticky="nw", pady=self.pads)
            self.geths(self).grid(row=32, column=1, columnspan=9, sticky="we", pady=3)

        #Calibration grid

        #self.l_logo.grid(row=1, column=1, columnspan=3, rowspan=1, sticky="nse", pady=self.pads)

        self.l_info.grid(row=2, column=1, columnspan=9, sticky="nwse", pady=self.padm)
        self.l_title.grid(row=3, column=1, columnspan=4, sticky="nw", pady=self.padm)
        self.geths(self).grid(row=4, column=1, columnspan=9, sticky="we", pady=3)
        self.l_cb_title.grid(row=5, column=2, columnspan=7, sticky="nw", pady=self.padm)
        self.geths(self).grid(row=6, column=1, columnspan=9, sticky="we", pady=3)
        self.l_lh_title.grid(row=9, column=2, columnspan=7, sticky="nw", pady=self.padm)
        self.geths(self).grid(row=10, column=1, columnspan=9, sticky="we", pady=3)
        self.l_ld_title.grid(row=13, column=2, columnspan=7, sticky="nw", pady=self.padm)
        self.geths(self).grid(row=14, column=1, columnspan=9, sticky="we", pady=3)
        self.l_tec_title.grid(row=17, column=2, columnspan=7, sticky="nw", pady=self.padm)
        self.geths(self).grid(row=18, column=1, columnspan=9, sticky="we", pady=3)
        self.l_pzt_title.grid(row=27, column=2, columnspan=7, sticky="nw", pady=self.padm)
        self.geths(self).grid(row=28, column=1, columnspan=9, sticky="we", pady=3)
        self.l_disc.grid(row=33, column=2, columnspan=9, sticky="nw", pady=self.padm)

    def geths(self, parent):
            hs = ttk.Separator(parent, orient=tk.HORIZONTAL)
            return hs

    def getvs(self, parent):
            vs = ttk.Separator(parent, orient=tk.VERTICAL)
            return vs

class CalibrationProc(tk.Frame):
    def __init__(self, master, module, row):
        tk.Frame.__init__(self, master)

        self.i = 0
        self.j=0
        self.a = []
        self.b=[]

        for item in Calibration[module]:
            if item!="":

                self.b.append(item)
                self.a.append(tk.Button(master, text=item.upper(), bg=Colours['grey'], font=fonts['calibration'], width=10, height=1, command=lambda target=item: self.select(module, target)))
                self.a.append(tk.Canvas(master, bg=Colours['red'], width=5, height=5))

                self.a[self.i].grid(row=row, column=4+self.i, sticky="nwse", padx=3, pady=5)
                self.a[self.i+1].grid(row=row, column=4 + self.i+1, sticky="nwse", padx=3, pady=5)
                self.i=self.i+2
                self.j=self.j+1

    # def calibrate(self, module, itm):
    #     for item in subCalibration:
    #         if item==itm:
    #             print(item)
    #             self.select(module, item)

    def select(self, module, itm):
        exec("self."+itm+"(\""+module+"\")")

    def dump(self, module):

        if "cb" in module:
            file="UCB_dump.csv"
        else:
            file ="LH_dump.csv"

        self.info = msgwindow(module, "dump")

        def target_method():
            with open(file) as dump_file:
                dump_reader = csv.reader(dump_file, delimiter=',')
                for row in dump_reader:
                    print(row[0].lower()[2:], row[1].lower(), "1", "1")
                    #setvalue(row[0].lower()[2:], row[1].lower(), "1", "1")
            return "Done"

        thread1 = threading.Thread(
            target=target_method,
        )
        thread1.start()

        while thread1.is_alive():
            None

        thread1.join()

        self.complete=completewindow(module)
        self.info.destroy()

    def ref_voltage(self, modules):
        print("ref_voltage")

    def ld_current(self, modules):
        print("ld_current")

    def ld_voltage(self, modules):
        print("ld_voltage")

    def tec_current(self, modules):
        print("tec_current")

    def tec_voltage(self, modules):
        print("tec_voltage")

    def thermistor(self, modules):
        print("thermistor")

    def pzt_voltage(self, modules):
        print("pzt_voltage")

    def diff_pd(self, modules):
        print("diff_pd")

    def cop_diode(self, modules):
        print("cop_diode")

class msgwindow(tk.Toplevel):

    def __init__(self, module, itm):
        tk.Toplevel.__init__(self)
        self.grab_set()
        self.configure(background=Background['main'])
        self.geometry("200x60")

        #self.msg = tk.Toplevel()
        self.title(itm.upper() + "processing")

        l = tk.Label(self, text=module.upper()+" is being calibrate \n"+"Please wait..", font=fonts['main'], bg=Background['main'])
        l.grid(row=0, column=0)

        b = tk.Button(self, text="OK", command=self.destroy, font=fonts['main'], bg=Background['submit'])
        b.grid(row=1, column=0, sticky="esnw")

        b = tk.Button(self, text="Cancel", command=self.destroy, font=fonts['main'], bg=Background['submit'])
        b.grid(row=1, column=1, sticky="esnw")

class completewindow(tk.Toplevel):

    def __init__(self, module):
        tk.Toplevel.__init__(self)
        self.grab_set()
        self.configure(background=Background['main'])
        self.geometry("200x60")

        #self.msg = tk.Toplevel()
        self.title("Process completed")

        l = tk.Label(self, text=module.upper()+" calibration is completed.", font=fonts['main'], bg=Background['main'])
        l.grid(row=0, column=0, sticky="esnw")

        b = tk.Button(self, text="OK", command=self.destroy, font=fonts['main'], bg=Background['submit'])
        b.grid(row=1, column=0, sticky="esnw")

