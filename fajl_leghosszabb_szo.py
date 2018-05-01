#Olvassunk be egy fájlt, mely kiírja a leghosszabb szót. Ha több ilyen is lenne, akkor a legelső leghosszabb szót írja ki
try:
    lista = []
    max = 0 #a max kezdőértéke mindig egy kicsi szám. Olyan kicsi, hogy biztosan nem lesz az adatok közt ennél kisebb
    with open("bemenet.txt") as file:
        for s in file: #végigmegy a fájl összes során (az s az akutális sor)
            if len(s.strip()) > max:
                max = len(s.strip())
                leghosszabb = s.strip()

    print("maximalis hossz: ",max)
    print("leghosszabb szo: ",leghosszabb)

except FileNotFoundError:
    print("Nem letezik az adott fajl!")
