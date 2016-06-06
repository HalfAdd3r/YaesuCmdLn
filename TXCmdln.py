#------------------------------------------------------------------------------
##!/usr/bin/env python3
#
# Filename: TXCmdln.py
# Author: Patrick J. Conant
# Email Address: pconant@gmail.com
#
# Description: CmdLn only CAT controller for Ham Radio.  Focused on Yaesu857D
#
# Last Changed:  20160412
#------------------------------------------------------------------------------

import argparse, re, sys, Yaesu857D
# argparse - input argument handling
# sys - system functions for quit on error
# re - Regex for clening inputs
# Yaesu857D - Tranciever specific conotrol line


#------------------------------------------------------------------------------
# freqClean - formats input as number only 8 char string
#------------------------------------------------------------------------------
def freqClean (numIn):
    regPurge = re.compile(r'\D+')
    
    # Treat data before first decimal as megahertz
    if "." in numIn:
        vals = numIn.partition(".")
        val1 = regPurge.sub("", vals[0])[:3] # num and 3 char max
        val2 = regPurge.sub("",vals[2])[:5] # num and 5 char max
        return "{0:0>3}{1:0<5}".format(val1, val2)

    # Otherwise ensure all numbers and 8 char length    
    else:
        return regPurge.sub("",numIn)[:8].ljust(8,"0")


#------------------------------------------------------------------------------
# Main Program 
#------------------------------------------------------------------------------
if __name__ == '__main__':
    
    # Argument Handling
    parser = argparse.ArgumentParser(description = \
                                     'CmdLn only CAT controller for Ham Radio')

    
    cmds = parser.add_mutually_exclusive_group(required = True) # Main Commands as group
    cmds.add_argument('-v', '--toggleVFO', action = 'store_true', help = 'Toggle VFO A/B')
    cmds.add_argument('-tx', '--txStatus', action = 'store_true', help = 'Get TX status')
    cmds.add_argument('-rx', '--rxStatus', action = 'store_true', help = 'Get TX status')
    cmds.add_argument('-f', '--frequency', help="Set Frequency")
    cmds.add_argument('-r', '--read',  action = 'store_true', \
                      help = 'Output current data only')
    
    args = parser.parse_args()

    try:
        radioConn = Yaesu857D.radio("COM3")
    except:
        print ("Unable to connect to Tranciever")
        sys.exit()

    if args.toggleVFO:
        radioConn.toggleVFO()
    elif args.read:
        print(radioConn.freq())
        print(radioConn.mode())
    elif args.txStatus:
        print(radioConn.txStatus())
    elif args.rxStatus:
        print(radioConn.rxStatus())
    elif args.frequency != "":
        radioConn.setFreq(freqClean(args.frequency))
    else:
        print(radioConn.freq())
        print(radioConn.mode())

