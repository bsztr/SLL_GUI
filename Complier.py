#Complier.py
import sys, os
from cx_Freeze import setup, Executable

__version__ = "0.0.1"

include_files = ['unik.png',"tcl86t.dll", "tk86t.dll"]
excludes = []
packages = ["tkinter","serial", "re", "ctypes", "struct", "binascii"]

os.environ['TCL_LIBRARY'] = r'C:\Users\Ben\AppData\Local\Programs\Python\Python37\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Ben\AppData\Local\Programs\Python\Python37\tcl\tk8.6'

setup(
    name = "Unik GUI",
    description='This is for PZT diagnosis',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'excludes': excludes,
    'include_msvcr': True,
}},
executables = [Executable("checkerror.py",base="Win32GUI", shortcutName="UNIK_GUI",
            shortcutDir="DesktopFolder",)]
)