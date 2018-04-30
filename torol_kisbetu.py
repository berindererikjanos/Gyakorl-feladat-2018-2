#Írjon függvényt mely a bementi szóból törli a kisbetűket

def szokoz_torol(s):
    uj = "" #üres stirng
    for i in range(len(s)): #bejárja karakterről-karakterre az eredeti stringet
        if not s[i].islower():
            uj+=s[i] #a hozzáfűzés művelet. Tehát ha nem kisbetű következik, akkor hozzáfűzöm az új stringhez
    return uj

#Általában ha módosítani kell valamit, akkor érdemes egy újat létrehozni az eredeti adatokkal és azt módosítani
#így megmarad a régi is

s = input("szo: ")
t = szokoz_torol(s)
print("torolve: ",t)
print("s: ",s)
