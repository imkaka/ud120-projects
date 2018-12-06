#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

from sklearn import neighbors
from sklearn import tree
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

features_train, labels_train, features_test, labels_test = makeTerrainData()


# the training data (features_train, labels_train) have both "fast" and "slow"
# points mixed together--separate them so we can give them different colors
# in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 1]


# initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color="b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color="r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


# your code here!  name your classifier object clf if you want the
# visualization code (prettyPicture) to show you the decision boundary

clf = neighbors.KNeighborsClassifier(n_neighbors=3)
clf.fit(features_train, labels_train)
print "KNN: ", clf.score(features_test, labels_test)

clf1 = tree.DecisionTreeClassifier(min_samples_split=40)
clf1.fit(features_train, labels_train)
print "DT: ", clf1.score(features_test, labels_test)

clf2 = SVC(C=100000)
clf2.fit(features_train, labels_train)
print "SVC:", clf2.score(features_test, labels_test)

clf3 = GaussianNB()
clf3.fit(features_train, labels_train)
print "Naive Bayes:", clf3.score(features_test, labels_test)

clf4 = RandomForestClassifier()
clf4.fit(features_train, labels_train)
print "Random Forest: ", clf4.score(features_test, labels_test)

clf5 = AdaBoostClassifier()
clf5.fit(features_train, labels_train)
print "Ada Boost: ", clf5.score(features_test, labels_test)

try:
    prettyPicture(clf5, features_test, labels_test)
except NameError:
    pass
