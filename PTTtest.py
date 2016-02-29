import serial
import binascii
from enum import Enum

class modes (Enum):
    FM = '08'
    CW = '02'


# PTT Test - Careful to not kurchunk!

ser = serial.Serial(port="COM3", \
    baudrate=4800,parity=serial.PARITY_NONE, \
    stopbits=serial.STOPBITS_TWO, bytesize=serial.EIGHTBITS, timeout=1)

#inputtest=b"\x00\x00\x00\x00\x81"
inputtest=bytes.fromhex('0000000008') #PTT On
inputtest=bytes.fromhex('0000000088') #PTT OFf
ser.write(inputtest)
ser.close()


