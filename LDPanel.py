import tkinter as tk
from CONFIG import *
from COMM import *
from Dynamic import *
from init_start import *
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use("TkAgg")
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from tkinter.messagebox import askyesnocancel
import pandas, os, sys, clr, time

#sys.path.append(r"C:\Program Files\Thorlabs\Kinesis")



# NB the
#clr.AddReference("Thorlabs.MotionControl.Benchtop.PiezoCLI")
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS

        return base_path + relative_path
    except Exception:
        base_path = os.getcwd()

        return base_path + relative_path




targetpath = resource_path(r"\DLLs")
#print(targetpath)
sys.path.append(targetpath)

clr.AddReference("Thorlabs.MotionControl.DeviceManagerCLI")
clr.AddReference("Thorlabs.MotionControl.KCube.InertialMotorCLI")
clr.AddReference("System")

import clr
#from Thorlabs.MotionControl.Benchtop.PiezoCLI import BenchtopPiezo
from Thorlabs.MotionControl.DeviceManagerCLI import DeviceManagerCLI
from Thorlabs.MotionControl.KCube.InertialMotorCLI import KCubeInertialMotor, InertialMotorStatus
from System import Decimal


class LDPanel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        if "LDR" in Globals.available:

            self.base="ld"
            self.configure(bg=Background['main'])
            # self.l_logo = Logo(self)
            # self.l_logo.update_logo()

            #LD definitions
            self.l_ld_ld_title = tk.Label(self, text="LD driver", font=fonts['title'], bg=Background['main'])


            self.l_curr = tk.Label(self, text="Current target (A)", font=fonts['main'], bg=Background['main'])
            self.t_curr = tk.Text(self, width=6, height=1)
            self.s_curr = ld_label(self)
            self.s_curr.update_status(getaddress(self.base+"_d", "curr"), "curr", "driver")
            self.b_curr = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                  command=lambda: submit(self, self.base+"_d", "curr"))

            self.l_act = tk.Label(self, text="Actual current (A)", font=fonts['main'], bg=Background['main'])
            self.s_act = ld_label(self)
            self.s_act.readin_ld(self.base)
            self.b_act = tk.Button(self, width=3, height=1, text="Plot", font=fonts['submit'], bg=Background['plot'], fg="white",
                                    command=lambda: self.plot(self.base, "LD supply current", "act"))

            self.l_cl = tk.Label(self, text="Current limit (A)", font=fonts['main'], bg=Background['main'])
            self.t_cl = tk.Text(self, width=6, height=1)
            self.s_cl = ld_label(self)
            self.s_cl.update_status(getaddress(self.base+"_d", "cl"), "cl", "driver")
            self.b_cl = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                  command=lambda: submit(self, self.base+"_d", "cl"))

            self.l_dc = tk.Label(self, text="Supply Voltage (V)*", font=fonts['main'], bg=Background['main'])
            self.t_dc = tk.Text(self, width=6, height=1)
            self.s_dc = ld_label(self)
            self.s_dc.update_status(getaddress(self.base+"_d", "dc"), "dc", "driver")
            self.b_dc = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                  bg=Background['submit'],
                                  command=lambda: submit(self, self.base+"_d", "dc"))

            self.l_ld_disclaimer = tk.Label(self, text="*Only change when there is no doubt.", font=fonts['main'],
                                            bg=Background['main'])

            self.l_delay = tk.Label(self, text="Stabilisation delay (s)", font=fonts['main'], bg=Background['main'])
            self.t_delay = tk.Text(self, width=6, height=1)
            self.s_delay = ld_label(self)
            self.s_delay.update_status(getaddress(self.base + "_d", "delay"), "delay", "driver")
            self.b_delay = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                  bg=Background['submit'],
                                  command=lambda: submit(self, self.base + "_d", "delay"))

            self.b_on=tk.Button(self, text="Pump on", width=13, command=lambda: self.laser_on(), bg=Colours['green'], fg="snow", font=fonts['main'])
            self.b_off=tk.Button(self, text="Pump off", width=13, command=lambda: self.laser_off(), bg=Colours['red'], fg="snow", font=fonts['main'])

            self.b_clpc = tk.Button(self, text="CLP compensation", width=20, font=fonts['main'],
                                        bg=Background['submit'],
                                        command=lambda: self.openclp(master, base))

            #LD grid
            # self.l_logo.grid(row=0, column=1, columnspan=4, rowspan=1, sticky="e", pady=5)
            # self.geths(self).grid(row=1, column=1, columnspan=4, sticky="we", pady=5)
            self.l_ld_ld_title.grid(row=2, column=1, columnspan=1, sticky="nw", pady=2)

            self.l_curr.grid(row=3, column=1, columnspan=1, sticky="nw", pady=2)
            self.t_curr.grid(row=3, column=2, columnspan=1, sticky="nw", pady=2)
            self.s_curr.grid(row=3, column=3, columnspan=1, sticky="eswn", pady=2)
            self.b_curr.grid(row=3, column=4, columnspan=1, sticky="nw", pady=2)

            self.l_act.grid(row=4, column=1, columnspan=1, sticky="nw", pady=2)
            self.s_act.grid(row=4, column=2, columnspan=2, sticky="nwes", pady=2)
            self.b_act.grid(row=4, column=4, columnspan=1, sticky="nw", pady=2)

            self.l_delay.grid(row=5, column=1, columnspan=1, sticky="nw", pady=2)
            self.t_delay.grid(row=5, column=2, columnspan=1, sticky="nw", pady=2)
            self.s_delay.grid(row=5, column=3, columnspan=1, sticky="nwse", pady=2)
            self.b_delay.grid(row=5, column=4, columnspan=1, sticky="nw", pady=2)

            self.l_cl.grid(row=6, column=1, columnspan=1, sticky="nw", pady=2)
            self.t_cl.grid(row=6, column=2, columnspan=1, sticky="nw", pady=2)
            self.s_cl.grid(row=6, column=3, columnspan=1, sticky="esnw", pady=2)
            self.b_cl.grid(row=6, column=4, columnspan=1, sticky="nw", pady=2)

            self.l_dc.grid(row=7, column=1, columnspan=1, sticky="nw", pady=2)
            self.t_dc.grid(row=7, column=2, columnspan=1, sticky="nw", pady=2)
            self.s_dc.grid(row=7, column=3, columnspan=1, sticky="nwse", pady=2)
            self.b_dc.grid(row=7, column=4, columnspan=1, sticky="nw", pady=2)

            self.b_on.grid(row=8, column=1, columnspan=1, sticky="nw", pady=(5, 0), padx=2)
            self.b_off.grid(row=8, column=2, columnspan=1, sticky="nw", pady=(5, 0), padx=2)
            self.l_ld_disclaimer.grid(row=9, column=1, columnspan=4, sticky="nw", pady=2)
            self.b_clpc.grid(row=10, column=1, columnspan=4, sticky="nw", pady=2)

    def laser_on(self):
            self.bit=getvalue(control['address'])['value']
            if readbit(self.bit, 3) == "1":
                if readbit(self.bit, 17) == "1":
                    if readbit(self.bit, 0) != "1":
                        addvalue(control['address'], 1)
                        Globals.incident_message = "LD pump is switching on."
                    else:
                        Globals.incident_message = "LD pump is switched on already."
                else:
                    Globals.incident_message = "TECs need to stabilise first."

    def laser_off(self):
            if getbit(control['address'], 0) == "1":
                resvalue(control['address'], 1)
                Globals.incident_message = "Laser pump turned off. \n"
            else:
                Globals.incident_message = "Laser pump turned off already. \n"

    def plot(self, base, subject, type="act"):
        plot=graph(self, base, subject, type)

    def geths(self, parent):
        hs = ttk.Separator(parent, orient=tk.HORIZONTAL)
        return hs

    def openclp (self, master, base):
        comp = compensation(master, base)

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
        self.interval = 1000
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
        b2 = tk.Button(self, text="Write", command=lambda: self.write(self.x, self.y), font=fonts['main'],
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
        self.ax.plot(self.x, self.y, color='b', label=subject + " (A)")
        #if self.check == 1:
        #    self.ax.plot(self.x, self.z, color='b', label="BP temperature")

        # ax.plot([1,2,3,4,5],[1,2,3,4,5])
        self.ax.set_xlabel('time (s)')
        self.ax.xaxis.set_label_position('top')
        self.ax.set_ylabel('Current (A)')
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
        return self.ax.plot(self.x, self.y, color='b', label=self.base + " (A)")

    def write(self, x, y, z=[], type=False):
        df = pandas.DataFrame(data={"(s)": x, "Current(A)": y})
        df_folder = "C:/Plotting/"
        if not os.path.exists(df_folder):
            os.makedirs(df_folder)
        file = df_folder + "LD_curr" + str(time.time()) + ".csv"
        df.to_csv(file, sep=',', index=False)


class PlotMagic(object):

    def __init__(self):
        self.x = 0
        print("Plotmagic started")

    def __call__(self, address, interval):
        self.x = self.x + interval / 1000
        self.y = getvalue(address, "u", "u")['value']
        # if box == 1:
        #     self.z = getvalue("dfd4", "u", "k")['value']
        #     return self.x, self.y, self.z
        #else:
        return self.x, self.y


class compensation(tk.Toplevel):

    def __init__(self, master, b):
        tk.Toplevel.__init__(self)
        # self.grab_set()
        self.configure(background=Background['main'])
        self.geometry("750x500")
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


        self.title = tk.Label(self, text = "CLP compensation settings", font=fonts['title'], bg=Background['main'])



        self.l_clpe = tk.Label(self, text="Enable compensation (1-on)", font=fonts['main'], bg=Background['main'])
        self.t_clp_enable = tk.Text(self, width=6, height=1)
        self.s_clp_enable = ld_label(self)
        self.s_clp_enable.update_status(getaddress("ld_d", "clp_enable"), "clp_enable", "driver")
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

        self.l_clp_repeat = tk.Label(self, text="CLP repeat interval (s)", font=fonts['main'], bg=Background['main'])
        self.t_clp_repeat = tk.Text(self, width=6, height=1)
        self.s_clp_repeat = ld_label(self)
        self.s_clp_repeat.update_status(getaddress("ld_d", "clp_repeat"), "clp_repeat", "driver")
        self.b_clp_repeat = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                  bg=Background['submit'],
                                  command=lambda: submit(self, "ld_d", "clp_repeat", min = 60, max = 3600))

        self.l_clp_step = tk.Label(self, text="CLP current step (uA)", font=fonts['main'], bg=Background['main'])
        self.t_clp_step = tk.Text(self, width=6, height=1)
        self.s_clp_step = ld_label(self)
        self.s_clp_step.update_status(getaddress("ld_d", "clp_step"), "clp_step", "driver")
        self.retrieveclpstep()
        self.b_clp_step = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                  bg=Background['submit'],
                                  command=lambda: self.setclpstep())

        self.title2 = tk.Label(self, text="Crystal shifter settings", font=fonts['title'], bg=Background['main'])

        self.l_shifte = tk.Label(self, text="Enable shifting (1-on)", font=fonts['main'], bg=Background['main'])
        self.t_shift_enable = tk.Text(self, width=6, height=1)
        self.s_shift_enable = gui_label(self)
        self.s_shift_enable.update_status(getaddress("gui", "shift_enable"), "shift_enable")
        self.b_shifte = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                  bg=Background['submit'],
                                  command=lambda: submit(self, "gui", "shift_enable", min = -0.1, max = 1.1))

        self.retrieveclp()
        self.retrieveclpstep()

        self.l_shifts = tk.Label(self, text="Shift step", font=fonts['main'], bg=Background['main'])
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

        self.l_clp_step.grid(row=5, column=1, columnspan=1, sticky="nw", pady=self.pady)
        self.t_clp_step.grid(row=5, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_clp_step.grid(row=5, column=3, columnspan=1, sticky="nw", pady=self.pady)
        self.b_clp_step.grid(row=5, column=4, columnspan=1, sticky="nw", pady=self.pady)
        self.cdisc.grid(row=6, column=1, columnspan=4, sticky="nw", pady=self.pady)

        self.title2.grid(row=10, column=1, columnspan=2, sticky="nw", pady=self.pady)

        self.l_shifte.grid(row=11, column=1, columnspan=1, sticky="nw", pady=self.pady)
        self.t_shift_enable.grid(row=11, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_shift_enable.grid(row=11, column=3, columnspan=1, sticky="nw", pady=self.pady)
        self.b_shifte.grid(row=11, column=4, columnspan=1, sticky="nw", pady=self.pady)

        self.l_shifts.grid(row=12, column=1, columnspan=1, sticky="nw", pady=self.pady)
        self.t_shift_step.grid(row=12, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_shift_step.grid(row=12, column=3, columnspan=1, sticky="nw", pady=self.pady)
        self.b_shifts.grid(row=12, column=4, columnspan=1, sticky="nw", pady=self.pady)

        self.l_shiftser.grid(row=13, column=1, columnspan=1, sticky="nw", pady=self.pady)
        self.t_shift_serial.grid(row=13, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_shift_serial.grid(row=13, column=3, columnspan=1, sticky="nw", pady=self.pady)
        self.b_shiftser.grid(row=13, column=4, columnspan=1, sticky="nw", pady=self.pady)

        self.l_shiftth.grid(row=14, column=1, columnspan=1, sticky="nw", pady=self.pady)
        self.t_shift_threshold.grid(row=14, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_shift_threshold.grid(row=14, column=3, columnspan=1, sticky="nw", pady=self.pady)
        self.b_shiftth.grid(row=14, column=4, columnspan=1, sticky="nw", pady=self.pady)

        self.l_shiftc.grid(row=15, column=1, columnspan=1, sticky="nw", pady=self.pady)
        #self.t_shift_count.grid(row=15, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_shift_count.grid(row=15, column=3, columnspan=1, sticky="nw", pady=self.pady)
        #self.b_shiftc.grid(row=15, column=4, columnspan=1, sticky="nw", pady=self.pady)

        self.l_shiftpos.grid(row=16, column=1, columnspan=1, sticky="nw", pady=self.pady)
        self.t_shift_position.grid(row=16, column=2, columnspan=1, sticky="nw", pady=self.pady)
        self.s_shift_position.grid(row=16, column=3, columnspan=1, sticky="nw", pady=self.pady)
        self.b_shiftpos.grid(row=16, column=4, columnspan=1, sticky="nw", pady=self.pady)

        self.b_shift.grid(row=20, column=2, columnspan=2, sticky="nw", pady=self.pady)
        self.b_connect.grid(row=20, column=3, columnspan=2, sticky="nw", pady=self.pady)
        self.disc.grid(row=21, column=1, columnspan=4, sticky="nw", pady=self.pady)

        self.shifter_connect = 0

    def geths(self, parent):
            hs = ttk.Separator(parent, orient=tk.HORIZONTAL)
            return hs

    def retrieveclp(self):

        val = getvalue(getaddress("ld_d", "clp_enable"), "1", "1")["value"]
        instr = int(val[6:7])

        if instr == 2:
            self.s_clp_enable.configure(text="on")
        else:
            self.s_clp_enable.configure(text="off")

    def enableclp(self):
            val = getvalue(getaddress("ld_d", "clp_enable"),"1", "1")["value"]
            instr = int(val[6:7])
            vall = int(retrieve(self.t_clp_enable))
            #print(val, instr, vall)
            if vall == 1:
                if instr == 2:
                    self.s_clp_enable.configure(text = "Already on")
                else:
                    setvalue(getaddress("ld_d", "clp_enable"), "0x55502AAA","1", "1")
                    self.s_clp_enable.configure(text="Activated")
            elif vall == 0:
                if instr == 0:
                    self.s_clp_enable.configure(text = "Already off")
                else:
                    setvalue(getaddress("ld_d", "clp_enable"), "0x55500AAA","1", "1")
                    self.s_clp_enable.configure(text="Turned off")
            else:
                self.s_clp_enable.configure(text="Error")
                self.cdisc.configure(text = "Use 1 or 0 to turn compensation on or off.")

    def setclpstep(self):
        vall = retrieve(self.t_clp_step)
        #val = 1000000*val
        if vall > 30000 or vall < -30000:
                self.cdisc.configure(text = "Step size is out of limit.")
                self.s_clp_step.configure(text = "error")
        elif vall < 200 and vall > -100:
            self.cdisc.configure(text="Min step size is abs(100).")
            self.s_clp_step.configure(text="error")
        else:
            val = int(vall/100)
            val = self.int2hex4(val)
            #val = val[:-4]
            subval = "0x55" + val + "AA"
            setvalue(getaddress("ld_d", "clp_step"), subval,"1", "1")
            self.cdisc.configure(text = f"Step set to {str(vall)} uA.")
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
        #print(steps, step)
        val = hex2signed(step)
        if val > 2**15:
            val = -(2**16-val)
        self.s_clp_step.configure(text = 100*val)

    def getshifterstatus(self):
        bool1 = int(getvalue(getaddress("gui", "shift_enable"))["value"])
        if bool1 == 1 and self.shifter_connect == 1:
            return 1
        else:
            return 0

    def shiftit(self):
        if self.getshifterstatus() == 1:
            stp = getvalue(getaddress("gui", "shift_step"),"i", "1")["value"]
            self.dev.move(stp)

            pos = getvalue(getaddress("gui", "shift_position"), "i", "1")["value"]
            newpos = pos + stp
            setvalue(getaddress("gui", "shift_position"), newpos, "i", "1")
            self.s_shift_position.configure(text = str(newpos))

            c = getvalue(getaddress("gui", "shift_count"), "u", "1")["value"]
            newc = c + 1
            setvalue(getaddress("gui", "shift_count"), newc, "u", "1")
            self.s_shift_count.configure(text = str(newc))
        else:
            self.disc.configure(text = "Connect driver first, enable shifting.")

    def submit_q(self):
        bool = askyesnocancel("Confirm to proceed", "Are you sure you want to move shifter reference position? \nThis will zero counter, the shifter will NOT actuate.")
        if bool:
            vall = retrieve(self.t_shift_position)
            setvalue(getaddress("gui", "shift_position"), vall, "i", "1")
            setvalue(getaddress("gui", "shift_count"), 0)
            self.s_shift_position.configure(text = vall)
            self.s_shift_count.configure(text = 0)

    def connectit(self):
        self.dev = BenchtopPiezoWrapper(getvalue(getaddress("gui", "shift_serial"))["value"])
        self.dev.connect()
        self.b_connect.configure(text = "DISCONNECT", command = lambda: self.disconnectit(), bg=Colours['red'], fg = "white")
        self.shifter_connect = 1
        self.disc.configure(text="Driver connected")

    def disconnectit(self):
        self.dev.close()
        self.b_connect.configure(text = "CONNECT", command = lambda: self.connectit(), bg=Colours['green'], fg = "black")
        self.shifter_connect = 0
        self.disc.configure(text="Driver disconnected")

class BenchtopPiezoWrapper():
    def __init__(self, serial_number):
        self._ser = str(serial_number)
        #print("serial",self._ser)
        DeviceManagerCLI.BuildDeviceList()
        #print("avail device", DeviceManagerCLI.GetDeviceList())
        self._pzt = KCubeInertialMotor.CreateKCubeInertialMotor(self._ser)
        self.channels = []
        self.connected = False

    def connect(self):
        """Initialise communications, populate channel list, etc."""
        assert not self.connected
        self._pzt.Connect(self._ser)
        self.connected = True
        #print(self._pzt.GetDeviceInfo().Name)
        self._pzt.StartPolling(250)
        self._pzt.EnableDevice()


        assert len(self.channels) == 0, "Error connecting: we've already initialised channels!"
        # #for i in range(self._piezo.ChannelCount):
        # for i in range(1):
        #     #chan = self._piezo.GetChannel(i + 1)  # Kinesis channels are one-indexed
        #     chan = self._piezo.channel()
        #     chan.WaitForSettingsInitialized(5000)
        #     chan.StartPolling(250)  # getting the voltage only works if you poll!
        #     time.sleep(0.5)  # ThorLabs have this in their example...
        #     chan.EnableDevice()
        #     # I don't know if the lines below are necessary or not - but removing them
        #     # may or may not work...
        #     time.sleep(0.5)
        #     config = chan.GetPiezoConfiguration(chan.DeviceID)
        #     info = chan.GetDeviceInfo()
        #     max_v = Decimal.ToDouble(chan.GetMaxOutputVoltage())
        #     self.channels.append(chan)
        #     print("succes")

    def close(self):
        """Shut down communications"""
        # if not self.connected:
        #     print(f"Not closing piezo device {self._ser}, it's not open!")
        #     return
        self._pzt.StopPolling()
        try:
            self._pzt.Disconnect(True)
        except:
            pass
        # for chan in self.channels:
        #     chan.StopPolling()
        # self.channels = []
        # self._pzt.Disconnect(True)

    def move(self, target):
        self._pzt.SetPositionAs(InertialMotorStatus.MotorChannels.Channel1, 0);
        self._pzt.MoveTo(InertialMotorStatus.MotorChannels.Channel1, target, 60000)
        time.sleep(1)
        curr = self._pzt.GetPosition(InertialMotorStatus.MotorChannels.Channel1)

        return curr

    def __del__(self):
        try:
            if self.connected:
                self.close()
        except:
            print(f"Error closing communications on deletion of device {self._ser}")

    def set_output_voltages(self, voltages):
        """Set the output voltage"""
        assert len(voltages) == len(self.channels), "You must specify exactly one voltage per channel"
        for chan, v in zip(self.channels, voltages):
            chan.SetOutputVoltage(Decimal(v))

    def get_output_voltages(self):
        """Retrieve the output voltages as a list of floating-point numbers"""
        return [Decimal.ToDouble(chan.GetOutputVoltage()) for chan in self.channels]

    # def resource_path(self, relative_path):
    #     try:
    #         base_path = sys._MEIPASS
    #     except Exception:
    #         base_path = os.path.abspath(".")
    #
    #     return os.path.join(base_path, relative_path)

    output_voltages = property(get_output_voltages, set_output_voltages)