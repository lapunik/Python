retezec = "  Dobrý Den, Dnes je Pěkné počasí\n"

print(retezec)
print(retezec.lower())
print(retezec.upper())
print(retezec.capitalize()) # Velké pouze první písmeno 
print(retezec.title()) # Velká všechna první písmena
print(retezec.strip()) # Ořezání všech bílých znaků z krajů
print(retezec.lstrip()) # Ořezání všech bílých znaků z leva
print(retezec.rstrip()) # Ořezání všech bílých znaků z prava

print(retezec.startswith(" ")) # Vrací true pokud řetězec začíná daným substringem 
print(retezec.startswith("  D")) 
print(retezec.startswith("q")) 

print(retezec.endswith("\n")) # Vrací true pokud řetězec začíná daným substringem 
print(retezec.endswith("počasí\n")) 
print(retezec.endswith("q")) 

print(retezec.count("e")) # Vrátí počet znaků e
print(retezec.count("Den")) # Vrátí počet slov Den
print(retezec.count(" ")) # Vrátí počet mezer

print(retezec.index("D"))
print(retezec.index("Pěkné")) # Vrátí index kde se nachází první slovo "Pěkné" 
# print(retezec.index("červená")) # pokud ve stringu nic nenajde, hodí value error 

print(retezec.replace("Pěkné","Hnusné"))
print(retezec.replace("o"," i "))

print("Ahoj, jak se {} máte? Já se mám {}.".format("zítra","špatně"))
print("Ahoj, jak se {den} máte? Já se mám {nálada}.".format(den="dnes",nálada="dobře"))
x = "včera"
y = "neskutečně"
print(f"Ahoj, jak se {x} máte? Já se mám {y}.")
x = 5
print(f"Druhá mocnina čísla {x} je {x**2}")

print(retezec.split(" ")) # oddělovač není zahrnut ve výsledném listu
print(retezec.split("Dnes"))

print(" ".join(["Ahoj","jak", "se", "máš?"]))
print("".join(["Ahoj","jak", "se", "máš?"]))
print("  boom  ".join(["Ahoj","jak", "se", "máš?"]))

print("".join(retezec.split(" "))) # odstranění mezer ve stringu, nejdřív roztrhání pomocí split a pak spojení bez mezer