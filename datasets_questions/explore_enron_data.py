#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
import pandas as pd

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# count = 0
# for d in enron_data.keys():
#     if enron_data[d]['poi'] == 1:
#         count += 1
# print(enron_data)
# print(enron_data.keys())  # ["messages"])
# print(enron_data.keys())
print(enron_data['SKILLING JEFFREY K']['total_payments'])
print(enron_data['LAY KENNETH L']['total_payments'])
print(enron_data['FASTOW ANDREW S']['total_payments'])
print(enron_data)
pd.set_option('display.max_columns', 146)
data = pd.DataFrame(enron_data)
# print(data.shape)
em = 0
sal = 0
print(len(enron_data))
for k in enron_data.values():
    if k['total_payments'] == 'NaN':
        sal += 1
    # if k['email_address'] == 'NaN':
        # em += 1
print(sal)
