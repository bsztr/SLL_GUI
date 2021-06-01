from archive.ClientPanel_NAVY import *
from CONFIG import *


#Init

#GUI
if Globals.available==[]:
    Globals.available=runinit()
print("System is running")
Gui=ClientPanel_NAVY()
Gui.start()







