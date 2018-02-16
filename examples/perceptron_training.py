# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 18:17:00 2018

Uses a perceptron from scikit-learn to identify obstacles in front of the Vikingbot.

@author: Etcyl
"""

from sklearn.linear_model import perceptron
import pandas as pd
import pickle

#Make a perceptron classifier 
perc_class = perceptron.Perceptron(max_iter=100)

#Data in scikit-learn is typically a Numpy array, but here it is a Pandas DataFrame
#Create Numpy array for tree data
#Each input variable represents a sonic sensor reading
#If the sensor reading is between 2 and 30, then it is treated as 1 otherwise it is treated as 0

#1 means go right, 2 means turn around
inputs_and_targets = pd.DataFrame({
        'A' : [0, 0, 0, 0, 1, 1, 1, 1],
        'B' : [0, 0, 1, 1, 0, 0, 1, 1],
        'C' : [0, 1, 0, 1, 0, 1, 0, 1],
        'Targets' : [1, 2, 1, 2, 1, 2, 1, 2]
        })

#Train the perceptron model on the inputs and targets
perc_class.fit(inputs_and_targets[['A', 'B', 'C']], inputs_and_targets ['Targets'])

#Get and print the average performance
print("The mean accuracy is: ", perc_class.score(inputs_and_targets[['A', 'B', 'C']], inputs_and_targets ['Targets']))

#Pickle the model for later use on the Vikingbot
filename = 'perc_class.sav'
pickle.dump(perc_class, open(filename, 'wb'))
