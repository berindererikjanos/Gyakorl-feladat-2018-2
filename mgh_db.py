#Írjon függvényt mely a bementi szóra megszámolja, hogy hány darab magánhangzó van benne
def mgh_db(s):
    db=0
    for i in range(len(s)):
        if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
            db+=1
    return db

s = input()
print(mgh_db(s))
