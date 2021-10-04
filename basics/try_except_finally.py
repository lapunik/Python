# vyzkoušíme klasický try except

try: 
    hodnota1 = int(input("Zadej prvni hodnotu: "))
    hodnota2 = int(input("Zadej druhou hodnotu: "))
#except jenom except, nebo konkretni chyba
except ValueError: 
    print("Hodnota neni cele číslo, ukončuji program")
    exit()
    
finally:
    print("Kod co se provede potom, co se dokonci blok try-except, dokonce i když je v except exti()")

print("Součet čísel je: " + str(hodnota1+hodnota2))

# když chci konkretni exception, tak si pustim program, simuluji chybu a konzole mi vzdy vypise název výjimky, 
# dvojtečku a pak nějaký kecy. Právě nezev výjimky  můžu napsat za except a budu chytat jen výjimky vyvolené touto chybou 