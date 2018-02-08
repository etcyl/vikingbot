# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 23:53:00 2018

@author: Etcyl*
         ECE 479: Intelligent Robotics 2 (Machine Vision and Learning)
         Portland, OR
         
         Various Vikingbot functions used here cited from: https://github.com/mlherd/vikingbot
"""

#import modules, set constants here
#from sklearn import linear_model
import motor_controller as MC #modules for Vikingbot control
import ultrasonic as US
import RPi.GPIO as GPIO
import time
import rand #random number generator for random behavior

#set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

#Check front, left, and right for obstacles
def obstacle_check():
    #get sensor reading
    sensor_reading = get_sensor_reading()
    #learner_class = get_class(sensor_reading)
    #emote_and_drive(learner_class)
    return

def get_sensor_reading():
    ultrasonic_sensor = US.Ultrasonic()
    readings = [0]*3 #make list of 3 zeroes to store the 3 readings (front, left, and right)
    readings[0] = ultrasonic_sensor.measure() #get X3 parameter for learner, front obstacle detection
    time.sleep(0.1)
    MC.MotorController.turnLeft() #get X2 parameter for learner, left obstacle detection
    GPIO.cleanup() 
    readings[1] = ultrasonic_sensor.measure() 
    time.sleep(0.1)
    MC.MotorController.turnRight() #turn right twice because we originally turned left from facing forward
    GPIO.cleanup()     
    MC.MotorController.turnRight()
    GPIO.cleanup() 
    readings[2] = ultrasonic_sensor.measure()  #get X1 parameter for learner, right obstacle detection
    MC.MotorController.turnLeft() #Face front again
    GPIO.cleanup()
    return readings 
    
def get_class(sensor_reading):
    return #classification as a number [0, 5]

def emote_and_drive(learner_class):
    if learner_class == 1:
        drive(0)
    elif learner_class == 2:
        #emote(front)
        drive(2)
    elif learner_class == 3:
        #emote(left)
        drive(3)
    elif learner_class == 4:
        #emote(right)
        drive(4)
    elif learner_class == 5:
        #emote(all)
        drive(5)
    else:
        print "Error: learner_class not mapping to known instance"

    return

def drive(position_to_drive):
    #Num   Action
    #1 --> left, right, or forwards (randomly picks one)
    #2 --> left, or right
    #3 --> forwards, or right
    #4 --> forwards, or left
    #5 --> backwards

    if position_to_drive == 0:
        #generate random number between 1 and 3
        num = 1
        if num == 1:
            MC.MotorController.turnLeft()
        elif num == 2:
            MC.MotorController.goForward()
        elif num == 3:
            MC.MotorController.turnRight()
    elif position_to_drive == 1:
        num = 2
        if num == 1:
            MC.MotorController.turnLeft()
        else:
            MC.MotorController.goForward()
    elif position_to_drive == 2:
        num = 3
        if num == 2:
            MC.MotorController.goForward()
        else:
            MC.MotorController.turnRight()
    elif position_to_drive == 3:
            MC.MotorController.goForward()
    else:
        print "Error"
        
    MC.MotorController.set_SleepTime(2)   
    GPIO.cleanup() 
    return
    
"""
def emote():
    #Randomly emotes one of the following behaviors:
    #Num   Behavior
    #1 --> LED flashes on for 500 ms and off for 500 ms, for 3 sec
    #2 --> LED flashes on for 2 sec and off for 1 sec, for 3 sec
    #3 --> 
    #4 --> 
    #5 --> 

    #generate random number between 1 and 5
    num = 1
    if position_to_drive == 0:

    elif position_to_drive == 1:

    elif position_to_drive == 2:
            vikingbotMotors.turnRight()
    elif position_to_drive == 3:
            vikingbotMotors.goForward()
    else:
        print Error
        
    vikingbotMotors.set_SleepTime(2)   
    GPIO.cleanup() 
    return    

"""
