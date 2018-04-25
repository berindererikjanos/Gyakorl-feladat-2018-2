#írjunk programot amely bekér 1 számot és eldönti róla, hogy prímszám-e

def prim_e(n):

    if n==1 or n==0:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False

    return True

a = int(input("Adjon meg egy számot: "))

print(type(a))
if prim_e()
