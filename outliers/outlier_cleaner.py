#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    # your code goes here
    for age, pred, actual in zip(ages, predictions, net_worths):
        cleaned_data.append((age, actual, abs(actual - pred)))
    cleaned_data = sorted(cleaned_data, key=lambda x: x[2])
    cleaned_data = cleaned_data[:81]

    return cleaned_data
