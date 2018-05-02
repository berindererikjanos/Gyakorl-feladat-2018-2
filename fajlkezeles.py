
try:
    # file = open("bemenet.txt","r")
    # for s in file:
    #     print(s)
    # file.close()
    with open("bemenet.txt") as file:
        for s in file:
            print(s)


except FileNotFoundError:
    print("Nem letezik az adott fajl!")
