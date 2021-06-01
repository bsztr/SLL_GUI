from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib
from COMM import getvalue

class RegrMagic(object):

    def __init__(self):
        self.x = 0

    def __call__(self, address):
        #time.sleep(1)
        self.x=self.x+1
        self.y1 = getvalue(address, "u", "k")['value']
        self.y2 = getvalue(address, "u", "k")['value']-1
        return self.x, self.y1, self.y2
address="dfd4"
regr_magic = RegrMagic()

def frames():
    while True:
        yield regr_magic(address)

fig = plt.figure()
plt.axhline(y=25, color='r', linestyle='-', label="Set temperature")

x = []
y = []
z = []
def animate(args):
    x.append(args[0])
    y.append(args[1])
    z.append(args[2])
    return plt.plot(x, y, color='g'), plt.plot(x, z, color='r')


anim = animation.FuncAnimation(fig, animate, frames=frames, interval=300)
plt.show()