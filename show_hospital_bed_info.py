from tabulate import tabulate
import pandas as pc
import csv
x=[]
with open('HOSPITAL BED INFO.csv','r+') as cs:
    csv_reader=csv.reader(cs)
    for line in csv_reader:
        x.append(line)
# create header
head=x[0]
x[0]=""
# Create table
print(tabulate(x,headers=head,tablefmt='github'))
cs.close()
                  