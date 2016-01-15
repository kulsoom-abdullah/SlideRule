#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
#from classifyDT import classify
from sklearn import tree
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
#clf = classify(features_train, labels_train)

clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
#accuracy = accuracy_score(labels_test, pred)
acc = accuracy_score(labels_test, pred)

print acc #0.978384527873
print "accuracy = {0} num features = {1}".format(acc, len(features_train[0])) #3785
#changing selector = SelectPercentile(f_classif, percentile=10) to selector = SelectPercentile(f_classif, percentile=1) then num features = 379 accuracy = 0.967007963595 a less complex tree



