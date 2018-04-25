#írjon programot, mely bekér 2 számot és visszaadja a legnagyobb közös osztót

def legnagyobb_kozos_oszto(m,n):
    f = min(m,n)

    while True:
        if m%f == 0 and n%f == 0:
            return f

        f-=1


a = int(input("Adja meg az első számot: "))
b = int(input("Adja meg a második számot: "))
print(legnagyobb_kozos_oszto(a,b))
print("Ennyi a legnagyobb közös osztó")