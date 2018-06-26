import csv

from src.program.Operations import Operations
matrix = []
with open('csv/donnees_regression.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # skip first line since array is dynamic an first line is for number of data.
    next(csv_reader)
    for line in csv_reader:
        numbers = line[0].split(';')
        numbers = [float(n) for n in numbers]
        matrix.append(numbers)

    operations = Operations()
    regression = operations.regression(matrix)
    b1 = round(regression[0], 9)
    b0 = round(regression[1], 8)

    print('b1 = ', b1)
    print('b0 = ', b0)
    print()
    print()

    exit = False
    while not exit:
        i = input('Which value do you which to calculate? (x or y): ')
        if i == 'x':
            y = float(input('Please enter a value for y (4 decimals max): '))
            print(y)
            x = round((y-b0)/b1, 5)
            print('X = %d' % x)
        elif i == 'y':
            x = float(input('Please enter a value for x (4 decimals max): '))
            y = round(b0 + x*b1, 5)
            print('Y = %d' % y)
        else:
            print('Wrong input')
        c = input('do you wish to continue? (y or n): ')
        if c == 'n':
            exit = True

