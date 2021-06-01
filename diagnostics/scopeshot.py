from ds1054z import DS1054Z
import time
import matplotlib
matplotlib.use("QT5Agg")
import matplotlib.pyplot as plt
import numpy as np
import PyQt5
import os
import ast

# item = "230"
# #now = str(time.time())
# now =""
#
# scope = DS1054Z('169.254.89.41')
#
# diffa = scope.get_waveform_samples(1)
# diffb = scope.get_waveform_samples(2)
# ramp = scope.get_waveform_samples(4)
#
# file2write = open("screenshot/" + "DIFFA" + item + now, 'w')
# file2write.write(str(diffa))
# file2write.close()
#
# file2write2 = open("screenshot/" + "DIFFB" + item + now, 'w')
# file2write2.write(str(diffb))
# file2write2.close()
#
# file2write2 = open("screenshot/" + "RAMP" + item + now, 'w')
# file2write2.write(str(ramp))
# file2write2.close()
#
directory = r'C:\Users\Ben\OneDrive - Mrs\Unik_GUI\screenshot'
i=1
fig = plt.Figure(figsize=(7, 7), dpi=100)
plt.clf()
for filename in os.listdir(directory):
    if "RAMP" in filename:
        first = 10
        gain = filename[-3:]

        file2write = open("screenshot/DIFFA" + gain, 'r')
        ddiffa = ast.literal_eval(file2write.read())
        file2write.close()

        file2write = open("screenshot/DIFFB" + gain, 'r')
        ddiffb = ast.literal_eval(file2write.read())
        file2write.close()

        file2write = open("screenshot/RAMP" + gain, 'r')
        dramp = ast.literal_eval(file2write.read())
        file2write.close()

        error = [x1 - x2 for (x1, x2) in zip(ddiffa, ddiffb)]


        if i > 4:
            first = 20
        if first == 20:
            second = (i-4)
        else:
            second = i
        quant = i+ 420
        ax = fig.add_subplot(quant)

        fig.subplots_adjust(hspace=.5)
        #dramp = np.linspace(0, 1, len(dramp))
        #plt.clf()
        ax.set_title("Lock signal for gain at " + gain)
        #ax.xlabel('Voltage (V)')
        #plt.xaxis.set_label_position('top')
        #ax.ylabel('Amplitude (V)')
        ax.plot(dramp, ddiffa, label="DIFFA")
        #ax.plot(dramp, ddiffb, label="DiffB")
        #ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
        #               fancybox=True, shadow=True, ncol=5)
        i += 1
    fig.savefig("screenshot/images/" + "rammmm signal at "  + ".png")
