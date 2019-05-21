"""
@author: Aleksander Brynjulf Hübert
May 21, 2019
"""

import math
import csv
import random

###FILE READING###
def openFile(file): 
    """
    Method for opening CSV files into dataframe
    """
    data = []
    with open(file) as datafile: 
        lines = csv.reader(datafile)
        for row in lines:
            data.append(row)
    return data


def dataSplitter(dataset, splits = .67): 
    """
    Method for splitting testing and training data
    """
    n = int(len(dataset)*splits)

    random.shuffle(dataset)

    training = dataset[:n] 
    testing = dataset[n:]

    return (training, testing)

    
###DISTANCE CALCULATIONS###
def euclideanDistance(obs1, obs2, dimension):
    """
    Finds Euclidean distance between two observations
    for multi-dimensional data
    """

    distance = 0
    for item in range(0,dimension-1):
        distance = distance + math.pow((float(obs2[item]) - float(obs1[item])),2)

    return math.sqrt(distance)