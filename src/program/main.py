import csv


from src.program.Operations import Operations

list = []
with open('csv/donnees.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # skip first line since array is dynamic an first line is for number of data.
    next(csv_reader)
    for number in csv_reader:
        list.append(int(number[0]))

operations = Operations(list)

average = round(operations.average(), 1)
variance = round(operations.variance(), 4)
standard_deviation = round(operations.standard_deviation(), 2)

print('Moyenne: ', average)
print('Variance: ', variance)
print('Ecart Type: ', standard_deviation)


