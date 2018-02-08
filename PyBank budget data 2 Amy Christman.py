import os
import csv
import sys
import datetime

#list holders
Date_column = [0, " "]
Revenue_column = [0, " "]
rowNR = 0

r = ('csvreader')
# open and read csv file

with open('budget_data_1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')

with open('budget_data_1.csv', 'a') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    

#for row in csvreader:
#print(type(row))

row = []

with open('budget_data_1.csv', 'a') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    reader = csvreader
    rowNr = 0
    if rowNR < 1:
        Date_column.append(row[0])
        #Revenue_column.append(row[0])

        rowNR = rowNR + 1

print (Date_column)
print (Revenue_column)

#date = (range(0, 100))
#print(date)


