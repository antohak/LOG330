import unittest
import sys
import csv

sys.path.insert(0, '/home/travis/build/tonyown1/LOG330/src/program/')

from Operations import Operations

class test_variance(unittest.TestCase):
    def test_var_05(self):
        list = []
        with open('src/test/csv_test/data_original.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for number in csv_reader:
                list.append(int(number[0]))
        operations = Operations()
        self.assertAlmostEqual(operations.variance(list), 391417.8778)

    def test_var_06(self):
        list = []
                                     #data_with_string.csv
        with open('src/test/csv_test/data_original.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for number in csv_reader:
                list.append(int(number[0]))
        operations = Operations()
        self.assertAlmostEqual(operations.variance(list), 391417.8778)