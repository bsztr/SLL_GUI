#Definition of variables
import tkinter as tk
from tkinter import ttk
from LockPanel import *
from LDPanel import *
from GeneralPanel import *
from TecPanel import *
from CalPanel import *
from COMM import *
from Dynamic import *
from CONFIG import *
from init_start import *
import Globals

class ClientPanel(tk.Frame):


    def __init__(self):

        self.l_ld_curr_actual_n = 1
        self.l_clp_curr_actual_n = 1
        self.l_clp1_curr_actual_n = 1
        self.l_tec0_temp_actual_n = 1
        self.l_tec1_temp_actual_n = 1
        self.l_tec2_temp_actual_n = 1
        self.l_tec3_temp_actual_n = 1

        global message
        message = ""
        available = Globals.available
        Names = Globals.Names
        self.gui = tk.Tk()
        # self.gui.geometry("395x590")
        self.gui.title("UniKLasers GUI")
        self.gui.configure(bg=Background['main'])
        self.button = 18
        self.canvas_width = 355
        self.canvas_height = 200

        self.Unik = tk.PhotoImage(file="unik.png")
        self.l_unik = tk.Label(image=self.Unik, bg=Background['main'])

        self.l_detect = tk.Label(self.gui, text=self.lh_detect(), font=fonts['detection'], fg="grey",
                                 bg=Background['main'])
        # self.l_info=tk.Label(self.gui, text="Solo 640", fg=Colours['solo'], font=fonts['model'], bg=Background['main'])
        self.l_info = Logo(self.gui)
        self.l_info.update_logo()
        self.serialnumber = str(getvalue(getaddress("lh", "serial"), lh['serial'][1], lh['serial'][2])['value'])
        self.l_serial = tk.Label(self.gui, text="S/N: " + self.serialnumber, font=fonts['detection'], fg="grey",
                                 bg=Background['main'])
        self.l_power = tk.Label(self.gui, text="Power status", font=fonts['indicator'], bg=Background['main'])
        self.l_tec = tk.Label(self.gui, text="TEC status", font=fonts['indicator'], bg=Background['main'])
        self.l_laser = tk.Label(self.gui, text="Pump LD status", font=fonts['indicator'], bg=Background['main'])
        self.l_lock = tk.Label(self.gui, text="Lock status", font=fonts['indicator'], bg=Background['main'])
        self.l_error = tk.Label(self.gui, text="Error", font=fonts['indicator'], bg=Background['main'])
        self.l_messages = tk.Label(self.gui, text="Messages", anchor="e", font=fonts['main'], bg=Background['main'])
        # self.l_pump_power=tk.Label(self.gui, text="Pump current (mA)")
        # self.l_pump_power_actual=tk.Label(self.gui, text="Actual: 3200 (mA)", fg="green", font=("Helvetica", 8))
        self.l_copy = tk.Label(self.gui, text="All rights reserved", bg=Background['main'], font=fonts['detection'])

        # Temperature & current display
        if "LDR" in available:
            self.ldr_n = tk.StringVar()
            self.l_ld_curr = tk.Label(self.gui, textvariable=self.ldr_n, font=fonts['temperature'],
                                      bg=Background['main'])
            self.getnametec("ldr", self.l_ld_curr, self.ldr_n)
            self.l_ld_curr_actual = ld_label(self.gui)
            self.l_ld_curr_actual.update_ld_main("ld", "act")
            self.l_ld_curr.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
            self.l_ld_curr_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")
            Globals.row = Globals.row + 2

        if "PZT0" in available:
            self.l_clp_curr = tk.Label(self.gui, text="CLP power:", font=fonts['temperature'],
                                       bg=Background['main'])
            self.l_clp_curr_actual = pzt_label(self.gui)
            self.l_clp_curr_actual.update_clp_main(getaddress("pzt0", "clp_power"), "clp_power")
            self.l_clp_curr.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
            self.l_clp_curr_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")

            Globals.row = Globals.row + 2

            self.pzt0_n = tk.StringVar()
            self.l_pzt0_stat = tk.Label(self.gui, textvariable=self.pzt0_n, font=fonts['temperature'],
                                        bg=Background['main'])
            self.getnametec("pzt0", self.l_pzt0_stat, self.pzt0_n)
            self.l_pzt0_stat_actual = pzt_label(self.gui)
            self.l_pzt0_stat_actual.update_status_main("pzt0")
            self.l_pzt0_stat.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
            self.l_pzt0_stat_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")
            Globals.row = Globals.row + 2

        if "PZT1" in available:
            self.l_clp1_curr = tk.Label(self.gui, text="CLP1 power:", font=fonts['temperature'],
                                        bg=Background['main'])
            self.l_clp1_curr_actual = pzt_label(self.gui)
            self.l_clp1_curr_actual.update_clp_main(getaddress("pzt1", "clp_power"), "clp_power")
            self.l_clp1_curr.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
            self.l_clp1_curr_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")

            Globals.row = Globals.row + 2

            self.pzt1_n = tk.StringVar()
            self.l_pzt1_stat = tk.Label(self.gui, textvariable=self.pzt1_n, font=fonts['temperature'],
                                        bg=Background['main'])
            self.getnametec("pzt1", self.l_pzt1_stat, self.pzt1_n)
            self.l_pzt1_stat_actual = pzt_label(self.gui)
            self.l_pzt1_stat_actual.update_status_main("pzt1")
            self.l_pzt1_stat.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
            self.l_pzt1_stat_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")

        if "TEC0" in available:
            self.tec0_n = tk.StringVar()
            self.l_tec0_temp = tk.Label(self.gui, textvariable=self.tec0_n, font=fonts['temperature'],
                                        bg=Background['main'])
            self.getnametec("tec0", self.l_tec0_temp, self.tec0_n)
            self.l_tec0_temp_actual = temp_label(self.gui)
            self.l_tec0_temp_actual.update_temp_main("tec0", "act")
            self.l_tec0_temp.grid(row=Globals.rowtec, column=3, columnspan=1, rowspan=2, sticky="nw")
            self.l_tec0_temp_actual.grid(row=Globals.rowtec, column=4, columnspan=1, rowspan=2, sticky="nw")
            Globals.rowtec = Globals.rowtec + 2

        if "TEC1" in available:
            self.tec1_n = tk.StringVar()
            self.l_tec1_temp = tk.Label(self.gui, textvariable=self.tec1_n, font=fonts['temperature'],
                                        bg=Background['main'])
            self.getnametec("tec1", self.l_tec1_temp, self.tec1_n)
            self.l_tec1_temp_actual = temp_label(self.gui)
            self.l_tec1_temp_actual.update_temp_main("tec1", "act")
            self.l_tec1_temp.grid(row=Globals.rowtec, column=3, columnspan=1, rowspan=2, sticky="nw")
            self.l_tec1_temp_actual.grid(row=Globals.rowtec, column=4, columnspan=1, rowspan=2, sticky="nw")
            Globals.rowtec = Globals.rowtec + 2

        if "TEC2" in available:
            self.tec2_n = tk.StringVar()
            self.l_tec2_temp = tk.Label(self.gui, textvariable=self.tec2_n, font=fonts['temperature'],
                                        bg=Background['main'])
            self.getnametec("tec2", self.l_tec2_temp, self.tec2_n)
            self.l_tec2_temp_actual = temp_label(self.gui)
            self.l_tec2_temp_actual.update_temp_main("tec2", "act")
            self.l_tec2_temp.grid(row=Globals.rowtec, column=3, columnspan=1, rowspan=2, sticky="nw")
            self.l_tec2_temp_actual.grid(row=Globals.rowtec, column=4, columnspan=1, rowspan=2, sticky="nw")
            Globals.rowtec = Globals.rowtec + 2

        if "TEC3" in available:
            self.tec3_n = tk.StringVar()
            self.l_tec3_temp = tk.Label(self.gui, textvariable=self.tec3_n, font=fonts['temperature'],
                                        bg=Background['main'])
            self.getnametec("tec3", self.l_tec3_temp, self.tec3_n)
            self.l_tec3_temp_actual = temp_label(self.gui)
            self.l_tec3_temp_actual.update_temp_main("tec3", "act")
            self.l_tec3_temp.grid(row=Globals.rowtec, column=3, columnspan=1, rowspan=2, sticky="nw")
            self.l_tec3_temp_actual.grid(row=Globals.rowtec, column=4, columnspan=1, rowspan=2, sticky="nw")
            Globals.rowtec = Globals.rowtec + 2

        self.c_power = tk.Canvas(self.gui, width=20, height=10)
        # self.c_power.create_oval(0,0,10,10)
        self.getindicatorcolour("power", self.c_power)
        self.c_tec = tk.Canvas(self.gui, width=20, height=10)
        self.getindicatorcolour("tec", self.c_tec)
        self.c_laser = tk.Canvas(self.gui, width=20, height=10)
        self.getindicatorcolour("ld", self.c_laser)
        self.c_lock = tk.Canvas(self.gui, width=20, height=10)
        self.getindicatorcolour("pzt", self.c_lock)
        self.c_error = tk.Canvas(self.gui, width=20, height=10)
        self.geterrorcolour(self.c_error)
        self.c_message = tk.Canvas(self.gui, bg="ghost white", width=self.canvas_width, height=self.canvas_height)
        self.update_messages(self.c_message)
        self.vbar = tk.Scrollbar(self.gui, orient=tk.VERTICAL)
        self.vbar.config(command=self.c_message.yview)

        self.t_ppower = tk.Text(self.gui, width=6, height=1)
        self.t_ppower.insert(tk.END, "1000")
        self.t_pcurr = tk.Text(self.gui, width=6, height=1)
        self.t_pcurr.insert(tk.END, "1000")
        self.t_ttemp = tk.Text(self.gui, width=6, height=1)
        self.t_ttemp.insert(tk.END, "1000")

        self.b_lon = tk.Button(self.gui, text="SYSTEM ON", bg=Colours['green'], fg=Colours["white"],
                               command=lambda: self.laser_on(), font=fonts['subbutton'], height=1, width=5)
        # elf.b_standby = tk.Canvas(self.gui, height=1, width=5)
        # self.b_standby.create_text(50,50, text="STANDBY", angle=90, anchor="nw", font=fonts['main'], fill=Colours["white"])
        # self.b_standby.configure(bg=Colours['darkgrey'])
        self.b_ldon = tk.Button(self.gui, text="PUMP ON", bg=Colours['grey'], fg=Colours["darkgrey"],
                                font=fonts['subbutton'], height=1, width=5)
        # self.b_ldoff = tk.Button(self.gui, text="LD\noff", bg=Colours['grey'], fg=Colours["darkgrey"],font=fonts['subbutton'], height=1, width=5)
        self.b_loff = tk.Button(self.gui, text="SYSTEM OFF", bg=Colours['red'], fg="white",
                                command=lambda: self.laser_off(), font=fonts['subbutton'], height=1, width=10)
        self.b_lock = tk.Button(self.gui, text="RELOCK", fg=Colours["darkgrey"], bg=Colours['grey'], command="",
                                font=fonts['subbutton'], height=1, width=10)
        self.b_alignment = tk.Button(self.gui, text="EXT ALIGNMENT", fg="black", bg=Colours['lightgrey'],
                                     command=lambda: self.alignment(), font=fonts['main'], height=1, width=7)
        self.b_highp = tk.Button(self.gui, text="FULL POWER", fg="black", bg=Colours['lightgrey'],
                                 command=lambda: self.highp(), font=fonts['main'], height=1, width=7)
        self.b_more = tk.Button(self.gui, text="Reset", bg=Colours['grey'], command=self.reset,
                                font=fonts['subbutton'], height=1, width=14)
        self.b_clear = tk.Button(self.gui, text="Clear", bg=Colours['grey'],
                                 command=lambda: self.clear(self.c_message), font=fonts['status'], height=1,
                                 width=5)

        self.ld_scale = tk.Scale(self.gui, from_=Globals.Names["low"], to=Globals.Names["high"], tickinterval=0.4,
                                 resolution=0.2, orient=tk.HORIZONTAL,
                                 bg=Background["main"], font=fonts["main"], label="LD power (A)", command="")
        self.ld_scale.set(Globals.Names["high"])
        self.ld_scale.configure(command=lambda x: self.ld_powerscale())
        # Grid - Info pan
        self.l_unik.grid(row=1, column=1, columnspan=4, rowspan=2, sticky="nw", padx=3, pady=3)
        self.l_detect.grid(row=4, column=1, columnspan=4, rowspan=2, sticky="nw")
        self.geths(self.gui).grid(row=5, column=1, columnspan=10, sticky="we")
        self.l_info.grid(row=2, column=5, columnspan=4, rowspan=1, sticky="nes", padx=(0, 30))
        self.l_serial.grid(row=3, column=5, columnspan=4, rowspan=2, sticky="ne", padx=(0, 20))

        # Indicator pan
        self.indpad = 2
        self.l_power.grid(row=6, column=6, columnspan=1, rowspan=2, sticky="nws", pady=self.indpad)
        self.c_power.grid(row=6, column=5, columnspan=1, rowspan=2, sticky="wns", pady=self.indpad)
        self.l_tec.grid(row=8, column=6, columnspan=1, rowspan=2, sticky="nws", pady=self.indpad)
        self.c_tec.grid(row=8, column=5, columnspan=1, rowspan=2, sticky="wns", pady=self.indpad)
        self.l_laser.grid(row=10, column=6, columnspan=1, rowspan=2, sticky="wns", pady=self.indpad)
        self.c_laser.grid(row=10, column=5, columnspan=1, rowspan=2, sticky="wns", pady=self.indpad)
        self.l_lock.grid(row=12, column=6, columnspan=1, rowspan=2, sticky="wns", pady=self.indpad)
        self.c_lock.grid(row=12, column=5, columnspan=1, rowspan=2, sticky="wns", pady=self.indpad)
        self.l_error.grid(row=14, column=6, columnspan=1, rowspan=2, sticky="wns", pady=self.indpad)
        self.c_error.grid(row=14, column=5, columnspan=1, rowspan=2, sticky="wns", pady=self.indpad)

        # Buttons
        self.b_lon.grid(row=23, column=1, columnspan=4, rowspan=1, sticky="nwes", padx=5, pady=(2, 2))
        self.ld_scale.grid(row=21, column=1, columnspan=4, rowspan=2, sticky="nwes", padx=(3, 3), pady=(2, 2))
        # self.b_ldoff.grid(row=22, column=4, columnspan=1, rowspan=2, sticky="nwes", padx=(2, 5), pady=(25,12))
        self.b_loff.grid(row=25, column=1, columnspan=2, rowspan=2, sticky="nwse", padx=5, pady=(10, 0))
        self.geths(self.gui).grid(row=24, column=1, rowspan=2, columnspan=4, sticky="we", pady=(0, 8), padx=5)
        self.b_lock.grid(row=25, column=3, columnspan=2, rowspan=2, sticky="nwse", pady=(10, 0), padx=(0, 5))
        self.b_more.grid(row=25, column=5, columnspan=3, rowspan=2, sticky="nwse", pady=(10, 0), padx=(3, 6))
        self.b_ldon.grid(row=21, column=5, columnspan=3, rowspan=1, sticky="nwes", padx=(3, 6), pady=2)
        self.b_highp.grid(row=22, column=5, columnspan=3, rowspan=1, sticky="nwes", pady=2, padx=(3, 6))
        self.b_alignment.grid(row=23, column=5, columnspan=3, rowspan=1, sticky="nwes", pady=2, padx=(3, 6))

        # Actual controls
        # self.l_pump_power.grid(row=6, column=7, columnspan=2, rowspan=1, sticky="nw")
        # self.l_pump_power_actual.grid(row=7, column=7, columnspan=1, rowspan=1, sticky="nw")

        # Messages pan
        self.geths(self.gui).grid(row=27, column=1, rowspan=2, columnspan=7, sticky="ewns", pady=10)
        self.l_messages.grid(row=29, column=1, columnspan=5, rowspan=2, sticky="nw")
        self.b_clear.grid(row=29, column=6, columnspan=2, rowspan=1, sticky="nwse", pady=(0, 6), padx=6)
        self.c_message.grid(row=31, column=1, columnspan=6, rowspan=4, padx=3)
        self.vbar.grid(row=31, column=7, rowspan=4, sticky="nse", padx=6)
        self.l_copy.grid(row=35, column=1, columnspan=7, rowspan=2)

    def geths(self, parent):
        hs = ttk.Separator(parent, orient=tk.HORIZONTAL)
        return hs

    def getvs(self, parent):
        vs = ttk.Separator(parent, orient=tk.VERTICAL)
        return vs

    def start(self):
        self.gui.mainloop()

    def status(self):
        available = Globals.available
        config = ""
        for i in range(0, len(available)):
            config = "Configuration: " + ", ".join(available) + "\n"
        return config

    def status_bit(self):
        Globals.status_bit = getvalue(control["address"])["value"]

    def refresh(self):
        self.gui.update_idletasks()
        self.gui.update()
        if hasattr(self, "window"):
            self.window.update_idletasks()
            self.window.tab_parent.update_idletasks()
            self.window.update()
            self.window.tab_parent.update()

    def message_trigger(self, message_in):
        global message
        message = message + message_in
        return message

    def update_messages(self, canvas):
        self.status_bit()
        config = self.status()
        self.text = canvas.create_text(0, 0, font=fonts['messages'], fill=Colours['darkgrey'],
                                       text=config + message, anchor="nw")
        canvas.move(self.text, 10, 10)
        self.getmessage()
        self.geterror()
        # self.incident_error(canvas)
        if Globals.refresh == 1:
            canvas.delete("all")
            self.front_panel()
        self.refresh()
        self.update_messages_after = canvas.after(1500, lambda: self.update_messages(canvas))

    def clear(self, canvas):
        canvas.delete('all')
        global message
        message = ""

    def getmessage(self):
        if Globals.laser_off == 0:
            if Globals.incident_message != Globals.recorded_message:
                self.message_trigger(Globals.incident_message + "\n")
                Globals.recorded_message = Globals.incident_message
        if Globals.subscription_off == 1:
            Globals.laser_off = 1

    def geterror(self):
        if Globals.laser_off == 0:
            error_c = getvalue(error["address"], "u", "1")["value"]
            if Globals.incident_error != Globals.recorded_error:
                self.message_trigger("ERROR" + Globals.incident_errorn + ": " + Globals.incident_error + "\n")
                self.c_error.configure(bg=Colours["red"])
                Globals.recorded_error = Globals.incident_error
            if error_c != Globals.error_count:
                error_t = error[
                    str(getvalue(hex(int(error["address"], 16) - 1 - 2 * (error_c - 1)), "i", "1")["value"])]
                if error_t != Globals.incident_error:
                    self.c_error.configure(bg=Colours["red"])
                    self.message_trigger("ERROR: " + error_t + "\n")
                Globals.error_count = error_c

    def getcolour(self, result):
        if result > 30:
            return Colours['red']
        else:
            return Colours['green']

    def geterrorcolour(self, canvas):
        canvas.configure(bg=Colours["darkgrey"])
        # if Globals.error_disp==1:
        #     exec("Globals." + "error" + " = Colours['red']")
        # else:
        #     exec("Globals." + "error" + " = Colours['darkgrey']")
        # canvas.configure(bg=Globals.error)
        # canvas.after(500, lambda: self.geterrorcolour(canvas))

    def getindicatorcolour(self, id, canvas):
        self.indicator()
        canvas.configure(bg=eval("Globals." + id))
        canvas.after(1500, lambda: self.getindicatorcolour(id, canvas))

    def indicator(self):
        source = Globals.status_bit
        list = {"ld", "pzt", "tec"}
        for item in list:
            if readbit(source, eval("indicator[item]")["grey"]) == "1":
                if readbit(source, eval("indicator[item]")["amber"]) == "1":
                    if readbit(source, eval("indicator[item]")["green"]) == "1":
                        exec("Globals." + item + " = Colours['green']")
                    else:
                        exec("Globals." + item + " = Colours['amber']")
                else:
                    exec("Globals." + item + " = Colours['amber']")
            else:
                exec("Globals." + item + " = Colours['darkgrey']")
        if readbit(source, 3) == "1":
            Globals.power = Colours["green"]
        else:
            Globals.power = Colours["darkgrey"]

    def lh_detect(self):
        if "LH" in Globals.available:
            return "Laserhead detected"
        else:
            return "Error: LH not detected"

    def activation(self):
        if Globals.subscription_off != 1:
            Globals.laser_off = 0
            self.actual = Globals.status_bit

            if readbit(self.actual, 3) != "1":
                # init_COMM()
                comm_start()
                self.update_messages(self.c_message)
            self.front_panel()

        else:
            self.laser_off()

    def front_panel(self):

        # Globals.row = 6
        # Globals.rowtec = 6
        Names = Globals.Names

        if "LDR" in Globals.available:
            if not hasattr(self, "l_ld_curr_actual"):
                self.ldr_n = tk.StringVar()
                self.l_ld_curr = tk.Label(self.gui, textvariable=self.ldr_n, font=fonts['temperature'],
                                          bg=Background['main'])
                self.getnametec("ldr", self.l_ld_curr, self.ldr_n)
                self.l_ld_curr_actual = ld_label(self.gui)
                self.l_ld_curr_actual.update_ld_main("ld", "act")
                self.l_ld_curr.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
                self.l_ld_curr_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")
                Globals.row = Globals.row + 2

            elif self.l_ld_curr_actual_n == 0 or Globals.ldrr == 1:
                self.ldr_n = tk.StringVar()
                self.l_ld_curr = tk.Label(self.gui, textvariable=self.ldr_n, font=fonts['temperature'],
                                          bg=Background['main'])
                self.getnametec("ldr", self.l_ld_curr, self.ldr_n)
                self.l_ld_curr_actual = ld_label(self.gui)
                self.l_ld_curr_actual.update_ld_main("ld", "act")
                self.l_ld_curr.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
                self.l_ld_curr_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")
                Globals.row = Globals.row + 2

        elif hasattr(self, "l_ld_curr_actual"):
            self.l_ld_curr.grid_forget()
            self.l_ld_curr_actual.stop_ld_main()
            self.l_ld_curr_actual.grid_forget()
            Globals.row = Globals.row - 2

        if "PZT0" in Globals.available:
            if not hasattr(self, "l_clp_curr"):
                self.l_clp_curr = tk.Label(self.gui, text="CLP power:", font=fonts['temperature'],
                                           bg=Background['main'])
                self.l_clp_curr_actual = pzt_label(self.gui)
                self.l_clp_curr_actual.update_clp_main(getaddress("pzt0", "clp_power"), "clp_power")
                self.l_clp_curr.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
                self.l_clp_curr_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")

                Globals.row = Globals.row + 2

                self.pzt0_n = tk.StringVar()
                self.l_pzt0_stat = tk.Label(self.gui, textvariable=self.pzt0_n, font=fonts['temperature'],
                                            bg=Background['main'])
                self.getnametec("pzt0", self.l_pzt0_stat, self.pzt0_n)
                self.l_pzt0_stat_actual = pzt_label(self.gui)
                self.l_pzt0_stat_actual.update_status_main("pzt0")
                self.l_pzt0_stat.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
                self.l_pzt0_stat_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")

                Globals.row = Globals.row + 2

            elif self.l_clp_curr_actual_n == 0 or Globals.pzt0r == 1:
                self.l_clp_curr = tk.Label(self.gui, text="CLP power:", font=fonts['temperature'],
                                           bg=Background['main'])
                self.l_clp_curr_actual = pzt_label(self.gui)
                self.l_clp_curr_actual.update_clp_main(getaddress("pzt0", "clp_power"), "clp_power")
                self.l_clp_curr.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
                self.l_clp_curr_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")

                Globals.row = Globals.row + 2

                self.pzt0_n = tk.StringVar()
                self.l_pzt0_stat = tk.Label(self.gui, textvariable=self.pzt0_n, font=fonts['temperature'],
                                            bg=Background['main'])
                self.getnametec("pzt0", self.l_pzt0_stat, self.pzt0_n)
                self.l_pzt0_stat_actual = pzt_label(self.gui)
                self.l_pzt0_stat_actual.update_status_main("pzt0")
                self.l_pzt0_stat.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
                self.l_pzt0_stat_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")

                Globals.row = Globals.row + 2

        elif hasattr(self, "l_clp_curr"):
            self.l_pzt0_stat.grid_forget()
            self.l_pzt0_stat_actual.stop_status()
            self.l_pzt0_stat_actual.grid_forget()
            self.l_clp_curr.grid_forget()
            self.l_clp_curr_actual.stop_clp()
            self.l_clp_curr_actual.grid_forget()
            Globals.row = Globals.row - 4

        if "PZT1" in Globals.available:
            if not hasattr(self, "l_clp1_curr"):
                self.l_clp1_curr = tk.Label(self.gui, text="CLP1 power:", font=fonts['temperature'],
                                            bg=Background['main'])
                self.l_clp1_curr_actual = pzt_label(self.gui)
                self.l_clp1_curr_actual.update_clp_main(getaddress("pzt1", "clp_power"), "clp_power")
                self.l_clp1_curr.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
                self.l_clp1_curr_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")

                Globals.row = Globals.row + 2

                self.pzt1_n = tk.StringVar()
                self.l_pzt1_stat = tk.Label(self.gui, textvariable=self.pzt1_n, font=fonts['temperature'],
                                            bg=Background['main'])
                self.getnametec("pzt1", self.l_pzt1_stat, self.pzt1_n)
                self.l_pzt1_stat_actual = pzt_label(self.gui)
                self.l_pzt1_stat_actual.update_status_main("pzt1")
                self.l_pzt1_stat.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
                self.l_pzt1_stat_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")

            elif self.l_clp1_curr_actual_n == 0 or Globals.pzt1r == 1:
                self.l_clp1_curr = tk.Label(self.gui, textvariable="CLP1 power:", font=fonts['temperature'],
                                            bg=Background['main'])
                self.l_clp1_curr_actual = pzt_label(self.gui)
                self.l_clp1_curr_actual.update_clp_main(getaddress("pzt1", "clp_power"), "clp_power")
                self.l_clp1_curr.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
                self.l_clp1_curr_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")

                Globals.row = Globals.row + 2

                self.pzt1_n = tk.StringVar()
                self.l_pzt1_stat = tk.Label(self.gui, textvariable=self.pzt1_n, font=fonts['temperature'],
                                            bg=Background['main'])
                self.getnametec("pzt1", self.l_pzt1_stat, self.pzt1_n)
                self.l_pzt1_stat_actual = pzt_label(self.gui)
                self.l_pzt1_stat_actual.update_status_main("pzt1")
                self.l_pzt1_stat.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
                self.l_pzt1_stat_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")

        elif hasattr(self, "l_clp1_curr"):
            self.l_pzt1_stat.grid_forget()
            self.l_pzt1_stat_actual.stop_status()
            self.l_pzt1_stat_actual.grid_forget()
            self.l_clp1_curr.grid_forget()
            self.l_clp1_curr_actual.stop_clp()
            self.l_clp1_curr_actual.grid_forget()
            Globals.row = Globals.row - 4

        if "TEC0" in Globals.available:
            if not hasattr(self, "l_tec0_temp_actual"):
                self.tec0_n = tk.StringVar()
                self.l_tec0_temp = tk.Label(self.gui, textvariable=self.tec0_n, font=fonts['temperature'],
                                            bg=Background['main'])
                self.getnametec("tec0", self.l_tec0_temp, self.tec0_n)
                self.l_tec0_temp_actual = temp_label(self.gui)
                self.l_tec0_temp_actual.update_temp_main("tec0", "act")
                self.l_tec0_temp.grid(row=Globals.rowtec, column=3, columnspan=1, rowspan=2, sticky="nw")
                self.l_tec0_temp_actual.grid(row=Globals.rowtec, column=4, columnspan=1, rowspan=2, sticky="nw")
                Globals.rowtec = Globals.rowtec + 2

            elif self.l_tec0_temp_actual_n == 0 or Globals.tec0r == 1:
                self.tec0_n = tk.StringVar()
                self.l_tec0_temp = tk.Label(self.gui, textvariable=self.tec0_n, font=fonts['temperature'],
                                            bg=Background['main'])
                self.getnametec("tec0", self.l_tec0_temp, self.tec0_n)
                self.l_tec0_temp_actual = temp_label(self.gui)
                self.l_tec0_temp_actual.update_temp_main("tec0", "act")
                self.l_tec0_temp.grid(row=Globals.rowtec, column=3, columnspan=1, rowspan=2, sticky="nw")
                self.l_tec0_temp_actual.grid(row=Globals.rowtec, column=4, columnspan=1, rowspan=2, sticky="nw")
                Globals.rowtec = Globals.rowtec + 2

        elif hasattr(self, "l_tec0_temp_actual"):
            self.l_tec0_temp.grid_forget()
            self.l_tec0_temp_actual.grid_forget()
            self.l_tec0_temp_actual.stop_temp_main()
            Globals.rowtec = Globals.rowtec - 2

        if "TEC1" in Globals.available:
            if not hasattr(self, "l_tec1_temp_actual"):
                self.tec1_n = tk.StringVar()
                self.l_tec1_temp = tk.Label(self.gui, textvariable=self.tec1_n, font=fonts['temperature'],
                                            bg=Background['main'])
                self.getnametec("tec1", self.l_tec1_temp, self.tec1_n)
                self.l_tec1_temp_actual = temp_label(self.gui)
                self.l_tec1_temp_actual.update_temp_main("tec1", "act")
                self.l_tec1_temp.grid(row=Globals.rowtec, column=3, columnspan=1, rowspan=2, sticky="nw")
                self.l_tec1_temp_actual.grid(row=Globals.rowtec, column=4, columnspan=1, rowspan=2, sticky="nw")
                Globals.rowtec = Globals.rowtec + 2

            elif self.l_tec1_temp_actual_n == 0 or Globals.tec1r == 1:
                self.tec1_n = tk.StringVar()
                self.l_tec1_temp = tk.Label(self.gui, textvariable=self.tec1_n, font=fonts['temperature'],
                                            bg=Background['main'])
                self.getnametec("tec1", self.l_tec1_temp, self.tec1_n)
                self.l_tec1_temp_actual = temp_label(self.gui)
                self.l_tec1_temp_actual.update_temp_main("tec1", "act")
                self.l_tec1_temp.grid(row=Globals.rowtec, column=3, columnspan=1, rowspan=2, sticky="nw")
                self.l_tec1_temp_actual.grid(row=Globals.rowtec, column=4, columnspan=1, rowspan=2, sticky="nw")
                Globals.rowtec = Globals.rowtec + 2

        elif hasattr(self, "l_tec1_temp_actual"):
            self.l_tec1_temp.grid_forget()
            self.l_tec1_temp_actual.grid_forget()
            self.l_tec1_temp_actual.stop_temp_main()
            Globals.rowtec = Globals.rowtec - 2

        if "TEC2" in Globals.available:
            if not hasattr(self, "l_tec2_temp_actual"):
                self.tec2_n = tk.StringVar()
                self.l_tec2_temp = tk.Label(self.gui, textvariable=self.tec2_n, font=fonts['temperature'],
                                            bg=Background['main'])
                self.getnametec("tec2", self.l_tec2_temp, self.tec2_n)
                self.l_tec2_temp_actual = temp_label(self.gui)
                self.l_tec2_temp_actual.update_temp_main("tec2", "act")
                self.l_tec2_temp.grid(row=Globals.rowtec, column=3, columnspan=1, rowspan=2, sticky="nw")
                self.l_tec2_temp_actual.grid(row=Globals.rowtec, column=4, columnspan=1, rowspan=2, sticky="nw")
                Globals.rowtec = Globals.rowtec + 2

            elif self.l_tec2_temp_actual_n == 0 or Globals.tec2r == 1:
                self.tec2_n = tk.StringVar()
                self.l_tec2_temp = tk.Label(self.gui, textvariable=self.tec2_n, font=fonts['temperature'],
                                            bg=Background['main'])
                self.getnametec("tec2", self.l_tec2_temp, self.tec2_n)
                self.l_tec2_temp_actual = temp_label(self.gui)
                self.l_tec2_temp_actual.update_temp_main("tec2", "act")
                self.l_tec2_temp.grid(row=Globals.rowtec, column=3, columnspan=1, rowspan=2, sticky="nw")
                self.l_tec2_temp_actual.grid(row=Globals.rowtec, column=4, columnspan=1, rowspan=2, sticky="nw")
                Globals.rowtec = Globals.rowtec + 2

        elif hasattr(self, "l_tec2_temp_actual"):
            self.l_tec2_temp.grid_forget()
            self.l_tec2_temp_actual.grid_forget()
            self.l_tec2_temp_actual.stop_temp_main()
            Globals.rowtec = Globals.rowtec - 2

        if "TEC3" in Globals.available:
            if not hasattr(self, "l_tec3_temp_actual"):
                print("1")
                self.tec3_n = tk.StringVar()
                self.l_tec3_temp = tk.Label(self.gui, textvariable=self.tec3_n, font=fonts['temperature'],
                                            bg=Background['main'])
                self.getnametec("tec3", self.l_tec3_temp, self.tec3_n)
                self.l_tec3_temp_actual = temp_label(self.gui)
                self.l_tec3_temp_actual.update_temp_main("tec3", "act")
                self.l_tec3_temp.grid(row=Globals.rowtec, column=3, columnspan=1, rowspan=2, sticky="nw")
                self.l_tec3_temp_actual.grid(row=Globals.rowtec, column=4, columnspan=1, rowspan=2, sticky="nw")
                Globals.rowtec = Globals.rowtec + 2

            elif self.l_tec3_temp_actual_n == 0 or Globals.tec3r == 1:
                print("2")
                self.tec3_n = tk.StringVar()
                self.l_tec3_temp = tk.Label(self.gui, textvariable=self.tec3_n, font=fonts['temperature'],
                                            bg=Background['main'])
                self.getnametec("tec3", self.l_tec3_temp, self.tec3_n)
                self.l_tec3_temp_actual = temp_label(self.gui)
                self.l_tec3_temp_actual.update_temp_main("tec3", "act")
                self.l_tec3_temp.grid(row=Globals.rowtec, column=3, columnspan=1, rowspan=2, sticky="nw")
                self.l_tec3_temp_actual.grid(row=Globals.rowtec, column=4, columnspan=1, rowspan=2, sticky="nw")
                Globals.rowtec = Globals.rowtec + 2

        elif hasattr(self, "l_tec3_temp_actual"):
            print("3")
            self.l_tec3_temp.grid_forget()
            self.l_tec3_temp_actual.grid_forget()
            self.l_tec3_temp_actual.stop_temp_main()
            Globals.rowtec = Globals.rowtec - 2

        Globals.refresh = 0
        Globals.ldrr = 0
        Globals.pzt0r = 0
        Globals.pzt1r = 0
        Globals.tec0r = 0
        Globals.tec1r = 0
        Globals.tec2r = 0
        Globals.tec3r = 0
        Globals.lhr = 0
        Globals.cbr = 0

        self.l_ld_curr_actual_n = 1
        self.l_clp_curr_actual_n = 1
        self.l_clp1_curr_actual_n = 1
        self.l_tec0_temp_actual_n = 1
        self.l_tec1_temp_actual_n = 1
        self.l_tec2_temp_actual_n = 1
        self.l_tec3_temp_actual_n = 1

        return self.actual

    def laser_on(self):
        if Globals.tec_stab == 1:
            self.ld_on()
        else:
            self.activation()
            self.actual = Globals.status_bit

            self.message_trigger("System is powering up. \n")

            #self.actual=getvalue(control["address"])['value']

            if readbit(self.actual, 10) == "0":
                 addvalue(control["address"], control["tec"])
                 self.message_trigger("TECs are initialising, this will take some time. \n")

            self.tec_on()

    def tec_on(self):
        if Globals.laser_off == 0:
            if Globals.tec_stab == 1:
                self.ld_on()
            else:
                self.actual = Globals.status_bit
                self.tec_after = self.gui.after(1000, self.tec_on)
                if readbit(self.actual, 17) == "1":
                    self.message_trigger("TECs have stabalised. \n")
                    self.gui.after_cancel(self.tec_after)
                    Globals.tec_stab = 1
                    self.b_ldon.configure(bg = Colours["green"], fg=Colours["white"], command=lambda: self.ld_on())
                    #self.b_ldoff.configure(bg = Colours["red"], fg=Colours["white"], command=lambda: self.ld_off())
                    self.message_trigger("Initialisation complete, LDs can now be switched on.\n")

    def ld_on(self):
        if Globals.laser_off == 0:
            if Globals.tec_stab == 1:
                self.actual = Globals.status_bit
                self.ld_after = self.gui.after(1000, self.ld_on)
                self.b_ldon.configure(text ="PUMP OFF", bg=Colours["red"], fg=Colours["white"], command=lambda: self.ld_off())
                if readbit(self.actual, 17) == "1":
                    #self.message_trigger("TECs have stabalised. \n")
                    if readbit(self.actual, 0) != "1":
                        addvalue(control['address'], 1)
                    setvalue(getaddress("ld_d", "curr"), Globals.Names['high'], "u", "u")
                    self.message_trigger("Pump LD is turning on. \n")
                    if readbit(self.actual, 1) == "1":
                        addvalue(control["address"], control["pzt"])
                    self.gui.after_cancel(self.ld_after)
                    self.pzt_on()
            else:
                self.message_trigger("TECs not stabilised yet.")
        else:
            return "break"

    def ld_off(self):
        if hasattr(self, 'ld_after'):
            self.gui.after_cancel(self.ld_after)
        if hasattr(self, 'pzt_after'):
            self.gui.after_cancel(self.pzt_after)
        if hasattr(self, 'lock_after'):
            self.gui.after_cancel(self.lock_after)
        if getbit(control['address'], 0) == "1":
            resvalue(control['address'], 1)
        if getbit(control['address'], 1) == "1":
            resvalue(control['address'], 2)
            self.message_trigger("Pump LD has been swithched off.\n")
        else:
            self.message_trigger("Pump LD has already been switched off.\n")
        self.b_ldon.configure(text="PUMP ON", bg=Colours["green"], fg=Colours["white"], command=lambda: self.ld_on())
        self.b_lock.configure(fg=Colours["darkgrey"], command="")

    def pzt_on(self):

        if Globals.laser_off == 0:
            self.actual = Globals.status_bit
            if readbit(self.actual, 1) != "1":
                addvalue(control["address"], control["pzt"])
            self.pzt_after = self.gui.after(1000, self.pzt_on)
            if readbit(self.actual, 19) == "1":

                if readbit(self.actual, 20) == "1":
                    self.message_trigger("Pump LD has stabilised, locking will be initiated \n")

                    if "PZT0" in Globals.available:
                        if readbit(self.actual, 6) == "1":
                            resvalue(control['address'], control["pzt0_m"])
                            self.actual = self.actual - control["pzt0_m"]
                        if readbit(self.actual, 8) == "0":
                            addvalue(control['address'], control["pzt0_l"])
                            self.actual = self.actual + control["pzt0_l"]

                    if "PZT1" in Globals.available:
                        if readbit(self.actual, 7) == "1":
                            resvalue(control['address'], control["pzt1_m"])
                            self.actual = self.actual - control["pzt1_m"]
                        if readbit(self.actual, 9) == "0":
                            addvalue(control['address'], control["pzt1_l"])
                            self.actual = self.actual + control["pzt1_l"]

                    self.gui.after_cancel(self.pzt_after)
                    self.lock()
        else:
            return "break"

    def lock(self):
        if Globals.laser_off == 0:
            timeout = time.time() + 400
            self.actual = Globals.status_bit
            self.lock_after = self.gui.after(1000, self.lock)
            self.b_lock.configure(fg=Colours["solo"], command=lambda: self.lock_on())
            if readbit(self.actual, 21) == "1":
                self.message_trigger("The laser has been locked. \n")
                self.gui.after_cancel(self.lock_after)
            if time.time() > timeout:
                self.message_trigger("The laser could not be locked, please reset the system. \n")
                self.gui.after_cancel(self.lock_after)
        else:
            return "break"

    def laser_off(self):

        Globals.laser_off = 1
        Globals.tec_stab = 0

        if getbit(control['address'], 1) == "1":
            resvalue(control['address'], 2)
        if getbit(control['address'], 0) == "1":
            resvalue(control['address'], 1)
        if getbit(control['address'], 10) == "1":
            resvalue(control['address'], 1024)
            self.message_trigger("The system is turning off." + "\n")
        elif Globals.subscription_off == 1:
            self.message_trigger("License expired, turning off." + "\n")
        else:
            self.message_trigger("The system is already turned off." + "\n")
        if hasattr(self, 'window'):
            self.window.destroy()
        if hasattr(self, 'tec_after'):
            self.gui.after_cancel(self.tec_after)
        if hasattr(self, 'ld_after'):
            self.gui.after_cancel(self.ld_after)
        if hasattr(self, 'pzt_after'):
            self.gui.after_cancel(self.pzt_after)
        if hasattr(self, 'lock_after'):
            self.gui.after_cancel(self.lock_after)
        if hasattr(self, 'getnametec_after'):
            self.gui.after_cancel(self.getnametec_after)
        if hasattr(self, 'l_tec2_temp_actual'):
            self.l_tec2_temp_actual.stop_temp_main()
            self.l_tec2_temp_actual_n = 0
            Globals.rowtec = Globals.rowtec - 2
        if hasattr(self, 'l_tec3_temp_actual'):
            self.l_tec3_temp_actual.stop_temp_main()
            self.l_tec3_temp_actual_n = 0
            Globals.rowtec = Globals.rowtec - 2
        if hasattr(self, 'l_tec0_temp_actual'):
            self.l_tec0_temp_actual.stop_temp_main()
            self.l_tec0_temp_actual_n = 0
            Globals.rowtec = Globals.rowtec - 2
        if hasattr(self, 'l_tec1_temp_actual'):
            self.l_tec1_temp_actual.stop_temp_main()
            self.l_tec1_temp_actual_n = 0
            Globals.rowtec = Globals.rowtec - 2
        if hasattr(self, 'l_ld_curr_actual'):
            self.l_ld_curr_actual.stop_ld_main()
            self.l_ld_curr_actual_n = 0
            Globals.row = Globals.row - 2
        if hasattr(self, 'l_clp_curr_actual'):
            self.l_clp_curr_actual.stop_clp()
            self.l_pzt0_stat_actual.stop_status()
            self.l_clp_curr_actual_n = 0
            Globals.row = Globals.row - 4
        if hasattr(self, 'l_clp1_curr_actual'):
            self.l_clp1_curr_actual.stop_clp()
            self.l_pzt1_stat_actual.stop_status()
            self.l_clp1_curr_actual_n = 0
            Globals.row = Globals.row - 4

        self.b_ldon.configure(text="PUMP ON", bg=Colours["grey"], fg=Colours["darkgrey"], command="")
        self.b_lock.configure(fg=Colours["darkgrey"], command="")
        # if hasattr(self, 'status_refresh_after'):
        #     self.gui.after_cancel(self.status_refresh_after)

        self.message_trigger("Successful shutdown." + "\n")

        # if hasattr(self, 'status_bit_after'):
        #     print("here")
        #     self.gui.after_cancel(self.status_bit_after)

        setvalue(control['address'], 0)
        self.gui.update()
        if hasattr(self, 'update_messages_after'):
            self.gui.after_cancel(self.update_messages_after)
        # ser.close()

    def lock_on(self):
        # if readbit(self.bit, 18) == "1":
        #     if readbit(self.bit, 19) == "1":
        actual = getvalue(control['address'])['value']
        if readbit(actual, 0) == "1":
            if readbit(actual, 1) == "1":
                if "PZT0" in Globals.available:
                    if readbit(actual, 6) == "1":
                        resvalue(control['address'], control["pzt0" + "_m"])
                        actual = actual - control["pzt0" + "_m"]
                    if readbit(actual, 8) == "0":
                        addvalue(control['address'], control["pzt0" + "_l"])
                        actual = actual + control["pzt0" + "_l"]
                    else:
                        setvalue(base["pzt0"][0], 1073741824)
                        self.message_trigger("PZT0 is relocked. \n")

                if "PZT1" in Globals.available:
                    if readbit(actual, 7) == "1":
                        resvalue(control['address'], control["pzt1" + "_m"])
                        actual = actual - control["pzt1" + "_m"]
                    if readbit(actual, 9) == "0":
                        addvalue(control['address'], control["pzt1" + "_l"])
                        actual = actual + control["pzt1" + "_l"]
                    else:
                        setvalue(base["pzt1"][0], 1073741824)
                        self.message_trigger("PZT1 is relocked \n")
            else:
                self.message_trigger("PZT is not switched on.\n")
        else:
            self.message_trigger("Pump is not switched on.\n")

    def alignment(self):
        self.alignment_bit = getvalue(control["address"])["value"]
        if readbit(self.alignment_bit, 0) == "1":
            self.ld_scale.configure(command="")
            self.ld_scale.set(Globals.Names["low"])
            self.ld_scale.configure(command=lambda x: self.ld_powerscale())
            setvalue(getaddress("ld_d", "curr"), Globals.Names['low'], "u", "u")
            self.ramp_enabled()
            self.message_trigger("Power level set to external alignment. \n")
        else:
            self.message_trigger("Pump LD needs to stabilise first. \n")

    def highp(self):
        if getbit(control['address'], 10) == "1":
            if getbit(control['address'], 0) == "1":
                resvalue(control["address"], 1)
                self.ld_scale.configure(command="")
                self.ld_scale.set(Globals.Names["high"])
                self.ld_scale.configure(command=lambda x: self.ld_powerscale())
                self.message_trigger(
                    "Power level set to full power, make sure to comply with safety regulations. \n")
                self.laser_on()
            else:
                self.message_trigger("Pump LD needs to stabilise first. \n")
        else:
            self.message_trigger("TECs need to stabilise first. \n")

    def ld_powerscale(self):
        result = float(self.ld_scale.get())
        self.alignment_bit = getvalue(control["address"])["value"]
        if readbit(self.alignment_bit, 0) == "1":
            setvalue(getaddress("ld_d", "curr"), result, "u", "u")
            self.message_trigger("Power level set  " + str(result) + " A.\n")
            self.pzt_on()

        else:
            self.message_trigger("Pump LD needs to stabilise first. \n")

    def power_indicator(self, id):
        source = getvalue(indicator["read"])['value']
        if readbit(source, indicator[id]["green"]) == "1":
            return Colours['green']
        elif readbit(source, indicator[id]["orange"]) == "1":
            return Colours['amber']
        elif readbit(source, indicator[id]["red"]) == "1":
            return Colours['red']
        else:
            return Colours['darkgrey']

    def findCenter(self, canvas, text):
        coords = canvas.bbox(text)
        xOffset = 10 + (coords[2] - coords[0]) / 2
        yOffset = 10 + (coords[3] - coords[1]) / 2
        return [xOffset, yOffset]

    def getcircle(self, canvas):
        return canvas.create_oval(20, 20, 80, 80, width=0)

    def getnametec(self, base, label, status):
        status.set(getNames()[base] + " :")
        label.configure(textvariable=status)
        self.getnametec_after = label.after(1500, lambda: self.getnametec(base, label, status))

    def ramp_enabled(self):
        actual = getvalue(control['address'])['value']
        if "PZT0" in Globals.available:
            bit = [8, 6]

            if readbit(actual, 1) != "1":
                addvalue(control['address'], 2)

            if readbit(actual, bit[1]) == "1":
                resvalue(control['address'], control["pzt0_m"])
                actual = actual - control["pzt0_m"]

            if readbit(actual, bit[0]) == "1":
                resvalue(control['address'], control["pzt0_l"])
                actual = actual - control["pzt0_l"]

        if "PZT1" in Globals.available:
            bit = [9, 7]

            if readbit(actual, 1) != "1":
                addvalue(control['address'], 2)

            if readbit(actual, bit[1]) == "1":
                resvalue(control['address'], control["pzt1_m"])
                actual = actual - control["pzt1_m"]

            if readbit(actual, bit[0]) == "1":
                resvalue(control['address'], control["pzt1_l"])
                actual = actual - control["pzt1_l"]

    def reset(self):

        if getbit(control['address'], 3) != "1":
            comm_start()
            comm_init()
            self.front_panel()
        else:
            comm_init()

        self.message_trigger("Reset completed. \n")
        self.c_error.configure(bg=Colours["darkgrey"])
# def new_top(self, master):
#     self.activation()
#     if hasattr(self, "window"):
#         self.window.destroy()
#     self.window = newwin(master)

# class newwin(tk.Toplevel):
#
#     def __init__(self, master):
#         tk.Toplevel.__init__(self)
#         #self.grab_set()
#         #self.protocol("WM_DELETE_WINDOW", self.close)
#         self.configure(background=Background['main'])
#
#         self.tab_parent = ttk.Notebook(self)
#         self.TEC = TECPanel(self.tab_parent)
#         self.TEC.configure(bg=Background['main'])
#         self.LDP = LDPanel(self.tab_parent)
#         self.LockP = LockPanel(self.tab_parent)
#         self.GeneralP = GeneralPanel(self.tab_parent)
#         self.CalP = CalPanel(self.tab_parent)
#         self.tab_parent.add(self.GeneralP, text="General")
#         self.tab_parent.add(self.TEC, text="TEC")
#         self.tab_parent.add(self.LDP, text="LD driver")
#         self.tab_parent.add(self.LockP, text="Lock")
#         self.tab_parent.add(self.CalP, text="Calibration")
#         self.tab_parent.grid(row=1, column=1, rowspan=1, columnspan=4, sticky="nw")
#
#     def close(self):
#         self.destroy()
#         master.self.setTopLevel(None)



