A = [3,2,4,8,6,10,9,8,4,3,0,0,2,1,8,1,5,7,11]
B = []
for i in range(len(A)):
    if(A[i] not in B):
        B.append(A[i])
print('The original list of numbers is')
print(A)
print('The duplicates taken out turns the list into')
print(B)
for z in range(len(B)):
    for y in range(z + 1,len(B)):
        if B[z] > B[y]:
            box = B[z]
            B[z] = B[y]
            B[y] = box
print('The list numbers sorted out would be')
print(B)
