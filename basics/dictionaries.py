seznam = [4,71.5,"ahoj",False]

print(seznam[2])

# místo indexů máme u slovníků klíč 
# klíč i hodnota může být jakákoliv hodnota (bool, string, int, float)

slovnik = {"hodnota1": 4,"hodnota2": 71.2, True: "ahoj", 5 : False}

print(slovnik[True])
#stejná  hodnota ze slovniku jako z seznamu, ale dostali jsme ji pomoci klice misto indexu 
print(slovnik[5])
print(slovnik["hodnota2"])

#přidávání ke slovníku prostě přidáním další klíče a hodoty

slovnik["novy"] = 77

print(slovnik)

# samozřejmě i slovníky mohou mít v sobě listy, nebo další slovníky
slovnik[False] = {"a": 15,"b": 7.8, 44: "nevim"}
slovnik["hodnota3"] = [1,8.7,"dalsi",True]

# ale nemůžeme mít list nebo slovník jako klíč slovníku

print(slovnik)

for klic,hodnota in slovnik.items(): # pouze klíče: .keys() pouze hodnoty: .values()
    print(klic,hodnota)

