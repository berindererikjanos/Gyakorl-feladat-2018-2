import random

prime = set(range(2,5001))
for i in range(2,5001):
    if i in prime:
        n = i+i;
        while n <= 5000:
            prime.discard(n)
            n += i
           
           
print("Az 5000-nél kisebb prímszámok: ",prime)
