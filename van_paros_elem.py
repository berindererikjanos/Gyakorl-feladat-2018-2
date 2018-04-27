# Kérjen be egy 5 elemű listát és vizsgálja meg, hogy szerepel e benne páros szám


def minden_paros(lista):
    for i in range(len(lista)):
        if lista[i] % 2 == 0: #elég 1x igaznak lennie az ifnek. Elég 1db páros számot találni
            return True
    return False #ha 1x sem volt igaz a fenti if, akkor false, hiszen akkor nem volt páros szám


lista = [1, 3, 5, 7, 5]
print(minden_paros(lista))
