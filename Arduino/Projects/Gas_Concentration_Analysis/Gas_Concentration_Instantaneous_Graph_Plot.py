import serial
import numpy as np
import matplotlib.pyplot as plt
import time
# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM4', 115200, timeout=1)
time.sleep(2)

'''
DOCS:
        This code is written to analysis the Gas Concentration, in the Atmosphere,
        for the Current Second and the last 10 Seconds.

        NOTE:
            1. The Values analyased will be updated by keeping only the track of the
            Last 10 Seconds Analysis Values from the Current Second.
'''
Values=[]
Period=[]
t = 0
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
plt.ylim(0,1000)
lin, = ax.plot(Period,Values,'-')
while(True):
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        nums = int(string) # convert the unicode string to an int
        Values.append(nums)
        Period.append(t)
        if(len(Values)>=10):
            Values.pop(0)
            Period.pop(0)
        t+=1;
    lin.set_xdata(Period)
    lin.set_ydata(Values)
    ax.clear()
    plt.title("Gas Analysis")
    plt.xlabel("Time Period")
    plt.ylabel("Gas Concentration")
    plt.ylim(0,600)
    ax.plot(Period,Values)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.show()
    print(Values,Period)
    time.sleep(1)
ser.close()

print(num)
