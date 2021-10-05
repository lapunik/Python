### Komentáře #############################################################################################################################################

# Takhle se pise komentar
"""
Tohle je také komentář, ale blokový
"""

### Datové typy a výpis ###################################################################################################################################

# Datove typy se neudavaji, takže:
"ahoj" # string
'ahoj' # taky string
'uvozovky se pisou  takhle "", proste to druhy nez ohranicuje cely text ' # string co obsahuje uvozovky
15 # int
0.4 # float
True # bool, pozor vele "T"

# pro vypis do konzelo prikaz "print()"
print(7)
print("Ahoj")

#pokud chci novou promenou, tak proste napisu jejo jmeno
hodnota = 5
a = 952
retezec = "Nejaky kecy"
logicka = True

print(hodnota)
print(retezec)
print(logicka)

print(retezec[1]) # Stringy se chovají jako listy
print(retezec[1:4]) 

print("Prevedu int na sting, abych ho mohl vypsat " + str(hodnota) + "to je ono")
### Aritmetické operace ####################################################################################################################################
print(2+6)
print(15-9)
print(5*9)
print(7/3) # po deleni se číslo vždy převede na float, pokud chci celočíselné dělení, musím použít dvě lomítka (zaokrouhleni dolu)

print(8//3) # zaokrouhleni dolu

print(7**3) # mocnina

print(4%3) # zbytek po delení

### Vstup ####################################################################################################################################################

# zakomentuju inputy, aby mě neotravovali dál v kódu 

#hodnota = input("Zadej hodnotu: ") # nemusí mít text, viz níže
print(hodnota)

#a = input()
print(a)

print(a + hodnota) # součet proběhl na úrovni stringů, pokud chci sčítat čísla, musím přetypovat:

### Přetypování ###############################################################################################################################################

cislo = "6"

print(19 + int(cislo))
print(10 + int(1.8)) # vysledek bude 11, čili int

print(str(15)+str(0)) # Vypsalo se 150, protože sčítám stringy

# přetypovat mohu rovnou celý vstup input:
hodnota = int(input("Zadej int: "))

### Divná věc oproti C ########################################################################################################################################

x = 15 # int
x = "Ahoj" # do stejné proměné uložím nejdřív int, pak string a je jí to uplně jedno
print(x)