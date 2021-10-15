import serial
from serial.tools.list_ports import comports
from time import sleep, time
import os, pandas
ports = comports()
selected_port = None
for port in ports:
    if "Arduino Uno" in port.description:
        selected_port = port.device
ser = serial.Serial(
    port=selected_port,
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=1,
    bytesize=8,
    timeout=10
)
# ser.write("\n".encode())
sleep(2)

def move_stage(distance, direction):
    # distance up to 99, direction boolean
    # Full travel distance =~ 92
    distance = str(distance)
    if len(distance) < 2:
        distance = "0" + distance
    else:
        distance = str(distance)[:2]     # Limiting distance to two digits
    if direction:       # Making sure format is correct, anything other than 0 is True
        direction = 1
    else:
        direction = 0
    # Serial format = 'XXY\n' - 'XX' - distance(int), 'Y' - Direction (bool)
    msg = f"{distance}{direction}\n"
    ser.write(msg.encode("UTF-8"))

# Example
dire = 0
#0 towards pr:ylf
move_stage(1, dire)
d = (480/3500)*150
p =0
dset = 3
d = 60
df_folder = "C:/349_OPM/"
if not os.path.exists(df_folder):
    os.makedirs(df_folder)
file = df_folder + "Stage_shift test 13092021 2" + ".csv"
for i in range(dset):
    df = pandas.DataFrame(data={"time": [time()], "position": [p]})
    df.to_csv(file, sep=',', index=False, mode="a", header=False)
    sleep(1)
for i in range(30):
    p = p+d
    move_stage(d,dire)
    for i in range(dset):
        df = pandas.DataFrame(data={"time": [time()], "position": [p]})
        df.to_csv(file, sep=',', index=False, mode="a", header = False)
        sleep(1)



sleep(2)
ser.close()
