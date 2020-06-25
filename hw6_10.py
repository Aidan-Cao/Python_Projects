import matplotlib.pyplot as plt
import numpy
import csv
Data = open("/Users/janec/Downloads/dataX.csv", newline='')
x = csv.reader(Data, delimiter='')#this  will make an array of values
Data = open("/Users/janec/Downloads/dataY0.csv", newline='')
y = csv.reader(Data, delimiter='') #this  will make an array of values
sumy=0

yarray=[]
with open("/Users/janec/Downloads/dataY0.csv", newline='') as csvfile:
    for row in csvfile:
        if not row.strip():
            print(row)
            yarray.append(float(row[0]))

'''
with open("/Users/janec/Downloads/dataY0.csv", newline='') as csvfile:
    y =  csv.reader(csvfile, delimiter=' ', quotechar='|') 
    for row in y:
	    print(float((row[0])))
'''

delta=0.006283185307179587
#plt.plot([x,y])
#plt.show()

for i in y:
    sumy = sumy + abs(i)

area = delta * sumy
print (area)