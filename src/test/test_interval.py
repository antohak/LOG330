import unittest
import sys
import csv

sys.path.insert(0, '/home/travis/build/tonyown1/LOG330/src/program/')

from Operations import Operations

class test_interval(unittest.TestCase):
    def test_interval_70_13(self):
        matrix = []
        with open('src/test/csv_test/donnees_regression_original.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                numbers = line[0].split(';')
                numbers = [float(n) for n in numbers]
                matrix.append(numbers)

        operations = Operations()
        std = operations.standard_deviation_pair(matrix)
        interval = operations.interval(1.108, std, matrix)
        limit = operations.limits(matrix, interval)
        self.assertTrue(limit[0] == 683.18 and limit[1] == 1116.82, msg=None)

    def test_interval_90_14(self):
        matrix = []
        with open('src/test/csv_test/donnees_regression_original.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                numbers = line[0].split(';')
                numbers = [float(n) for n in numbers]
                matrix.append(numbers)

        operations = Operations()
        std = operations.standard_deviation_pair(matrix)
        interval = operations.interval(1.806, std, matrix)
        limit = operations.limits(matrix, interval)
        self.assertTrue(limit[0] == 546.59 and limit[1] == 1253.41, msg=None)
