#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  led.py
#  
#  Copyright 2022  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import RPi.GPIO as GPIO
import time
from datetime import datetime

entrada = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.HIGH)

print ("\033c")
print ("")
print ("")
print ("\033[1m" + "\033[32m" + "\33[5m" + "    >>> CH1  ON <<<" + "\033[0m")
print ("    --- CH2 OFF ---")
print ("")
     
def Entrada ():
    entrada = 0
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    entrada = input ()
    return entrada
    
def menu ():
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    print ("    ----------------")
    print ("    Menu")
    print ("    CH 1 ON: prem 1")
    print ("    CH 2 ON: prem 2")
    print ("    SORTIR:  prem 3")
    print ("    ----------------")
    print ("")
    print('\033[1m' + '\033[31m' + '    EB3CJR BCN 2022' + '\033[0m')
    print("    %s" %(date_time))
    print ("")

menu ()

while True:    
    entrada = Entrada ()
    print ("")
    #print (">>> has entrat: %s" %(entrada))

       
    if entrada == 1:
        a = 0
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        GPIO.output(11, GPIO.HIGH)
        print ("\033c")
        print ("")
        print ("\033[1m" + "\033[32m" + "\33[5m" + "    >>> CH1  ON <<<" + "\033[0m")
        print ("    --- CH2 OFF ---")
        print ("")
        print ("")
        entrada = 0  
        menu ()
         
    if entrada == 2:
        print ("\033c")
        print ("")
        print ("    --- CH1 OFF ---")
        print ("\033[1m" + "\033[93m" + "\33[5m" + "    >>> CH2  ON <<<" + "\033[0m")
        print ("")
        print ("")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        GPIO.output(11, GPIO.LOW)
        entrada = 0
        menu ()
        
    if entrada == 3:
        print ("FI DEL PROGRAMA")
        break

