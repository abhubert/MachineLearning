"""
@author: Aleksander Brynjulf Hübert
May 21, 2019
"""
import csv
import math
from util import euclideanDistance
from util import dataSplitter

class KNN:
    def __init__(self):
        self.k = 5

    def findNeighbors(self, training, point, k):
        """
        calculates the neighbor points
        """
        dim = len(training[0])-1

        distance = []
        neighbor = []

        for i in range(0,len(training)):
            x = euclideanDistance(training[i][1:], point[1:], dim)
            distance.append((training[i][0],x))

        distance = sorted(distance, key=lambda tup: tup[1])

        for i in range(0,k):
            neighbor.append(distance[i])

        return neighbor


    def calculateLabel(self, neighbor):
        """
        Finds the best lable for the point using the neighbors
        """
        labels = {}

        for item in neighbor:
            if item not in labels:
                labels[item] = 1
            else: 
                labels[item] = labels[item] + 1
        
        return max(labels, key=lambda i: labels[i])

    def accuracyTest(self, testing, labels):
        """
        Checks the accuracy of the KNN
        """

        accuracy = 0

        for i in range(0,len(testing)):
            if labels[i][0] == testing[i][0]:
                accuracy = accuracy + 1
            else:
                continue
        
        return accuracy/len(testing)

    def knnRun(self, dataset,k):
        """
        Runs the KNN
        """
        labels = []
        
        training, testing = dataSplitter(dataset)

        for item in testing:
            labels.append(self.calculateLabel(self.findNeighbors(training, item, k)))

        return self.accuracyTest(testing, labels)