from tabulate import tabulate
import csv
x=[]
with open('PATIENT_INFO.csv','r') as cs:
    csv_reader=csv.reader(cs)
    for line in csv_reader:
        a=line[8]
        b=a.replace("|", ",\n")
        line[8]=b
        x.append(line)
# create header
head=x[0]
x[0]=""
# Create table
print(tabulate(x,headers=head,tablefmt='simple'))
cs.close()