import csv
import math
import unittest

class Operations:
    """
        the init function of the class that will initialize certain values
        @:param takes a list of numbers
    """
    def __init__(self, list):
        self.list = list
        self.n = len(self.list)

    """
        Calculates the average 
        @:return will return float representation of average
    """
    def average(self):
        list = self.list
        n = self.n
        sum = 0
        for x in list:
            sum += x
        return round(float((1/n) * sum), 1)
    """
        Calculates the variance 
        @:return will return float representation of variance
    """
    def variance(self):
        list = self.list
        n = self.n
        average = self.average()
        sum = 0
        for x in list:
            sum += float((x - average)*(x - average))
        return round(float(1/(n-1) * sum), 4)

    """
        Calculates the standard deviation 
        @:return will return the s.d
    """
    def standard_deviation(self):
        return round(math.sqrt(self.variance()), 2)

list = []
with open('donnees.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # skip first line since array is dynamic an first line is for number of data.
    next(csv_reader)
    for number in csv_reader:
        list.append(int(number[0]))

operations = Operations(list)

average = round(operations.average(), 1)
variance = round(operations.variance(), 4)
standard_deviation = round(operations.standard_deviation(), 2)

print('Moyenne: ', average)
print('Variance: ', variance)
print('Ecart Type: ', standard_deviation)


