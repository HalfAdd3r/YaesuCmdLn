import serial
import binascii
from enum import Enum

class modes (Enum):
    FM = '08'
    CW = '02'


ser = serial.Serial(port="COM3", \
    baudrate=4800,parity=serial.PARITY_NONE, \
    stopbits=serial.STOPBITS_TWO, bytesize=serial.EIGHTBITS, timeout=1)

#inputtest=b"\x00\x00\x00\x00\x81"
inputtest=bytes.fromhex('0000000081')
ser.write(inputtest)
ser.close()


ser = serial.Serial(port="COM3", \
    baudrate=4800,parity=serial.PARITY_NONE, \
    stopbits=serial.STOPBITS_TWO, bytesize=serial.EIGHTBITS, timeout=1)

#outputtest=b"\x00\x00\x00\x00\x03"
outputtest=bytes.fromhex('0000000003')
ser.write(outputtest)
out = binascii.hexlify(ser.read(5)).decode('ascii')

ser.close()


print("Value is: ", out[:-2], modes(out[-2:]).name)

