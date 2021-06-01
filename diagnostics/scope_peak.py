from scipy.signal import find_peaks
import ast
import os
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#directory = r'C:\Users\Ben\OneDrive - Mrs\Unik_GUI\scope'
#directory = r'D:\scope long run 0.05 0.5 with vbg\scope'

mih1 = r'D:\scope long run 0.05 0.5 with vbg'
mih2 = r'D:\scope new mih vbg 0.1 1 3.36'
mih3 = r'D:\scope new mih vbg 0.1 1.2 3.66'
mih4 = r'C:\Users\Ben\OneDrive - Mrs\Unik_GUI\scope'

directory = [mih1, mih2, mih3, mih4]

TEC_c = [[] for i in range(len(directory))]
RAMP_c = [[] for i in range(len(directory))]
PEAK_c = [[] for i in range(len(directory))]
i=0
for item in directory:
    k=0
    for filename in os.listdir(item):
        if "TEC" in filename:
            #print(filename)

            if filename[9] == "R":
                TEC = filename[3:8]
            if filename[8] == "R":
                TEC = filename[3:7]
            if filename[7] == "R":
                TEC = filename[3:6]

            if filename[-5] == "P":
                RAMP = filename[-4:]
            else:
                RAMP = filename[-5:]

            file2write = open(item + '/' + filename, 'r')
            data = ast.literal_eval(file2write.read())
            file2write.close()

            scale = max(data)*0.05
            #
            # if i == 0:
            #     scale = 0.04
            #
            # if i == 1:
            #     scale = 0.15

            #fig = plt.Figure(figsize=(7, 5), dpi=100)


            peak = find_peaks(data, height=scale, distance=10)
            peaks = [[] for i in range(2)]
            peaks = list(zip(np.ndarray.tolist(peak[0]),np.ndarray.tolist(peak[1]["peak_heights"])))
            peaks.sort(key=lambda x: x[1], reverse=True)

            #print(peaks)

            if len(peaks) > 1:
                if peaks[0][0] > peaks[1][0]:
                    peaks[0], peaks[1] = peaks[1], peaks[0]

                data[peaks[0][0]:peaks[1][0]]
                peak = find_peaks(data, height=scale, distance=10)
            x = np.linspace(0, 10, len(data))

            #peak = peak[peak[4].argsort()[::-1]]
            peak_number = len(peak[0])
            #print(peak_number)
            # peak_diff = [b - a for a, b in zip(peak[0], peak[0][1:])]
            # if peak_diff == []:
            #     peak_diff = 770

            TEC_c[i].append(float(TEC))
            RAMP_c[i].append(float(RAMP))
            PEAK_c[i].append(peak_number)

            if peak_number < 6:
                k += 1
            #PEAK_c.append(abs(770-np.mean(peak_diff)))
            #PEAK_c.append(-abs(350-np.mean(peak_diff)))
            #print(peak_diff)
    print(k / len(PEAK_c[i]))
    i+=1




#Axes3D.plot_surface(TEC_c, RAMP_c, PEAK_c)
# unq, ids, count = np.unique(TEC_c, return_inverse=True, return_counts=True)
# print(ids)
# print(unq)
# out_signal = np.column_stack((unq/10, np.bincount(ids, PEAK_c) / count))
#plt.clf()

fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1, projection='3d')
ax2 = fig.add_subplot(2, 2, 2, projection='3d')
ax3 = fig.add_subplot(2, 2, 3, projection='3d')
ax4 = fig.add_subplot(2, 2, 4, projection='3d')

axis =[ax1,ax2,ax3,ax4]
colormap=["Greens_r","Blues_r","Oranges_r", "Reds_r" ]
# ax = plt.axes(projection='3d')
# ax = plt.subplot(2,2,1)


ax1.title.set_text("MIH 2.16 MODE DISTRIBUTION")
ax2.title.set_text("MIH 3.36 MODE DISTRIBUTION")
ax3.title.set_text("MIH 4.1 MODE DISTRIBUTION")
ax4.title.set_text("MIH 3.66 MODE DISTRIBUTION")

i=0
for item in axis:
    item.set_xlabel('TEC')
# plt.xaxis.set_label_position('top')
    item.set_ylabel('RAMP')
# plt.plot(x, data, label="Frequency amplitude")
# plt.plot(x, np.multiply(pzt,0.05), label="Ramp amplitude")
    item.scatter3D(TEC_c[i], RAMP_c[i], PEAK_c[i], c =PEAK_c[i], cmap = colormap[i])
    item.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
           fancybox=True, shadow=True, ncol=5)
    item.view_init(azim=-90, elev=0)
    item.set_xlim(30,45)
    item.set_zlim(0,20)
    i+=1

# print(len(unq))
# print(unq)
# print(len(out_signal))
# print(out_signal[:,1])
#plt.acorr(out_signal[:,1], maxlags=60)
#plt.xticks(np.linspace(-60,60,10), np.round(np.linspace(-60*0.1, 60*0.1, 10),2))
#plt.plot(unq, out_signal[:,1])

plt.show()

#plt.savefig("scope/adjusted/" + "TEC" + TEC + "RAMP" + RAMP + ".png")
