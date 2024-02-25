import serial
import time
'''
ser=serial.Serial('COM5',9600)
time.sleep(2)

while(True):
    b=ser.readline()
    print(b)
    time.sleep(0.1)'''
ser = serial.Serial('COM5', 9800, timeout=1)
time.sleep(2)

user_input = 'L'
while user_input != 'q':
    user_input = input('H = on, L = off, q = quit'  )
    byte_command = encode(user_input)
    ser.writelines(byte_command)   # send a byte
    time.sleep(0.5) # wait 0.5 seconds

print('q entered. Exiting the program')
ser.close()
