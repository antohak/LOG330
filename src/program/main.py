import csv

from src.program.Operations import Operations
matrix = []
reduced_matrix = []
with open('csv/donnees_de_test.csv', 'r') as csv_file:
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

    c = operations.correlation(reduced_matrix)[0]

    print('\nCalcule de la correlation')
    print('-----------------------------\n')
    print('correlation = ', c)
    print('')

    message = "La correlation entre le temps consacre aux etudes selon les donnees\n" \
              "et les resultas obtenus a l'intra par les etudiants est "

    if c >= 0 and c < 0.2:
        message += "faible"
    if c >= 0.2 and c < 0.4:
        message += "moyenne"
    if c >= 0.4 and c < 0.7:
        message += "forte"
    if c >= 0.7 and c < 0.9:
        message += "tres forte"
    if c >= 0.9 and c <= 1:
        message += "parfaite"

    print(message)





