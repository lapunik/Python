

### 1 #################################################################################################
name = "Vojta"
age = 27
color = "dark blue"

print("Hi, I\'m " + name + ", I\'m " + str(age) + " years old and my favorit color is " + color)

### 2 #################################################################################################
cislo = 23
# cislo = input()
print(cislo)

prvocislo = True

for i in range(2,cislo):
    if((cislo%i) == 0):
        print("Cislo neni prvocislo")
        break
    if(i == cislo-1):
        print("Cislo je prvocislo")

### 3 #################################################################################################
def faktorial_metoda(hodnota):
    vysledek = hodnota
    for i in range(2,hodnota):
        vysledek = vysledek * i
    return vysledek

print(faktorial_metoda(5))

### 4 #################################################################################################The hell

def nacti_hodnotu(min, max):
    print("Zadej hodnotu: ")
    cislo = int(input())    
    while((cislo < min) or (cislo > max)):
        print("Spatna hodnota, zadej znovu: ")
        cislo = int(input())     
    return cislo

#a = nacti_hodnotu(0,10)
#b = nacti_hodnotu(0,10)
a = 5
b = 2

try:
    print(a/b)
except ZeroDivisionError as e:
    print("Deleni nulou: " + str(e))
except:
    print("Chyba")

### 5 #################################################################################################


### 6 #################################################################################################
### 7 #################################################################################################
### 8 #################################################################################################
### 9 #################################################################################################
### 10 ################################################################################################


### Codify 1: 1 ########################################################################################
"""
# GPT solution:
def longest_increasing_subsequence(arr):
    dp = [1] * len(arr)
    for i in range(1, len(arr)): # 1 až 8  
        for j in range(i): # 0 až i
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# My solution: 
def longest_increasing_subsequence_m(l,vnoreni):
    rozhodovac = 0

    for i in range(1,len(l)): #najdu další větší prvek 
        if(l[i] > l[0]):
            if(rozhodovac == 0):
                l_n = l[i:len(l)] 
                a = longest_increasing_subsequence_m(l_n,vnoreni+1)
                rozhodovac = 1 
            else:
                l_n = l[i:len(l)] 
                b = longest_increasing_subsequence_m(l_n,vnoreni+1)
                rozhodovac = 2
                break
    
    if (rozhodovac == 0):
        return vnoreni
    elif (rozhodovac == 1):
        return a
    elif (rozhodovac == 2):
        if(a < b):
            return b
        else:
            return a
    else:
        return 0
    
def longest_increasing_subsequence(l):
    a = []
    for i in range(0,len(l)):
       a.append(longest_increasing_subsequence_m(l[i:len(l)],1))
    return max(a)   

# print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])) # 4 (sekvence: [2, 3, 7, 101])

### Codify 1: 2 ########################################################################################

def group_anagrams(words: list[str]) -> list[list[str]]:

    w = []
    for i in words:
        w.append(sorted(i))

    alt = []
    result = []

    for i in w:
        if(not(i in alt)):
            alt.append(i)
            result.append([])


    for i in range(0,len(alt)):
        for j in range(0,len(w)):
            if(alt[i] == w[j]):
                result[i].append(words[j])

    return result

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

### Codility Binary gap: #################################################################################

def solution(N):
    text = str(bin(N))  
    max = 0
    prubezne_max = 0
    stav = 0
    for i in range(2, len(text)):
        if text[i] == '1':
            if stav == 0:
                stav = 1
            else:
                if prubezne_max > max:
                    max = prubezne_max
                prubezne_max = 0 
        else:
            prubezne_max += 1
    return max
    

print(solution(32)) 

### Codify test: ##########################################################################################

def solution2(A, K):
    
    if(len(A) == 0) or (K == 0):
        return A
    
    while(K >= len(A)):
        K -= len(A)
        if(K == 0):
            return A

    numbers = set(A)

    if(len(numbers)==0):
        return A

    result = []
    for i in range(-K,0):
        result.append(A[i])

    for i in range(0,len(A)-K):
        result.append(A[i])

    return result
"""

### Divide and conquer #####################################################################################
from timeit import default_timer as timer

def find_min(A):
    min = A[0]
    for i in A[1:]:
        if(min > i):
            min = i
    return min

def find_min_rec(A):
    if len(A) == 1:
        return A[0]
    
    mid = len(A) // 2
    left_min = find_min_rec(A[:mid])
    right_min = find_min_rec(A[mid:])
    
    return min(left_min, right_min)


A = [15,6,2,3, 14, 8, 9, 55, 2, 3, 44]
start = timer()
print(find_min(A))
end = timer()
b = end - start
start = timer()
print(find_min_rec(A))
end = timer()
a = end - start
print("Rekurze: ",a, "\nBez rekurze", b, "\nRozdil: ", a - b )


