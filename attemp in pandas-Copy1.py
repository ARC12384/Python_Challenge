
# coding: utf-8

# In[ ]:


import os
import csv
import sys
import datetime
import pandas as pd



# In[1]:


#list holders
Date_column = (" ")
Revenue_column = (" ")
rowNR = 0


# In[2]:


r = ('csvreader')
# open and read csv fil


# In[4]:


with open('budget_data_1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')

#with open('budget_data_1.csv', 'a') as csvfile:
#  csvreader = csv.reader(csvfile, delimiter= ',')


# In[5]:


row = []

with open('budget_data_1.csv', 'a') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    reader = csvreader
    rowNr = 0
    if rowNR < 1:
        Date_column.append(row[0])
        #Revenue_column.append(row[0])

        rowNR = rowNR + 1


# In[6]:


print (Date_column)
print (Revenue_column)

