A = [1,3,4,7,3,9,0,8,6,5,5,2]
B = []
print('This is the original')
print(A)
# 1,2,3,4,5,6,7,8,9,10
#gets rid of all repeats

for i in range(len(A)):
    if(A[i] not in B):
        B.append(A[i])
print('Code deletes all duplicates')
print(B) #print [0,1,2,3,4,5,6,7,8,9]
for i in range(10):
    for j in range(i,10):
        if B[j] < B[i]:
            temp = B[i]
            B[i]=B[j]
            B[j]=temp
print('Code sorts the numbers')
print (B)
