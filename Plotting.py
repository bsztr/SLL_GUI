import tkinter as tk
from CONFIG import *
from tkinter import ttk
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use("TkAgg")
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from init_start import getaddress
from COMM import getvalue, setvalue, readbit
from tkinter.messagebox import showinfo
import os
import pandas
import time
import Globals


class pidplot(tk.Label):
    def __init__(self, master, title, b, subject, row, column):
        tk.Frame.__init__(self, master)

        self.pdy=3
        self.pdx = 2
        # self.arg1= eval(base[b][1])[rel][1]
        # self.arg2=eval(base[b][1])[rel][2]
        # self.pzt=pzt
        # self.sign="(C)"
        # self.lock=0
        # self.manual=0

        self.l_name = tk.Label(master, text=title, font=fonts['main'], bg=Background['main'])
        self.l_set = tk.Label(master, text="Temperature (C)", font=fonts['main'], bg=Background['main'])
        self.t_set = tk.Text(master, font=fonts['main'], width=12, height=1)
        self.t_set.insert(tk.INSERT, eval("Globals." + b + "_set"))
        self.l_time= tk.Label(master, text="Sampling(ms)", font=fonts['main'], bg=Background['main'])
        self.t_time= tk.Text(master, font=fonts['main'], width=12, height=1)
        self.t_time.insert(tk.INSERT, "1000")
        self.check=tk.IntVar()
        self.l_bp=tk.Label(master, text="all?", font=fonts['status'], bg=Background['main'])
        self.t_bp=tk.Checkbutton(master, bg=Background['main'], var=self.check)
        self.l_p = tk.Label(master, text="P", font=fonts['main'], bg=Background['main'])
        self.t_p = tk.Text(master, font=fonts['main'], width=12, height=1)
        rel="p"
        self.address=getaddress(b+"_d", rel)
        bb=b[:3]+"_d"
        self.resultp = round(getvalue(self.address, eval(bb)[rel][1], eval(bb)[rel][2])['value'], 2)
        self.t_p.insert(tk.INSERT, self.resultp)
        self.l_i = tk.Label(master, text="I", font=fonts['main'], bg=Background['main'])
        self.t_i = tk.Text(master, font=fonts['main'], width=6, height=1)
        rel="i"
        self.address=getaddress(b+"_d", rel)
        bb=b[:3]+"_d"
        self.resulti = round(getvalue(self.address, eval(bb)[rel][1], eval(bb)[rel][2])['value'], 2)
        self.t_i.insert(tk.INSERT, self.resulti)
        self.l_d = tk.Label(master, text="D", font=fonts['main'], bg=Background['main'])
        self.t_d = tk.Text(master, font=fonts['main'], width=6, height=1)
        rel="d"
        self.address=getaddress(b+"_d", rel)
        bb=b[:3]+"_d"
        self.resultd = round(getvalue(self.address, eval(bb)[rel][1], eval(bb)[rel][2])['value'], 2)
        self.t_d.insert(tk.INSERT, self.resultd)

        self.b_button = tk.Button(master, text="Plot", font=fonts['submit'], bg=Background['plot'], fg="white", command= lambda: self.plot(b, subject, self.check))

        self.l_name.grid(row=row+1, column=column, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.l_set.grid(row=row+2, column=column, columnspan=2, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.t_set.grid(row=row+3, column=column, columnspan=2, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.l_time.grid(row=row + 2, column=column+1, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.t_time.grid(row=row + 3, column=column+1, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.l_bp.grid(row=row + 3, column=column + 2, sticky="esnw", pady=self.pdy, padx=self.pdx)
        self.t_bp.grid(row=row + 3, column=column + 3, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.l_p.grid(row=row + 4, column=column, columnspan=2, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.t_p.grid(row=row + 5, column=column, columnspan=2, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.l_i.grid(row=row + 4, column=column+1, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.t_i.grid(row=row + 5, column=column+1, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.l_d.grid(row=row + 4, column=column+2, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.t_d.grid(row=row + 5, column=column+2, sticky="nw", pady=self.pdy, padx=self.pdx)
        self.b_button.grid(row=row+5, column=column+3, sticky="nw", pady=self.pdy, padx=self.pdx)

        self.geths(master).grid(row=row, column=column, columnspan= 5, sticky="we", pady=self.pdy, padx=self.pdx)
        #self.geths(master).grid(row=row+6, column=column, columnspan=5, sticky="we", pady=self.pdy, padx=self.pdx)
        self.getvs(master).grid(row=row, column=column+4, rowspan=6, sticky="sn", pady=self.pdy, padx=self.pdx)


    def geths(self, parent):
            hs = ttk.Separator(parent, orient=tk.HORIZONTAL)
            return hs

    def getvs(self, parent):
            hs = ttk.Separator(parent, orient=tk.VERTICAL)
            return hs

    def plot(self, base, subject, box):
        self.duration=int(round(float(self.t_time.get("1.0", 'end-1c')),0))
        self.set=round(float(self.t_set.get("1.0", 'end-1c')),2)
        if round(getvalue(getaddress(base+"_d", "set"), "u", "k")["value"],2) != self.set:
            setvalue(getaddress(base + "_d", "set"), self.set, "u", "k")

        self.p=float(self.t_p.get("1.0", 'end-1c'))
        self.resultp = round(getvalue(getaddress(base+"_d", "p"), "f", "1")["value"],2)
        self.i=float(self.t_i.get("1.0", 'end-1c'))
        self.resulti = round(getvalue(getaddress(base+"_d", "i"), "f", "1")["value"],2)
        self.d=float(self.t_d.get("1.0", 'end-1c'))
        self.resultd = round(getvalue(getaddress(base+"_d", "d"), "f", "1")["value"],2)

        if base != "tec3":
            if self.p != self.resultp:
                setvalue(getaddress(base+"_d", "p"), self.p, "f", "1")
            if self.i != self.resulti:
                setvalue(getaddress(base+"_d", "i"), self.i, "f", "1")
            if self.d != self.resultd:
                setvalue(getaddress(base+"_d", "d"), self.d, "f", "1")

        plot=graph(self, base, subject, 'act', box)

class graph(tk.Toplevel):

        def __init__(self, master, b, subject, rel, box):
            tk.Toplevel.__init__(self)
            #self.grab_set()
            self.configure(background=Background['main'])
            self.geometry("750x680")
            self.title("Plotting")
            self.address=getaddress(b, rel)
            self.arg1=eval(base[b][1])[rel][1]
            self.arg2=eval(base[b][1])[rel][2]
            self.interval=master.duration
            self.alltec=["tec0", "tec1", "tec2", "tec3"]
            self.alltec.remove(b)
            self.alltec[:] = [item for item in self.alltec if item.upper() in Globals.available]
            self.x=[]
            self.x0 = []
            self.x1 = []
            self.x2 = []
            self.x3 = []
            self.y = []
            self.v = []
            self.w = []
            self.q = []
            self.z = []

            self.tec_lib= {"tec0": [self.v, getaddress("tec0", "act"), self.x0],
            "tec1": [self.w , getaddress("tec1", "act"), self.x1],
            "tec2": [self.q, getaddress("tec2", "act"), self.x2],
            "tec3": [self.z, getaddress("tec3", "act"), self.x3]}

            self.base=b
            self.check=box.get()
            self.run=self.setup(master, b, subject)


        def setup(self, master, b, subject):

            self.base = b

            l = tk.Label(self, text=subject.upper() + " is being plotted for " + b.upper() + ".",
                         bg=Background['main'], font=fonts['title'])
            l.grid(row=0, column=0, columnspan=8, sticky="esnw", pady=(15, 0))

            b1 = tk.Button(self, text="Done", command=self.destroy, font=fonts['main'], bg=Background['submit'])
            if self.check==1:
                b2 = tk.Button(self, text="Write", command=lambda: self.write(self.x, self.y, self.v, self.w, self.q, self.z, True, b), font=fonts['main'],
                           bg=Background['submit'])
            else:
                b2 = tk.Button(self, text="Write", command=lambda: self.write(self.x, self.y, [], False, b), font=fonts['main'], bg=Background['submit'])
            b1.grid(row=1, column=2, columnspan=2, sticky="esnw", padx=2)
            b2.grid(row=1, column=4, columnspan=2, sticky="esnw", padx=2)
            self.set=master.set

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
            toolbar_frame.grid(row=5, column=0, columnspan=8, sticky="eswn")
            toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
            toolbar.update()

            if self.check==1:
                self.l_tec0=tk.Label(self, text="TEC0", font=fonts['main'], bg=Background['main'])
                self.c_tec0=tk.Canvas(self,  width=4, height=20)
                self.c_tec0.configure(bg=Colours["darkgrey"])
                #self.c_tec0.create_text(0,0,font=fonts['subtitle'], fill=Colours['white'], text="     TEC0", anchor="nw")
                self.l_tec0.grid(row=3, column=2, columnspan=1, sticky="eswn", pady=5, padx=(70,0))
                self.c_tec0.grid(row=4, column=2, columnspan=1, sticky="eswn", pady=5, padx=(70,0))
                self.l_tec1 = tk.Label(self, text="TEC1", font=fonts['main'], bg=Background['main'])
                self.c_tec1 = tk.Canvas(self, width=5, height=20)
                self.c_tec1.configure(bg=Colours["darkgrey"])
                #self.c_tec1.create_text(0, 0, font=fonts['subtitle'], fill=Colours['white'], text="     TEC1", anchor="nw")
                self.l_tec1.grid(row=3, column=3, columnspan=1, sticky="eswn", pady=5, padx=(25,10))
                self.c_tec1.grid(row=4, column=3, columnspan=1, sticky="eswn", pady=5, padx=(25,10))
                self.l_tec2 = tk.Label(self, text="TEC2", font=fonts['main'], bg=Background['main'])
                self.c_tec2 = tk.Canvas(self, width=5, height=20)
                self.c_tec2.configure(bg=Colours["darkgrey"])
                #self.c_tec2.create_text(0, 0, font=fonts['subtitle'], fill=Colours['white'], text="     TEC2", anchor="nw")
                self.l_tec2.grid(row=3, column=4, columnspan=1, sticky="eswn", pady=5, padx=(10,25))
                self.c_tec2.grid(row=4, column=4, columnspan=1, sticky="eswn", pady=5, padx=(10,25))
                self.l_tec3 = tk.Label(self, text="TEC3", font=fonts['main'], bg=Background['main'])
                self.c_tec3 = tk.Canvas(self, width=5, height=20)
                self.c_tec3.configure(bg=Colours["darkgrey"])
                #self.c_tec3.create_text(0, 0, font=fonts['subtitle'], fill=Colours['white'], text="     TEC3", anchor="nw")
                self.l_tec3.grid(row=3, column=5, columnspan=1, sticky="eswn", pady=5, padx=(0,70))
                self.c_tec3.grid(row=4, column=5, columnspan=1, sticky="eswn", pady=5, padx=(0,70))
                self.getindicator()

            self.ax = fig.add_subplot(111)

            boxo = self.ax.get_position()
            self.ax.set_position([boxo.x0, boxo.y0 + boxo.height * 0.1,
                             boxo.width, boxo.height * 0.9])

            # Put a legend below current axis

            if self.check==1:
                self.ax.plot(self.x0, self.tec_lib["tec0"][0], color='g', label="tec0")
                self.ax.plot(self.x1,self.tec_lib["tec1"][0],color='b', label="tec1")
                self.ax.plot(self.x2, self.tec_lib["tec2"][0], color='orange', label="tec2")
                self.ax.plot(self.x3, self.tec_lib["tec3"][0], color='purple', label="tec3")
                #self.getindicator()


            else:
                self.ax.axhline(y=self.set, color='r', linestyle='--', label="Set temperature")
                self.ax.plot(self.x, self.y, color='g', label=self.base.upper() + " temperature")

            #ax.plot([1,2,3,4,5],[1,2,3,4,5])
            #self.df = pandas.DataFrame()
            self.ax.set_xlabel('time (s)')
            self.ax.xaxis.set_label_position('top')
            self.ax.set_ylabel('temperature (C)')
            self.ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
                      fancybox=True, shadow=True, ncol=5)

            ani=animation.FuncAnimation(fig, self.animate, frames=self.frames, interval=self.interval)
            plt.show()
            #print(ani)

            return ani

        def frames(self):
            while True:
                yield self.plot_data(self.base, self.interval, self.check, self.tec_lib, self.alltec)


        def animate(self, args):
            self.x.append(args[0])
            self.y.append(args[1])
            #di = pandas.DataFrame(data={"time(s)": [args[0]], "tec0": [args[1]]})
            #self.df = self.df.append(di)
            if self.check==1:
                #self.z.append(args[2])
                return self.ax.plot(self.x0, self.tec_lib["tec0"][0], color='g', label="tec0"), self.ax.plot(self.x1, self.tec_lib["tec1"][0], color='b', label="tec1"), \
                       self.ax.plot(self.x2, self.tec_lib["tec2"][0], color='orange', label="tec2"), self.ax.plot(self.x3, self.tec_lib["tec3"][0], color='purple', label="tec3")

            else:
                return self.ax.plot(self.x, self.y, color='g', label=self.base.upper() + " temperature")

        def write(self, x, y, v=[], w=[], q=[], z=[], type=False, base=""):
            if type == True:
                df = pandas.DataFrame(data={"time(s)": x, "tec0": v, "tec1": w, "tec2": q, "tec3": z})
            else:
                df = pandas.DataFrame(data={"time(s)": x, base + "temperature(C)": y})
            df_folder="C:/Plotting/"
            if not os.path.exists(df_folder):
                os.makedirs(df_folder)
            file=df_folder + "TEC temp" +  str(time.time())+".csv"
            df.to_csv(file, sep=',', index=False)
            showinfo("Plot done","File written to C:/Plotting")

        def getindicator(self):
            if Globals.laser_off == 1:
                self.after_cancel(self.indicator_timer)

            else:
                if "TEC0" in Globals.available:
                    Globals.tec0_statusbit = getvalue(base["tec0"][0])["value"]
                if "TEC1" in Globals.available:
                    Globals.tec1_statusbit = getvalue(base["tec1"][0])["value"]
                if "TEC2" in Globals.available:
                    Globals.tec2_statusbit = getvalue(base["tec2"][0])["value"]
                if "TEC3" in Globals.available:
                    Globals.tec3_statusbit = getvalue(base["tec3"][0])["value"]

                if readbit(Globals.tec0_statusbit, 17) == "1":
                    if readbit(Globals.tec0_statusbit, 14) == "1":
                        self.c_tec0.configure(bg=Colours["green"])
                    else:
                        self.c_tec0.configure(bg=Colours["amber"])

                if readbit(Globals.tec1_statusbit, 17) == "1":
                    if readbit(Globals.tec1_statusbit, 14) == "1":
                        self.c_tec1.configure(bg=Colours["green"])
                    else:
                        self.c_tec1.configure(bg=Colours["amber"])

                if readbit(Globals.tec2_statusbit, 17) == "1":
                    if readbit(Globals.tec2_statusbit, 14) == "1":
                        self.c_tec2.configure(bg=Colours["green"])
                    else:
                        self.c_tec2.configure(bg=Colours["amber"])

                if readbit(Globals.tec3_statusbit, 17) == "1":
                    if readbit(Globals.tec3_statusbit, 14) == "1":
                        self.c_tec3.configure(bg=Colours["green"])
                    else:
                        self.c_tec3.configure(bg=Colours["amber"])
                self.indicator_timer = self.master.after(3000, self.getindicator)


class PlotMagic(object):

    def __init__(self):
        self.x = 0
        print("Plotmagic started")

    def __call__(self, bas, interval, box, lib, tecall):
        self.x = self.x + interval/1000
        result = getvalue(lib[bas][1], "u", "k")["value"]
        self.y = result
        lib[bas][2].append(self.x)
        lib[bas][0].append(result)
        if box==1:
            for item in tecall:

                lib[item][2].append(self.x)
                lib[item][0].append(getvalue(lib[item][1], "u", "k")["value"])
            return self.x, self.y
        else:
            return self.x, self.y
