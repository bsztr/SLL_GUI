#import visa
from ThorlabsPM100 import ThorlabsPM100
from pymeasure.instruments import thorlabs
import pymeasure

dev = pymeasure.instruments.thorlabs.ThorlabsPM100USB
print(pymeasure.instruments.list_resources())
aa = dev.sensor(dev)
print(aa)
# rm = visa.ResourceManager()
# print(rm.list_resources())
# inst = rm.open_resource('USB::0x1313::0x8078::P0010641::INSTR', timeout=1)
# power_meter = ThorlabsPM100(inst=inst)
#
# print(power_meter.read)
