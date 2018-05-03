import math

def area(r):
  a = r**2*math.pi
  return a

ls = [4,5,6,7,8,9,234,21]
for i in ls:
  print("Kör területe: ",area(i))
 
area =lambda r : r**2*math.pi
ls = [6,21,14,563,123,56]
print("Adott számok területe: ",list(map(lambda r : r**2*math.pi,[5,10,24,52,56,21,45])))
