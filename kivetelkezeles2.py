#Kérjen be a felhasználótól egy egész számot. Ha nem egész számot adna meg, akkor kérjen be újat.
#A program írja ki a beolvasott számra, hogy páros vagy páratlan


while True:

    try: #a try-ban lévő utasításokat "megpróbálja" végrehajtani, ha nem volt kivétel akkor lefut
        #ha volt kivétel akkor az except ágak valamelyike lefut, és lekezeli az adott kivételes esetet ("hibát")
        n = int(input("Adjon meg egy szamot "))

        if n%2==0:
            print("paros")
        else:
            print("paratlan")

        break
    except ValueError:
        print("Nem szamot adott meg!")

