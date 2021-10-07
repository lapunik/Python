class Penezenka:  
    
    def __init__(self,penize,predmety): 
        self.penize = penize 
        self.obsah = predmety

    # metoda vrací string, pokud zavolám print přímo na instanci třídy, pokud není definovaná metoda __str__ (__repr__ slouží pro programátora, __str__ pro uživatele)
    def __repr__(self): # Vždy pouze self parametr!!!!
        return f"Penezenka(penize = {self.penize}, obsah = {self.obsah})"

    # metoda vrací string, pokud zavolám print přímo na instanci třídy, text by měl být uživatelsky přívětivý
    def __str__(self):
        return f"Penezenka ma v sobě {self.penize}kč a obsahuje nasledující předměty {self.obsah})"

    # Tyhle funkce funguji stejně jako str, jen vrací jiné typy proměnných
    def __int__(self):
        return self.penize

    def __float__(self):
        return float(self.penize)

    def __bool__(self):
        if self.penize == 0:
            return False
        else:
            return True

    # očekává velikost
    def __len__(self):
        return len(self.obsah)

    # definuje co se stane, když se budu pokoušet instanci sčítat s nějakou hodnotou
    def __add__(self,jina):
        return (self.penize + jina)

    # definuje co se stane, když se budu pokoušet sčítat nějakou hodnotu s instancí třídy
    __radd__ = __add__ # nemusím funkci definovat znovu a rovnou natvrdo řeknu, že když se volá __radd__, tak se má volat stejná funkce jako při __add__

    # totéž jako __add__, pouze pro odčítání
    def __sub__(self,jina):
        return (self.penize - jina)

    def __rsub__(self,jina):
        return (jina - self.penize)

    # __mul__ (násobení), __div__ (dělení), __truediv__ (desettiné dělení, normální), __floordiv__ (celočíselné dělení), __divmod__ (modulo)

    # definuje co se vrátí, pokud položím instanci == něčemu (nemá __req__)
    def __eq__(self, jina):
        return self.penize == jina

    # __ne__ (nerovná se), __lt__ (menší než), __gt__ (větší než), __le__ (menší nebo rovno), __ge__ (větší nebo rovno)
 
    # iterátor: abych mohl volat for přímo na instanci. Když je volán for, tak vlsatně volá tuto metodu u objektu který má být iterován
    def __iter__(self):
        # return iter(self.obsah) # volám předpřipravenou funkci iter, která dělá přesně to co potřebuju, ale kdybych si chtěl iterátor vytvořit sám tak:
        self.i = 0 
        return self

    # -cyklus for nejprve vytvoří iterátor pomocí funkce __iter__ a následně volá při každé iteraci fiunkci __next__
    def __next__(self):
        if len(self.obsah) > self.i:
            objekt = self.obsah[self.i]
            self.i += 1
        else:
            raise StopIteration
        return objekt

    # když chci, aby se instance mohla chovat jako funkce, když zavolán instanci kulatý závorky a daný počet argumentů, tak se mi spustí tato funkce
    def __call__(self,a,b):
        return self.penize + a + b

    # zavolá se, pokud se snažím odvolat se na vlastnost třídy, která ale není deklarovaná
    def __getattr__(self,nazev):
        # v názvu je název který jsme použili při volání z instace, u našeho příkladu to byl: zadny_takovy_atribut_ve_tride_neni
        # kdybychom chtěl konkrétní název takového atributu odchytávat, můžu normálně dát if nazev == "zadny_takovy_atribut_ve_tride_neni", tak vrať cokoliv, třeba int nebo str
        return None



penezenka = Penezenka(200,["Cestovní pas","Občanský průkaz","Platební karta"])

print(repr(penezenka))
print(penezenka)
print(int(penezenka))
print(float(penezenka))
print(bool(penezenka))
print(len(penezenka)) 
print(penezenka + 100)
print(100 + penezenka)
print(penezenka - 100)
print(100 - penezenka)
print(penezenka==200)
print(penezenka==100)

for i in penezenka:
    print(i)

print(penezenka(5,38))
print(penezenka.zadny_takovy_atribut_ve_tride_neni) 