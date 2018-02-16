# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 02:42:34 2018

Support functions for the Vikingbot and scikit-learn models.

@author: Etcyl
"""

def convert_sensor_reading(sensor_reading):
    print('Converting sensor values to Boolean values')
    if sensor_reading > 0 and sensor_reading < 30:
        converted_val = 1
    else:
        converted_val = 0
    return converted_val
