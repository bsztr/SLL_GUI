# import tkinter as tk
# import serial
# import re
# import ctypes

Background={
    "main": "#ffffff",
    "submit": "#b2bec3",

    "alert": "#00b894"
}

fonts={
    "main": ("Proxima Nova Rg", 10),
}

ser = serial.Serial(
    port="COM4",
    baudrate=57600,
    parity=serial.PARITY_NONE,
    stopbits=1,
    bytesize=8,
    timeout=5
)

def getvalue(address):
    arg="0x"+str(address.lower())
    ser.write(("GET$"+arg+chr(13)).encode())
    result = dict()
    reply = str(ser.read(29))
    hex = re.findall(r'0x[0-9A-F]+', reply, re.I)
    if "OK" in reply:
        result['success']=1
        if hex[0] == arg:
            result['valid'] = 1
        else:
            result['valid'] = 0
    else:
        result['success']=0
        result['valid']=0

    result['value'] = int(hex[1], 16)

    return result

def setvalue(address, val):

    arg="0x"+str(address.lower())
    ser.write(("SET$"+arg+"$0x"+val+chr(13)).encode())
    result = dict()
    reply = str(ser.read(7))
    if "OK" in reply:
        check=getvalue(address)
        print("Register set to " + str(check['value']))
        if check['value']==int(val,16):
            #Need to work out data type
            result['value']=int(val,16)
            #Need to convert to user defined value
            result['success']=1
        else:
            result['value']="error"
    else:
        result['value']="error"
        result['success']=0
    return result

# def comm_start():
#     ser.reset_output_buffer()
#     val=8
#     address="03fa"
#     val=ctypes.c_uint32(val).value
#     val="0x%08x" %val
#     arg="0x"+str(address.lower())
#     ser.write(("SET$"+arg+"$"+val+chr(13)).encode())
#     reply = str(ser.read(7))
#     return reply

def comm_init():
    setvalue("03fa", "00000008")
    ser.reset_output_buffer()
    ser.write(("RST" + chr(13)).encode())
    reply = str(ser.read(400).decode())
    setvalue("03fa", "00000000")
    return reply

def reset():
    target="ffffffff"
    if hex(getvalue("ffa0")['value'])[2:]!=target:
        setvalue("03fa", "00000008")
        setvalue("ffa0", target)
        setvalue("03fa", "00000000")

# def check_key(master):
#
#     master.withdraw()
#     win=tk.Toplevel()
#     l_info=tk.Label(win, text="Check key is in middle position. Press OK to continue.")
#     l_info.pack()
#     b_confirm=tk.Button(win, text="OK", command=win.destroy)
#     b_confirm.pack()
#     gui.wait_window(win)
#     master.update()
#     master.deiconify()

def update_main(self):
    result = round(getvalue('bff7')['value']/10e+2, 2)
    self.configure(text=str(result) + " (mA)", fg="black", font=fonts['main'],
                       bg=Background['main'])
    self.after(2000, lambda: update_main(self))

comm_init()

gui = tk.Tk()
gui.geometry("400x150")
gui.title("UniKLasers check error")
gui.configure(bg=Background['main'])

l_error=tk.Label(gui, text="Accumulated error", font=fonts['main'], bg=Background['main'])
b_error=tk.Button(gui, text="Reset", command=lambda: reset(), font=fonts['main'], bg=Background['alert'])

l_act = tk.Label(gui, text="Actual current (mA)", font=fonts['main'], bg=Background['main'])
s_act = tk.Label(gui, text="", font=fonts['main'], bg=Background['main'])
update_main(s_act)

l_disclaimer = tk.Label(gui, text="1) Ensure key is in the middle position (warm-up).\n" +
                                  "2) Press reset, then continue with power-up procedure.\n" +
                                  "3) Current readings should appear after warm-up.",
                        font=fonts['main'], bg=Background['main'])

b_reinit=tk.Button(gui, text="Reinitialise system", command=lambda: comm_init(), font=fonts['main'], bg=Background['submit'])

l_error.grid(row=1, column=1, columnspan=1, sticky="nw", pady=2)
b_error.grid(row=1, column=2, columnspan=2, sticky="nw", pady=2)

l_act.grid(row=2, column=1, columnspan=1, sticky="nw", pady=2)
s_act.grid(row=2, column=2, columnspan=2, sticky="nw", pady=2)

l_disclaimer.grid(row=3, column=1, columnspan=4, sticky="nw", pady=2)
b_reinit.grid(row=1, column=4, columnspan=2, sticky="nw", pady=2, padx=3)

gui.mainloop()





