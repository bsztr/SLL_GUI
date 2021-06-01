from tkinter import *
from tkinter import ttk
from LockPanel import *
from LDPanel import *
from GeneralPanel import *
gui = Tk()
gui.geometry("360x560")
gui.title("UniKLasers GUI")
def newwin(): # new window definition
    newwin = Toplevel(gui)
    tab_parent= ttk.Notebook(newwin)
    TEC=Frame(tab_parent)
    Lock=Frame(tab_parent)
    LDP = LDPanel(tab_parent)
    LockP=LockPanel(tab_parent)
    AdvancedP = AdvancedPanel(tab_parent)
    tab_parent.add(TEC, text="TEC")
    tab_parent.add(LockP, text="Lock")
    tab_parent.add(LDP, text="LD driver")
    tab_parent.add(AdvancedP, text="Advanced")

    #Grid
    tab_parent.grid(row=1, column=1, rowspan=1, columnspan=4, sticky="nw")

    #TEC - Def
    l_warm=Label(TEC,text="Warm up time (s)")
    t_warm=Text(TEC, width=6, height=1)
    l_logo = Label(TEC, text="Solo 640", font=("Helvetica", 16, "bold"))

    l_bp_title = Label(TEC, text="BP TEC", font=("Helvetica", 10, "bold"))
    l_bp_v = Label(TEC, text="Voltage(mV)")
    t_bp_v = Text(TEC, width=6, height=1)
    l_bp_c = Label(TEC, text="Current (mA)")
    t_bp_c = Text(TEC, width=6, height=1)
    l_bp_p = Label(TEC, text="P Gain")
    t_bp_p = Text(TEC, width=6, height=1)
    l_bp_i = Label(TEC, text="I Gain")
    t_bp_i = Text(TEC, width=6, height=1)
    l_bp_sat = Label(TEC, text="Set temperature (C)")
    t_bp_sat = Text(TEC, width=6, height=1)
    l_bp_act = Label(TEC, text="Actual temperature (C)")
    t_bp_act = Label(TEC, width=6, height=1, text="21.2", fg="green")

    l_ld_title = Label(TEC, text="LD TEC", font=("Helvetica", 10, "bold"))
    l_ld_v = Label(TEC, text="Voltage(mV)")
    t_ld_v = Text(TEC, width=6, height=1)
    l_ld_c = Label(TEC, text="Current (mA)")
    t_ld_c = Text(TEC, width=6, height=1)
    l_ld_p = Label(TEC, text="P Gain")
    t_ld_p = Text(TEC, width=6, height=1)
    l_ld_i = Label(TEC, text="I Gain")
    t_ld_i = Text(TEC, width=6, height=1)
    l_ld_sat = Label(TEC, text="Set temperature (C)")
    t_ld_sat = Text(TEC, width=6, height=1)
    l_ld_act = Label(TEC, text="Actual temperature (C)")
    t_ld_act = Label(TEC, width=6, height=1, text="29.2", fg="red")

    l_nlc1_title = Label(TEC, text="NLC1 TEC", font=("Helvetica", 10, "bold"))
    l_nlc1_v = Label(TEC, text="Voltage(mV)")
    t_nlc1_v = Text(TEC, width=6, height=1)
    l_nlc1_c = Label(TEC, text="Current (mA)")
    t_nlc1_c = Text(TEC, width=6, height=1)
    l_nlc1_p = Label(TEC, text="P Gain")
    t_nlc1_p = Label(TEC, width=6, height=1, text="1.16")
    l_nlc1_i = Label(TEC, text="I Gain")
    t_nlc1_i = Label(TEC, width=6, height=1, text="1.2E-4")
    l_nlc1_sat = Label(TEC, text="Set temperature (C)")
    t_nlc1_sat = Text(TEC, width=6, height=1)
    l_nlc1_act = Label(TEC, text="Actual temperature (C)")
    t_nlc1_act = Label(TEC, width=6, height=1, text="23.4", fg="green")

    l_nlc2_title = Label(TEC, text="NLC2 TEC", font=("Helvetica", 10, "bold"))
    l_nlc2_v = Label(TEC, text="Voltage(mV)")
    t_nlc2_v = Text(TEC, width=6, height=1)
    l_nlc2_c = Label(TEC, text="Current (mA)")
    t_nlc2_c = Text(TEC, width=6, height=1)
    l_nlc2_p = Label(TEC, text="P Gain")
    t_nlc2_p = Text(TEC, width=6, height=1)
    l_nlc2_i = Label(TEC, text="I Gain")
    t_nlc2_i = Text(TEC, width=6, height=1)
    l_nlc2_sat = Label(TEC, text="Set temperature (C)")
    t_nlc2_sat = Text(TEC, width=6, height=1)
    l_nlc2_act = Label(TEC, text="Actual temperature (C)")
    t_nlc2_act = Label(TEC, width=6, height=1, text="20.6", fg="green")

    #TEC - Grid
    l_warm.grid(row=1, column=1, sticky="senw", pady=10)
    t_warm.grid(row=1, column=2, sticky="senw", pady=10)
    l_logo.grid(row=1, column=7, columnspan=4, sticky="e", pady=5)
    geths(TEC).grid(row=2, column=1, columnspan=11, sticky="we", pady=5)

    l_bp_title.grid(row=3, column=1, columnspan=2, sticky="nw", pady=2)
    l_bp_v.grid(row=4, column=1, sticky="nw", pady=2)
    t_bp_v.grid(row=4, column=2, sticky="nw", pady=2)
    l_bp_c.grid(row=5, column=1, sticky="nw", pady=2)
    t_bp_c.grid(row=5, column=2, sticky="nw", pady=2)
    l_bp_p.grid(row=6, column=1, sticky="nw", pady=2)
    t_bp_p.grid(row=6, column=2, sticky="nw", pady=2)
    l_bp_i.grid(row=7, column=1, sticky="nw", pady=2)
    t_bp_i.grid(row=7, column=2, sticky="nw", pady=2)
    l_bp_sat.grid(row=8, column=1, sticky="nw", pady=2)
    t_bp_sat.grid(row=8, column=2, sticky="nw", pady=2)
    l_bp_act.grid(row=9, column=1, sticky="nw", pady=2)
    t_bp_act.grid(row=9, column=2, sticky="nw", pady=2)
    getvs(TEC).grid(row=2, column=3, rowspan=8, sticky="ns", padx=10)

    l_ld_title.grid(row=3, column=4, columnspan=2, sticky="nw", pady=2)
    l_ld_v.grid(row=4, column=4, sticky="nw", pady=2)
    t_ld_v.grid(row=4, column=5, sticky="nw", pady=2)
    l_ld_c.grid(row=5, column=4, sticky="nw", pady=2)
    t_ld_c.grid(row=5, column=5, sticky="nw", pady=2)
    l_ld_p.grid(row=6, column=4, sticky="nw", pady=2)
    t_ld_p.grid(row=6, column=5, sticky="nw", pady=2)
    l_ld_i.grid(row=7, column=4, sticky="nw", pady=2)
    t_ld_i.grid(row=7, column=5, sticky="nw", pady=2)
    l_ld_sat.grid(row=8, column=4, sticky="nw", pady=2)
    t_ld_sat.grid(row=8, column=5, sticky="nw", pady=2)
    l_ld_act.grid(row=9, column=4, sticky="nw", pady=2)
    t_ld_act.grid(row=9, column=5, sticky="nw", pady=2)
    getvs(TEC).grid(row=2, column=6, rowspan=8, sticky="ns", padx=10)

    l_nlc1_title.grid(row=3, column=7, columnspan=2, sticky="nw", pady=2)
    l_nlc1_v.grid(row=4, column=7, sticky="nw", pady=2)
    t_nlc1_v.grid(row=4, column=8, sticky="nw", pady=2)
    l_nlc1_c.grid(row=5, column=7, sticky="nw", pady=2)
    t_nlc1_c.grid(row=5, column=8, sticky="nw", pady=2)
    l_nlc1_p.grid(row=6, column=7, sticky="nw", pady=2)
    t_nlc1_p.grid(row=6, column=8, sticky="nw", pady=2)
    l_nlc1_i.grid(row=7, column=7, sticky="nw", pady=2)
    t_nlc1_i.grid(row=7, column=8, sticky="nw", pady=2)
    l_nlc1_sat.grid(row=8, column=7, sticky="nw", pady=2)
    t_nlc1_sat.grid(row=8, column=8, sticky="nw", pady=2)
    l_nlc1_act.grid(row=9, column=7, sticky="nw", pady=2)
    t_nlc1_act.grid(row=9, column=8, sticky="nw", pady=2)
    getvs(TEC).grid(row=2, column=9, rowspan=8, sticky="ns", padx=10)

    l_nlc2_title.grid(row=3, column=10, columnspan=2, sticky="nw", pady=2)
    l_nlc2_v.grid(row=4, column=10, sticky="nw", pady=2)
    t_nlc2_v.grid(row=4, column=11, sticky="nw", pady=2)
    l_nlc2_c.grid(row=5, column=10, sticky="nw", pady=2)
    t_nlc2_c.grid(row=5, column=11, sticky="nw", pady=2)
    l_nlc2_p.grid(row=6, column=10, sticky="nw", pady=2)
    t_nlc2_p.grid(row=6, column=11, sticky="nw", pady=2)
    l_nlc2_i.grid(row=7, column=10, sticky="nw", pady=2)
    t_nlc2_i.grid(row=7, column=11, sticky="nw", pady=2)
    l_nlc2_sat.grid(row=8, column=10, sticky="nw", pady=2)
    t_nlc2_sat.grid(row=8, column=11, sticky="nw", pady=2)
    l_nlc2_act.grid(row=9, column=10, sticky="nw", pady=2)
    t_nlc2_act.grid(row=9, column=11, sticky="nw", pady=2)

    #Lock Definition
    l_pzt0_title = Label(Lock, text="PZT0 Settings", font=("Helvetica", 10, "bold"))
    l_pzt0_pd1l = Label(Lock, text="PD1 load")
    t_pzt0_pd1l = Text(Lock, width=6, height=1)
    l_pzt0_pd1s = Label(Lock, text="PD1 amplifier setting")
    t_pzt0_pd1s = Text(Lock, width=6, height=1)
    l_pzt0_pd2l = Label(Lock, text="PD2 load")
    t_pzt0_pd2l = Text(Lock, width=6, height=1)
    l_pzt0_pd2s = Label(Lock, text="PD2 amplifier setting")
    t_pzt0_pd2s = Text(Lock, width=6, height=1)
    l_pzt0_lppl = Label(Lock, text="LP photodiode load")
    t_pzt0_lppl = Text(Lock, width=6, height=1)
    l_pzt0_lpas = Label(Lock, text="LP amplifier setting")
    t_pzt0_lpas = Text(Lock, width=6, height=1)
    l_pzt0_lpcs = Label(Lock, text="LP calibration setting")
    t_pzt0_lpcs = Text(Lock, width=6, height=1)
    l_pzt0_lp = Label(Lock, text="Laser power (mW)")
    t_pzt0_lp = Text(Lock, width=6, height=1)
    l_pzt0_cmin = Label(Lock, text="Conditional min (mV)")
    t_pzt0_cmin = Text(Lock, width=6, height=1)
    l_pzt0_cmax = Label(Lock, text="Conditional max (mV)")
    t_pzt0_cmax = Text(Lock, width=6, height=1)
    l_pzt0_offset = Label(Lock, text="Offset (mV)")
    t_pzt0_offset = Text(Lock, width=6, height=1)
    l_pzt0_clp = Label(Lock, text="P gain")
    t_pzt0_clp = Text(Lock, width=6, height=1)
    l_pzt0_cli = Label(Lock, text="I gain")
    t_pzt0_cli = Text(Lock, width=6, height=1)
    l_pzt0_adelay = Label(Lock, text="Activation delay (s)")
    t_pzt0_adelay = Text(Lock, width=6, height=1)
    l_pzt0_parkp = Label(Lock, text="Park position (V)")
    t_pzt0_parkp = Text(Lock, width=12, height=1)
    l_pzt0_actv = Label(Lock, text="Actual voltage (V)")
    t_pzt0_actv = Label(Lock, width=12, height=1, text="12.4")
    l_pzt0_acts = Label(Lock, text="Actual signal (mV)")
    t_pzt0_acts = Label(Lock, width=12, height=1, text="12.4")

    l_pzt1_title = Label(Lock, text="PZT1 Settings", font=("Helvetica", 10, "bold"))
    l_pzt1_pd1l = Label(Lock, text="PD1 load")
    t_pzt1_pd1l = Text(Lock, width=6, height=1)
    l_pzt1_pd1s = Label(Lock, text="PD1 amplifier setting")
    t_pzt1_pd1s = Text(Lock, width=6, height=1)
    l_pzt1_pd2l = Label(Lock, text="PD2 load")
    t_pzt1_pd2l = Text(Lock, width=6, height=1)
    l_pzt1_pd2s = Label(Lock, text="PD2 amplifier setting")
    t_pzt1_pd2s = Text(Lock, width=6, height=1)
    l_pzt1_lppl = Label(Lock, text="LP photodiode load")
    t_pzt1_lppl = Text(Lock, width=6, height=1)
    l_pzt1_lpas = Label(Lock, text="LP amplifier setting")
    t_pzt1_lpas = Text(Lock, width=6, height=1)
    l_pzt1_lpcs = Label(Lock, text="LP calibration setting")
    t_pzt1_lpcs = Text(Lock, width=6, height=1)
    l_pzt1_lp = Label(Lock, text="Laser power (mW)")
    t_pzt1_lp = Text(Lock, width=6, height=1)
    l_pzt1_cmin = Label(Lock, text="Conditional min (mV)")
    t_pzt1_cmin = Text(Lock, width=6, height=1)
    l_pzt1_cmax = Label(Lock, text="Conditional max (mV)")
    t_pzt1_cmax = Text(Lock, width=6, height=1)
    l_pzt1_offset = Label(Lock, text="Offset (mV)")
    t_pzt1_offset = Text(Lock, width=6, height=1)
    l_pzt1_clp = Label(Lock, text="P gain")
    t_pzt1_clp = Text(Lock, width=6, height=1)
    l_pzt1_cli = Label(Lock, text="I gain")
    t_pzt1_cli = Text(Lock, width=6, height=1)
    l_pzt1_adelay = Label(Lock, text="Activation delay (s)")
    t_pzt1_adelay = Text(Lock, width=6, height=1)
    l_pzt1_parkp = Label(Lock, text="Park position (V)")
    t_pzt1_parkp = Text(Lock, width=12, height=1)
    l_pzt1_actv = Label(Lock, text="Actual voltage (V)")
    t_pzt1_actv = Label(Lock, width=12, height=1, text="12.4")
    l_pzt1_acts = Label(Lock, text="Actual signal (mV)")
    t_pzt1_acts = Label(Lock, width=12, height=1, text="12.3")

    l_pzt0_control = Label(Lock, text="PZT0 Control", font=("Helvetica", 10, "bold"))
    b_pzt0_lock= Button(Lock, text="Lock", width=15)
    b_pzt0_scan=Button(Lock, text="Scan",bg="grey", fg="black", width=15)
    b_pzt0_park=Button(Lock, text="Park",bg="orange", fg="white", width=15)
    #b_pzt0_ok=Button(Lock, text="Ok", width=5)

    l_pzt1_control = Label(Lock, text="PZT1 Control", font=("Helvetica", 10, "bold"))
    b_pzt1_lock= Button(Lock, text="Lock", width=15)
    b_pzt1_scan=Button(Lock, text="Scan",bg="grey", fg="black", width=15)
    b_pzt1_park=Button(Lock, text="Park",bg="orange", fg="white", width=15)
    #b_pzt1_ok = Button(Lock, text="Ok", width=5)

    #Lock grid

    l_pzt0_title.grid(row=2, column=1, columnspan=2, sticky="nw", pady=2)
    l_pzt0_pd1l.grid(row=3, column=1, columnspan=1, sticky="nw", pady=2)
    t_pzt0_pd1l.grid(row=3, column=2, columnspan=1, sticky="nw", pady=2)
    l_pzt0_pd1s.grid(row=4, column=1, columnspan=1, sticky="nw", pady=2)
    t_pzt0_pd1s.grid(row=4, column=2, columnspan=1, sticky="nw", pady=2)
    l_pzt0_pd2l.grid(row=5, column=1, columnspan=1, sticky="nw", pady=2)
    t_pzt0_pd2l.grid(row=5, column=2, columnspan=1, sticky="nw", pady=2)
    l_pzt0_pd2s.grid(row=6, column=1, columnspan=1, sticky="nw", pady=2)
    t_pzt0_pd2s.grid(row=6, column=2, columnspan=1, sticky="nw", pady=2)
    l_pzt0_lppl.grid(row=7, column=1, columnspan=1, sticky="nw", pady=2)
    t_pzt0_lppl.grid(row=7, column=2, columnspan=1, sticky="nw", pady=2)
    l_pzt0_lpas.grid(row=8, column=1, columnspan=1, sticky="nw", pady=2)
    t_pzt0_lpas.grid(row=8, column=2, columnspan=1, sticky="nw", pady=2)
    l_pzt0_lpcs.grid(row=9, column=1, columnspan=1, sticky="nw", pady=2)
    t_pzt0_lpcs.grid(row=9, column=2, columnspan=1, sticky="nw", pady=2)
    l_pzt0_lp.grid(row=10, column=1, columnspan=1, sticky="nw", pady=2)
    t_pzt0_lp.grid(row=10, column=2, columnspan=1, sticky="nw", pady=2)
    l_pzt0_cmin.grid(row=11, column=1, columnspan=1, sticky="nw", pady=2)
    t_pzt0_cmin.grid(row=11, column=2, columnspan=1, sticky="nw", pady=2)
    l_pzt0_cmax.grid(row=12, column=1, columnspan=1, sticky="nw", pady=2)
    t_pzt0_cmax.grid(row=12, column=2, columnspan=1, sticky="nw", pady=2)
    l_pzt0_offset.grid(row=13, column=1, columnspan=1, sticky="nw", pady=2)
    t_pzt0_offset.grid(row=13, column=2, columnspan=1, sticky="nw", pady=2)
    l_pzt0_clp.grid(row=14, column=1, columnspan=1, sticky="nw", pady=2)
    t_pzt0_clp.grid(row=14, column=2, columnspan=1, sticky="nw", pady=2)
    l_pzt0_cli.grid(row=15, column=1, columnspan=1, sticky="nw", pady=2)
    t_pzt0_cli.grid(row=15, column=2, columnspan=1, sticky="nw", pady=2)
    l_pzt0_adelay.grid(row=16, column=1, columnspan=1, sticky="nw", pady=2)
    t_pzt0_adelay.grid(row=16, column=2, columnspan=1, sticky="nw", pady=2)
    getvs(Lock).grid(row=1, column=3, rowspan=19, sticky="ns", padx=10)

    l_pzt1_title.grid(row=2, column=4, columnspan=2, sticky="nw", pady=2)
    l_pzt1_pd1l.grid(row=3, column=4, columnspan=1, sticky="nw", pady=2)
    t_pzt1_pd1l.grid(row=3, column=5, columnspan=1, sticky="nw", pady=2)
    l_pzt1_pd1s.grid(row=4, column=4, columnspan=1, sticky="nw", pady=2)
    t_pzt1_pd1s.grid(row=4, column=5, columnspan=1, sticky="nw", pady=2)
    l_pzt1_pd2l.grid(row=5, column=4, columnspan=1, sticky="nw", pady=2)
    t_pzt1_pd2l.grid(row=5, column=5, columnspan=1, sticky="nw", pady=2)
    l_pzt1_pd2s.grid(row=6, column=4, columnspan=1, sticky="nw", pady=2)
    t_pzt1_pd2s.grid(row=6, column=5, columnspan=1, sticky="nw", pady=2)
    l_pzt1_lppl.grid(row=7, column=4, columnspan=1, sticky="nw", pady=2)
    t_pzt1_lppl.grid(row=7, column=5, columnspan=1, sticky="nw", pady=2)
    l_pzt1_lpas.grid(row=8, column=4, columnspan=1, sticky="nw", pady=2)
    t_pzt1_lpas.grid(row=8, column=5, columnspan=1, sticky="nw", pady=2)
    l_pzt1_lpcs.grid(row=9, column=4, columnspan=1, sticky="nw", pady=2)
    t_pzt1_lpcs.grid(row=9, column=5, columnspan=1, sticky="nw", pady=2)
    l_pzt1_lp.grid(row=10, column=4, columnspan=1, sticky="nw", pady=2)
    t_pzt1_lp.grid(row=10, column=5, columnspan=1, sticky="nw", pady=2)
    l_pzt1_cmin.grid(row=11, column=4, columnspan=1, sticky="nw", pady=2)
    t_pzt1_cmin.grid(row=11, column=5, columnspan=1, sticky="nw", pady=2)
    l_pzt1_cmax.grid(row=12, column=4, columnspan=1, sticky="nw", pady=2)
    t_pzt1_cmax.grid(row=12, column=5, columnspan=1, sticky="nw", pady=2)
    l_pzt1_offset.grid(row=13, column=4, columnspan=1, sticky="nw", pady=2)
    t_pzt1_offset.grid(row=13, column=5, columnspan=1, sticky="nw", pady=2)
    l_pzt1_clp.grid(row=14, column=4, columnspan=1, sticky="nw", pady=2)
    t_pzt1_clp.grid(row=14, column=5, columnspan=1, sticky="nw", pady=2)
    l_pzt1_cli.grid(row=15, column=4, columnspan=1, sticky="nw", pady=2)
    t_pzt1_cli.grid(row=15, column=5, columnspan=1, sticky="nw", pady=2)
    l_pzt1_adelay.grid(row=16, column=4, columnspan=1, sticky="nw", pady=2)
    t_pzt1_adelay.grid(row=16, column=5, columnspan=1, sticky="nw", pady=2)


    getvs(Lock).grid(row=1, column=6, rowspan=19, sticky="ns", padx=10)

    l_pzt0_control.grid(row=2, column=7, columnspan=3, sticky="nw", pady=2)
    b_pzt0_lock.grid(row=3, column=7, columnspan=1, sticky="nw", pady=2, padx=2)
    b_pzt0_scan.grid(row=3, column=8, columnspan=1, sticky="nw", pady=2, padx=2)
    b_pzt0_park.grid(row=4, column=9, columnspan=1, sticky="nw", pady=5, padx=2)

    l_pzt1_parkp.grid(row=4, column=7, columnspan=1, sticky="nw", pady=7)
    t_pzt1_parkp.grid(row=4, column=8, columnspan=1, sticky="nw", pady=7)
    #b_pzt0_ok.grid(row=4, column=9, columnspan=1, sticky="nw", pady=2)
    l_pzt1_actv.grid(row=5, column=7, columnspan=1, sticky="nw", pady=2)
    t_pzt1_actv.grid(row=5, column=8, columnspan=1, sticky="nw", pady=2)
    l_pzt1_acts.grid(row=6, column=7, columnspan=1, sticky="nw", pady=2)
    t_pzt1_acts.grid(row=6, column=8, columnspan=1, sticky="nw", pady=2)

    l_pzt1_control.grid(row=7, column=7, columnspan=3, sticky="nw", pady=2)
    b_pzt1_lock.grid(row=8, column=7, columnspan=1, sticky="nw", pady=2, padx=2)
    b_pzt1_scan.grid(row=8, column=8, columnspan=1, sticky="nw", pady=2, padx=2)
    b_pzt1_park.grid(row=9, column=9, columnspan=1, sticky="nw", pady=5, padx=2)

    l_pzt0_parkp.grid(row=9, column=7, columnspan=1, sticky="nw", pady=7)
    t_pzt0_parkp.grid(row=9, column=8, columnspan=1, sticky="nw", pady=7)
    #b_pzt1_ok.grid(row=4, column=9, columnspan=1, sticky="nw", pady = 2)
    l_pzt0_actv.grid(row=10, column=7, columnspan=1, sticky="nw", pady=2)
    t_pzt0_actv.grid(row=10, column=8, columnspan=1, sticky="nw", pady=2)
    l_pzt0_acts.grid(row=11, column=7, columnspan=1, sticky="nw", pady=2)
    t_pzt0_acts.grid(row=11, column=8, columnspan=1, sticky="nw", pady=2)



    #Advanced definition

    l_adv_device = Label(Advanced, text="Device summary", font=("Helvetica", 10, "bold"))
    l_adv_model = Label(Advanced, text="Model ID:")
    t_adv_model = Label(Advanced, text="Solo 640")
    l_adv_date = Label(Advanced, text="Date of manufacture:")
    t_adv_date = Label(Advanced, text="06/06/2019")
    l_adv_serial = Label(Advanced, text="Serial number:")
    t_adv_serial = Label(Advanced, text="122234")
    l_adv_power = Label(Advanced, text="Output power (mW):")
    t_adv_power = Label(Advanced, text="1000")
    l_adv_wavelength = Label(Advanced, text="Wavelength (nm):")
    t_adv_wavelength = Label(Advanced, text="640")

    #Advanced grid

    l_adv_device.grid(row=2, column=1, columnspan=2, sticky="nw", pady=5)
    l_adv_model.grid(row=3, column=1, columnspan=1, sticky="nw", pady=5)
    t_adv_model.grid(row=3, column=2, columnspan=1, sticky="ne", pady=5)
    l_adv_date.grid(row=4, column=1, columnspan=1, sticky="nw", pady=5)
    t_adv_date.grid(row=4, column=2, columnspan=1, sticky="ne", pady=5)
    l_adv_serial.grid(row=5, column=1, columnspan=1, sticky="nw", pady=5)
    t_adv_serial.grid(row=5, column=2, columnspan=1, sticky="ne", pady=5)
    l_adv_power.grid(row=6, column=1, columnspan=1, sticky="nw", pady=5)
    t_adv_power.grid(row=6, column=2, columnspan=1, sticky="ne", pady=5)
    l_adv_wavelength.grid(row=7, column=1, columnspan=1, sticky="nw", pady=5)
    t_adv_wavelength.grid(row=7, column=2, columnspan=1, sticky="ne", pady=5)

def geths(parent):
        hs = ttk.Separator(parent, orient=HORIZONTAL)
        return hs

def getvs(parent):
        vs = ttk.Separator(parent, orient=VERTICAL)
        return vs

#Definition of variables

Unik = PhotoImage(file="unik.png")
l_unik = Label(image=Unik)

l_detect=Label(gui, text="Laserhead detected", font=("Helvetica", 9, "italic"), fg="grey")
l_info=Label(gui, text="Solo 640", font=("Helvetica", 20, "bold"))
l_serial=Label(gui, text="S/N: 122234", font=("Helvetica", 9, "italic"), fg="grey")
l_power=Label(gui, text="Power up")
l_tec=Label(gui, text="TEC init")
l_laser=Label(gui, text="Laser init")
l_lock=Label(gui, text="Lock status")
l_error=Label(gui, text="Error")
l_messages=Label(gui, text="Messages", anchor="e")
l_pump_power=Label(gui, text="Pump current (mA)")
l_pump_power_actual=Label(gui, text="Actual: 3200 (mA)", fg="green", font=("Helvetica", 8))
l_bp_temp=Label(gui, text="Base plate temperature (C)")
l_ld_temp=Label(gui, text="Laser diode temperature (C)")
l_copy=Label(gui, text="All rights reserved")
l_bp_temp_actual=Label(gui, text="Actual: 24.3 (C)", fg="green", font=("Helvetica", 8))
l_ld_temp_actual=Label(gui, text="Actual: 24.7 (C)", fg="green", font=("Helvetica", 8))
l_nlc_temp=Label(gui, text="NLC1 Temperature (C)")
l_nlc_temp_actual=Label(gui, text="Actual: 27.4 (C)", fg="red", font=("Helvetica", 8))

c_power=Canvas(gui, bg="green", width=10, height=10)
c_tec=Canvas(gui, bg="green", width=10, height=10)
c_laser=Canvas(gui, bg="orange", width=10, height=10)
c_lock=Canvas(gui, bg="grey", width=10, height=10)
c_error=Canvas(gui, bg="grey", width=10, height=10)
c_message=Canvas(gui, bg="white", width=350, height=200)
c_message.create_text(110,30,font="Times 8 italic",
                        text=">> Power up initiated \n>> TEC started \n>> Temperature is stabilising, please wait..")

t_ppower=Text(gui, width=6, height=1)
t_ppower.insert(END, "1000")
t_pcurr=Text(gui, width=6, height=1)
t_pcurr.insert(END, "1000")
t_ttemp=Text(gui, width=6, height=1)
t_ttemp.insert(END, "1000")

b_lon=Button(gui, text="Laser on", bg="green", fg="white")
b_loff=Button(gui, text="Laser off",bg="red", fg="white")
b_lock=Button(gui, text="Lock on", fg="black")
b_more=Button(gui, text="More", command=newwin, width=20)

#Grid - Info pan
l_unik.grid(row=1, column=1, columnspan=4, rowspan=2)
l_detect.grid(row=4, column=1, columnspan=4, rowspan=2, sticky="nw")
geths(gui).grid(row=5, column=1, columnspan=10, sticky="we")
l_info.grid(row=2, column=7, columnspan=4, rowspan=1, sticky="ne")
l_serial.grid(row=3, column=7, columnspan=4, rowspan=2, sticky="ne")

#Indicator pan
l_power.grid(row=6, column=1, columnspan=2, rowspan=1, sticky="nw")
c_power.grid(row=6, column=3, columnspan=1, rowspan=1, sticky="w")
l_tec.grid(row=7, column=1, columnspan=2, rowspan=1, sticky="nw")
c_tec.grid(row=7, column=3, columnspan=1, rowspan=1, sticky="w")
l_laser.grid(row=8, column=1, columnspan=2, rowspan=1, sticky="nw")
c_laser.grid(row=8, column=3, columnspan=1, rowspan=1, sticky="w")
l_lock.grid(row=9, column=1, columnspan=2, rowspan=1, sticky="nw")
c_lock.grid(row=9, column=3, columnspan=1, rowspan=1, sticky="w")
l_error.grid(row=10, column=1, columnspan=2, rowspan=1, sticky="nw")
c_error.grid(row=10, column=3, columnspan=1, rowspan=1, sticky="w")

#Buttons
b_lon.grid(row=11, column=1, columnspan=4, rowspan=2, sticky="nwse", padx=5, pady=(2,0))
b_loff.grid(row=14, column=1, columnspan=2, rowspan=2, sticky="nwse", padx=5)
geths(gui).grid(row=13, column=1, rowspan=2, columnspan=4, sticky="we", pady=(0,8), padx=5)
b_lock.grid(row=14, column=3, columnspan=2, rowspan=2, sticky="nwse", padx=5)
b_more.grid(row=14, column=7, columnspan=4, rowspan=2, sticky="ne")

#Actual controls
l_pump_power.grid(row=6, column=7, columnspan=2, rowspan=1, sticky="nw")
#t_ppower.grid(row=7, column=7, columnspan=1, rowspan=2, sticky="nw")
l_pump_power_actual.grid(row=7, column=7, columnspan=1, rowspan=1, sticky="nw")


l_bp_temp.grid(row=8, column=7, columnspan=2, rowspan=1, sticky="nw")
#t_ttemp.grid(row=11, column=7, columnspan=1, rowspan=2, sticky="nw", pady=(0,30))
l_bp_temp_actual.grid(row=9, column=7, columnspan=1, rowspan=1, sticky="nw")

l_ld_temp.grid(row=10, column=7, columnspan=2, rowspan=1, sticky="nw")
#t_ttemp.grid(row=11, column=7, columnspan=1, rowspan=2, sticky="nw", pady=(0,30))
l_ld_temp_actual.grid(row=11, column=7, columnspan=1, rowspan=1, sticky="nw")

l_nlc_temp.grid(row=12, column=7, columnspan=2, rowspan=1, sticky="nw")
#t_pcurr.grid(row=9, column=7, columnspan=1, rowspan=2, sticky="nw")
l_nlc_temp_actual.grid(row=13, column=7, columnspan=1, rowspan=1, sticky="nw")


#Messages pan
geths(gui).grid(row=16, column=1, rowspan=2, columnspan=10, sticky="ewns", pady=10)
l_messages.grid(row=18, column=1, columnspan=10, rowspan=2, sticky="nw")
c_message.grid(row=20, column=1, columnspan=10, rowspan=4)
l_copy.grid(row=24, column=1, columnspan=10, rowspan=2)

gui.mainloop()
