import unittest
import sys
import csv

sys.path.insert(0, '/home/travis/build/tonyown1/LOG330/src/program/')

from Operations import Operations

class test_correlation(unittest.TestCase):
    def test_corr_07(self):
        matrix = []
        with open('src/test/csv_test/donnees_correlation_original.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                numbers = line[0].split(';')
                numbers = [float(n) for n in numbers]
                matrix.append(numbers)

        operations = Operations()
        self.assertAlmostEqual(operations.correlation(matrix)[0], 0.95592053)

    def test_corr_08(self):
        matrix = []
                      #donnes_correlation_with_string.csv
        with open('src/test/csv_test/donnees_correlation_original.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                numbers = line[0].split(';')
                numbers = [float(n) for n in numbers]
                matrix.append(numbers)
        operations = Operations()
        self.assertAlmostEqual(operations.correlation(matrix)[0], 0.95592053)
