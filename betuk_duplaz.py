#Írjon függvényt mely a bementi szóban minden karaktert megkettőz:
#Példa: alma
#Ki: aallmmaa


def duplaz(s):
    uj = ""
    for i in range(len(s)):

        uj+=s[i]
        uj+=s[i]
    return uj

#a bemeneti karakterről eldönti, hogy magánhangzó-e
def mgh_e(c):
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        return True
    else:
        return False

def mgh_duplaz(s):
    uj = ""
    for i in range(len(s)):
        if mgh_e(s[i]): #ha az adott karatker mgh, akkor 2x teszem bele
            uj += s[i]
            uj += s[i]
        else: #egyébként 1x
            uj+=s[i]
    return uj

s = input()
print(duplaz(s))
print(mgh_duplaz(s))
