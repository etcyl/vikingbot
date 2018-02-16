# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 17:24:18 2018

Uses a tree from scikit-learn to identify obstacles in front of the Vikingbot.

@author: Etcyl
"""

from sklearn.tree import DecisionTreeClassifier
import numpy as np

#Make a decision tree classifier 
tree = DecisionTreeClassifier(random_state=0)

#Data in scikit-learn is typically a Numpy array
#Create Numpy array for tree data
#Each input variable represents a sonic sensor reading
#If the sensor reading is between 2 and 30, then it is treated as 1 otherwise it is treated as 0
inputs = np.array([[0,0,0], #No objects
                   [0,0,1], #Object is to the right
                   [0,1,0], #Object is in front
                   [0,1,1], #Object is to the right and in front
                   [1,0,0], #Object is to the left
                   [1,0,1], #Object is to the left and to the right
                   [1,1,0], #Object is to the left and in front
                   [1,1,1]]) #Object is to the right, left, and in front

#Targets map to classes such as "object to the left and right" or "object to the front"
targets = np.array([[2],
                    [2], 
                    [1], 
                    [1],
                    [2], 
                    [1], 
                    [2],
                    [1]]) 

#Get and print the results
results = cross_val_score(tree, inputs, targets, cv = 4)
print (results)
