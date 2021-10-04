### Print ##############################################################################################################################

print("Ahoj", 4, True, 5.8) # více hodnot oddělí mezerou
print("Ahoj", 4, True, 5.8, sep = ", ") # do sep zvolím oddělovač, tady je to čárka a mezera
print("Ahoj", 4, True, 5.8, end = " Tohle je konec.") # Do end můžeme napsat to co má být na konci řádku
print("Ahoj", 4, True, 5.8, sep = "\n") # odřádkování klasicky zpětné lomítko n
print("Ahoj", 4, True, 5.8, end = "") # odřádkování klasicky zpětné lomítko n
print(" dalsi radek pokracuje, protože jsem nahoře dal end prázdný, místo defalutně nastaveného odřádkování")

print("\\ zpetne lomitko napiseme klasicky, pokud hodime dve zpetne lomitka za sebou")

print("retezit " + "můžeme " + "pomoci " + "pluska" + "i s cislem " + str(7))

### Type ##############################################################################################################################

print(type(5))
print(type(5.8))
print(type(True))
print(type(print))

### Len ##############################################################################################################################

print(len("Ahoj"))
print(len([15,6,True,7.8,"ahoj"]))
print(len({15:"patnact",16:"sestnact"}))

### Abs ##############################################################################################################################

print(abs(15))
print(abs(-15))
print(abs(2+2j)) # komplexni čísla, hodně hustý

### Round ##############################################################################################################################


print(round(9.4)) # vrací integer
print(round(9.5))
print(round(9.6))

### Min, max, Sorted #####################################################################################################################

print(min(["aa","!bf","+ca"])) # vrátí podle prvního místa podle ASCII tabulky
print(min([15,6,7]))

print(max(["aa","!bf","+ca"]))
print(max([15,6,7]))

print(sorted(["aa","!bf","+ca"]))
print(sorted([15,6,7]))

print(sorted(["aa","!bf","+ca"], reverse = True))
print(sorted([15,6,7], reverse = True))

### Sum ##################################################################################################################################

print(sum([15,6,7]))
print(sum([15.4,6.8,7.0]))
