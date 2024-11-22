A = [1,2,3,4,5]
B = [1,2,3,99,4,5]
lenA = len(A)
lenB = len(B)
i = 1
j = 1 
k = 0

while((i<=lenA) and (j<=lenB) and (k<=1)):

    if(A[i-1] == B[j-1]):
        i = i+1
    else:
        k = k+1
    j = j+1
a = (i>lenA) and (j>lenB) and (k==1)
print(a)