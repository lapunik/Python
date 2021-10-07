# když chci zjistit třídu můžu použít funkci type
x = type(print)
print(x)
x = type(15)
print(x)
x = type(True)
print(x)

# Jak vytvořit třídu:

class Osoba: # dobrá praxe říká, že v názvech tříd nepoužíváme podtržítka a začínáme velkými písmeny 
    
    # "self" je jakoby "this", pak se můžu odkazovat na třídu pomocí self.METODA
    def __init__(self,jmeno,vek): # konstruktor
        #pass # dočasný kód, aby neházel chybu, že má tenhle řádek prázdný
        self.jmeno = jmeno
        self.vek = vek

    def info(self):
        return f"Jmenuji se {self.jmeno} a je mi {self.vek} let."

    def vek_ve_dnech(self):
        return self.vek*365.25



honza = Osoba("Honza",24)
print(honza.info())
jakub = Osoba("Jakub",19) 
print(jakub.info())

print(jakub.vek_ve_dnech())
