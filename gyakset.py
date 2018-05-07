kosar = {'alma', 'narancs', 'alma', 'körte', 'narancs', 'banán'}
print(kosar) #a többször szereplő elemek csak egyszer szerepelnek

if 'narancs' in kosar:
    print("A megadott szó bennevan a kosárban")
else:
    print("A megadótt szó nincs benne a kosárban!")

if "kakukkfu" in kosar:
    print("A megadott szó bennevan a kosárban")
else:
    print("A megadott szó nincs benne a kosárban")

a = set('abracadabra')
b = set('alacazam')

print("az A halmak betűi: ",a)
print("Azok a betűk amelyek A-ban megvannak, de B-ből hiányoznak: ",a-b)
print("Azok a betűk, amelyek A-ban vagy B-ben megvannak: ",a|b)
print("Azok a betűk, melyek A-ban is és B-ben is megvannak: ",a&b)
print(a^b)
