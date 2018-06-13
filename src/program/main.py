import csv

from src.progra
m.Operations import Operations
matrix = []
with open('csv/donnees_correlation.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # skip first line since array is dynamic an first line is for number of data.
    next(csv_reader)
    for line in csv_reader:
        numbers = line[0].split(';')
        numbers = [float(n) for n in numbers]
        matrix.append(numbers)

    operations = Operations()
    correlation = operations.correlation(matrix)

    print('r = ', round(correlation[0], 8))
    print('r*r = ', round(correlation[1], 8))



