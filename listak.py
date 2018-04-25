#Lista: tobb adat tárolására alkalmas eszköz
#Példa: szükségem van 100 darab számra,  vagy  szóra akkor nem hozok létre 100 db változót, hanem egy 10 elemű listába pakolom

lista = [1,4,5,6,2,0]

print("lista merete: ",len(lista))

print("lista: ",lista)

lista.append(7) #hozzáfűzi a végére

print("lista: ",lista)

lista.remove(5) #törli az 5-ös elemet

print("lista: ",lista)

print("------------")
lista2 = lista[0:4] #0-4közt
lista3 = lista[::] #másolat
lista4 = lista[::-1] #visszafelé

print("lista2: ",lista2)
print("lista3: ",lista3)
print("lista4: ",lista4)
