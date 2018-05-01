#Olvassunk be egy fájlt, mely az 5 karakternél hosszabb (enter nélkül) szavakat kiírja, és elmenti egy listába
try:
    lista = []
    with open("bemenet.txt") as file:
        for s in file: #végigmegy a fájl összes során (az s az akutális sor)
            if len(s.strip())>5: #a strip() függvény levágja a fölösleges whitespace karaktereket a string végéről
                lista.append(s)

    print("hosszabb mint 5 karakter: ",lista)

except FileNotFoundError:
    print("Nem letezik az adott fajl!")
