import tkinter as tk
import csv

class TEC0(tk.Frame):
    def __init__(self):


class CB(tk.Frame):
    def __init__(self):



    def dump(self, address):

        with open(address) as dump_file:
            dump_reader = csv.reader(dump_file, delimiter=',')
            for row in dump_reader:
                setvalue(row[0].lower()[2:], row[1].lower(), "u", "1")
        return "Dump is done"