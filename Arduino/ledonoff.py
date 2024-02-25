import serial
import time
import Programs.Hardware_Processes.Voice_Proc as p
with serial.Serial("COM3",9600,timeout=1) as ser:
        temp=''
        while(temp!='q'):
            a=p.bot.recognize("Command")
            print(a)
            temp=a
            a=bytes(a,'utf-8')
            ser.write(a)
            time.sleep(10)


'''import serial # you need to install the pySerial :pyserial.sourceforge.net
import time
# your Serial port should be different!
arduino = serial.Serial('COM5', 9600)


command =input("Type something..: (on/ off / bye )");
if command =="on":
	    print ("The LED is on...")
	    time.sleep(1) 
	    arduino.write('1') 
	    
elif command =="off":
		print ("The LED is off...")
		time.sleep(1) 
		arduino.write('0')
		
elif command =="bye":
		print ("See You!...")
		time.sleep(1) 
		arduino.close()
else:
		print ("Sorry..type another thing..!")
		

time.sleep(2) #waiting the initialization...

onOffFunction()'''
