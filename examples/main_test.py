# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 02:54:09 2018

@author: Etcyl
"""

import support_funcs as sf
import motor_controller as MC
import ultrasonic as US
import RPi.GPIO as GPIO
import pickle

#Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

#Create objects for Vikingbot motor controller and HC-SR04 sensor
vb_motor = MC.MotorController()
HC_sensor = US.Ultrasonic()

#DO setup here
#...

#Get the pickled models
filename = 'name.sav'
perc_class_load = pickle.load(open(filename, 'rb'))
filename = 'name.sav'
sensor_vals = pickle.load(open(filename, 'rb'))

#Check front, left, and right of the vb for objects using the sk model
while(1):
    obj_front = HC_sensor.get_distance()
    bool_front = sf.convert_sensor_reading(obj_front)
    vb_motor.turnLeft()
    vb_motor.set_SleepTime(1)
    obj_left = HC_sensor.get_distance()
    bool_left = sf.convert_sensor_reading(obj_left)
    vb_motor.turnRight()
    vb_motor.set_SleepTime(1)
    vb_motor.turnRight()
    vb_motor.set_SleepTime(1)
    obj_right = HC_sensor.get_distance()
    bool_right = sf.convert_sensor_reading(obj_right)
    current_A = sensor_vals.iloc[0]['A']
    current_B = sensor_vals.iloc[0]['B']   
    current_C = sensor_vals.iloc[0]['C']
    sensor_vals['A'] = sensor_vals['A'].replace([current_A], bool_left)
    sensor_vals['B'] = sensor_vals['B'].replace([current_B], bool_front)
    sensor_vals['C'] = sensor_vals['C'].replace([current_C], bool_right)
    class_label = perc_class_load.predict(sensor_vals[['A', 'B', 'C']])
    if class_label == 1: #Class label is 1, so turn right then forwards
        vb_motor.turnRight()
        vb_motor.set_SleepTime(1)
        vb_motor.goForward()
        vb_motor.set_SleepTime()
    elif class_label == 2: #Turn around then forwards 
        vb_motor.goBack()
        vb_motor.set_SleepTime(1)   
        vb_motor.goForward()
        vb_motor.set_SleepTime()
