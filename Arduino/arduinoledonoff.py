import serial
import time
ser = serial.Serial('COM6', 9800, timeout=1)
time.sleep(2)

user_input = '1'.encode()
while user_input != 'q':
   # user_input = input('Enter the choice')
    byte_command =bytes(user_input)
    ser.writelines(byte_command)   # send a byte
    time.sleep(0.5) # wait 0.5 seconds

print('q entered. Exiting the program')
ser.close()
