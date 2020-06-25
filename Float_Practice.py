'''
A = [1,'1','3',4,5,6,'10', 10, 100]
B = [] # int list
C = [] # string to float

for i in range(len(A)):
    if(type(A) is int):#if type A[i] is string
        B.append(A[i])
    else:
        C.append(A[i])
        float(A[i])

print(C)
print(B)
'''
A = [1,'1','3',4,5,6,'10', 10, 100]
B = [] # int list
C = [] # string to float

for i in range(len(A)):
    if(type(A[i]) is int):#if type A[i] is string
        B.append(A[i])
    else:
        C.append(float(A[i]))
        float(A[i])

#A = '1'
        
print(C)
print(B)
