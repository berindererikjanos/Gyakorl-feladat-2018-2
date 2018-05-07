gyumolcsok = ['narancs', 'alma', 'körte', 'barack', 'banán', 'kiwi', 'alma']
print("Az almák száma: ",gyumolcsok.count('alma')) #hány alma van?
print("A málnák száma: ",gyumolcsok.count('málna')) #hány málna van?
print("Hanyadik indexen található: ", gyumolcsok.index('körte')) #hanyadik index?
gyumolcsok.append('Erik') #a listához hozzáfűztem az Erik szót
print(gyumolcsok)
gyumolcsok.sort() #rendezi a listát ABC sorrendben
print(gyumolcsok)

gyumolcsok.reverse()  #megfordítja az elemek sorrendjét a listában
print(gyumolcsok)


gyumolcsok.remove('narancs') #kitörli a listából a narancsot
print(gyumolcsok)
