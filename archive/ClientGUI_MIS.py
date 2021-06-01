from ClientPanel import *
from COMM import *
from CONFIG import *


#Init

#GUI
if Globals.available==[]:
    Globals.available=runinit()
print("System is running")
Gui=ClientPanel()
Gui.start()







