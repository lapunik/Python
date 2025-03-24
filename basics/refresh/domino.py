def solution(A):

    domino = []
    for i in range(0,len(A),2):
        domino.append([A[i],A[i+1]])

    num_dominos = [1]

    for i in range(1,len(domino)):
        max_num_dominos = 1
        for j in range(0,i):
            if(domino[i][0] == domino[j][1]):
                if(max_num_dominos < num_dominos[j]+1):
                    max_num_dominos = num_dominos[j]+1
        num_dominos.append(max_num_dominos)

    return (len(domino) - (max(num_dominos)))



# solution([2,4,1,3,4,6,2,4,1,6])
print(solution([5,1,2,6,6,1,3,1,4,3,1,3,4,6,1,2,3,1,6,2]))