import unittest
import sys
import csv

sys.path.insert(0, '/home/travis/build/tonyown1/LOG330/src/program/')

from Operations import Operations

class test_regression(unittest.TestCase):
    def test_reg_09(self):
        matrix = []
        with open('src/test/csv_test/donnees_regression_original.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                numbers = line[0].split(';')
                numbers = [float(n) for n in numbers]
                matrix.append(numbers)

        operations = Operations()
        regression = operations.regression(matrix)
        self.assertAlmostEqual(regression[0], 1.727932426)
        self.assertAlmostEqual(regression[1], -22.55253275)

    def test_reg_10(self):
        matrix = []
                      #donnes_regression_with_string.csv
        with open('src/test/csv_test/donnees_regression_original.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                numbers = line[0].split(';')
                numbers = [float(n) for n in numbers]
                matrix.append(numbers)
        operations = Operations()
        regression = operations.regression(matrix)
        self.assertAlmostEqual(regression[0], 1.727932426)
        self.assertAlmostEqual(regression[1], -22.55253275)
