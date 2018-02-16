# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 19:00:34 2018

Uses a Support Vector Machine (SVM) from scikit-learn to identify obstacles in front of the Vikingbot.

@author: Etcyl
"""

from sklearn import svm
import pandas as pd
import pickle

#Make a SVM classifier 
SVM_class = svm.SVC()

inputs_and_targets = pd.DataFrame({
        'A' : [0, 0, 0, 0, 1, 1, 1, 1],
        'B' : [0, 0, 1, 1, 0, 0, 1, 1],
        'C' : [0, 1, 0, 1, 0, 1, 0, 1],
        'Targets' : [0, 1, 2, 3, 4, 5, 6, 7]
        })

#Train the SVM model on the inputs and targets
SVM_class.fit(inputs_and_targets[['A', 'B', 'C']], inputs_and_targets ['Targets'])

#Get and print the aaverage performance
print("The mean accuracy is: ", SVM_class.score(inputs_and_targets[['A', 'B', 'C']], inputs_and_targets ['Targets']))

#Pickle the model for later use on the Vikingbot
filename = 'svm_class.sav'
pickle.dump(SVM_class, open(filename, 'wb'))
