import csv

filepath = 'data/windturbine_example.csv'

with open(filepath) as csv_file:
    line = csv.reader(csv_file)
    for row in line:
        print(row)