import serial
import binascii
import time
from enum import Enum

class modes (Enum):
    AM = '04'
    CW = '02'
    CWR = '03'
    DIG = '0A'
    FM = '08'
    FMN = '88'
    LSB = '00'
    PKT = '0C'
    USB = '01'

class radio:
    comPort = None
    
    def __pullValue(self, hexVal):
        output=bytes.fromhex(hexVal)
        self.ser.write(output)
        return binascii.hexlify(self.ser.read(5)).decode('ascii')
        
    def __setValue(self,hexVal):
        inputVal=bytes.fromhex(hexVal)
        self.ser.write(inputVal)
        
    def __con(self):
        self.ser = serial.Serial(port=self.comPort, baudrate=4800, \
                            parity=serial.PARITY_NONE, \
                            stopbits=serial.STOPBITS_TWO, \
                            bytesize=serial.EIGHTBITS, timeout=1)
        
    
    def __init__(self, comPort):
        self.comPort = comPort 
        
    def freq(self):
        self.__con()
        out = self.__pullValue('0000000003')[:-2]
        self.ser.close()
        return out
        
        
    def mode(self):
        self.__con()
        out = self.__pullValue('0000000003')[-2:]
        self.ser.close()
        return modes(out).name
        

    def toggleVFO(self):
        self.__con()
        self.__setValue('0000000081')
        self.ser.close()

    def __exit__(self):
        self.ser.close()

