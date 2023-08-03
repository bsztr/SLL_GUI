import tkinter as tk
from CONFIG import *
from COMM import *
from Dynamic import ld_label, pzt_label, gui_label, compensation
from init_start import *
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use("TkAgg")
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from tkinter.messagebox import askyesnocancel
import pandas, os, sys, time
import numpy as np

#sys.path.append(r"C:\Program Files\Thorlabs\Kinesis")



# NB the
#clr.AddReference("Thorlabs.MotionControl.Benchtop.PiezoCLI")



class LDPanel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        if "LDR" in Globals.available:

            fwv = str(getvalue(getaddress("ld", "fw"), "u", "1")["value"])

            try:
                ld_fwv = f"ver: {fwv[0]}.{fwv[1]}.{fwv[2]}"
            except:
                ld_fwv = f"ver: {fwv}"

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

            # self.l_dc = tk.Label(self, text="Supply Voltage (V)*", font=fonts['main'], bg=Background['main'])
            # self.t_dc = tk.Text(self, width=6, height=1)
            # self.s_dc = ld_label(self)
            # self.s_dc.update_status(getaddress(self.base+"_d", "dc"), "dc", "driver")
            # self.b_dc = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
            #                       bg=Background['submit'],
            #                       command=lambda: submit(self, self.base+"_d", "dc"))

            self.l_ld_disclaimer = tk.Label(self, text="*Only change when there is no doubt.", font=fonts['main'],
                                            bg=Background['main'])

            self.l_delay = tk.Label(self, text="Stabilisation delay (s)", font=fonts['main'], bg=Background['main'])
            self.t_delay = tk.Text(self, width=6, height=1)
            self.s_delay = ld_label(self)
            self.s_delay.update_status(getaddress(self.base + "_d", "delay"), "delay", "driver")
            self.b_delay = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
                                  bg=Background['submit'],
                                  command=lambda: submit(self, self.base + "_d", "delay"))

            # self.l_Kp = tk.Label(self, text="LD PID compensation value", font=fonts['main'], bg=Background['main'])
            # self.t_Kp = tk.Text(self, width=6, height=1)
            # self.s_Kp = ld_label(self)
            # self.s_Kp.update_status(getaddress(self.base, "Kp"), "Kp", "slot")
            # self.b_Kp = tk.Button(self, width=3, height=1, text="OK", font=fonts['submit'],
            #                       bg=Background['submit'],
            #                       command=lambda: submit(self, self.base, "Kp"))

            self.b_on=tk.Button(self, text="Pump on", width=13, command=lambda: self.laser_on(), bg=Colours['green'], fg="snow", font=fonts['main'])
            self.b_off=tk.Button(self, text="Pump off", width=13, command=lambda: self.laser_off(), bg=Colours['red'], fg="snow", font=fonts['main'])
            self.b_save = tk.Button(self, text="SAVE", width=13, command=lambda: save_regs('ld'), bg=Colours['grey'],
                                   fg="black", font=fonts['main'])
            self.l_ldver = tk.Label(self, text=ld_fwv, font=fonts['main'], bg=Background['main'])

            # self.b_clpc = tk.Button(self, text="OPM settings", width=20, font=fonts['main'],
            #                             bg=Background['submit'],
            #                             command=lambda: self.openclp(master, base))

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

            # self.l_Kp.grid(row=6, column=1, columnspan=1, sticky="nw", pady=2)
            # self.t_Kp.grid(row=6, column=2, columnspan=1, sticky="nw", pady=2)
            # self.s_Kp.grid(row=6, column=3, columnspan=1, sticky="nwse", pady=2)
            # self.b_Kp.grid(row=6, column=4, columnspan=1, sticky="nw", pady=2)

            self.l_cl.grid(row=7, column=1, columnspan=1, sticky="nw", pady=2)
            self.t_cl.grid(row=7, column=2, columnspan=1, sticky="nw", pady=2)
            self.s_cl.grid(row=7, column=3, columnspan=1, sticky="esnw", pady=2)
            self.b_cl.grid(row=7, column=4, columnspan=1, sticky="nw", pady=2)

            # self.l_dc.grid(row=8, column=1, columnspan=1, sticky="nw", pady=2)
            # self.t_dc.grid(row=8, column=2, columnspan=1, sticky="nw", pady=2)
            # self.s_dc.grid(row=8, column=3, columnspan=1, sticky="nwse", pady=2)
            # self.b_dc.grid(row=8, column=4, columnspan=1, sticky="nw", pady=2)

            self.b_on.grid(row=9, column=1, columnspan=1, sticky="nw", pady=(5, 0), padx=2)
            self.b_off.grid(row=9, column=2, columnspan=1, sticky="nw", pady=(5, 0), padx=2)
            self.b_save.grid(row=9, column=3, columnspan=2, sticky="nw", pady=(5, 0), padx=2)
            self.l_ldver.grid(row=9, column=5, columnspan=1, sticky="nw", pady=(5, 0), padx=2)
            self.l_ld_disclaimer.grid(row=10, column=1, columnspan=4, sticky="nw", pady=2)
            # self.b_clpc.grid(row=11, column=1, columnspan=4, sticky="nw", pady=2)

    def laser_on(self):
            self.bit=getvalue(status['address'])['value']
            if readbit(self.bit, status["TEC_READY"]) == "1" and readbit(self.bit, status["LD_OK"]) == "0":
                        addvalue(control['address'], 2**control['ld'])
                        time.sleep(0.5)
                        Globals.incident_message = "LD pump is switching on."
            elif readbit(self.bit, status["LD_OK"]) == "1":
                        Globals.incident_message = "LD pump is switched on already."
            else:
                Globals.incident_message = "TECs need to stabilise first."

    def laser_off(self):
            if getbit(status['address'], status["LD_OK"]) == "1":
                resvalue(control['address'], 2**control['ld'])
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


