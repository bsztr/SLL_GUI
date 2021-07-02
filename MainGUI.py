from MainPanel import *
from COMM import *
from CONFIG import *
import Globals
from tkinter.messagebox import showinfo

#Init

#GUI
Globals.engineer = 1
if Globals.available==[]:
    Globals.available=runinit()
if "failed" in Globals.available:
    showinfo("Initialisation failed", f"Driver code:\n{Globals.available}")
    setvalue(control['address'], 0)
else:
    #print("System is running")
    Gui=MainPanel()
    Gui.start()







