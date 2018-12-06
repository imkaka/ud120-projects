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
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score, recall_score
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)


# your code goes here]


# Train Test Split
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.30, random_state=42)

# Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(train_features, train_labels)

# print clf.score(test_features, test_labels)
print "Precision: ",precision_score(test_labels, clf.predict(test_features))
print "Recall: ",recall_score(test_labels, clf.predict(test_features))

# print clf.predict(test_features)

# print test_labels
