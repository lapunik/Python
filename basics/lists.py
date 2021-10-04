pozdravy = ["ahoj","cau","nazdar","cus"]

print(pozdravy[1])
#můžu odkazovat i od zadu
print(pozdravy[-1])
print(pozdravy[-2])

print(pozdravy[0:2]) # posledni hodnota už není zahrnuta, prvni ano
print(pozdravy[0:-1]) # list bez posledniho elementu 

obecny_list = ["jablko", 4, False, 9.2, ["dalsi list", "to je ulet",4, 1.6]]

print(obecny_list[2])
print(obecny_list[4])
print(obecny_list[4][1])

vektor = range(11,20)
print(vektor[5])

hodnoty = [1,2,5,6,9]

for i in hodnoty:
    print(i)

# můžu projet obecny list

for i in obecny_list:
    print(i)

# pozor na přiřazování seznamů! přiřazuje se reference, nikoliv přímo hodnoty7
# pokud chci přiřadit hodnoty, musím použít metodu copy() např:

seznam = [1,2,3,4]
seznam2 = seznam
print(seznam)
print(seznam2)
seznam.clear()
print(seznam)
print(seznam2) # smazáním "seznamu" se smazal i "seznam2", protože "seznam2" pouze referoval na "seznam"
# pokud nechci aby se smazal i "seznam2", musím použít metodu .copy()
seznam = [1,2,3,4]
seznam2 = seznam.copy()
print(seznam)
print(seznam2)
seznam.clear()
print(seznam)
print(seznam2)

