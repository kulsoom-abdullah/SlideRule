#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
sys.path.append("../tools/")


# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
# ########################################################
# ## your code goes here ###
#
# before cutting down the dataset:
# training time: 145.805 s
# predict time: 14.884 s
# the score is:
# 0.984072810011
# AFTER The cut:
# training time: 0.082 s
# predict time: 0.886 s
# the score is:
# 0.884527872582
# AFter CUT using RBF instead of a linear kernel:
# training time: 0.092 s
# predict time: 1.007 s
# the score is:
# 0.616040955631
# (C= 10.0, 100., 1000., and 10000.
# respective scores = 0.616040955631, 0.616040955631,
# 0.821387940842, 0.892491467577
# 0.990898748578 score if I use all the data,
# rbf with C=10000 where training time: 95.936 s
# predict time: 9.707 s

# These lines effectively slice the training dataset down to 1% of
# its original size, tossing out 99% of the training data.
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

# clf = SVC(kernel='linear')
clf = SVC(C=10000.0, kernel='rbf')
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time() - t0, 3), "s"
t0 = time()
pred = clf.predict(features_test)
print "predict time:", round(time() - t0, 3), "s"
print "the score is:"
print accuracy_score(labels_test, pred)
answer = pred[10]
print "10th test point predicted is: {0}".format(answer)
answer = pred[26]
print "26th test point predicted is: {0}".format(answer)
answer = pred[50]
print "50th test point predicted is: {0}".format(answer)
count_chris = 0

for p in pred:
    if p == 1:
        count_chris += 1
print "num Chris predicted = {0}".format(count_chris)  # 877


# ########################################################
