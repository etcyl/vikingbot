# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 19:00:34 2018

Uses a Support Vector Machine (SVM), C-Support Vector Classification or SVC,
from scikit-learn to identify obstacles in front of the Vikingbot.

@author: Etcyl
"""

from sklearn import svm
import pandas as pd

#Make a SVM classifier 
SVM_class = svm.SVC()

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

#Train the SVM model on the inputs and targets
SVM_class.fit(inputs_and_targets[['A', 'B', 'C']], inputs_and_targets ['Targets'])

#Get and print the aaverage performance
print("The mean accuracy is: ", SVM_class.score(inputs_and_targets[['A', 'B', 'C']], inputs_and_targets ['Targets']))
