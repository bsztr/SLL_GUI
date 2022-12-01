import tkinter as tk
from tkinter import ttk
from CONFIG import *
from COMM import *
from init_start import *
from Dynamic import *
from Plotting import *
import Globals

class TECArch(tk.Frame):
    def __init__(self, master, title, base, y):
        tk.Frame.__init__(self, master)

        self.pdy=2
        self.pdx=5
        self.configure(bg=Background['main'])

        self.l_title = tk.Label(master, text=title, font=fonts['title'], bg=Background['main'])
        self.gettecname(base, self.l_title)
        self.l_set = tk.Label(master, text="Set temperature (C)", font=fonts['main'], bg=Background['main'])
        self.t_set = tk.Text(master, width=6, height=1)
        self.s_set=temp_label(self.master)
        self.s_set.update_temp(base, "set", "driver")
        self.b_set = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                    command=lambda: submit(self, base+"_d", "set", base+"threshold"))

        self.l_act = tk.Label(master, text="Actual temperature (C)", font=fonts['main'], bg=Background['main'])
        self.t_act = temp_label(self.master)
        self.t_act.readin_temp(base)

        self.l_c = tk.Label(master, text="TEC Current (A)", font=fonts['main'], bg=Background['main'])
        self.t_c = tk.Text(master, width=6, height=1)
        #self.t_c.update_status(getaddress(base, "current"), "current", "slot")
        self.b_c = tk.Button(master, width=3, height=1, text="Plot", font=fonts['submit'],
                                  bg=Background['plot'], fg="white",
                                  command=lambda: self.plot(base, "current (A)", "current", self.t_c, "req current"))

        if base != "tec3":
            self.l_p = tk.Label(master, text="P Gain", font=fonts['main'], bg=Background['main'])
            self.t_p = tk.Text(master, width=6, height=1)
            self.s_p = temp_label(self.master)
            self.s_p.update_status(getaddress(base+"_d", "p"), "p", "driver")
            self.b_p = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                        command=lambda: submit(self, base+"_d", "p"))

            self.l_i = tk.Label(master, text="I Gain", font=fonts['main'], bg=Background['main'])
            self.t_i = tk.Text(master, width=6, height=1)
            self.s_i=temp_label(self.master)
            self.s_i.update_status(getaddress(base+"_d", "i"), "i", "driver")
            self.b_i = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                        command=lambda: submit(self, base+"_d", "i"))

            self.l_d = tk.Label(master, text="D Gain", font=fonts['main'], bg=Background['main'])
            self.t_d = tk.Text(master, width=6, height=1)
            self.s_d=temp_label(self.master)
            self.s_d.update_status(getaddress(base+"_d", "d"), "d", "driver")
            self.b_d = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                        command=lambda: submit(self, base+"_d", "d"))

            self.l_maxv = tk.Label(master, text="Max voltage (V)", font=fonts['main'], bg=Background['main'])
            self.t_maxv = tk.Text(master, width=6, height=1)
            self.s_maxv=temp_label(self.master)
            self.s_maxv.update_status(getaddress(base+"_d", "maxv"), "maxv", "driver")
            self.b_maxv = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                        command=lambda: submit(self, base+"_d", "maxv"))

            self.l_maxc = tk.Label(master, text="Max current (A)", font=fonts['main'], bg=Background['main'])
            self.t_maxc = tk.Text(master, width=6, height=1)
            self.s_maxc=temp_label(self.master)
            self.s_maxc.update_status(getaddress(base+"_d", "maxc"), "maxc", "driver")
            self.b_maxc = tk.Button(master, width=3, height=1, text="OK",font=fonts['submit'], bg=Background['submit'],
                                        command=lambda: submit(self, base+"_d", "maxc"))

        self.l_warm = tk.Label(master, text="Warm up (s)", font=fonts['main'], bg=Background['main'])
        self.t_warm = tk.Text(master, width=6, height=1)
        self.s_warm = temp_label(self.master)
        self.s_warm.update_status(getaddress(base + "_d", "warm"), "warm", "driver")
        self.b_warm = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                                    command=lambda: submit(self, base+"_d", "warm"))

        self.l_mint = tk.Label(master, text="Min temp", font=fonts['main'], bg=Background['main'])
        self.t_mint = tk.Text(master, width=6, height=1)
        self.s_mint = temp_label(self.master)
        self.s_mint.update_status(getaddress(base + "_d", "mint"), "mint", "driver")
        self.b_mint = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                             command=lambda: submit(self, base + "_d", "mint"))

        self.l_maxt = tk.Label(master, text="Max temp", font=fonts['main'], bg=Background['main'])
        self.t_maxt = tk.Text(master, width=6, height=1)
        self.s_maxt = temp_label(self.master)
        self.s_maxt.update_status(getaddress(base + "_d", "maxt"), "maxt", "driver")
        self.b_maxt = tk.Button(master, width=3, height=1, text="OK", font=fonts['submit'], bg=Background['submit'],
                             command=lambda: submit(self, base + "_d", "maxt"))


        self.temp_plot=pidplot(master, "PID plot", base, "temperature", 15,y)
        self.temp_ramp=iterate(master, "Scan temperature", base+"_d", "set", 22, y, False)

        self.l_title.grid(row=3, column=y, columnspan=4, sticky="nw", pady=self.pdy)
        self.l_set.grid(row=4, column=y, sticky="nw", pady=self.pdy)
        self.t_set.grid(row=4, column=y+1, sticky="nw", pady=self.pdy)
        self.s_set.grid(row=4, column=y+2, sticky="nwse", pady=self.pdy, padx=self.pdx)
        self.b_set.grid(row=4, column=y+3, sticky="nw", pady=self.pdy)
        self.l_act.grid(row=5, column=y, sticky="nw", pady=self.pdy)
        self.t_act.grid(row=5, column=y+1, sticky="nwse", pady=self.pdy, columnspan=3)
        if base != "tec3":
            self.l_p.grid(row=6, column=y, sticky="nw", pady=self.pdy)
            self.t_p.grid(row=6, column=y+1, sticky="nw", pady=self.pdy)
            self.s_p.grid(row=6, column=y+2, sticky="nwse", pady=self.pdy, padx=self.pdx)
            self.b_p.grid(row=6, column=y+3, sticky="nw", pady=self.pdy)
            self.l_i.grid(row=7, column=y, sticky="nw", pady=self.pdy)
            self.t_i.grid(row=7, column=y+1, sticky="nw", pady=self.pdy)
            self.s_i.grid(row=7, column=y+2, sticky="nwse", pady=self.pdy, padx=self.pdx)
            self.b_i.grid(row=7, column=y+3, sticky="nw", pady=self.pdy)
            self.l_d.grid(row=8, column=y, sticky="nw", pady=self.pdy)
            self.t_d.grid(row=8, column=y+1, sticky="nw", pady=self.pdy)
            self.s_d.grid(row=8, column=y+2, sticky="nwse", pady=self.pdy, padx=self.pdx)
            self.b_d.grid(row=8, column=y+3, sticky="nw", pady=self.pdy)
            self.l_c.grid(row=9, column=y, sticky="nw", pady=self.pdy)
            self.t_c.grid(row=9, column=y+1, sticky="nw", pady=self.pdy, columnspan=1)
            self.b_c.grid(row=9, column=y + 3, columnspan=1, sticky="nw", pady=self.pdy)
            self.l_maxv.grid(row=10, column=y, sticky="nw", pady=self.pdy)
            self.t_maxv.grid(row=10, column=y+1, sticky="nw", pady=self.pdy)
            self.s_maxv.grid(row=10, column=y+2, sticky="nwse", pady=self.pdy, padx=self.pdx)
            self.b_maxv.grid(row=10, column=y+3, sticky="nw", pady=self.pdy)
            self.l_maxc.grid(row=11, column=y, sticky="nw", pady=self.pdy)
            self.t_maxc.grid(row=11, column=y+1, sticky="nw", pady=self.pdy)
            self.s_maxc.grid(row=11, column=y+2, sticky="nwse", pady=self.pdy, padx=self.pdx)
            self.b_maxc.grid(row=11, column=y+3, sticky="nw", pady=self.pdy)
        self.l_mint.grid(row=12, column=y, sticky="nw", pady=self.pdy)
        self.t_mint.grid(row=12, column=y + 1, sticky="nw", pady=self.pdy)
        self.s_mint.grid(row=12, column=y + 2, sticky="nwse", pady=self.pdy, padx=self.pdx)
        self.b_mint.grid(row=12, column=y + 3, sticky="nw", pady=self.pdy)
        self.l_maxt.grid(row=13, column=y, sticky="nw", pady=self.pdy)
        self.t_maxt.grid(row=13, column=y + 1, sticky="nw", pady=self.pdy)
        self.s_maxt.grid(row=13, column=y + 2, sticky="nwse", pady=self.pdy, padx=self.pdx)
        self.b_maxt.grid(row=13, column=y + 3, sticky="nw", pady=self.pdy)
        self.l_warm.grid(row=14, column=y, sticky="nw", pady=self.pdy)
        self.t_warm.grid(row=14, column=y + 1, sticky="nw", pady=self.pdy)
        self.s_warm.grid(row=14, column=y + 2, sticky="nwse", pady=self.pdy, padx=self.pdx)
        self.b_warm.grid(row=14, column=y + 3, sticky="nw", pady=self.pdy)
        self.getvs(master).grid(row=2, column=y+4, sticky="ns", rowspan=11, padx=2*self.pdx)

    def geths(self, parent):
            hs = ttk.Separator(parent, orient=tk.HORIZONTAL)
            return hs

    def getvs(self, parent):
            vs = ttk.Separator(parent, orient=tk.VERTICAL)
            return vs

    def getcolour(self, result):
        if result != "":
            return Colours['red']
        else:
            return Colours['green']

    def gettecname(self, base, label):
            status=getNames()[base]
            label.configure(text=status)
            tecname_after = label.after(2000, lambda: self.gettecname(base, label))

    def plot(self, base, subject, type="clp", interval=1000, second = ""):
        if interval == 1000 or interval.get("1.0", 'end-1c') == "":
            self.duration = 1000
        else:
            self.duration=int(round(float(interval.get("1.0", 'end-1c')),0))
        plot=graph(self, base, subject, type, second)

class graph(tk.Toplevel):

    def __init__(self, master, b, subject, rel, second):
        tk.Toplevel.__init__(self)
        # self.grab_set()
        self.configure(background=Background['main'])
        self.geometry("750x600")
        self.title("Plotting")
        self.address = getaddress(b, rel)
        if second != "":
            self.second = getaddress(b, second)
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
        self.ax.plot(self.x, self.y, color='darkviolet', label=self.base.upper() + " Actual current (A)")
        if self.second != "":
            self.ax.plot(self.x, self.z, color='b', label="Requested current (A)")

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
            yield self.plot_data(self.address, self.interval, self.second)

    def animate(self, args):
        self.x.append(args[0])
        self.y.append(args[1])
        if self.second != "":
            self.z.append(args[2])

            return print("graph is on now!!"), self.ax.plot(self.x, self.y, color='darkviolet', label=self.base.upper() + " Actual current (A)"), self.ax.plot(
               self.x, self.z, 'b--', label="Requested current")

        else:
            return self.ax.plot(self.x, self.y, color='darkviolet', label=self.base.upper() + " Actual current (A)")

    def write(self, x, y, z=[], type=False, subject=""):
        if type == True:
            df = pandas.DataFrame(data={"time(s)": x, self.base.upper() + "Actual current (A)": y, "Requested current (A)": z})
        else:
            df = pandas.DataFrame(data={"time(s)": x,self.base.upper() + "Actual current (A)" : y})
        df_folder = "C:/Plotting/"
        if not os.path.exists(df_folder):
            os.makedirs(df_folder)
        file = df_folder + subject.upper() + str(time.time()) + ".csv"
        df.to_csv(file, sep=',', index=False)


class PlotMagic(object):

    def __init__(self):
        self.x = 0
        print("Plotmagic started")

    def __call__(self, address, interval, second):
        self.x = self.x + interval / 1000
        self.y = getvalue(address, "u", "u")['value']
        if second != "":
             self.z = getvalue(second, "i", "u")['value']
             if self.z < 0:
                 self.y = -self.y
             return self.x, self.y, self.z
        else:
            return self.x, self.y
