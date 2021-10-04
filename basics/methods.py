def Deleno(hodnota1,hodnota2):
    return hodnota1/hodnota2 

x = 5
y = 8

print(Deleno(x,y))
print(Deleno(hodnota2 = x, hodnota1=y)) # Zadávání s přímým přístupem k parametrům metody (prostě je můžu přeházet, netuším k čemu to může být dobrý)


def Krat(hodnota1,hodnota2=10): # Ve funkci můžu zadat výchozí hodnotu
    return hodnota1*hodnota2 

print(Krat(x)) # x*10


def Suma(*argumenty): # Metodě můžu předat libovolný počet argumentů (jakože list, ale není to list), ZNAČÍM HVĚZDIČKOU PŘED ARGUMENTEM
    hodnota = 0
    for i in argumenty:
        print(i)
        hodnota += i
    return hodnota

print(Suma(1,5,6,7,9)) # m;6u yadat argument; kolik chci


def Zlomek(**k_argumenty): # Metodě můžu předat i seznam, ZNAČÍM DVĚMI HVĚZDIČKAMI PŘED ARGUMENTEM

    print(k_argumenty)
    return k_argumenty["cinitel"] / k_argumenty["jmenovatel"]

print(Zlomek(cinitel=5,jmenovatel=2)) # nazvy musí odpovídat názvům použitých ve funkci