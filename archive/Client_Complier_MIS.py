#Complier.py
import sys, os
from cx_Freeze import setup, Executable

__version__ = "1.0.1"

include_files = ['unik.png', "unik.ico", "tcl86t.dll", "tk86t.dll", "dict"]
excludes = ["MainGUI"]
packages = ["tkinter","serial", "serial.tools.list_ports", "re", "decimal", "ctypes", "struct", "binascii", "matplotlib", "pandas", "math", "queue", "threading", "time", "datetime", "csv", "os", "numpy", "codecs", "json"]

os.environ['TCL_LIBRARY'] = r'C:\Users\Ben\AppData\Local\Programs\Python\Python37\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Ben\AppData\Local\Programs\Python\Python37\tcl\tk8.6'

setup(
    name = "UniKLasers GUI Client 1.0.1",
    description='Graphical user interface for UniKLasers',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'excludes': excludes,
    'include_msvcr': True,
}},
executables = [Executable("ClientGUI_MIS.py",base="Win32GUI", shortcutName="UniKLasers Client",
            shortcutDir="DesktopFolder", icon="unik.ico")],
data_files = [('C:\\Windows\\Fonts', ['font/Proxima Nova Alt Light.otf']), ('C:\\Windows\\Fonts', ['font/Proxima Nova Alt Thin.otf']), ('C:\\Windows\\Fonts', ['font/Proxima Nova Black.otf']),
              ('C:\\Windows\\Fonts', ['font/Proxima Nova Thin.otf']), ('C:\\Windows\\Fonts', ['font/ProximaNova-Regular.otf'])]
)

##python Client_Complier.py bdist_msi