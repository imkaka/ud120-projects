#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
from sklearn.svm import SVC
sys.path.append("../tools/")
from email_preprocess import preprocess


# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###

# clf = SVC(kernel="linear")
clf = SVC(C=10000)

# features_train = features_train[:len(features_train) / 100]
# labels_train = labels_train[:len(labels_train) / 100]

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time() - t0, 3), "s"

t1 = time()
count = 0
test = clf.predict(features_test)
for man in test:
    if man == 1:
        count += 1
print "Chris:", count
# print clf.predict(features_test[[26]])
# print clf.predict(features_test[[50]])
print "Testing time: ", round(time() - t1, 3), "s"

accurecy = clf.score(features_test, labels_test)
print accurecy


#########################################################
