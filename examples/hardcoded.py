"""
# -*- coding: utf-8 -*-
Created on Fri Feb 16 02:54:09 2018
@author: Etcyl
"""
import motor_controller as MC
import ultrasonic as US
import RPi.GPIO as GPIO
import support_funcs as sf

#DO setup here
#Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

#Create objects for Vikingbot motor controller and HC-SR04 sensor
vb_motor = MC.MotorController()
HC_sensor = US.Ultrasonic()
HC_sensor.setup_GPIO()

vb_motor.setup_GPIO(1,0)
# setup and start PWM set the dulty cycles to 90
vb_motor.setup_PWM()
vb_motor.start_PWM()
vb_motor.set_motorSpeed(90,90)

# set the delay between motions to 2 seconds
vb_motor.set_SleepTime(2)

sensor_vals = [0]*3
#...Finished setup

#Check front, left, and right of the vb for objects using the sk model
while(1):
    GPIO.setmode(GPIO.BCM)
    HC_sensor.setup_GPIO()
    vb_motor.setup_GPIO(1,0)
    obj_front = HC_sensor.get_distance()
    sensor_vals[1] = sf.convert_sensor_reading(obj_front)
    vb_motor.goBack()
    vb_motor.set_SleepTime(1)
    obj_left = HC_sensor.get_distance()
    sensor_vals[0] = sf.convert_sensor_reading(obj_left)
    vb_motor.goForward()
    vb_motor.set_SleepTime(1)
    vb_motor.goForward()
    vb_motor.set_SleepTime(1)
    obj_right = HC_sensor.get_distance()
    sensor_vals[2] = sf.convert_sensor_reading(obj_right)
    if sensor_vals[0] == 0 and sensor_vals[1] == 0 and sensor_vals[2] == 0:
        vb_motor.turnLeft()
        vb_motor.set_SleepTime(1)
        vb_motor.turnLeft()
        vb_motor.set_SleepTime(1)
    elif sensor_vals[0] == 0 and sensor_vals[1] == 0 and sensor_vals[2] == 1:
        vb_motor.goBack()
        vb_motor.set_SleepTime(1)   
        vb_motor.turnLeft()
        vb_motor.set_SleepTime(1)
    elif sensor_vals[0] == 0 and sensor_vals[1] == 1 and sensor_vals[2] == 0:
        vb_motor.turnRight()
        vb_motor.set_SleepTime(1)   
        vb_motor.turnLeft()
        vb_motor.set_SleepTime(1)
    elif sensor_vals[0] == 0 and sensor_vals[1] == 1 and sensor_vals[2] == 1:
        vb_motor.goBack()
        vb_motor.set_SleepTime(1)   
        vb_motor.turnLeft()
        vb_motor.set_SleepTime(1)
    elif sensor_vals[0] == 1 and sensor_vals[1] == 0 and sensor_vals[2] == 0:
        vb_motor.goForward()
        vb_motor.set_SleepTime(1)   
        vb_motor.turnLeft()
        vb_motor.set_SleepTime(1) 
    elif sensor_vals[0] == 1 and sensor_vals[1] == 0 and sensor_vals[2] == 1:
        vb_motor.turnLeft()
        vb_motor.set_SleepTime(1)   
        vb_motor.turnLeft()
        vb_motor.set_SleepTime(1)
    elif sensor_vals[0] == 1 and sensor_vals[1] == 1 and sensor_vals[2] == 0:
        vb_motor.goForward()
        vb_motor.set_SleepTime(1)   
        vb_motor.turnLeft()
        vb_motor.set_SleepTime(1)
    elif sensor_vals[0] == 1 and sensor_vals[1] == 1 and sensor_vals[2] == 1:
        vb_motor.turnRight()
        vb_motor.set_SleepTime(1)   
        vb_motor.turnLeft()
        vb_motor.set_SleepTime(1)   
    GPIO.cleanup()
