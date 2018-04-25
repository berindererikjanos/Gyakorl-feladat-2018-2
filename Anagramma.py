#Kérjen két szót, és írja ki, hogy anagrammák-e.
#Két szó anagramma, ha ugyanazokból a betűkből áll

def anagramma_e(s1,s2):
    s1_rendezve = sorted(s1) #ABC sorrendbe rendezi a betűket, és az eredményt egy új stringbe menti
    s2_rendezve = sorted(s2)

    if s1_rendezve == s2_rendezve:
        return True
    else:
        return False


s1 = input()
s2 = input()

print(anagramma_e(s1,s2))
