#!/usr/bin/python

from L3GD20 import L3GD20

import time
import sys
import math
import os
import signal

# Communication object
s = L3GD20(busId = 1, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)

# Preconfiguration
s.Set_PowerMode("Normal")
s.Set_FullScale_Value("250dps")
s.Set_AxisX_Enabled(True)
s.Set_AxisY_Enabled(True)
s.Set_AxisZ_Enabled(True)

# Print current configuration
s.Init()
s.Calibrate()

def getz(s):
    dxyz = s.Get_CalOut_Value()
    return abs(dxyz[2])

while True:

    # Calculate angle
    #dt = 0.1
    #x = 0
    #y = 0
    #z = 0

    

    if getz(s) > 20:
        #time.sleep(dt)
        pid = os.fork()
        if pid==0:
            print "sound"
            os.execvp('mpg123',('mpg123','cascada.mp3'))
        else:         
            while getz(s) > 20:
                print "waiting"
                print pid
                pass
            os.kill(pid, signal.SIGTERM)
            #os.waitpid(pid,0)
            print "stop"
            #time.sleep(.05)
    else:
        pid = os.fork()
        if pid==0:
            print "sound"
            os.execvp('mpg123',('mpg123','--loop','20','adele.mp3'))
        else:         
            while getz(s) < 20:
                print "waiting"
                print pid
                pass
            os.kill(pid, signal.SIGTERM)
            #os.waitpid(pid,0)
            print "stop"
            #time.sleep(.05)

        

	
	
