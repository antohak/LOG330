import unittest
import sys
import csv

sys.path.insert(0, '/home/travis/build/tonyown1/LOG330/src/test/')

from Operations import Operations

matrix = []
reduced_matrix = []
with open('src/test/csv_test/donnees_de_test_original.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    for line in csv_reader:
        matrix.append(line)

    operations = Operations()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j != 0:
                matrix[i][j] = float(matrix[i][j].replace(",", "."))

    for i in range(len(matrix)):
        data = operations.get_range_column(matrix[i], 1, 6)
        average = operations.average(data)
        temp = [average, matrix[i][7]]
        reduced_matrix.append(temp)



class test_etudes_intra(unittest.TestCase):
    def test_etudes_intra_11(self):
        operations = Operations()
        self.assertTrue(0 <= operations.correlation(reduced_matrix)[0] <=1)
