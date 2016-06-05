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

import argparse, Yaesu857D, sys
# argparse - input argument handling
# Yaesu857D - Tranciever specific conotrol line
# sys - system functions for quit on error


#------------------------------------------------------------------------------
# Main Program 
#------------------------------------------------------------------------------
if __name__ == '__main__':
    
    # Argument Handling
    parser = argparse.ArgumentParser(description = \
                                     'CmdLn only CAT controller for Ham Radio')

    
    cmds = parser.add_mutually_exclusive_group(required = True) # Main Commands as group
    cmds.add_argument('-t', '--toggleVFO', action = 'store_true', help = 'Toggle VFO A/B')
    cmds.add_argument('-r', '--read',  action = 'store_true',help = 'Output current data only')
    
    args = parser.parse_args()

    try:
        radioConn = Yaesu857D.radio("COM3")
    except:
        print ("Unable to connect to Tranciever")
        sys.exit()

    if args.toggleVFO:
        radioConn.toggleVFO()
    else if args.read:
        print(radioConn.freq())
        print(radioConn.mode())
    else:
        print(radioConn.freq())
        print(radioConn.mode())

##    print(bob.freq())
##    print (bob.mode())
##
##    bob.toggleVFO()
##
##    print(bob.freq())
##    print (bob.mode())

