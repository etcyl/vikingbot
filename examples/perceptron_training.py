# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 18:17:00 2018

Uses a perceptron from scikit-learn to identify obstacles in front of the Vikingbot.

@author: Etcyl
"""

from sklearn.linear_model import perceptron
import pandas as pd

#Make a perceptron classifier 
perc_class = perceptron.Perceptron(max_iter=100)

#Data in scikit-learn is typically a Numpy array, but here it is a Pandas DataFrame
#Each input variable represents a sonic sensor reading
#If the sensor reading is between 2 and 30, then it is treated as 1 otherwise it is treated as 0
#Inputs A, B, and C represent sensor readings to the left, in front, and to the right of the Vikingbot

inputs_and_targets = pd.DataFrame({
        'A' : [0, 0, 0, 0, 1, 1, 1, 1],
        'B' : [0, 0, 1, 1, 0, 0, 1, 1],
        'C' : [0, 1, 0, 1, 0, 1, 0, 1],
        'Targets' : [2, 2, 1, 1, 2, 1, 2, 1]
        })

perc_class.fit(inputs_and_targets[['A', 'B', 'C']], inputs_and_targets ['Targets'])

#Get and print the aaverage performance
print("The mean accuracy is: ", perc_class.score(inputs_and_targets[['A', 'B', 'C']], inputs_and_targets ['Targets']))
