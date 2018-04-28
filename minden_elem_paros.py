#Kérjen be egy 5 elemű listát és vizsgálja meg, hogy minden eleme páros-e

#A minden típusú állításánál a cáfolatra kell példát találni, és ha találtunk akkor az állítás hamis
def minden_paros(lista):
    for i in range(len(lista)):
        if lista[i]%2 == 1:
            return False
    return True #ha idáig eljut akkor a fenti if 1x sem volt igaz, azaz minden eleme páros volt



lista = [2,4,3,8,0]
print(minden_paros(lista))
