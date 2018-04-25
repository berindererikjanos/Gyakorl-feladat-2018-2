#Kérjen be egy egész számokból álló listát és írja ki:
#-összegét
#-átlaglát
#-hány páros szám van benne
#-hány prím szám van benne


def osszeg(lista):
    return sum(lista)

def atlag(lista):
    return sum(lista)/len(lista)

def paros_db(lista):
    db=0
    for i in range(len(lista)):
        if lista[i]%2 == 0:
            db+=1
    return db


def prim_e(n):
    if n==1 or n==0:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def prim_db(lista):
    db=0
    for i in range(len(lista)):
        if prim_e(lista[i]):
            db+=1
    return db



lista = [] #üres lista
while True:

    n = int(input())

    if n == 0:
        break

    lista.append(n)


print(lista)
print(osszeg(lista))
print(atlag(lista))
print(paros_db(lista)," db paros szam van benne")
print(prim_db(lista))
