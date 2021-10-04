### if ########################################################################################

x = 5
y = 18
z = 7

if x>y:
    print("Prvni podminka JE splnena")
elif x==y:
    print("Druha ppodminka JE splnena")
else:
    print("Ani jedna z podmínek není splněna")

# tady pokračuju kod, jako by se nechumelilo

print("Všechno dobrý")


# and = &&, or = ||, not = ! ("not" má přednost, potom "and" a potom teprve "or" )
if x>y and x>z or not(z==y) :
     print("Podminka JE splnena")

# můžu se podívat i jestli je hodnota v rozsahu

if 3 in range(1,7):
    # podminka by byla splnena, protože trojka je mezi jedna až sedm
    print ("podminka splnena")

### for ########################################################################################

for i in range(0,9):
    print(i)
print("Tady už jsem zase mimo cyklus")

### while ########################################################################################
"""
hodnota = 0

while hodnota<9 :
    hodnota = int(input("Zadej hodnotu: "))
    print("Hodnota je: " + str(hodnota))

print("Tady už jsem zase mimo cyklus")
"""
### přerušení cyklů ############################################################################
hodnota = 10
while True:
    print(hodnota)
    if(hodnota < 4):
        break
    hodnota -= 1

for i in range(0,9):
    print(i)
    break # zastaví celý for
    # continue # zastaví pouze jednu iteraci
