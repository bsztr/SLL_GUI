#Complier.py
import sys, os
from cx_Freeze import setup, Executable
import Globals

__version__ = Globals.guiver

include_files = ['Skyrlogo.png', "skyico.ico", "tcl86t.dll", "tk86t.dll", "dict", "DLLs/"]
excludes = ["MainGUI", "scope", "scope_ana_ramp", "scope_analysis","scope_peak", "trail2"]
packages = ["tkinter","serial", "tkinter.messagebox", "sys", "clr","hashlib", "stm32loader.main","serial.tools.list_ports", "decimal", "re", "ctypes", "struct", "binascii", "matplotlib", "pandas", "math", "queue", "threading", "time", "datetime", "csv", "os", "numpy", "codecs", "json"]

os.environ['TCL_LIBRARY'] = r'C:\Users\Ben\AppData\Local\Programs\Python\Python37\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Ben\AppData\Local\Programs\Python\Python37\tcl\tk8.6'

setup(
    name = "Skylark GUI Client",
    description='Graphical user interface for Skylark',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'excludes': excludes,
    'include_msvcr': True,
}},
executables = [Executable("ClientGUI.py",base="Win32GUI", shortcutName="Skylark Client",
            shortcutDir="DesktopFolder", icon="skyico.ico")],
data_files = [('C:\\Windows\\Fonts', ['font/Proxima Nova Alt Light.otf']), ('C:\\Windows\\Fonts', ['font/Proxima Nova Alt Thin.otf']), ('C:\\Windows\\Fonts', ['font/Proxima Nova Black.otf']),
              ('C:\\Windows\\Fonts', ['font/Proxima Nova Thin.otf']), ('C:\\Windows\\Fonts', ['font/ProximaNova-Regular.otf'])]
)

##python Client_Complier.py bdist_msi