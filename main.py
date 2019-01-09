# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:26:53 2019

@author: melab2
"""

''' @file main.py
There must be a docstring at the beginning of a Python
source file with an @file [filename] tag in it! '''
class MotorDriver:
    ''' This class implements a motor driver for the ME405 board. '''
    def __init__ (self):
        ''' Creates a motor driver by initializing GPIO pins and turning the motor off for safety. '''
        import pyb
        print ('Creating a motor driver')
        pinA10 = pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.OUT_PP) #ENA -> pin10
        pinA10.high()                                         #enable motor
    def set_duty_cycle (self, level):
        ''' This method sets the duty cycle to be sent to the motor to the given level. Positive values
        cause torque in one direction, negative values in the opposite direction.
        @param level A signed integer holding the duty cycle of the voltage sent to the motor '''
        import pyb    
        pinB4 = pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP) #set pinb4 to output
        pinB5 = pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP) #set pinb5 to output
        tim3 = pyb.Timer (3, freq = 20000)                  #configure Timer3
        ch1 = tim3.channel(1, pyb.Timer.PWM, pin = pinB4)   #set channel1 to pwm
        ch2 = tim3.channel(2, pyb.Timer.PWM, pin = pinB5)   #set channel2 to pwm
        print ('Setting duty cycle to ' + str (level))        
        if level >= 0:
            pinB4.high()
            ch2.pulse_width_percent(level)
        else:
            pinB5.high()
            ch1.pulse_width_percent(-level)

