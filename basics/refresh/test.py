"""
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
"""

def solution(A):
    #if(len(A) == 1):
    #   return 
    a = sorted(A)
    for i in range(0,len(a)):
        if(i+1 != a[i]):
            return i+1 
    return len(a)+1


A = [3,2,1]


print(solution(A))