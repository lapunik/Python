### Lists ################################################################################################

seznam = ["a","b",8.5,"dneska","a",14,False,"a"]

seznam.append("string") # přidání na konec
seznam.append(True)
seznam.append(7)
print(seznam)

seznam.insert(0,"nova") # vložení na začátek
print(seznam)
seznam.insert(2,"duha nova") # vložení na konkrétní index
print(seznam)
seznam.insert(-2,15.7) # vložení na konkrétní index od zadu
print(seznam)

print(seznam.pop(5)) # vrátí hodnotu na indexu a odstraní ji ze seznamu
print(seznam)

seznam.remove(8.5) # odstraní určitou hodnotu ze seznamu
print(seznam)
seznam.remove("a") # pokud je hodnota v seznamu vícekrát, odstraní pouze první hodnotu z leva
print(seznam)
#seznam.remove("tohle v listu není") # pokud hodnota v seznamu není, vyskočí value error
#print(seznam)

seznam2 = seznam.copy() # zkopírování seznamu
print(seznam2)

seznam2.clear() # odstraní celý obsah listu
print(seznam2)

print(seznam.count("a")) # vypíše kolikrát se prvek nachází v listu
print(seznam.index("a")) # vypíše index na kterém se nachází hodnota

seznam.reverse() # převrácení sezamu
print(seznam) 

# seznam.sort() # uspořádat nelze v seznamu s různými typy
# print(seznam) # takže vyskočí TypeError

seznam2 = [3,2,4,1]
seznam3 = ["c","b","d","a"]
seznam2.sort() # uspořádání podle velikosti
print(seznam2) 
seznam3.sort() # uspořádání podle ASCII
print(seznam3)
seznam2.sort(reverse=True) # uspořádání podle velikosti
print(seznam2) 

### Dictionaries ################################################################################################

slovnik = {"a":51,7:True,False:"promena",8.6:78}
print(slovnik)

print(slovnik.pop(7)) # zadávám klíč místo indexu, vrátí hodnotu a vymaže ji ze slovníku
print(slovnik)

slovnik2 = slovnik.copy() # zkopírování slovníku do jiného slovníku
print(slovnik2)

slovnik2.clear() # smaže celý slovník
print(slovnik2)

print(slovnik.items()) # Vrátí všechny pár ve formát "dict_items" (ideální pro projíždění ve for loopu)
print(list(slovnik.items())) # S převedením do listu
print(list(slovnik.items())[2]) # S převedením do listu
print(list(slovnik.items())[2][1]) # S převedením do listu

print(slovnik.keys()) # Vrátí všechny klíče ve formát "dict_items" (ideální pro projíždění ve for loopu)
print(list(slovnik.keys())) # S převedením do listu
print(list(slovnik.keys())[2]) # S převedením do listu

print(slovnik.values()) # Vrátí všechny hodnoty ve formát "dict_items" (ideální pro projíždění ve for loopu)
print(list(slovnik.values())) # S převedením do listu
print(list(slovnik.values())[2]) # S převedením do listu
