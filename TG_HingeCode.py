#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class definition Hinge

This is the code for the hinge. Drive servo so that hinge parts open and close the door

By: Brittany Lowell, brittany.lowell@ucdenver
"""

# Imports

# Imports
#import numpy as np
#import matplotlib

#class Hinge():
  """
  Code that opens and closes door of coffee maker
  """
# Servo Control
import time
import wiringpi

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.01


def opendoor(pulse,delay_period):
    while True:
            for pulse in range(50, 250, 1):
                    wiringpi.pwmWrite(18, pulse)
                    time.sleep(delay_period)



def closedoor(pulse,delay_period):
    while True:
            for pulse in range(250, 50, -1):
                    wiringpi.pwmWrite(18, pulse)
                    time.sleep(delay_period)
