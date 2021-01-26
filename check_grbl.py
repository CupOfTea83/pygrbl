import serial
from COM_scan import serial_ports
import time

print(serial_ports())
try:
    realport = serial.Serial(serial_ports()[0], baudrate=115200, timeout=1)
except Exception as e:
    print(e)

time.sleep(2)

if realport:
    realport.write(b'$#\r\n')
    time.sleep(2)
    #realport.write(b'$\n')
    
    print(realport.readlines())
