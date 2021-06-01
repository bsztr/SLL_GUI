#Complier.py
import sys, os
from cx_Freeze import setup, Executable

__version__ = "1.0.2"

include_files = ['unik.png', "unik.ico", "tcl86t.dll", "tk86t.dll", "dict"]
excludes = ["MainGUI", "scope", "scope_ana_ramp", "scope_analysis","scope_peak", "trail2"]
packages = ["tkinter","serial", "serial.tools.list_ports", "re", "ctypes", "decimal", "struct", "binascii", "matplotlib", "pandas", "math", "queue", "threading", "time", "datetime", "csv", "os", "numpy", "codecs", "json"]

os.environ['TCL_LIBRARY'] = r'C:\Users\Ben\AppData\Local\Programs\Python\Python37\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Ben\AppData\Local\Programs\Python\Python37\tcl\tk8.6'

setup(
    name = "UniKLasers GUI Client NAVY",
    description='Graphical user interface for UniKLasers, prepared for NAVY S-640',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'excludes': excludes,
    'include_msvcr': True,
}},
executables = [Executable("ClientGUI_NAVY.py",base="Win32GUI", shortcutName="UniKLasers Client NAVY",
            shortcutDir="DesktopFolder", icon="unik.ico")],
data_files = [('C:\\Windows\\Fonts', ['font/Proxima Nova Alt Light.otf']), ('C:\\Windows\\Fonts', ['font/Proxima Nova Alt Thin.otf']), ('C:\\Windows\\Fonts', ['font/Proxima Nova Black.otf']),
              ('C:\\Windows\\Fonts', ['font/Proxima Nova Thin.otf']), ('C:\\Windows\\Fonts', ['font/ProximaNova-Regular.otf'])]
)

##python Client_Complier_NAVY.py bdist_msi