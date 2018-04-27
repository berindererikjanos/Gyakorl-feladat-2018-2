#Kérjünk be egy stringet és toroljuk belőle a szóközöket.

#Stringből nem lehet torolni! Csak úgy lehet törölni, ha létrehozunk egy új stringet amibe nem tesszük bele
#a szóközöket

def szokoz_torol(s):
    uj = "" #üres stirng
    for i in range(len(s)): #bejárja karakterről-karakterre az eredeti stringet
        if s[i] != ' ':
            uj+=s[i] #a hozzáfűzés művelet. Tehát ha nem szóköz következik, akkor hozzáfűzöm az új stringhez
    return uj

#Általában ha módosítani kell valamit, akkor érdemes egy újat létrehozni az eredeti adatokkal és azt módosítani
#így megmarad a régi is

s = input("szo: ")
t = szokoz_torol(s)
print("torolve: ",t)
print("s: ",s)

