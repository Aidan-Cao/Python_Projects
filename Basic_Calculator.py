import math
import csv
#import matplotlib.pyplot as plt
#import numpy as np

print('This is the Basic Calculator where you can make simple calculations such as +, -, /, *, and ^. ')
A = input('Type in first Input : ')
math_op = input('Math operation : ')
B = input('Type in second input : ')

if('+' in math_op):# subtraction
    print(float(A) + float(B))

elif('-' in math_op):# subtraction
    print(float(A) - float(B))

elif('*' in math_op):# multiplication
    print(float(A) * float(B))

elif('/' in math_op):# division
    print(float(A) / float(B))

elif('^' in math_op):# power of
    print(math.pow(float(A),float(B)))

elif('^' in math_op):# exponents
    print(math.exp(float(A),float(B)))

elif('^' in math_op):# root
    print(math.pow(float(A),float(B)))

'''
plt.plot(csv[file: (null)])
plt.show




Import matplotlib.pyplot as plt
A = [1,2,3,4,5,6,7,8]
B = [1,2,3,4,5,6,7,8]
plt.plot
plt.show
'''

