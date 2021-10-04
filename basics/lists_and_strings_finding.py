string = "abcdef"

if ("u" in string): # podmínka bude nesplněna, string neobsahuje "u" 
    print("Podminka splnena")
else:
    print("Podminka NEsplnena")

if ("a" in string): # podmínka bude splněna, string obsahuje "a"
    print("Podminka splnena")
else:
    print("Podminka NEsplnena")


seznam = ["abc","bcd","cde","def"]

if ("ab" in seznam): # podmínka bude nesplněna, seznam neobsahuje element "ab", obsahuje pouze element "abc", ale to není totéž
    print("Podminka splnena")
else:
    print("Podminka NEsplnena")

if ("abc" in seznam): # podmínka bude splněna, seznam obsahuje "abc"
    print("Podminka splnena")
else:
    print("Podminka NEsplnena")

# Projedu všechny jednotlivé stringy v seznamu a podívám se, jestli náhodou některý z nich neobsahuje můj hledaný text

if any("ab" in s for s in seznam): # podmínka bude splněna, seznam obsahuje element "abc", který obsahuje "ab"
    print("Podminka splnena")
else:
    print("Podminka NEsplnena")

znak = "+"
seznam = ["+","-","*","/","%","**"]
