

def legnagyobbOszto(n):
    for i in range(n-1,0,-1):
        if n%i == 0:
            return i

n = int(input('Kérem adjon meg egy tetszőleges számot: '))
while n!=0:
    print(n, legnagyobbOszto(n))
    n = int(input('Kérem adjon meg egy tetszőleges számot: '))
    
    
     
