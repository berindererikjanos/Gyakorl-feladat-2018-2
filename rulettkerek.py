import random

wheel = set(range(1,37))

even = set(range(2,37,2))
odd = wheel - even
low = set(range(1,19))
high = wheel - low
red = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
black = wheel - red

wheel = wheel | {0,'00'}

print("Páros számok: ",even)
print("Páratlan számok: ",odd)
print("Kis számok: ",low)
print("Nagy számok: ",high
print("Piros számok: ",red)
print("Fekete számok: ",black)

num = random,choice(list(wheel))
print("Random generált szám: ",num)
print("------------------------------------------------------------------")

dict = {'even':even, 'odd':odd, 'low':low, 'high':high, 'red':red, 'black':black}
for k in dict:
    if num in dict[k]:
        print('The number {} is {}'.format(num,k))
        
print("-----------------------------------------------------------------")
print("Összes szám: ",wheel)
