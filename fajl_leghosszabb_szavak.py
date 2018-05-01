#Olvassunk be egy fájlt, mely kiírja a leghosszabb szavakat
# try:
#     lista = []
#     max = 0 #a max kezdőértéke mindig egy kicsi szám. Olyan kicsi, hogy biztosan nem lesz az adatok közt ennél kisebb
#     with open("bemenet.txt") as file:
#         for s in file: #végigmegy a fájl összes során (az s az akutális sor)
#             lista.append(s)
#             if len(s.strip()) > max:
#                 max = len(s.strip())
#
#     for i in range(len(lista)):
#         if len(lista[i].strip()) == max:
#             print(lista[i].strip())
#
#
# except FileNotFoundError:
#     print("Nem letezik az adott fajl!")


#Olvassunk be egy fájlt, mely kiírja a leghosszabb szavakat
try:
    lista = [] #akutális leghosszabb szavakat teszem el
    max = 0 #a max kezdőértéke mindig egy kicsi szám. Olyan kicsi, hogy biztosan nem lesz az adatok közt ennél kisebb
    with open("bemenet.txt") as file:
        for s in file: #végigmegy a fájl összes során (az s az akutális sor)
            if len(s.strip()) > max:
                max = len(s.strip())
                lista = []
            if len(s.strip()) == max:
                lista.append(s)

    print(lista)


except FileNotFoundError:
    print("Nem letezik az adott fajl!")
