#Olvassunk be egy fájlt, mely az 5 karakternél hosszabb (enter nélkül) szavakat kiírja, és elmenti egy listába
try:
    db = 0
    with open("bemenet.txt") as file:
        for s in file: #végigmegy a fájl összes során (az s az akutális sor)
            if "dinnye" in s: #ha az adott sorban a "dinyne" szó benne van akkor igaz
                db+=1

    print("Dinnyek szama: ",db)


except FileNotFoundError:
    print("Nem letezik az adott fajl!")
