import csv

from src.program.Operations import Operations
matrix = []
reduced_matrix = []
with open('csv/donnees_regression.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        numbers = line[0].split(';')
        numbers = [float(n) for n in numbers]
        matrix.append(numbers)

    operations = Operations()
    std = operations.standard_deviation_pair(matrix)
    interval_70 = operations.interval(1.108, std, matrix)
    interval_90 = operations.interval(1.806, std, matrix)
    print("Calcule de l'ecart type")
    print("-----------------------------")
    print(std)
    print()
    print("Calcule de l'intervalle et limites (70%)")
    print("---------------------------------------------")
    print("Intervalle: ", interval_70)
    print("Limites: ", operations.limits(matrix, interval_70))
    print()
    print("Calcule de l'intervalle et limites (90%)")
    print("---------------------------------------------")
    print("Intervalle: ", interval_90)
    print("Limites: ", operations.limits(matrix, interval_90))

