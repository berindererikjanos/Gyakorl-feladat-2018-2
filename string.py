s = input("Adjon meg egy szot: ")
print("A bekert szo: ",s)

print("A bekert szo hossza: ",len(s))
#Substring képzés (részsztring)
print("----------------------------")

# almafa
# 012345

s2 = s[2:4] #2-4-ig veszi a karaktereket, úgy, hogy a 4 nincs benne
s3 = s[0:3]
s4 = s[::] #másolatot képez a stirngről
s5 = s[4:1:-1]
s6 = s[::-1]

print("s2: ",s2)
print("s3: ",s3)
print("s4: ",s4)
print("s5: ",s5)
print("s6: ",s6)

print("-------------------")
#kérjunk be egy karaktert
c = input("Adjon meg egy betut! ")

if c.islower():
    print("A karakter kisbetu!")
elif c.isupper():
    print("A karakter nagybetu")
elif c.isdigit():
    print("Szamjegy")
elif c.isspace():
    print("Whitespace karakter") #enter, szóköz, tab
else: #elif nélkül ez az else csak az utolsó if-re vonatkozik. Ezért kisbetű esetén kiírná, hogy kisbetűs és egyéb is.
    print("Egyeb")

print("-------------------")
s7 = s.upper() #s.lower()
print("Nagybetűsen: ",s7)


print("---------------------")
s8 = input("Adjon meg szavakat vesszovel elvalasztva:")
szavak_lista = s8.split(",")
print(szavak_lista)
