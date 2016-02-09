#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
import numpy as np
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.tree import DecisionTreeClassifier as tree
from sklearn.metrics import accuracy_score
from sklearn import cross_validation
from sklearn.metrics import *

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 


features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

clf = tree()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
accuracy = accuracy_score(pred,labels_test)

print accuracy #0.724137931034
print np.array(labels_test)
print "number of POIs in the test set:"
num_pois_test = len([x for x in labels_test if x == 1.0])
print num_pois_test
print "total people in the test set:"
total_ppl_test= len(labels_test)
print total_ppl_test
print "If your identifier predicted 0. (not POI) for everyone in the test set, what would its accuracy be?"
acc = 1.0 -  float(num_pois_test)/total_ppl_test
print acc
#Do you get any true positives? (In this case, we define a true positive as a case where both the actual label and the predicted label are 1)

print precision_score(labels_test,clf.predict(features_test))
print recall_score(labels_test,clf.predict(features_test))
