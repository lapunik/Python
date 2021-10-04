seznam = [1,2,"tři",True,[4.8,"konec"]]
slovnik = {"a": 1,"b":2,"c":"tři","d":True,"e":[4.8,"konec"]}

tuple1 = (1,2,"tři",True,[4.8,"konec"])

for i in seznam:
    print(i)

for i in tuple1: # výpis n-tice je stejný jako výpis seznamu
    print(i)

# do n-tice nelze přidávat dodatečně hodnoty

# pokud chci n-tici o jedne hodnotě, musím použít hodnotu a čárku, 
tuple1 = (3) # nebude n-etice
tuple2 = (3,) # bude n-tice

print(tuple1)
print(tuple2)