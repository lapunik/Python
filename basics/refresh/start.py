def soucet(hodnota, hodnota2):
    return hodnota + hodnota2

a = 5
b = 2.6
c = '+'
d = "ahoj"
e = False

print(a)
print(b)
print(c)
print(d)
print(e)

print(a + b)
print(c + d)

for i in range(1,10):
    print("fuck")

while (a > 0):
    print(a)
    a = a - 1
    if(a == 2 and True):
        print(a+100)
    elif (a == 3):
        print("nothing")
        # break # ukonci cyklus 
        continue # ukonci cyklus 
    else: 
        print("dasli")
    print("konec cyklu")

print("end")

print(soucet(1,15))