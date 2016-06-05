#------------------------------------------------------------------------------
##!/usr/bin/env python3
#
# Filename: Yaesu857D
# Author: Patrick J. Conant
# Email Address: pconant@gmail.com
#
# Description: Class for controlling Yaesu857D via CAT commands.  Intended as
#               template for support of other CAT radios
#
# Last Changed:  20160412
#------------------------------------------------------------------------------

import serial
import binascii
#import time
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
    
    #------------------------------------------------------------------------------
    # __pullValue - Private reader helper
    #------------------------------------------------------------------------------
    def __pullValue(self, hexVal):
        output=bytes.fromhex(hexVal)
        self.ser.write(output)
        return binascii.hexlify(self.ser.read(5)).decode('ascii')

    #------------------------------------------------------------------------------
    # __setValue - Private reader helper
    #------------------------------------------------------------------------------
    def __setValue(self,hexVal):
        inputVal=bytes.fromhex(hexVal)
        self.ser.write(inputVal)
        
    #------------------------------------------------------------------------------
    # __con - Serial Connection helper
    #------------------------------------------------------------------------------
    def __con(self):
        self.ser = serial.Serial(port=self.comPort, baudrate=4800, \
                            parity=serial.PARITY_NONE, \
                            stopbits=serial.STOPBITS_TWO, \
                            bytesize=serial.EIGHTBITS, timeout=1)
        
    
    #------------------------------------------------------------------------------
    # __init - sets shared comPort Value 
    #------------------------------------------------------------------------------
    def __init__(self, comPort):
        self.comPort = comPort


    #------------------------------------------------------------------------------
    # __exit__ - ensures Comm closed
    #------------------------------------------------------------------------------
    def __exit__(self):
        self.ser.close()


    #------------------------------------------------------------------------------
    # freq - Requests current frequency
    #------------------------------------------------------------------------------
    def freq(self):
        self.__con()
        out = self.__pullValue('0000000003')[:-2]
        self.ser.close()
        return out
        
    #------------------------------------------------------------------------------
    # mode - Requests current mode
    #------------------------------------------------------------------------------
    def mode(self):
        self.__con()
        out = self.__pullValue('0000000003')[-2:]
        self.ser.close()
        return modes(out).name
        

    #------------------------------------------------------------------------------
    # toggleVFO - Swaps between A and B VFO
    #------------------------------------------------------------------------------
    def toggleVFO(self):
        self.__con()
        self.__setValue('0000000081')
        self.ser.close()

    
