import os
import csv
import sys
import datetime

#list holders
Date_column = []
Revenue_column = []

r = ('csvreader')
# open and read csv file

with open('budget_data_1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    
    for line in csvreader:
        print(line)

    for row in csvreader:
        print(type(row))

with open('budget_data_1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    for row in r:
        list.append(row[0], row[1:])


#date = (range(0, 100))
#print(date)


