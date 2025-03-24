def solution(N):

    start = ord('a')
    stop = ord('z')

    abc = ""

    for i in range(start,stop+1):
        abc += chr(i)

    abc_len = len(abc)

    for i in range(abc_len,1,-1):
        if(N%i==0):
            num = N//i
            break

    word = ""

    for i in range(0,int(N/num)):
        word += (num*(abc[i])) 

    return word


N = 30
a = solution(N)
print(a)
print(len(a))