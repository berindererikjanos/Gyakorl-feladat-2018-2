revName = lambda s1,s2: s2[::-1] + " " + s1[::-1]

gn = input('Give your given name: ')
sn = input('Give your family name: ')
print(revName(gn,sn))
