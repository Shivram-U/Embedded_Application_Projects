import serial
import numpy as np
import matplotlib.pyplot as plt
import time
# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM4', 115200, timeout=1)
time.sleep(2)


plt.title("Gas Analysis")
plt.xlabel("Time Period")
plt.ylabel("Gas Concentration")
Values=[]
Period=[]
t = 0
plt.ion()
plt.ylim(0,1000)
fig = plt.figure()
ax = fig.add_subplot(111)
lin, = ax.plot(Period,Values,'-')
while(True):
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        nums = int(string) # convert the unicode string to an int
        Values.append(nums)
        Period.append(t)
        
        t+=1;
    lin.set_xdata(Period)
    lin.set_ydata(Values)
    ax.clear()
    ax.plot(Period,Values)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.show()
    print(Values,Period)
    time.sleep(1)
ser.close()

print(num)