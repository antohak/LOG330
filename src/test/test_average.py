import unittest
import sys
import csv

sys.path.insert(0, '/home/travis/build/tonyown1/LOG330/src/program/')

from Operations import Operations

class test_average(unittest.TestCase):
    def test_avg_01(self):
        list = []
        with open('src/test/csv_test/data_original.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for number in csv_reader:
                list.append(int(number[0]))

        operations = Operations()
        self.assertAlmostEqual(operations.average(list), 638.9)

    def test_avg_02(self):
        list = []
                                     #data_with_string.csv
        with open('src/test/csv_test/data_original.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for number in csv_reader:
                list.append(int(number[0]))

        operations = Operations()
        self.assertAlmostEqual(operations.average(list), 638.9)
