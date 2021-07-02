from ClientPanel import *
from COMM import *
from CONFIG import *
from tkinter.messagebox import showinfo


#Init
Globals.engineer = 0
#GUI
if Globals.available==[]:
    Globals.available=runinit()
if "failed" in Globals.available:
    showinfo("Initialisation failed", f"Driver code:\n{Globals.available}")
    setvalue(control['address'], 0)
else:
    print("System is running")
    Gui=ClientPanel()
    Gui.start()









