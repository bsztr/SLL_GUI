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
from tkinter import messagebox
import hashlib

class ClientPanel(tk.Frame):


    def __init__(self):

        self.l_ld_curr_actual_n = 1
        self.l_clp_curr_actual_n = 1
        self.l_clp1_curr_actual_n = 1
        self.l_tec0_temp_actual_n = 1
        self.l_tec1_temp_actual_n = 1
        self.l_tec2_temp_actual_n = 1
        self.l_tec3_temp_actual_n = 1

        if "PZT0" in Globals.available:
            Globals.regoffset0 = getvalue(getaddress("pzt0_d", "dpotb_amp"), "u", "1")["value"]
            Globals.pzt0type = getvalue(getaddress("pzt0", "id"), "s", "1")["value"]

        if "PZT1" in Globals.available:
            Globals.regoffset1 = getvalue(getaddress("pzt1_d", "dpotb_amp"), "u", "1")["value"]
            Globals.pzt1type = getvalue(getaddress("pzt1", "id"), "s", "1")["value"]

        global message
        message = ""
        available = Globals.available
        Names = Globals.Names
        self.gui = tk.Tk()
        # self.gui.geometry("395x590")
        self.gui.title("Skylark GUI v" + Globals.guiver + "C")
        self.gui.configure(bg=Background['main'])
        self.button = 18
        self.canvas_width = 355
        self.canvas_height = 200

        self.Unik = tk.PhotoImage(file=self.resource_path("Skyrlogo.png"))
        self.Unik = self.Unik.zoom(2)
        self.Unik = self.Unik.subsample(15)
        self.l_unik = tk.Label(image=self.Unik, bg=Background['main'])

        self.l_detect = tk.Label(self.gui, text=self.lh_detect(), font=fonts['detection'], fg="grey",
                                 bg=Background['main'])
        self.b_connect = tk.Button(self.gui, text="x", font=fonts['status'], fg=Colours["darkred"], bg=Colours['grey'],
                                   width=1, height=1, command=lambda: self.disconnect())
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
        self.l_copy = tk.Label(self.gui, text="Logon", bg=Background['main'], font=fonts['detection'])
        self.l_copy2 = tk.Label(self.gui, text="All rights reserved", bg=Background['main'], font=fonts['detection'])
        self.l_copy.bind('<Triple-Button-1>', self.welcome)
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

            Globals.row = Globals.row + 2

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

        if "TEC4" in Globals.available:
            if not hasattr(self, "l_tec4_temp_actual"):
                self.l_tec4_temp_actual = temp_label(self.gui)
                self.l_tec4_temp_actual.update_temp_main("tec4", "act")
        if "TEC5" in Globals.available:
            if not hasattr(self, "l_tec5_temp_actual"):
                self.l_tec5_temp_actual = temp_label(self.gui)
                self.l_tec5_temp_actual.update_temp_main("tec5", "act")

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
        self.c_message = tk.Canvas(self.gui, width=self.canvas_width, height=self.canvas_height)
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
        if Globals.opmsetting == 1:
            self.b_lock = tk.Button(self.gui, text="Lock Power", fg=Colours["darkgrey"], bg=Colours['grey'], command="",
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
        if Globals.opmsetting != 1:
            self.b_lock = tk.Button(self.gui, text="RELOCK", fg=Colours["darkgrey"], bg=Colours['grey'], command="",
                                    font=fonts['subbutton'], height=1, width=10)
            self.l_reg_scale = tk.Label(self.gui, text="Regulation offset", font=fonts['main'],
                                     bg=Background['main'])
            self.reg_scale = tk.Scale(self.gui, from_=-20, to=20, tickinterval= False,
                                     resolution=1, orient=tk.HORIZONTAL,
                                     bg=Background["main"], font=fonts["main"], command="")
            self.reg_scale.set(0)
            self.b_plus_reg = tk.Button(self.gui, text="+", bg=Colours['grey'],
                                     command=lambda: self.regoffset(1), font=fonts['title'], height=1,
                                     width=5)
            self.b_neg_reg = tk.Button(self.gui, text="-", bg=Colours['grey'],
                                     command=lambda: self.regoffset(0), font=fonts['title'], height=1,
                                     width=5)
            self.reg_scale.configure(command=lambda x: self.pzt_regscale())
            self.reg_scale.grid(row=22, column=1, columnspan=4, rowspan=1, sticky="nwes", padx=(3, 3), pady=(2, 2))

        else:

        #####LD Adjustment pan

            self.l_reg_scale = tk.Label(self.gui, text="Output power regulation", font=fonts['main'],
                                     bg=Background['main'])
            self.ld_scale = tk.Scale(self.gui, from_=0, to=100, tickinterval= False,
                                     resolution=1, orient=tk.HORIZONTAL,
                                     bg=Background["main"], font=fonts["main"], command="")
            current_ld = getvalue(getaddress("ld_d", "curr"), "u", "u")["value"]
            stepy =Globals.shiftldrange/100
            orig = Globals.shiftmincurrent #+ Globals.shiftldrange/2
            opmstep = int(((current_ld -orig)/Globals.shiftldrange)*100)

            if abs(opmstep) > 100 or abs(opmstep) < 0:
                opmstep = 0
            self.ld_scale.set(opmstep)
            self.b_plus_reg = tk.Button(self.gui, text="+", bg=Colours['grey'],
                                     command=lambda: self.ldoffset(1), font=fonts['title'], height=1,
                                     width=5)
            self.b_neg_reg = tk.Button(self.gui, text="-", bg=Colours['grey'],
                                     command=lambda: self.ldoffset(0), font=fonts['title'], height=1,
                                     width=5)
            self.ld_scale.configure(command=lambda x: self.ld_regscale())
            self.ld_scale.grid(row=22, column=1, columnspan=4, rowspan=1, sticky="nwes", padx=(3, 3), pady=(2, 2))


            if opmstep > 95:
                self.b_shiftbutton = tk.Button(self.gui, text="Shift", fg="red",bg=Colours['grey'],
                                           command=lambda: self.startshift(), font=fonts['title'], height=1,
                                           width=5)
                self.b_shiftbutton.grid(row=29, column=3, columnspan=2, rowspan=1, sticky="nwse", pady=(0,6), padx=6)



        # Grid - Info pan
        self.l_unik.grid(row=1, column=1, columnspan=4, rowspan=2, sticky="nw", padx=3, pady=(18,0))
        self.l_detect.grid(row=4, column=1, columnspan=4, rowspan=2, sticky="nw")
        self.b_connect.grid(row=29, column=5, columnspan=1, rowspan=1, sticky="nwse", pady=(0, 6))
        self.geths(self.gui).grid(row=5, column=1, columnspan=10, sticky="we")
        self.l_info.grid(row=2, column=5, columnspan=4, rowspan=1, sticky="nes", pady=(10,0), padx=(0,5))
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
        self.l_reg_scale.grid(row=21, column=1, columnspan=2, rowspan=1, sticky="nws", padx=(3, 3), pady=(2, 2))
        self.b_plus_reg.grid(row=21, column=3, columnspan=1, rowspan=1, sticky="nwse", padx=(3, 3), pady=(2, 2))
        self.b_neg_reg.grid(row=21, column=4, columnspan=1, rowspan=1, sticky="nwse", padx=(3, 3), pady=(2, 2))
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
        self.l_copy2.grid(row=35, column=1, columnspan=5, rowspan=2, sticky="nsw", padx = (5,0))
        self.l_copy.grid(row=35, column=6, columnspan=2, rowspan=2, sticky="nse", padx = (0,5))

    def geths(self, parent):
        hs = ttk.Separator(parent, orient=tk.HORIZONTAL)
        return hs

    def getvs(self, parent):
        vs = ttk.Separator(parent, orient=tk.VERTICAL)
        return vs

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def on_closing(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?\nThis will not affect laser operation."):
            if Globals.disconnect != 1:
                 self.disconnect()
            self.gui.quit()
            self.gui.update()
            self.gui.destroy()

    def start(self):

        self.gui.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.gui.mainloop()

    def status(self):
        available=Globals.available
        config =""
        for i in range(0, len(available)):
            config = "Configuration: " + ", ".join(available) + "\n"
        return config

    def status_bit(self):
        Globals.status_bit = getvalue(status["address"])["value"]

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

    def welcome(self, e):
        if hasattr(self, "athpage"):
            self.athpage.destroy()
            del self.athpage
        if not hasattr(self, "athpage"):
            self.athpage = tk.Toplevel(self.gui)
            inp = tk.StringVar()
            tk.Label(self.athpage, text="Enter password").pack()
            tk.Entry(self.athpage, textvariable=inp, show ="*").pack()
            tk.Button(self.athpage, text="OK", command=lambda: self.authorise(inp)).pack()

    def authorise(self, ent):
        res = ent.get()
        res = bytes(res, encoding='utf-8')
        if hashlib.sha256(res).hexdigest() == Globals.engauth:
            self.athpage.destroy()
            del(self.athpage)
            Globals.engineer = 1
            self.new_top()
        else:
            self.athpage.destroy()
            del (self.athpage)




    def update_messages(self, canvas):
        if Globals.disconnect != 1:

            self.status_bit()
            config = self.status()
            canvas.delete('all')
            self.text=canvas.create_text(0,0,font=fonts['messages'], fill=Colours['darkgrey'], text=config + message, anchor="nw")
            canvas.move(self.text, 10, 10)
            self.getmessage()
            self.geterror()
            #self.incident_error(canvas)
            if Globals.refresh == 1:
                canvas.delete("all")
                self.front_panel()
            self.refresh()
            self.update_messages_after = canvas.after(1500, lambda: self.update_messages(canvas))
            Globals.runnning_PROC.append(self.update_messages_after)
            if Globals.disconnect_trigger == 1:
                Globals.disconnect_trigger == 0
                self.disconnect()

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
        if readbit(Globals.status_bit, status["ERROR"]) == "1" and Globals.error_disp != 1:
            self.c_error.configure(bg=Colours["red"])
            error_t = str(getvalue("0003", "u", "1")["value"])
            self.message_trigger("ERROR: " + error_t + "\n")
            Globals.error_disp = 1


    def getcolour(self, result):
        if result > 30:
            return Colours['red']
        else:
            return Colours['green']

    def geterrorcolour(self, canvas):
        if Globals.disconnect != 1:
            canvas.configure(bg=Colours["darkgrey"])

    def getindicatorcolour(self, id, canvas):
        self.indicator()
        canvas.configure(bg=eval("Globals." + id))
        canvas.after(1500, lambda: self.getindicatorcolour(id, canvas))

    def indicator(self):
        source = Globals.status_bit
        item = "ld"
        if "PZT0" in Globals.available:
            list = {"ld", "pzt0", "tec"}
        else:
            list = {"ld", "pzt1", "tec"}
        #print(source, bin(source))
        for item in list:
            if item == "pzt0" or item == "pzt1":
                itemo = "pzt"
            else:
                itemo = item
            if readbit(source, eval("indicator[item]")["grey"]) == "1":

                if readbit(source, eval("indicator[item]")["amber"]) == "1":

                    if readbit(source, eval("indicator[item]")["green"]) == "1":

                        exec("Globals." + itemo + " = Colours['green']")
                    else:
                        exec("Globals." + itemo + " = Colours['amber']")

                elif item == "pzt1" or item == "pzt0":
                    if readbit (source, eval("indicator[item]")["blue"]) == "1":
                        exec("Globals." + itemo + " = Colours['blue']")
                    elif readbit (source, eval("indicator[item]")["orange"]) == "1":
                        exec("Globals." + itemo + " = Colours['orange']")
                    elif readbit(source, eval("indicator[item]")["green"]) == "1":
                        exec("Globals." + itemo + " = Colours['green']")
                    elif readbit(source, eval("indicator[item]")["amber"]) == "1":
                        exec("Globals." + itemo + " = Colours['amber']")
                else:
                    exec("Globals." + itemo + " = Colours['darkgrey']")
            else:
                exec("Globals." + itemo + " = Colours['darkgrey']")
        if readbit(source, 0)=="1":
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
                # self.ldr_n = tk.StringVar()
                # self.l_ld_curr = tk.Label(self.gui, textvariable=self.ldr_n, font=fonts['temperature'],
                #                           bg=Background['main'])
                self.getnametec("ldr", self.l_ld_curr, self.ldr_n)
                # self.l_ld_curr_actual = ld_label(self.gui)
                self.l_ld_curr_actual.update_ld_main("ld", "act")
                # self.l_ld_curr.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
                # self.l_ld_curr_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")
                # Globals.row = Globals.row + 2

        elif hasattr(self, "l_ld_curr_actual"):
            self.l_ld_curr.grid_forget()
            self.l_ld_curr_actual.stop_ld_main()
            self.l_ld_curr_actual.grid_forget()
            del (self.l_ld_curr_actual)
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
                # self.l_clp_curr = tk.Label(self.gui, text="CLP power:", font=fonts['temperature'],
                #                            bg=Background['main'])
                # self.l_clp_curr_actual = pzt_label(self.gui)
                self.l_clp_curr_actual.update_clp_main(getaddress("pzt0", "clp_power"), "clp_power")
                # self.l_clp_curr.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
                # self.l_clp_curr_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")

                # Globals.row = Globals.row + 2

                # self.pzt0_n = tk.StringVar()
                # self.l_pzt0_stat = tk.Label(self.gui, textvariable=self.pzt0_n, font=fonts['temperature'],
                #                             bg=Background['main'])
                self.getnametec("pzt0", self.l_pzt0_stat, self.pzt0_n)
                # self.l_pzt0_stat_actual = pzt_label(self.gui)
                self.l_pzt0_stat_actual.update_status_main("pzt0")
                # self.l_pzt0_stat.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
                # self.l_pzt0_stat_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")

                # Globals.row = Globals.row + 2

        elif hasattr(self, "l_clp_curr") and hasattr(self, "l_pzt0_stat"):
            self.l_pzt0_stat.grid_forget()
            self.l_pzt0_stat_actual.stop_status()
            self.l_pzt0_stat_actual.grid_forget()
            self.l_clp_curr.grid_forget()
            self.l_clp_curr_actual.stop_clp()
            self.l_clp_curr_actual.grid_forget()
            del (self.l_pzt0_stat_actual)
            del (self.l_clp_curr_actual)
            del (self.l_clp_curr)
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

                Globals.row = Globals.row + 2

            elif self.l_clp1_curr_actual_n == 0 or Globals.pzt1r == 1:
                # self.l_clp1_curr = tk.Label(self.gui, textvariable="CLP1 power:", font=fonts['temperature'],
                #                            bg=Background['main'])
                # self.l_clp1_curr_actual = pzt_label(self.gui)
                self.l_clp1_curr_actual.update_clp_main(getaddress("pzt1", "clp_power"), "clp_power")
                # self.l_clp1_curr.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
                # self.l_clp1_curr_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")

                # Globals.row = Globals.row + 2

                # self.pzt1_n = tk.StringVar()
                # self.l_pzt1_stat = tk.Label(self.gui, textvariable=self.pzt1_n, font=fonts['temperature'],
                #                            bg=Background['main'])
                self.getnametec("pzt1", self.l_pzt1_stat, self.pzt1_n)
                # self.l_pzt1_stat_actual = pzt_label(self.gui)
                self.l_pzt1_stat_actual.update_status_main("pzt1")
                # self.l_pzt1_stat.grid(row=Globals.row, column=1, columnspan=1, rowspan=2, sticky="nw")
                # self.l_pzt1_stat_actual.grid(row=Globals.row, column=2, columnspan=1, rowspan=2, sticky="nw")

                # Globals.row = Globals.row + 2

        elif hasattr(self, "l_clp1_curr") and hasattr(self, "l_pzt1_stat"):
            self.l_pzt1_stat.grid_forget()
            self.l_pzt1_stat_actual.stop_status()
            self.l_pzt1_stat_actual.grid_forget()
            self.l_clp1_curr.grid_forget()
            self.l_clp1_curr_actual.stop_clp()
            self.l_clp1_curr_actual.grid_forget()
            del (self.l_pzt1_stat_actual)
            del (self.l_clp1_curr_actual)
            del (self.l_clp1_curr)
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
                # self.tec0_n = tk.StringVar()
                # self.l_tec0_temp = tk.Label(self.gui, textvariable=self.tec0_n, font=fonts['temperature'],
                #                            bg=Background['main'])
                self.getnametec("tec0", self.l_tec0_temp, self.tec0_n)
                # self.l_tec0_temp_actual = temp_label(self.gui)
                self.l_tec0_temp_actual.update_temp_main("tec0", "act")
                # self.l_tec0_temp.grid(row=Globals.rowtec, column=3, columnspan=1, rowspan=2, sticky="nw")
                # self.l_tec0_temp_actual.grid(row=Globals.rowtec, column=4, columnspan=1, rowspan=2, sticky="nw")
                # Globals.rowtec = Globals.rowtec + 2

        elif hasattr(self, "l_tec0_temp_actual"):
            self.l_tec0_temp.grid_forget()
            self.l_tec0_temp_actual.grid_forget()
            self.l_tec0_temp_actual.stop_temp_main()
            del (self.l_tec0_temp_actual)
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
                # self.tec1_n = tk.StringVar()
                # self.l_tec1_temp = tk.Label(self.gui, textvariable=self.tec1_n, font=fonts['temperature'],
                #                            bg=Background['main'])
                self.getnametec("tec1", self.l_tec1_temp, self.tec1_n)
                # self.l_tec1_temp_actual = temp_label(self.gui)
                self.l_tec1_temp_actual.update_temp_main("tec1", "act")
                # self.l_tec1_temp.grid(row=Globals.rowtec, column=3, columnspan=1, rowspan=2, sticky="nw")
                # self.l_tec1_temp_actual.grid(row=Globals.rowtec, column=4, columnspan=1, rowspan=2, sticky="nw")
                # Globals.rowtec = Globals.rowtec + 2

        elif hasattr(self, "l_tec1_temp_actual"):
            self.l_tec1_temp.grid_forget()
            self.l_tec1_temp_actual.grid_forget()
            self.l_tec1_temp_actual.stop_temp_main()
            del (self.l_tec1_temp_actual)
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
                # self.tec2_n = tk.StringVar()
                # self.l_tec2_temp = tk.Label(self.gui, textvariable=self.tec2_n, font=fonts['temperature'],
                #                            bg=Background['main'])
                self.getnametec("tec2", self.l_tec2_temp, self.tec2_n)
                # self.l_tec2_temp_actual = temp_label(self.gui)
                self.l_tec2_temp_actual.update_temp_main("tec2", "act")
                # self.l_tec2_temp.grid(row=Globals.rowtec, column=3, columnspan=1, rowspan=2, sticky="nw")
                # self.l_tec2_temp_actual.grid(row=Globals.rowtec, column=4, columnspan=1, rowspan=2, sticky="nw")
                # Globals.rowtec = Globals.rowtec + 2

        elif hasattr(self, "l_tec2_temp_actual"):
            self.l_tec2_temp.grid_forget()
            self.l_tec2_temp_actual.grid_forget()
            self.l_tec2_temp_actual.stop_temp_main()
            del (self.l_tec2_temp_actual)
            Globals.rowtec = Globals.rowtec - 2

        if "TEC3" in Globals.available:
            if not hasattr(self, "l_tec3_temp_actual"):
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
                # self.tec3_n = tk.StringVar()
                # self.l_tec3_temp = tk.Label(self.gui, textvariable=self.tec3_n, font=fonts['temperature'],
                #                            bg=Background['main'])
                self.getnametec("tec3", self.l_tec3_temp, self.tec3_n)
                # elf.l_tec3_temp_actual = temp_label(self.gui)
                self.l_tec3_temp_actual.update_temp_main("tec3", "act")
                # self.l_tec3_temp.grid(row=Globals.rowtec, column=3, columnspan=1, rowspan=2, sticky="nw")
                # self.l_tec3_temp_actual.grid(row=Globals.rowtec, column=4, columnspan=1, rowspan=2, sticky="nw")
                # Globals.rowtec = Globals.rowtec + 2

        elif hasattr(self, "l_tec3_temp_actual"):
            self.l_tec3_temp.grid_forget()
            self.l_tec3_temp_actual.grid_forget()
            self.l_tec3_temp_actual.stop_temp_main()
            del (self.l_tec3_temp_actual)
            Globals.rowtec = Globals.rowtec - 2

        if "TEC4" in Globals.available:
            if not hasattr(self, "l_tec4_temp_actual"):
                self.l_tec4_temp_actual = temp_label(self.gui)
                self.l_tec4_temp_actual.update_temp_main("tec4", "act")
        if "TEC5" in Globals.available:
            if not hasattr(self, "l_tec5_temp_actual"):
                self.l_tec5_temp_actual = temp_label(self.gui)
                self.l_tec5_temp_actual.update_temp_main("tec5", "act")

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
        if Globals.disconnect == 1:
            self.connect()
        if Globals.tec_stab == 1:
            self.ld_on()
        else:
            self.activation()
            self.actual = Globals.status_bit

            self.message_trigger("System is powering up. \n")

            #self.actual=getvalue(control["address"])['value']

            if getbit(status["address"], status["STATUS_OK"]) == "1" and getbit(status["address"],status["TEC_WARMING_UP"]) == "0":
                addvalue(control['address'],2 ** control["tec0"] + 2 ** control["tec1"] + 2 ** control["tec2"] + 2 ** control["tec3"] + 2 ** control["tec4"] + 2 ** control["tec5"])
                self.message_trigger("TECs are turning on.\n")

            self.tec_on()

    def tec_on(self):
        if Globals.laser_off == 0:
            if Globals.tec_stab == 1:
                self.ld_on()
            else:
                self.actual = Globals.status_bit
                self.tec_after = self.gui.after(1000, self.tec_on)
                Globals.runnning_PROC.append(self.tec_after)
                if readbit(self.actual, status["TEC_READY"]) == "1":
                    self.gui.after_cancel(self.tec_after)
                    Globals.tec_stab = 1
                    self.b_ldon.configure(bg=Colours["green"], fg=Colours["white"], command=lambda: self.ld_on())
                    self.message_trigger("Initialisation complete, the pump can now be switched on.\n")

    def ld_on(self):
        if Globals.laser_off == 0 or Globals.laser_turnhigh == 1:

            if Globals.tec_stab == 1:
                self.actual = Globals.status_bit
                if hasattr(self, 'ld_after'):
                    self.gui.after_cancel(self.ld_after)
                self.ld_after = self.gui.after(1000, self.ld_on)
                Globals.runnning_PROC.append(self.ld_after)
                self.b_ldon.configure(text="PUMP OFF", bg=Colours["red"], fg=Colours["white"],
                                      command=lambda: self.ld_off())
                if readbit(self.actual, status["TEC_READY"]) == "1" and readbit(self.actual,
                                                                                status["LD_WARMING_UP"]) == "0":
                    addvalue(control['address'], 2 ** control['ld'])
                    self.message_trigger("Pump LD is turning on. \n")
                    self.gui.after_cancel(self.ld_after)
                    self.pzt_on()
                    setvalue(getaddress("ld_d", "curr"), Globals.Names['high'], "u", "u")
                if readbit(self.actual, status["TEC_READY"]) == "1" and Globals.laser_turnhigh == 1:
                    Globals.ramp_enabled = 0
                    Globals.laser_turnhigh = 0
                    setvalue(getaddress("ld_d", "curr"), Globals.Names['high'], "u", "u")
                    self.lock_on()

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
        # if getbit(control['address'], 6) == "1":
        #     resvalue(control['address'], 2**control["pzt0"])
        # if getbit(control['address'], 7) == "1":
        #     resvalue(control['address'], 2**control["pzt1"])
        if getbit(control['address'], control["ld"]) == "1":
            print("SWITCHING OFF")
            setvalue(control["address"],
                     2 ** control["tec0"] + 2 ** control["tec1"] + 2 ** control["tec2"] + 2 ** control["tec3"] + 2 **
                     control["tec4"] + 2 ** control["tec5"])
            self.message_trigger("Pump LD has been swithched off.\n")
        else:
            self.message_trigger("Pump LD has already been switched off.\n")
        self.b_ldon.configure(text="PUMP ON", bg=Colours["green"], fg=Colours["white"], command=lambda: self.ld_on())
        self.b_lock.configure(fg=Colours["darkgrey"], command="")
        Globals.ramp_enabled = 0
        Globals.laser_turnhigh = 0

    def pzt_on(self):

        if Globals.laser_off == 0:
            self.actual = Globals.status_bit
            if getbit(status["address"], status["LD_STABLE"]) == "1":
                addvalue(control['address'], 2 ** control['pzt0'] + 2 ** control['pzt1'])
                time.sleep(3)
                # self.ramp_enabled()
            self.pzt_after = self.gui.after(1000, self.pzt_on)
            Globals.runnning_PROC.append(self.pzt_after)
            if getbit(status["address"], status["LD_STABLE"]) == "1":

                if getbit(status["address"], status["LD_STABLE"]) == "1":
                    self.message_trigger("Pump LD has stabilised, locking will be initiated \n")
                    if "PZT0" in Globals.available:
                        control_bit = getvalue(control["address"])["value"]
                        if readbit(control_bit, control["pzt0_lock"]) == "1":
                            resvalue(control["address"], 2 ** control["pzt0_lock"])
                        if readbit(control_bit, control["pzt0_ramp"]) == "1":
                            resvalue(control["address"], 2 ** control["pzt0_ramp"])
                        if readbit(control_bit, control["pzt0_park"]) == "1":
                            resvalue(control["address"], 2 ** control["pzt0_park"])
                        if readbit(control_bit, control["pzt0_tune"]) != "1":
                            addvalue(control["address"], 2 ** control["pzt0_tune"])

                    if "PZT1" in Globals.available:
                        control_bit = getvalue(control["address"])["value"]
                        if readbit(control_bit, control["pzt1_lock"]) == "1":
                            resvalue(control["address"], 2 ** control["pzt1_lock"])
                        if readbit(control_bit, control["pzt1_ramp"]) == "1":
                            resvalue(control["address"], 2 ** control["pzt1_ramp"])
                        if readbit(control_bit, control["pzt1_park"]) == "1":
                            resvalue(control["address"], 2 ** control["pzt1_park"])
                        if readbit(control_bit, control["pzt1_tune"]) != "1":
                            addvalue(control["address"], 2 ** control["pzt1_tune"])

                    self.gui.after_cancel(self.pzt_after)
                    self.lock()
        else:
            return "break"

    def lock(self):
        if Globals.laser_off == 0:
            timeout = time.time() + 400
            self.actual = Globals.status_bit
            self.lock_after = self.gui.after(1000, self.lock)
            Globals.runnning_PROC.append(self.lock_after)
            self.b_lock.configure(fg=Colours["solo"], command=lambda: self.lock_on())
            if getbit(status["address"], status["PZT_0_Locked"]) == "1" or getbit(status["address"],
                                                                                  status["PZT_1_Locked"]) == "1":
                self.message_trigger("The laser has been locked. \n")
                self.gui.after_cancel(self.lock_after)
            if time.time() > timeout:
                self.message_trigger("The laser could not be locked, please reset the system. \n")
                self.gui.after_cancel(self.lock_after)
        else:
            return "break"

    def disconnect(self):
        if Globals.laser_off != 1:
            global message
            self.message_trigger("Laserhead is disconnected.\n")
            config = self.status()
            self.text = self.c_message.create_text(0, 0, font=fonts['messages'], fill=Colours['darkgrey'], text=config + message,
                                           anchor="nw")
            self.c_message.move(self.text, 10, 10)

            Globals.disconnect = 1

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
                #Globals.rowtec=Globals.rowtec-2
            if hasattr(self, 'l_tec3_temp_actual'):
                self.l_tec3_temp_actual.stop_temp_main()
                self.l_tec3_temp_actual_n = 0
                #Globals.rowtec = Globals.rowtec - 2
            if hasattr(self, 'l_tec0_temp_actual'):
                self.l_tec0_temp_actual.stop_temp_main()
                self.l_tec0_temp_actual_n = 0
                #Globals.rowtec = Globals.rowtec - 2
            if hasattr(self, 'l_tec1_temp_actual'):
                self.l_tec1_temp_actual.stop_temp_main()
                self.l_tec1_temp_actual_n = 0
                #Globals.rowtec = Globals.rowtec - 2
            if hasattr(self, 'l_tec4_temp_actual'):
                self.l_tec4_temp_actual.stop_temp_main()
                #self.l_tec4_temp_actual_n = 0
                #Globals.rowtec=Globals.rowtec-2
            if hasattr(self, 'l_tec5_temp_actual'):
                self.l_tec5_temp_actual.stop_temp_main()
                #self.l_tec5_temp_actual_n = 0
                #Globals.rowtec=Globals.rowtec-2
            if hasattr(self, 'l_ld_curr_actual'):
                self.l_ld_curr_actual.stop_ld_main()
                self.l_ld_curr_actual_n = 0
                #Globals.row = Globals.row - 2
            if hasattr(self, 'l_clp_curr_actual'):
                self.l_clp_curr_actual.stop_clp()
                self.l_pzt0_stat_actual.stop_status()
                self.l_clp_curr_actual_n = 0
                #Globals.row = Globals.row - 4
            if hasattr(self, 'l_clp1_curr_actual'):
                self.l_clp1_curr_actual.stop_clp()
                self.l_pzt1_stat_actual.stop_status()
                self.l_clp1_curr_actual_n = 0
                #Globals.row = Globals.row - 4
            time.sleep(1)
            self.gui.update()
            if hasattr(self, 'update_messages_after'):
                self.gui.after_cancel(self.update_messages_after)
            stop_COMM()
            self.b_connect.configure(text = "+", fg = Colours["green"], command=lambda: self.connect())
            self.l_detect.configure(text="Laserhead disconnected")
        else:
            stop_COMM()
            Globals.disconnect = 1

    def connect(self):
        if Globals.laser_off != 1:
            init_COMM()
            Globals.disconnect = 0
            self.update_messages(self.c_message)
            self.activation()
            self.message_trigger("Laserhead is connected. \n")
            self.b_connect.configure(text="x", fg=Colours["darkred"], command=lambda: self.disconnect())
            self.l_detect.configure(text=self.lh_detect())
        else:
            init_COMM()
            Globals.disconnect = 0

    def laser_off(self):

        Globals.laser_off = 1
        Globals.tec_stab = 0
        self.actual = getvalue(control["address"])["value"]
        if readbit(self.actual, status["TEC_READY"]) == "1":
            setvalue(control["address"], 0)
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
            # Globals.rowtec=Globals.rowtec-2
        if hasattr(self, 'l_tec3_temp_actual'):
            self.l_tec3_temp_actual.stop_temp_main()
            self.l_tec3_temp_actual_n = 0
            # Globals.rowtec = Globals.rowtec - 2
        if hasattr(self, 'l_tec0_temp_actual'):
            self.l_tec0_temp_actual.stop_temp_main()
            self.l_tec0_temp_actual_n = 0
            # Globals.rowtec = Globals.rowtec - 2
        if hasattr(self, 'l_tec1_temp_actual'):
            self.l_tec1_temp_actual.stop_temp_main()
            self.l_tec1_temp_actual_n = 0
            # Globals.rowtec = Globals.rowtec - 2
        if hasattr(self, 'l_tec4_temp_actual'):
            self.l_tec4_temp_actual.stop_temp_main()
            # self.l_tec4_temp_actual_n = 0
            # Globals.rowtec=Globals.rowtec-2
        if hasattr(self, 'l_tec5_temp_actual'):
            self.l_tec5_temp_actual.stop_temp_main()
            # self.l_tec5_temp_actual_n = 0
            # Globals.rowtec=Globals.rowtec-2
        if hasattr(self, 'l_ld_curr_actual'):
            self.l_ld_curr_actual.stop_ld_main()
            self.l_ld_curr_actual_n = 0
            # Globals.row = Globals.row - 2
        if hasattr(self, 'l_clp_curr_actual'):
            self.l_clp_curr_actual.stop_clp()
            self.l_pzt0_stat_actual.stop_status()
            self.l_clp_curr_actual_n = 0
            # Globals.row = Globals.row - 4
        if hasattr(self, 'l_clp1_curr_actual'):
            self.l_clp1_curr_actual.stop_clp()
            self.l_pzt1_stat_actual.stop_status()
            self.l_clp1_curr_actual_n = 0
            # Globals.row = Globals.row - 4

        self.b_ldon.configure(text="PUMP ON", bg=Colours["grey"], fg=Colours["darkgrey"], command="")
        self.b_lock.configure(fg=Colours["darkgrey"], command="")
        # if hasattr(self, 'status_refresh_after'):
        #     self.gui.after_cancel(self.status_refresh_after)

        self.message_trigger("Successful shutdown." + "\n")

        # if hasattr(self, 'status_bit_after'):
        #     print("here")
        #     self.gui.after_cancel(self.status_bit_after)

        # setvalue(control['address'], 0)
        self.gui.update()
        if hasattr(self, 'update_messages_after'):
            self.gui.after_cancel(self.update_messages_after)
        # ser.close()

    def lock_on(self):

        if getbit(status["address"], status["LD_STABLE"]) == "1":
            self.message_trigger("PZT is now locking.\n")
            if "PZT0" in Globals.available:
                control_bit = getvalue(control["address"])["value"]
                if readbit(control_bit, control["pzt0_lock"]) == "1":
                    resvalue(control["address"], 2 ** control["pzt0_lock"])
                if readbit(control_bit, control["pzt0_ramp"]) == "1":
                    resvalue(control["address"], 2 ** control["pzt0_ramp"])
                if readbit(control_bit, control["pzt0_park"]) == "1":
                    resvalue(control["address"], 2 ** control["pzt0_park"])
                if readbit(control_bit, control["pzt0_tune"]) != "1":
                    addvalue(control["address"], 2 ** control["pzt0_tune"])

            if "PZT1" in Globals.available:
                control_bit = getvalue(control["address"])["value"]
                if readbit(control_bit, control["pzt1_lock"]) == "1":
                    resvalue(control["address"], 2 ** control["pzt1_lock"])
                if readbit(control_bit, control["pzt1_ramp"]) == "1":
                    resvalue(control["address"], 2 ** control["pzt1_ramp"])
                if readbit(control_bit, control["pzt1_park"]) == "1":
                    resvalue(control["address"], 2 ** control["pzt1_park"])
                if readbit(control_bit, control["pzt1_tune"]) != "1":
                    addvalue(control["address"], 2 ** control["pzt1_tune"])
            else:
                self.message_trigger("PZT is not switched on.\n")
        else:
            self.message_trigger("Pump is not switched on.\n")

    def alignment(self):
        if hasattr(self, 'pzt_after'):
            self.gui.after_cancel(self.pzt_after)
        if hasattr(self, 'lock_after'):
            self.gui.after_cancel(self.lock_after)
        self.alignment_bit = getvalue(control["address"])["value"]
        if readbit(self.alignment_bit, 0) == "1":
            if hasattr(self, "ld_scale"):
                self.ld_scale.configure(command="")
                self.ld_scale.set(Globals.Names["low"])
                self.ld_scale.configure(command=lambda x: self.ld_powerscale())
            setvalue(getaddress("ld_d", "curr"), Globals.Names['low'], "u", "u")
            self.ramp_enabled()
            self.message_trigger("Power level set to external alignment. \n")
        else:
            self.message_trigger("Pump LD needs to stabilise first. \n")

    def highp(self):
        if hasattr(self, 'pzt_after'):
            self.gui.after_cancel(self.pzt_after)
        if hasattr(self, 'lock_after'):
            self.gui.after_cancel(self.lock_after)
        if readbit(self.actual, status["TEC_READY"]) == "1":
            if readbit(self.actual, status["TEC_READY"]) == "1":
                if Globals.ramp_enabled == 1:

                    if hasattr(self, "ld_scale"):
                        self.ld_scale.configure(command="")
                        self.ld_scale.set(Globals.Names["high"])
                        self.ld_scale.configure(command=lambda x: self.ld_powerscale())

                    self.message_trigger(
                        "Power level set to full power, make sure to comply with safety regulations. \n")

                    Globals.ramp_enabled = 0
                    Globals.laser_turnhigh = 1
                    self.ld_on()

                else:
                    self.message_trigger("Pump LD is already set to full power \n")
            else:
                self.message_trigger("Pump LD needs to stabilise first. \n")
        else:
            self.message_trigger("TECs need to stabilise first. \n")

    def ld_powerscale(self):
        if hasattr(self, "ld_scale"):
            result = float(self.ld_scale.get())
            self.alignment_bit = getvalue(control["address"])["value"]
            if readbit(self.alignment_bit, 0) == "1":
                setvalue(getaddress("ld_d", "curr"), result, "u", "u")
                self.message_trigger("Power level set  " + str(result) + " A.\n")
                self.pzt_on()

            else:
                self.message_trigger("Pump LD needs to stabilise first. \n")

    def pzt_regscale(self):
        if hasattr(self, "reg_scale"):
            result = float(self.reg_scale.get())
            if result > 20:
                result = 20
                self.message_trigger("Regulation offset limit reached at +20. \n")
            if result < -1:
                result = -1
                self.message_trigger("Regulation offset limit reached at -20. \n")

        if "PZT0" in Globals.available:
            towrite = Globals.regoffset0 + result

            if towrite > 255:
                towrite = 255
            elif towrite < 0:
                towrite = 0
            # setvalue(getaddress("dphd", "dpot0"), towrite, "u", "1")
        if "PZT1" in Globals.available:
            towrite = Globals.regoffset1 + result

            if towrite > 255:
                towrite = 255
            elif towrite < 0:
                towrite = 0
            # setvalue(getaddress("dphd", "dpot1"), towrite, "u", "1")

    def regoffset(self, x):
        if x == 1:
            addv = 1
        else:
            addv = -1

        result = float(self.reg_scale.get()) + addv

        if result > 20:
            result = 20
            self.message_trigger("Regulation offset limit reached at +20. \n")
        if result < -20:
            result = -20
            self.message_trigger("Regulation offset limit reached at -20. \n")

        self.reg_scale.set(result)

        if "PZT0" in Globals.available:
            towrite = Globals.regoffset0 + result

            if towrite > 255:
                towrite = 255
            elif towrite < 0:
                towrite = 0
            setvalue(getaddress("dphd", "dpot0"), towrite, "u", "1")
        if "PZT1" in Globals.available:
            towrite = Globals.regoffset1 + result

            if towrite > 255:
                towrite = 255
            elif towrite < 0:
                towrite = 0
            setvalue(getaddress("dphd", "dpot1"), towrite, "u", "1")

    def ld_regscale(self):
        if hasattr(self, "ld_scale"):
            result = float(self.ld_scale.get())

            if result > 100:
                result = 100
                self.message_trigger("Power offset limit reached at +100. \n")
            if result < 0:
                result = 0
                self.message_trigger("Power offset limit reached at 0. \n")

            #self.ld_scale.set(result)
            if result > 95:
                if not hasattr(self, "b_shiftbutton"):
                    self.b_shiftbutton = tk.Button(self.gui, text="Shift", fg="red", bg=Colours['grey'],
                                                   command=lambda: self.startshift(), font=fonts['title'], height=1,
                                                   width=5)
                    self.b_shiftbutton.grid(row=29, column=3, columnspan=2, rowspan=1, sticky="nwse", pady=(0, 6),
                                            padx=6)
                    self.message_trigger("Crystal can be shifted to new position.\n")

            step = Globals.shiftldrange / 100
            orig = Globals.shiftmincurrent

            result = orig + step * result
            #print(result)
            setvalue(getaddress("ld_d", "curr"), result, "u", "u")

    def ldoffset(self, x):
        if x == 1:
            addv = 1
        else:
            addv = -1

        result = float(self.ld_scale.get()) + addv

        if result > 100:
            result = 100
            self.message_trigger("Power offset limit reached at +100. \n")
        if result < 0:
            result = 0
            self.message_trigger("Power offset limit reached at 0. \n")

        self.ld_scale.set(result)
        if result > 95:
            if not hasattr(self, "b_shiftbutton"):
                self.b_shiftbutton = tk.Button(self.gui, text="Shift", fg="red", bg=Colours['grey'],
                                               command=lambda: self.startshift(), font=fonts['title'], height=1,
                                               width=5)
                self.b_shiftbutton.grid(row=29, column=3, columnspan=2, rowspan=1, sticky="nwse", pady=(0, 6), padx=6)
                self.message_trigger("Crystal can be shifted to new position.\n")


        step = Globals.shiftldrange / 100
        orig = Globals.shiftmincurrent

        result = orig + step*result

       # setvalue(getaddress("ld_d", "curr"), result)


    def opm_on(self):
        self.b_lock.configure(fg=Colours["solo"], command=lambda: self.opm_off(), text = "Lock off")
        self.b_plus_reg.configure(command=lambda: self.opm_act())
        self.b_neg_reg.configure(command=lambda: self.opm_act())
        self.message_trigger("Laser power is getting locked.\n")
        self.connect_dev()
        Globals.opmrunning = 1
        if self.ard_on == 1:
            self.serard.write(f"002\n".encode("UTF-8"))
            time.sleep(2)
            self.serard.write(f"002\n".encode("UTF-8"))
            self.l_clp_curr_actual.stop_clp()
            self.opm_iacc = 0
            self.c = 0
            self.opm_ratio = getvalue(getaddress("ld_d", "clp_constant_M"), "f", "u")["value"]
            self.opm_target = self.getpowerlvl()
            #print(self.opm_target)
            self.currtar = np.round(self.opm_target,3)

            setvalue(getaddress("gui", "opm_target"), self.currtar,"f", "u")
            self.opm_run()


    def opm_off(self):
        self.message_trigger("Laser power is unlocked.\n")
        self.b_lock.configure(fg=Colours["solo"], command=lambda: self.opm_on(), text = "Lock on")
        self.b_plus_reg.configure(command=lambda: self.ldoffset(1))
        self.b_neg_reg.configure(command=lambda: self.ldoffset(0))
        self.gui.after_cancel(self.opmrun)
        Globals.opmrunning = 0
        if self.ard_on == 1:
            self.serard.write(f"003\n".encode("UTF-8"))
            time.sleep(2)
            self.serard.write(f"003\n".encode("UTF-8"))
            self.serard.close()
            self.ard_on = 0
            Globals.stageon = 0

    def opm_act(self):
        self.message_trigger("Power can only be adjusted, if power is unlocked.\n")


    def opm_run(self):
        if Globals.laser_off != 1:
            self.opmrun = self.gui.after(500, self.opm_run)
            Globals.runnning_PROC.append(self.opmrun)

            if self.c % 10 == 0:
                indtarget = getvalue(getaddress("gui", "opm_target"), "f", "u")["value"]
                if self.currtar != indtarget:
                    self.opm_target = indtarget
                self.opm_ratio = getvalue(getaddress("ld_d", "clp_constant_M"), "f", "u")["value"]
                self.opm_p = getvalue(getaddress("ld_d", "clp_constant_P"), "f", "u")["value"]/1000000
                self.opm_i = getvalue(getaddress("ld_d", "clp_constant_I"), "f", "u")["value"]/1000000


            if self.ard_on == 0:
                self.message_trigger("Device not connected. \n")
                self.opm_off()
            else:
                value = str(self.serard.read_all().decode()).splitlines()[:-1]
                if len(value) == 1:

                    power_reading = (int(value[0]))
                    print(power_reading)
                    if power_reading > -1 and power_reading < 1023:
                        power_reading =power_reading / self.opm_ratio
                        self.l_clp_curr_actual.configure(text = str(round(power_reading,3)))
                        err = self.opm_target - power_reading
                        self.opm_iacc = err + self.opm_iacc
                        pid_r = self.opm_p * err + self.opm_i * self.opm_iacc

                        curr_ld = getvalue(getaddress("ld", "curr"), "u", "u")["value"]
                        if self.c % 250:
                            setvalue(getaddress("ld_d", "curr"), curr_ld, "u", "u")
                        if pid_r > 0.12:
                            pid_r = 0.12
                        if pid_r < -0.12:
                            pid_r = -0.12
                        pid_output = curr_ld + pid_r
                        #self.message_trigger(f"UV is read as {power_reading}, output is {pid_output}, pid_r {pid_r} \n")
                        #print(Globals.shiftmincurrent, Globals.shiftmincurrent+Globals.shiftldrange, pid_output)
                        if pid_output < Globals.shiftmincurrent+Globals.shiftldrange and pid_output > Globals.shiftmincurrent:
                            setvalue(getaddress("ld", "curr"), pid_output, "u", "u")
                        # if self.c % 5 == 0:
                        #     self.message_trigger(
                        #         f"{self.opm_target}, {self.opm_p}, {power_reading}, {pid_output}, {pid_r}\n")
                self.c += 1
                self.serard.flushOutput()


    def getpowerlvl(self):
        if self.ard_on ==1:
            pwr = []
            for i in range(5):
                value = str(self.serard.read_all().decode()).splitlines()[:-1]
                print("value", value)
                if len(value) == 1:
                    power_reading = (int(value[0]))
                    pwr.append(power_reading)
                time.sleep(1)

            try:
                target = np.mean(pwr)/self.opm_ratio
            except:
                self.opm_off()
                self.message_trigger("Regulation failed.\n")
            return target
        else:
            return 0

    def connect_dev(self):
        ports = comports()
        selected_port = None
        if Globals.stageon ==0:
            for port in ports:
                print(port.description)
                if "CH340" in port.description or "Arduino" in port.description:
                    selected_port = port.device

            if selected_port == None:
                self.ard_on = 0
                self.message_trigger("No regulator found.")
            else:

                serd = serial.Serial(
                    port=selected_port,
                    baudrate=19200,
                    parity=serial.PARITY_NONE,
                    stopbits=1,
                    bytesize=8,
                    timeout=10
                )

                self.serard = serd
                self.ard_on = 1
                self.serard.flush()
                Globals.serdo = self.serard
                Globals.stageon = 1
        else:
            self.serard = Globals.serdo
            self.ard_on = 1
            self.serard.flush()


    def startshift(self):
        Globals.shiftNOW = 1

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
        Globals.ramp_enabled = 1

        if "PZT0" in Globals.available:
            control_bit = getvalue(control["address"])["value"]
            if readbit(control_bit, control["pzt0_tune"]) == "1":
                resvalue(control["address"], 2 ** control["pzt0_tune"])
            if readbit(control_bit, control["pzt0_park"]) == "1":
                resvalue(control["address"], 2 ** control["pzt0_park"])
            if readbit(control_bit, control["pzt0_lock"]) == "1":
                resvalue(control["address"], 2 ** control["pzt0_lock"])
            if readbit(control_bit, control["pzt0_ramp"]) != "1":
                addvalue(control["address"], 2 ** control["pzt0_ramp"])

        if "PZT1" in Globals.available:
            control_bit = getvalue(control["address"])["value"]
            if readbit(control_bit, control["pzt1_tune"]) == "1":
                resvalue(control["address"], 2 ** control["pzt1_tune"])
            if readbit(control_bit, control["pzt1_park"]) == "1":
                resvalue(control["address"], 2 ** control["pzt1_park"])
            if readbit(control_bit, control["pzt1_lock"]) == "1":
                resvalue(control["address"], 2 ** control["pzt1_lock"])
            if readbit(control_bit, control["pzt1_ramp"]) != "1":
                addvalue(control["address"], 2 ** control["pzt1_ramp"])

    def reset(self):

        # if getbit(control['address'], 3) != "1":
        #     comm_start()
        #     comm_init()
        #     self.front_panel()
        # else:
        #     comm_init()
        setvalue(control["address"], 2**control["reset_errors"], "u", "1")
        time.sleep(3)
        setvalue(control["address"], 0)
        self.message_trigger("Reset completed. \n")
        self.c_error.configure(bg=Colours["darkgrey"])

    def new_top(self):

        self.activation()
        if hasattr(self, "window"):
            if hasattr(self.window, "master_after"):
                self.window.after_cancel("master_after")
            if hasattr(self.window, "status_after"):
                self.window.after_cancel("status_after")
            if hasattr(self.window, "tecname_after"):
                self.window.after_cancel("tecname_after")
            self.window.tab_parent.destroy()
            self.window.destroy()
            del self.window.tab_parent
            del self.window
        Globals.Toplevel = 0
        self.gui.update_idletasks()
        self.gui.update()
        self.window = newwin(self)
        Globals.Toplevel = 1

class newwin(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master.gui)
        # self.protocol("WM_DELETE_WINDOW", self.close)
        self.configure(background=Background['main'])
        self.tab_parent = ttk.Notebook(self)
        self.TEC = TECPanel(self.tab_parent)
        self.TEC.configure(bg=Background['main'])
        self.LDP = LDPanel(self.tab_parent)
        self.LockP = LockPanel(self.tab_parent)
        self.GeneralP = GeneralPanel(self.tab_parent, master)
        # self.CalP = CalPanel(self.tab_parent)
        self.tab_parent.add(self.GeneralP, text="General")
        self.tab_parent.add(self.TEC, text="TEC")
        self.tab_parent.add(self.LDP, text="LD driver")
        self.tab_parent.add(self.LockP, text="PZT")
        # self.tab_parent.add(self.CalP, text="Calibration")
        self.tab_parent.grid(row=1, column=1, rowspan=1, columnspan=4, sticky="nw")
        self.tab_parent.enable_traversal()

    def close(self):
        self.destroy()
        master.gui.self.setTopLevel(None)



