dalsi_vypocet = "ano"
while(dalsi_vypocet == "ano"):
    hodnota1 = input("Zadej první hodnotu: ")
    while(True):
        operace = input("Zadej operaci(+,-,*,/,%,**): ")
        if operace in ["+","-","*","/","%","**"]:
            break
        print("Chyba v zadani operace, zkus to znovu!")
    hodnota2 = input("Zadej druhou hodnotu: ")
    if hodnota2=="0" and operace == "/":
        print("Výsledek je: nekonečno")
    else:
        print("Výsledek je: " + str(eval(hodnota1+operace+hodnota2)))
    while(True):
        dalsi_vypocet = input("Chceš počítat další příklad (ano/ne)? ")
        if(dalsi_vypocet in ["ano","ne"]):
            break
        print("Chyba v zadání, vyber (ano/ne): ")