class Osoba:  
    
    def __init__(self,jmeno="???",vek=-1): 
        self.jmeno = jmeno
        self.vek = vek

    def pozdrav(self):
       return f"Jmenuji se {self.jmeno} a je mi {self.vek} let."

class Programator(Osoba):
   
    def __init__(self,jmeno="???",vek=-1,jazyky=[]): 
        super().__init__(jmeno,vek) # třída super veme automaticky třídu Osoba
        self.jazyky = jazyky
    
    def pozdrav(self):
        retezec = super().pozdrav() + " Umím jazyky "
        for i in self.jazyky:
            retezec = retezec +  i  + ", "
        return retezec



emil = Osoba("Emil",21)
print(emil.pozdrav())

emil = Programator("Karel",29,["Python","C++","C#"])
print(emil.pozdrav())