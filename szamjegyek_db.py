#Írjon függvényt mely a bementi szóra megszámolja, hogy hány darab számjegy van benne

def szamjegyek_db(s):
    db = 0
    for i in range(len(s)): #végigmegyünk a szón
        if s[i].isdigit(): #ha az adott karaktere számjegy
            db+=1 #akkor a darab változót 1-gyel növeljük
    return db


s=input()
print(szamjegyek_db(s))
