#Complier.py
import sys, os
from cx_Freeze import setup, Executable
import Globals

__version__ = Globals.guiver

include_files = ['Skyrlogo.png', "skyico.ico", "tcl86t.dll", "tk86t.dll", "dict"]
excludes = [""]
packages = ["tkinter", "serial", "sys", "hashlib", "stm32loader.main","serial.tools.list_ports", "decimal", "re", "ctypes", "struct", "binascii", "matplotlib", "pandas", "math", "queue", "threading", "time", "datetime", "csv", "os", "numpy", "codecs", "json"]

os.environ['TCL_LIBRARY'] = r'C:\Users\Ben\AppData\Local\Programs\Python\Python37\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Ben\AppData\Local\Programs\Python\Python37\tcl\tk8.6'

setup(
    name = "Skylark ENG",
    description='Graphical user interface for Skylark',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'excludes': excludes,
    'include_msvcr': True
}},
executables = [Executable("MainGUI.py", base="Win32GUI", shortcutName="Skylark",
            shortcutDir="DesktopFolder", icon="skyico.ico")]
)
#('C:\\Windows\\Fonts', ['font\\Jost-Light.ttf']),('C:\\Windows\\Fonts', ['font\\Jost-Thin.ttf']),('C:\\Windows\\Fonts', ['font\\Jost-Regular.ttf'])
##python Main_Complier.py bdist_msi